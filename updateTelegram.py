"""This programm is used to send shooting results to a telegram receiver. It can be used to send the result as URL or as photo.
"""

import telegram as t
import pickle
import argparse
from pathlib import Path 

from targetlib.target import Target

def main(receiver, coordinates, type, asLink, withTable, withTenth, allData, headline, transparency):
    #Setup bot and get updates
    
    f = Path(__file__).with_name('token.txt').open("r")
    if not f:
        print("Token file 'token.txt' missing!!!")
        return
    token = f.read()
    f.close()
    bot = t.Bot(token=token)
    updates = bot.get_updates(allowed_updates=[t.Update.MESSAGE], timeout=1, read_latency=5)

    #Try open database or add a new empty one
    try:
        f = Path(__file__).with_name("database.pkl").open("rb")
        user2messId = pickle.load(f)
        f.close()
    except (EOFError, FileNotFoundError) as e:
       user2messId = dict()

    #Answer all register and unregister requrests
    while(len(updates) > 0):
        print("%d Updates" % len(updates))
        for upd in updates:
            if upd.message.text == '/register':
                user2messId[upd.message.from_user.full_name.upper()] = upd.message.chat.id
                bot.sendMessage(upd.message.chat.id, "Erfolgreich registriert!")
            elif upd.message.text == '/unregister':
                try:
                    del user2messId[upd.message.from_user.full_name.upper()]
                    bot.sendMessage(upd.message.chat.id, "Erfolgreich abgemeldet!")
                except KeyError:
                    bot.sendMessage(upd.message.chat.id, "Doppelt abmelden hilft besser!")
        #Set updates marked as read
        updates = bot.get_updates(offset=upd.update_id+1,allowed_updates=[t.Update.MESSAGE])

    #Write Username and ID to database
    f = Path(__file__).with_name("database.pkl").open("wb")
    pickle.dump(user2messId,f)
    f.close()

    #If message should be sent, then do so to the ID in the database
    if receiver:
        receiver = receiver.upper()
        if receiver in user2messId:
            if asLink:
                #Build up URL with given coordinates
                message = "https://barthler.ddns.net:8080/pic"
                if len(coordinates) > 0:
                    message+="?"
                    for i in range(0, len(coordinates) // 2):
                        if(i > 0):
                            message+="&"
                        message+="x%d=%d&y%d=%d" % (i+1, coordinates[2*i], i+1, coordinates[2*i+1])
                if not withTable:
                    message+="&withtable="
                if not withTenth:
                    message+="&tenth="
                if not type:
                    message+="&type=%s" % type
                bot.sendMessage(user2messId[receiver], message)                        
            else:
                #Send as picture
                #Setup picture
                if allData:
                    divisor = 4
                else:
                    divisor = 2


                target = Target(2048, 2048, len(coordinates) // divisor if withTable else 0 , type, headline, transparency)
                for i in range(0, len(coordinates) // divisor):
                    try:
                        if allData:
                            x = coordinates[divisor*i]
                            y = coordinates[divisor*i+1]
                            teiler = coordinates[divisor*i+2]
                            ringValue = coordinates[divisor*i+3]
                            if(x == None or y == None):
                                break
                            target.drawShotByAllInfo(x, y, teiler, ringValue)
                        else:
                            x = coordinates[divisor*i]
                            y = coordinates[divisor*i+1]
                            if(x == None or y == None):
                                break
                            target.drawShotByCoordinates(x, y)
                    except ValueError:
                        break

                if withTable:
                    target.drawTable(withTenth)
                    target.drawCenter()

                #Send as photo
                bot.send_document(user2messId[receiver], target.getPicture())
                print("Message to %s successfully sent" % receiver)
        else:
            print("%s is not in database" % receiver)
    else:
        #Otherwise just print actual database entries
        print(user2messId)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target', help='Whom to be send', nargs='?', default=None)
    parser.add_argument('-t', '--type', help='Type (b - black, r - red, g - green)', default='b')
    parser.add_argument('--asLink', dest='asLink', help='Send as Link', default=False, action=argparse._StoreTrueAction)
    parser.add_argument('-n', '--noTable', dest='withTable', help='Without ring table', default=True, action=argparse._StoreFalseAction)
    parser.add_argument('-e', '--noTenth', dest='withTenth', help='Rings without tenth', default=True, action=argparse._StoreFalseAction)
    parser.add_argument('--allData', dest='allData', help='Pass ring value and teiler directly instead of math. Is ignored when using --asLink', default=False, action=argparse._StoreTrueAction)
    parser.add_argument('-l', '--headline', dest='headline', help='Optional header text that is printed on top of the picture. e.g. for serial number use', default=None)
    parser.add_argument('--noTrans', dest='transparency', help='If true shots will be drawn with transparency', default=True, action=argparse._StoreFalseAction)
    parser.add_argument('data', type=float, help='Coordinates in pairs e.g. x1 y1 x2 y2 ... Means number of data arguments must be a multiple of two!' + \
        'If --allData flag is set Coordinates in pairs plus ring value and teiler e.g. x1 y1 t1 rv1 x2 y2 t2 rv2...', nargs='*')
    args = parser.parse_args()
    main(args.target, args.data, args.type, args.asLink, args.withTable, args.withTenth, args.allData, args.headline, args.transparency)
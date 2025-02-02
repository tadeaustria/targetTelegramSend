# Telegram Bot for shooting results

This script uses the [targetlib](https://github.com/tadeaustria/targetlib) to send results via [Telegram messenger](https://telegram.org/).

## Requirements

* [python-telegram-bot](https://python-telegram-bot.org/)
* numpy
* [pillow](https://pillow.readthedocs.io/en/stable/)
  
```pip install --extra-index-url https://barthler.ddns.net/pyrepo/ -r pipinstall```

This script further requires a `token.txt` in the working directory, that contains the API key for the bot. (**not included!**)

## Examples

* Message <br> ```python updateTelegram.py 'Tade barthler' 'msg' 'Hello World'```

* Picture Normal Mode <br> ```python updateTelegram.py 'Tade barthler' 'pic' '--noTenth' '--type' 'b' '2000' '-200' '-250' '250' '250' '-250' '-250' '-250' '500' '500' '-500' '500' '500' '-500' '-500' '-500' '-388' '400' '-666' '-400'```
* Picture Full Mode <br> ```python updateTelegram.py 'Tade barthler' 'pic' '--noTenth' '--type' 'b' '--allData' '2000' '-200' '200' '10' '-250' '250' '210' '9.5' '250' '-250' '200' '8' '-250' '-250' '200' '7' '500' '500' '200' '6' '-500' '500' '200' '5' '500' '-500' '2000' '4' '-500' '-500' '200' '3' '-388' '400' '200' '2' '-666' '-400' '20000' '1'```
* Picture With Headline <br> ```python updateTelegram.py 'Tade barthler' 'pic' '--noTenth' '--type' 'b' '-l' '45616 - 45617'  '2000' '-200' '-250' '250' '250' '-250' '-250' '-250' '500' '500' '-500' '500' '500' '-500' '-500' '-500' '-388' '400' '-666' '-400'```
* Picture No transparency <br> ```python updateTelegram.py 'Tade barthler' 'pic' '--noTenth' '--noTrans' '2000' '-200' '-250' '250' '250' '-250' '-250' '-250' '500' '500' '-500' '500' '500' '-500' '-500' '-500' '-388' '400' '-666' '-400'```

* Update Only <br> ```python updateTelegram.py 'Tade barthler' 'upd'```
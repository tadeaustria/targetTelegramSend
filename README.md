# Telegram Bot for shooting results

This script uses the [targetlib](https://github.com/tadeaustria/targetlib) to send results via [Telegram messenger](https://telegram.org/).

## Requirements

* [python-telegram-bot](https://python-telegram-bot.org/)
* numpy
* [pillow](https://pillow.readthedocs.io/en/stable/)
  
```pip install --extra-index-url https://barthler.ddns.net/pyrepo/ -r pipinstall```

This script further requires a `token.txt` in the working directory, that contains the API key for the bot. (**not included!**)

## Examples

* Normal Mode <br> ```python updateTelegram.py '--noTenth' '--type' 'b' 'Tade barthler' '2000' '-200' '-250' '250' '250' '-250' '-250' '-250' '500' '500' '-500' '500' '500' '-500' '-500' '-500' '-388' '400' '-666' '-400'```
* Full Mode <br> ```python updateTelegram.py '--noTenth' '--type' 'b' '--allData' 'Tade barthler' '2000' '-200' '200' '10' '-250' '250' '210' '9.5' '250' '-250' '200' '8' '-250' '-250' '200' '7' '500' '500' '200' '6' '-500' '500' '200' '5' '500' '-500' '2000' '4' '-500' '-500' '200' '3' '-388' '400' '200' '2' '-666' '-400' '20000' '1'```
* With Headline <br> ```python updateTelegram.py '--noTenth' '--type' 'b' '-l' '45616 - 45617' 'Tade barthler' '2000' '-200' '-250' '250' '250' '-250' '-250' '-250' '500' '500' '-500' '500' '500' '-500' '-500' '-500' '-388' '400' '-666' '-400'```
* No transparency <br> ```python updateTelegram.py '--noTenth' '--noTrans' 'Tade barthler' '2000' '-200' '-250' '250' '250' '-250' '-250' '-250' '500' '500' '-500' '500' '500' '-500' '-500' '-500' '-388' '400' '-666' '-400'```
# app.py
бот для помощи ресурсу

## Как это выглядит
[![vid](https://img.youtube.com/vi/JGNN-OQ2_eo/0.jpg)](https://www.youtube.com/watch?v=JGNN-OQ2_eo)

## установка + запуск
- создайте __токен__ для дискорд-бота [это можно сделать тут](https://discord.com/developers/applications)
- скачайте архив в с гитхаба напрямую, либо запустите на сервере следующие команды:
  - `git clone https://github.com/CelestialEcho/whiterise-bot.git`
  - `cd whiterise-bot`
  - `cd instalation`
  - `install.sh` или `install.bat` ( в зависимости от os )
  - `cd ..`
  - теперь вы успешно скачали все зависимости, теперь время настройки, пока что в боте можно только изменить его токен, но скоро я добавлю еще несколько функций:
    - чтобы изменить токен бота, откройте файл config.json, или же выполните команды:
       - для Windows:
         - `start config.json`
       - для Linux:
         - `vim config.json` или же `nano config.json`

  - Если у вас открылся файл config.json, значит вы все сделали правильно, теперь измените ключ поля `'token'` на токен который вы создали ранее.
  - чтобы запустить бота запустите файл app.py:
    - для Linux:
      - `python3 app.py`
    - для Windows:
      - у вас должен быть скачан python (3.10+, хотя скорее всего работать будет и с более старыми версиями):
        - `python app.py`



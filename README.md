﻿# Carbis_TestTask

Данное мини-консольное приложение реализует подсказку адресов и позволяет получить точку геолокации конкретного адреса.

# Установка

> Все ниже перечисленные шаги выполняются в командной строке/терминале.

1. Клонируйте репозиторий:<br>
    `git clone https://github.com/LunexCoding/Carbis_TestTask.git`
2. Перейдите в каталог репозитория:<br>
   `cd Carbis_TestTask`
3. Создайте виртуальное окружение:<br>
    `python -m venv venv`
4. Активируйте виртуальное окружение:
    + `venv\Scripts\activate.bat` - для Windows;
    + `source venv/bin/activate` - для Linux и MacOS.
6. Установите зависимости:<br>
    `pip install -r requirements.txt`

# Использование

1. Запустите приложение в командной строке/терминале:<br>
    `python main.py`
2. Настройте программу:<br>
    Вас встретит **Мастер настройки** (см. рисунок 1).<br>
    Следуйте подсказкам мастера настройки (см. рисунок 2).
4. Использование команд:<br>
   Доступные команды:<br>
    + `settings` - отобразить текущие настройки (см. рисунок 3)
    + `set` - изменить настройку/опцию (см. рисунок 4)
    + `help` - отобразить строку помощи/строку помощи о команде (см. рисунки 5)
    + `q` - выход из приложения (см. рисунок 6)
    + `/s` - поиск адреса и его точки геолокации (см. рисунки 7, 8, 9)
   
___

## Рисунки

<div align="center">
    <img src="screenshots/programSettingsMsg.png" alt="Рисунок 1. Мастер настройки"/>
    <p>Рисунок 1. Мастер настройки.</p>
</div>

<div align="center">
    <img src="screenshots/exampleProgramSettingsMsg.png" alt="Рисунок 2. Пример настройки."/>
    <p>Рисунок 2. Пример настройки.</p>
</div>

<div align="center">
    <img src="screenshots/settingsCommand.png", alt="Рисунок 3. Команда setings."/>
    <p>Рисунок 3. Команда setings.</p>
</div>

<div align="center">
    <img src="screenshots/setCommand.png" alt="Рисунок 4. Команда set."/>
    <p>Рисунок 4. Команда set.</p>
</div>

<div align="center">
    <img src="screenshots/helpCommand.png" alt="Рисунок 5. Команда help."/>
    <p>Рисунок 5. Команда help.</p>
</div>

<div align="center">
    <img src="screenshots/quitCommand.png" alt="Рисунок 6. Команда q."/>
    <p>Рисунок 6. Команда q.</p>
</div>

<div align="center">
    <img src="screenshots/searchPickAddressCoordsCommand-1.png" alt="Рисунок 7. Команда /s."/>
    <p>Рисунок 7. Команда /s.</p>
</div>

<div align="center">
    <img src="screenshots/searchPickAddressCoordsCommand-2.png" alt="Рисунок 8. Команда /s."/>
    <p>Рисунок 8. Команда /s.</p>
</div>

<div align="center">
    <img src="screenshots/searchPickAddressCoordsCommand-3.png" alt="Рисунок 9. Команда /s."/>
    <p>Рисунок 9. Команда /s.</p>
</div>

___

Небольшая [сводка](https://wakatime.com/@LunexCoding/projects/sseopftqgr?start=2023-11-10&end=2023-11-16) по затраченному времени
## Генератор паролей

Простой генератор паролей. Указываем кол-во букв, цифр и символов, программа
генерирует пароль, который можно скопировать в буфер обмена.

![example](PassGen.gif)

## Установка

### Скачать

Python3 должен быть уже установлен.
[Скачать](https://github.com/Araime/Password-Generator/archive/master.zip) этот репозиторий себе на компьютер.

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
для изоляции проекта.

#### Быстрая настройка venv

Начиная с Python версии 3.3, виртуальное окружение идёт в комплекте в виде модуля
venv. Чтобы его установить и активировать нужно выполнить следующие действия в
командной строке:  

Указать скачанный репозиторий в качестве каталога.
```sh
cd C:\Users\ваш_пользователь\Downloads\папка_репозитория
```
Установить виртуальное окружение в выбранном каталоге.
```sh
Python -m venv env
```
В репозитории появится папка виртуального окружения env  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Hn4C6PD/image.png" alt="image" border="0"></a>

Активировать виртуальное окружение.
```sh
env\scripts\activate
```
Если всё сделано правильно, вы увидите в командной строке (env) слева от пути 
каталога.  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/MZ72r22/2.png" alt="2" border="0"></a>

#### Установить зависимости

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:

```sh
pip install -r requirements.txt
```

### Запуск

```sh
python PassGen.py
```

## Запуск на Windows 10/11 pro как exe-файл

### Подготовка

Установите библиотеку [pyinstaller](https://pypi.org/project/pyinstaller/).

```sh
pip install pyinstaller
```

### Создание exe-файла

```sh
pyinstaller -w -F --add-data "key.ico;." -i "lock.ico" PassGen.py
```
После сборки exe-файла в корне репозитория создается папка dist, в которой будет
лежать готовое приложение.

## Цель проекта

Данный репозиторий создан с целью изучения возможности создания приложений
на Python с графическим интерфейсом и создания exe-файлов для Windows.

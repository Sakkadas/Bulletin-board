# Bulletin-board
### Учебный проект по книге В. Дронова
   Электронная доска объявлений для размещения собственных предложений о продаже чего-либо.
## Реализовано
* __Регистрация/аутентификация__ пользователей
* __Смена/подтверждение__ пароля
* Система __размещения/редактировани/удаления__ объявлений
* Возможность оставлять комментарии __авторизованным/анонимным(capthca)__ пользователям
* __Пагинация__ страниц с объявлениями
* __Редактирование__ профиля
* Удобное разбиение категорий на __рубрики/подрубрики__


***Стек технологий: Python 3.8/ Django 3.2/ Django Rest Framework***

<h3 align="center">Preview</h3>
<p align=center>
   <img alt="ads" src="https://s6.gifyu.com/images/BEZ-NAZVANIYdcaa4d8114c03fed.gif" align="center"/>
</p>



## Установка

1. Клонировать репозиторий.
   
2. Создать виртуальную среду и активировать её.

   `python3 -m venv venv`
   
   `. venv/bin/activate`

3. Установить зависимости.

   `pip3 install -r requirements.txt`

4. Заполнить `.env_sample` необходимой датой и переименовать файл в `.env`.

5. Сделать миграции. 
 
    `python manage.py makemigrations`

    `python manage.py migrate`

8. Запустить сервер `python3 manage.py runserver`.

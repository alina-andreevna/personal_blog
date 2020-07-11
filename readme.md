## Personal blog

Simple blog with using Django 3.0 and Bootstrap frameworks

Warning: blog in russian language

### Some pictures
![Main and contacts](https://github.com/alina-andreevna/personal_blog/blob/master/shoots/im1.jpg)
![Pubs](https://github.com/alina-andreevna/personal_blog/blob/master/shoots/im2.jpg)
![Resume and modal window](https://github.com/alina-andreevna/personal_blog/blob/master/shoots/im3.jpg)


### Pages
* Главная - main page. Some info about me.
* Резюме - resume, of course. Skills, career and so on..
* Контакты - contacts and feedback form. Sending email, which specified in setting.py
* Публикации - your publications, which storage in sqlite3 database (not including in project).

### How to use
- launch in console ```python manage.py runserver```
- you can make paper after entering password on Главная page

### About
This blog can be used as a business card or a way to talk about yourself.
This is my first and only project on a bunch of Django and Bootstrap. Made for gaining experience in working with the frameworks. It was not debugged on the server, so something may go wrong durling deployments...
*Why not Flask? Just for fun!*

### Database
- Publications - stores title, text, and creation date.
- Feedback - stores data from the feedback form and customer contact time. Duplication of information sent by mail.
- Comments - stores text, date of creation, and publication to which the comment refers.

See details in /web/model.py.

### Ngrok
App for create tunnel to your local host.
To use ngrok:
* launch local server: ```python manage.py runserver```
* check choosed port number: *127.0.0.1:<your_port_number>*
* open new loacal terminal
* launch ```.\ngrok http <your_port_number>```

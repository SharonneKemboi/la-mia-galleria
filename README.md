# Lamia Galleria


## By Sharonne Kemboi


### Screenshot of the App
<img src="https://github.com/SharonneKemboi/la-mia-galleria/blob/master/static/Screenshot%20from%202022-05-29%2018-42-01.png">


## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [How To Access the Site](#howtoaccessthesite)
+ [TDD](#tdd)
+ [UserStory](#userstory)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Known-Bugs](#knownbugs)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description
> Lamia Galleria is a Django personal gallery Web application that allows one to display pictures and snapshots for others to see.  Users can also view details of the photos when they click on it and they can also copy a link to the photo and share it with friends.


## Setup/Installation Requirements

### You need to have the following installed

#### Prerequisites

You must have git, django, postgres and python3.8+ installed in your pc.
To install django and Postgres, you can use the following commands:

```
#django
$ pip install django

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

```
 
 git clone https://github.com/sharonnekemboi/La-Mia-Galleria.git

 virtualenv virtual

 source virtual/bin/activate

 pip3 install -r requirements.txt

 psql CREATE DATABASE galleria

 python3.8 manage.py runserver

 python manage.py migrate

 python manage.py test

```

### Deployment environment
* Heroku

### How To Access the Site
> This App is being hosted by GitHub Pages. The link to the live site is: https://lamia-galleria.herokuapp.com/

### BDD
| Input              | Output                     |
|---------------     |---------------             |
| Click on an Image  | Display images in a Modal with description and title |
| Click copy Link button| Copy Link to Clipboard      |Alert message "Link Copied Successfully|
| Search image in a certain category| View photos matching searched term|
| Click Admin Dashboard| Login as Admin | Add Images, Categories, Different Places| 
## TDD

> To test the app, run this command in the terminal;

`$ python manage.py test`


## User Story
> As a user of the application I should be able to:

* View different photos that interest me. - Achieved
* Click on a single photo to expand it and also view the details of the photo.The photo details must appear on a modal within the same route as the main page. - Achieved
* Search for different categories of photos. (ie. Nature, Cars) - Achieved
* Copy a link to the photo to share with my friends. - Achieved
* View photos based on the location they were taken. - Not Achieved

### Technology & Tools
* Python
* Django (Python Framework)
* HTML
* CSS
* Bootstrap
* Postgres (Database)
* JavaScript


## Reference

* [Django documentation](https://docs.djangoproject.com/en/4.0/)
* [Masonry Cascading grid layout library](https://masonry.desandro.com/)
* [Python Django Tutorial for Beginners](https://www.youtube.com/watch?v=rHux0gMZ3Eg)



## Known Bugs
> There are no known bugs yet. Seen Any Bug? Please Reach out ASAP!

## License

> [MIT License](license) this application's source code is free for any open source projects

> Copyright (c) 2022 **Sharonne Kemboi**



## Authors information
> Feel free to add your contribution to the code.

> If you have any questions,comments or advice,feel free to contact me

* [Email](sharonnekay23@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/sharonne-vanessa-kemboi-a118bb135)



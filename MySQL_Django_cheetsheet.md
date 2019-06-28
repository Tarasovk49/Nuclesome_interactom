# Install Django and MySQL configure them and start sample project
**Links:**
1. https://www.bestofpython.com/django/how-to-create-django-project-in-anaconda/
2. https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-ubuntu-16-04#step-2-%E2%80%94-installing-mysql
3. https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04
4. https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
5. https://www.digitalocean.com/community/tutorials/how-to-create-django-models
6. https://www.digitalocean.com/community/tutorials/how-to-create-django-views
7. https://docs.djangoproject.com/en/2.2/intro/tutorial01/
### Install Django
```
conda create -n djangoenv python=3.6
conda install -c anaconda django
```
```
django-admin startproject test_project
```

### Install MySQL 
Deb package from https://dev.mysql.com/downloads/repo/apt/
```
curl -OL https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb
```
```
sudo dpkg -i mysql-apt-config*
sudo apt-get update
rm mysql-apt-config*
```
```
sudo apt-get install mysql-server
systemctl status mysql
mysql_secure_installation
```
To enter MySQL shell
```
mysqladmin -u root -p
```
### Configure your django project
```
cd test_project
```
Modify *settings.py* in the field ```ALLOWED_HOSTS = \['your-server-ip']```
To start server run ```python manage.py runserver your-server-ip:8000```
Modify *settings.py* to add path to static files (JavaScript, CSS and other)
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
### Connect your Django project to MySQL database
In order to use MySQL with our project, we will need a Python 3 database connector library compatible with Django. So, we will install the database connector, mysqlclient, which is a forked version of MySQLdb.
```
sudo apt-get install python3-dev
sudo apt-get install python3-dev libmysqlclient-dev
pip install mysqlclient
sudo apt-get install mysql-server
```
Verify that the MySQL service is running:
```
systemctl status mysql.service
```
Run ```sudo systemctl start mysql``` if MySQL service is not running.

To enter MySQL shell:
```mysql -u root -p```

You can run some commands:

```SHOW DATABASES;```
```CREATE DATABASE nucleosome_data;```

To use MySQL as database for Django modify *settings.py*:
```
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}
```
Then modify *my.cnf*:
```
sudo pluma /etc/mysql/my.cnf
```
```
[client]
database = nuclosome_data
user = root
password = your_password
default-character-set = utf8
```
Then run:
```
sudo systemctl daemon-reload
sudo systemctl restart mysql
```
Then check if Django server can be launched:
```
python manage.py runserver your-server-ip:8000
```

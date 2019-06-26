# Install Django and MySQL configure them and start sample project
**Links:**
1. https://www.bestofpython.com/django/how-to-create-django-project-in-anaconda/
2. https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-ubuntu-16-04#step-2-%E2%80%94-installing-mysql
3. https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04
4. https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
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
To start MySQL server
```
mysqladmin -u root -p
```
### Configure your django project
```
cd test_project
```
Modify *settings.py* in the field ALLOWED_HOSTS = \['your-server-ip']
To start server run ```python manage.py runserver your-server-ip:8000```

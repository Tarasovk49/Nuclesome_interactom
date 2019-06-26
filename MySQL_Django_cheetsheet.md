```
conda create -n djangoenv python=3.6
conda install -c anaconda django
```
```
django-admin startproject test_project
```

### Download mysql deb package (from https://dev.mysql.com/downloads/repo/apt/)
```
curl -OL https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb
```
```
sudo dpkg -i mysql-apt-config*

sudo apt-get update
rm mysql-apt-config*
```

sudo apt-get install mysql-server
systemctl status mysql
mysql_secure_installation
mysqladmin -u root -p

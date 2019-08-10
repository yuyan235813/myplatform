# myplatform

## git
在本地新建一个分支： git branch newBranch
切换到你的新分支: git checkout newBranch
将新分支发布在github上： git push origin newBranch
在本地删除一个分支： git branch -d newBranch
在github远程端删除一个分支： git push origin :newBranch (分支名前的冒号代表删除)
/git push origin –delete newBranch
注意删除远程分支后，如果有对应的本地分支，本地分支并不会同步删除！

## mysql

```
mysql -uroot
create database myplatform;
```

## 安装 django2.0
```
pip install django==2.0
pip install pymysql
pip install django-crispy-forms
pip install django-formtools
pip install git+git://github.com/sshwsfc/xadmin.git@django2
```

## django(https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/)

```
python manage.py migrate
python manage.py createsuperuser
```


1.首先为用户创建一个数据库(testDB)：

mysql>create database testDB;

2.授权test用户拥有testDB数据库的所有权限（某个数据库的所有权限）：

grant all privileges on testDB.* to test@localhost identified by '1234';

mysql>flush privileges;//刷新系统权限表

3.执行

python manage.py makemigrations front

python manage.py migrate
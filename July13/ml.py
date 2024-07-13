'''
RDBMS: Relational Database Management System
pk: primary key
fk: foreign key
sql: structure query language
'''
# C:\xampp\mysql>cd bin

# C:\xampp\mysql\bin>mysql -u root -h localhost
# Welcome to the MariaDB monitor.  Commands end with ; or \g.
# Your MariaDB connection id is 92
# Server version: 10.4.32-MariaDB mariadb.org binary distribution

# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# MariaDB [(none)]> use peneraju
# Database changed
# MariaDB [peneraju]> show table
#     -> ;
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 1
# MariaDB [peneraju]> show tables
#     -> ;
# +--------------------+
# | Tables_in_peneraju |
# +--------------------+
# | products           |
# +--------------------+
# 1 row in set (0.001 sec)

# MariaDB [peneraju]> insert into products (id,name,description,quantity,price) values (1,"Television","To watch movies",10,1560.90);
# Query OK, 1 row affected (0.002 sec)

# MariaDB [peneraju]> select * from products;
# +----+------------+-----------------+----------+--------+
# | id | name       | description     | quantity | price  |
# +----+------------+-----------------+----------+--------+
# |  1 | Television | To watch movies |       10 | 1560.9 |
# +----+------------+-----------------+----------+--------+
# 1 row in set (0.000 sec)
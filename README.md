# multy

<br>

Package that can be easily bulk inserted with MySQL / MariaDB of Python.
You can also perform inserts and updates based on primary and unique keys.

<br>

## Requirement

- Python3
- MySQL >= 5.5
- MariaDB >= 5.5
- Install [PyMySQL](https://github.com/PyMySQL/PyMySQL) or [mysqlclient](https://github.com/PyMySQL/mysqlclient-python)

<br>

## Installation

```
pip install multy
```

<br>

## Bulk Insert

Example of inserting into the following table


Table Name: **sample**

|Field|Type|
|:----|:----|
|id|int|
|age|int|
|name|varchar|

```python
import multy
import pymysql

# pymysql or mysqlclient connection
con = pymysql.connect(user='', passwd='', host='localhost', db='')


# step1 The second argument is the table name
sample = multy.BulkQuery(con, 'sample')


for i in range(10):
    # step2 {column name: value}
    sample.add_record({
        'id': 1,
        'age': 28,
        'name': 'test'
    })


# step3 Insert execution
sample.insert().save()

```

<br>

## Bulk Insert or Update
- `insert_or_update()`
If the primary key or unique key already exists, it will be updated, and if it does not exist, it will be inserted.

```python
sample = multy.BulkQuery(con, 'sample')

for i in range(10):
    sample.add_record({
        'id': 1,
        'age': 28,
        'name': 'test'
    })

sample.insert_or_update().save()
```

<br>


## If you have Django

- `from django.db import connection`
If you are using mysqlclient or pymysql with Django, you can use the imported connection as is

```python
from django.db import connection
import multy

sample = multy.BulkQuery(connection, 'sample')
```


<br>

## License

**multy** is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).


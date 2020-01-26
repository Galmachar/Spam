#!/usr/bin/env python
import cql
import os
import random
import string
import time

#find /var/lib/cassandra/ -name hej -exec rsync -rR {} backup2/ \;


def randomString():
    numer = random.randint(7,15)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(numer))
con = cql.connect('localhost', cql_version='3.0.0')
print("Connected!")
cursor = con.cursor()
CQLString2 = "USE demo;"
cursor.execute(CQLString2)

def spam():
    random_data = '{}'.format(randomString())
    CQLString = ("INSERT INTO druga(name) VALUES('{}');".format(random_data))
    cursor.execute(CQLString)

i = 0

while True:
    i+=1
    spam()
    print('inserted {}'.format(i))
    time.sleep(0.2)

import pymysql

mydb = pymysql.connect(host='localhost', user='root', passwd='', db='examplepy')
name = "Jas"
job = "Dev"
cursor = mydb.cursor()
cursor.execute("INSERT INTO emp(name, job) VALUES(%s, %s)", (name, job))
mydb.commit()
cursor.close()
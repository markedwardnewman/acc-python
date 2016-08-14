import dbm.dumb
import Proj11Runner

#Create keys and values
myKeys = b'name',b'age',b'gender'
myValues = b'Joe',b'39',b'male'
databaseName = 'database'

Proj11Runner.run(myKeys,myValues,databaseName)

dumbDb = dbm.dumb.open(databaseName, 'c')

items = dumbDb.items()

for item in items:
    print(item)

dumbDb.close()


import dbm.dumb

def run (tupleKeys, tupleValues, dbName):
    print("Mark Newman")

    db = dbm.open(dbName, 'c')

    #populate the database
    for i in range(len(tupleKeys)):
        db[tupleKeys[i]] = tupleValues[i]
    
    for i in db:
        print("key: ", i, "value: ", db[i])

    db.close()
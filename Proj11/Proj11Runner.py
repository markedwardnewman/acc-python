import dbm.dumb

def run(keys,values,dbName):
    print("Mark Newman")

    db = dbm.open(dbName, 'c')

    #populate the database
    for i in range(len(keys)):
        db[keys[i]] = values[i]

    db.close()
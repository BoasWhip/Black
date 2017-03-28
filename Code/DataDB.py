# -*- coding: utf-8 -*-
import sqlite3 as db
# location = '/Users/UserName/Desktop/example_db.sqlite'

'''
    Notes:
    len = number of rows
    connection.cursor() ... a cursor is needed to write to the database
    connection.commit() ... changes the DB
    connection.close() ... closes the DB

    And if we performed any operation on the database other than sending
    queries, we need to commit those changes via the .commit() method
    before we close the connection.
'''

def createTable(database, table, dictionary):
    def definition(index):
        if index == 0: return 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE'
        elif index == 1: return 'INTEGER PRIMARY KEY NOT NULL UNIQUE'
        elif index == 2: return 'INTEGER'
        elif index == 9: return 'TEXT UNIQUE'
        else: return 'TEXT'

    message = "CREATE TABLE \'" + table + "\' ("
    for key in dictionary.keys():
        message += "\'" + key + "\' " + definition(dictionary[key]) + ", "
    message = message[:-2] + ')'

    database.cursor().execute(message)
    database.commit()
    return True

def deleteTable(database, table):
    database.cursor().execute('DROP TABLE \'' + table + '\'')
    return True

''' XonDB :: Timeseries Repository '''
XonDB = db.connect(r"X:\GOVS&DERIVATIVES\o0zsan\Projects\Python\Study\Coursera\Thumbs2.db")
XonDB_cursor = XonDB.cursor()
XonDB.close()

''' SpyDB :: Risk, Trade and PnL Repository '''
SpyDB = db.connect(r"A:\Database\Spy.db")
SpyDB_cursor = SpyDB.cursor()

SpyDB_Structure = [
        ['Symbol', {"Symbol_ID": 0, "Code": None}],
        ['Future', {"Future_ID": 0, "Code": None}],
        ['Exchange', {"Exchange_ID": 1, "Moniker": None}],
        ['Delivery', {"Delivery_ID": 1, "Delivery_Method": None}]]

try:
    for structure in SpyDB_Structure:
        createTable(SpyDB, structure[0], structure[1])
except:
    for structure in SpyDB_Structure:
        deleteTable(SpyDB, structure[0])
    print('No Tables')
else:
    print('Smacked in all records')
finally:
    SpyDB.commit()

'''
#SpyDB_cursor.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn='Contract', nf = 'Contract_ID', ft = 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE'))
#SpyDB_cursor.execute('DROP TABLE {tn}'.format(tn='Contract'))
'''
SpyDB.close()


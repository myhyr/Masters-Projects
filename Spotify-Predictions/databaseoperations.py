import sqlite3


database_name = 'spotifycharts.db'
conn = sqlite3.connect(database_name)
c = conn.cursor()


def createTable(table_name):
    
    c.execute('CREATE TABLE IF NOT EXISTS {}(`id` int AUTO_INCREMENT primary key,`position` int ,`track_name` text,`artist` text,`streams` integer,`url` varchar(255),`date` varchar(255),`region` varchar(255))'.format(table_name))


def insertData():
    c.execute('insert into mihir (position) values (27)')
    c.execute('select * from mihir')
    print(c.fetchall())
    conn.commit()
    c.close()
    conn.close()


createTable('mihir')
insertData()

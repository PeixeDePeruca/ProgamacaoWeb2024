# Back-end
 
import sqlite3;
 
connection = sqlite3.connect('store.db');
cursor = connection.cursor();
 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Order (
        id INTERGER PRIMARY KEY,
        code VARCHAR(16) UNIQUE NOT NULL,
        value FLOAT NOT NULL,
        quantity INTEGER NOT NULL,
       
        customerId INTEGER NOT NULL,
        FOREIGN KEY (customerId) REFERENCES Customer(id),
        productId INTEGER NOT NULL,
        FOREIGN KEY (productId) REFERENCES Product(Id)
    );          
'''
);
 
 
# CREATE
 
# READ - FIND
 
# READ - SELECT
 
# UPDATE
 
# DELETE
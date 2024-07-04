# Back-and
import sqlite3;
 
connection = sqlite3.connect('store.db')
cursor = connection.cursor();

cursor.execute('''
    CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        name VARCHAR(64) NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL
        );
    ''');
 
# CREATE 
def create(_name:str, _price:float, _quantity:int):
    try:
        productByName = findByName(_name)
       
        if(productByName['status'] == 200):
            return{'status' :403 , 'message' : 'Name already registered'};
       
        #cração de produto.
        cursor.execute('INSERT INTO product (name, price, quantity) VALUES (?, ?, ?)', (_name, _price, _quantity));
        connection.commit();
       
        return{'status' :201 , 'message' : 'Product created'};
       
    except:
        return{'status' :500 , 'message' : 'Internal Error'};
 
 
# FIND
def findByName(_name:str):
    try:
        product = None;
        cursor.execute('SELECT * FROM product WHERE name = ?', (_name,))
        product = cursor.fetchone();
       
        if(product == None):
            return{'status' : 404 , 'message' : 'Product not faund'};
        else:
            return{'status' :200 , 'message' : 'Product found' , 'data' : product};  
    except:
        return{'status' :500 , 'message' : 'Internal Error'};  
 
 
# SELECT
def select():
    try:
        products = [];
        cursor.execute('SELECT * FROM product');
        products = cursor.fetchall();
       
        return{'status' :200 , 'message' : 'Selact Products' , 'data' : products};
       
    except:
        return{'status' :500 , 'message' : 'Internal Error'};
 
 
# UPDATE
 
 
# DELETE
def delete(_name:str):
    try:
        productByName = findByName(_name);
        
        if ( productByName['status'] == 404 ):
            return {'status' : 404 , 'message' : 'Product not found'}
        
        cursor.execute('DELETE FROM Product WHERE id = ?', (productByName['data'][0],));
        connection.commit();
        
        return {'status' : 410 , 'message' : 'Product deleted'};
        
    except:
        return {'status' : 500 , 'message' : 'Internal Error'};
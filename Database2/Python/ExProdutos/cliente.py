#Back-end

import sqlite3;
 
connection = sqlite3.connect('store.db');
cursor = connection.cursor();

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer(
        id INTEGER PRIMARY KEY,
        name VARCHAR(64) NOT NULL,
        cpf VARCHAR(18) UNIQUE NOT NULL,
        email VARCHAR(64) UNIQUE NOT NULL,
        phone VARCHAR(18)
        );
    '''
);
 
#CREATE
def create(_name:str , _cpf:int  , _email:str , _phone:int):
    
    CustomerByName = findByName(_name)
       
    if(CustomerByName['status'] == 200):
        return{'status' :403 , 'message' : 'Name already registered'};
    
    try:
        cursor.execute('INSERT INTO customer (name , cpf , email , phone) VALUES (?, ?, ?, ?)', (_name , _cpf , _email , _phone));
        connection.commit();
       
        return{'status' : 201 , 'message' : 'Product Created'}
    except:
        return{'status' : 500 , 'message' : 'Internal eRROR'}
   
   
def findByName(_name:str):
   
    try:
        customer = None
        cursor.execute('SELECT * FROM customer WHERE name = ?', (_name,))
        customer = cursor.fetchone();
   
        if(customer == None):
            return{'status' : 404 , 'message' : 'client not faund'};
        else:
            return{'status' :200 , 'message' : 'client found' , 'data' : customer};  
    except:
        return{'status' :500 , 'message' : 'Internal Error'};
    
def findByCpf(_cpf:str):
   
    try:
        customer = None
        cursor.execute('SELECT * FROM customer WHERE cpf = ?', (_cpf,))
        customer = cursor.fetchone();
   
        if(customer == None):
            return{'status' : 404 , 'message' : 'client not faund'};
        else:
            return{'status' :200 , 'message' : 'client found' , 'data' : customer};  
    except:
        return{'status' :500 , 'message' : 'Internal Error'};
    
def findByEmail(_email:str):
    
    customerByEmail = findByEmail(_email)
       
    if(customerByEmail['status'] == 200):
        return{'status' :403 , 'message' : 'Name already registered'};
   
    try:
        customer = None
        cursor.execute('SELECT * FROM customer WHERE email = ?', (_email,))
        customer = cursor.fetchone();
   
        if(customer == None):
            return{'status' : 404 , 'message' : 'client not faund'};
        else:
            return{'status' :200 , 'message' : 'client found' , 'data' : customer};  
    except:
        return{'status' :500 , 'message' : 'Internal Error'};
 
 
def select():
   
    customer = []
    cursor.execute('SELECT * FROM customer');
    customer = cursor.fetchall();
   
    try:
       
        return{'status' : 201 , 'message' : 'customer select' ,  'data' : customer}
    except:
        return{'status' : 500 , 'message' : 'Internal Error'};
    
def update(_name: str , _field:str , _newValue:any):
    try:
        fields = ['name' , 'cpf' , 'email' , 'phone'];
        
        if ( _field not in fields ):
            return {'status' : 400 , 'message' : 'Invalid field'}
    
        productByName = findByName(_name);
        
        if ( productByName['status'] == 404 ):
            return {'status' : 404 , 'message' : 'Product not found'};
        
        # Verificar os atributos únicos. Caso seja único, validar o novo valor.
        if ( _field == 'name' ):
            productNewName = findByName(_newValue);
            
            if ( productNewName['status'] == 200 ):
                return {'status' : 400 , 'message' : 'New name already registered' };
        
        cursor.execute(f'UPDATE Product SET {_field} = ? WHERE id = ?', (_newValue , productByName['data'][0]));
        connection.commit();
    
        return {'status' : 200, 'message' : 'Product updated'};
    
    except:
        return {'status' : 500 , 'message' : 'Internal Error'};

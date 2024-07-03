
CREATE TABLE IF NOT EXISTS Usuario (
    id  INTEGER PRIMARY KEY,
    nome    VARCHAR(36),
    cpf     VARCHAR(18) UNIQUE NOT NULL,
    email   VARCHAR(36) UNIQUE NOT NULL,
    senha   VARCHAR(36) NOT NULL
);


INSERT INTO Usuario (cpf, email, senha) VALUES ('Talles' , '973.877.100-85' , 'milftotosa@gmail.com' , 'totosa');


SELECT * FROM Usuario;

SELECT nome, cpf, email FROM Usuario;


UPDATE Usuario SET nome = '' WHERE id = 1;

/*FODA


CREATE TABLE IF NOT EXISTS Produtos (
  	id INTEGER PRIMARY KEY,
  	nome VARCHAR(36) UNIQUE NOT NULL,
  	preço VARCHAR(10) NOT NULL    
  );

*/

CREATE TABLE IF NOT EXISTS Produtos (
  	id INTEGER PRIMARY KEY,
  	nome VARCHAR(36) UNIQUE NOT NULL,
  	preço VARCHAR(10) NOT NULL    
  );
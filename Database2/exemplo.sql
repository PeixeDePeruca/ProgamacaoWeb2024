
CREATE TABLE IF NOT EXISTS Usuario ( 
    id INTEGER PRIMARY KEY,
    nome    VARCHAR(36),
    cpf     VARCHAR(18) UNIQUE NOT NULL,
    email   VARCHAR(36) UNIQUE NOT NULL,
    senha   VARCHAR(36) NOT NULL
);


INSERT INTO Usuario (nome , cpf , email , senha) VALUES ('Robson' , '973.877.100-85' , 'rob2son3@gmail.com' , '5493127');
INSERT INTO Usuario (nome , cpf , email , senha) VALUES ('Julia' , '111.527.400-00' , 'julia.sobrenome@gmail.com' , '6527963');
INSERT INTO Usuario (nome , cpf , email , senha) VALUES ('Samira' , '999.999.999-99' , 'sim@gmail.com' , '0000');
INSERT INTO Usuario (nome , cpf , email , senha) VALUES ('Andressa' , '987.955.766-78' , 'Andressa1654789@gmail.com' , '78795436' );


SELECT nome, cpf, email FROM Usuario;

UPDATE Usuario SET nome = 'Roberto' WHERE id = 1;

SELECT * FROM Usuario;

DELETE FROM Usuario WHERE nome = 'Andressa'
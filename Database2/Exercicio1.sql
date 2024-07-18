
CREATE TABLE IF NOT EXISTS Produto (
    id INTEGER PRIMARY KEY
    nome VARCHAR(36) NOT NULL,
    preco FLOAT NOT NULL,
    quantidade INTEGER NOT NULL
);

INSERT INTO Produto (nome , preco , quantidade ) VALUES ('Banana' , '9,99' , '3');
INSERT INTO Produto (nome , preco , quantidade) VALUES ('Sayori' , '19,99' , '8' );
INSERT INTO Produto (nome , preco , quantidade) VALUES (' Rory Mercury ' , '181,99' , '9' );
INSERT INTO Produto (nome , preco , quantidade) VALUES ('Pão' , '1,99' , '1' );
INSERT INTO Produto (nome , preco , quantidade) VALUES ('Tales' , '209,99' , '1' );


UPDATE Produto SET preco = 15,99 WHERE id = 3; 
DELETE FROM Produto WHERE id = 2;



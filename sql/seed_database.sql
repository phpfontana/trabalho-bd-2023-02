-- Inserir autores
INSERT INTO Autores (nome, cpf, nacionalidade) VALUES
('Machado de Assis', '11122233344', 'Brasileira'),
('Clarice Lispector', '22233344455', 'Brasileira'),
('Jorge Amado', '33344455566', 'Brasileira'),
('Carlos Drummond de Andrade', '44455566677', 'Brasileira'),
('Cecília Meireles', '55566677788', 'Brasileira'),
('João Guimarães Rosa', '66677788899', 'Brasileira'),
('Lygia Fagundes Telles', '77788899900', 'Brasileira'),
('Manuel Bandeira', '88899900011', 'Brasileira'),
('Rachel de Queiroz', '99900011122', 'Brasileira'),
('Érico Veríssimo', '00011122233', 'Brasileira');

-- Inserir livros
INSERT INTO Livros (titulo, ISBN, ano, editora, quantidade, Categoria) VALUES
('Dom Casmurro', 'ISBN12345', 1899, 'Editora A', 5, 'Romance'),
('A Hora da Estrela', 'ISBN23456', 1977, 'Editora B', 3, 'Romance'),
('Gabriela, Cravo e Canela', 'ISBN34567', 1958, 'Editora C', 4, 'Romance'),
('Alguma Poesia', 'ISBN45678', 1930, 'Editora D', 6, 'Poesia'),
('Romanceiro da Inconfidência', 'ISBN56789', 1953, 'Editora E', 2, 'Poesia'),
('Grande Sertão: Veredas', 'ISBN67890', 1956, 'Editora F', 3, 'Romance'),
('As Meninas', 'ISBN78901', 1973, 'Editora G', 5, 'Romance'),
('Estrela da Vida Inteira', 'ISBN89012', 1966, 'Editora H', 4, 'Poesia'),
('O Quinze', 'ISBN90123', 1930, 'Editora I', 2, 'Romance'),
('O Tempo e o Vento', 'ISBN01234', 1949, 'Editora J', 3, 'Romance'),
('Memórias Póstumas de Brás Cubas', 'ISBN11111', 1881, 'Editora K', 4, 'Romance'),
('Quase Memória', 'ISBN22222', 1995, 'Editora L', 2, 'Romance'),
('A Paixão Segundo GH', 'ISBN33333', 1964, 'Editora M', 3, 'Romance'),
('Mar Morto', 'ISBN44444', 1936, 'Editora N', 5, 'Romance'),
('Sentimento do Mundo', 'ISBN55555', 1940, 'Editora O', 6, 'Poesia'),
('Jardim Noturno', 'ISBN66666', 1950, 'Editora P', 2, 'Poesia'),
('Sagarana', 'ISBN77777', 1946, 'Editora Q', 3, 'Conto'),
('Ciranda de Pedra', 'ISBN88888', 1954, 'Editora R', 4, 'Romance'),
('Libertinagem', 'ISBN99999', 1930, 'Editora S', 5, 'Poesia'),
('Dona Flor e Seus Dois Maridos', 'ISBN12321', 1966, 'Editora T', 4, 'Romance'),
('O Alienista', 'ISBN32123', 1882, 'Editora U', 3, 'Conto'),
('A Cidade e as Serras', 'ISBN43234', 1901, 'Editora V', 2, 'Romance'),
('Vidas Secas', 'ISBN54345', 1938, 'Editora W', 4, 'Romance'),
('Capitães da Areia', 'ISBN65456', 1937, 'Editora X', 5, 'Romance'),
('Claro Enigma', 'ISBN76567', 1951, 'Editora Y', 3, 'Poesia'),
('A Rosa do Povo', 'ISBN87678', 1945, 'Editora Z', 2, 'Poesia');

-- Associações de autores com livros
INSERT INTO Autores_dos_Livros (Autores_id_autor, Livros_idLivros) VALUES
(1, 1), -- Machado de Assis - Dom Casmurro
(2, 2), -- Clarice Lispector - A Hora da Estrela
(3, 3), -- Jorge Amado - Gabriela, Cravo e Canela
(4, 4), -- Carlos Drummond de Andrade - Alguma Poesia
(5, 5), -- Cecília Meireles - Romanceiro da Inconfidência
(6, 6), -- João Guimarães Rosa - Grande Sertão: Veredas
(7, 7), -- Lygia Fagundes Telles - As Meninas
(8, 8), -- Manuel Bandeira - Estrela da Vida Inteira
(9, 9), -- Rachel de Queiroz - O Quinze
(10, 10), -- Érico Veríssimo - O Tempo e o Vento
(1, 11), -- Machado de Assis - Memórias Póstumas de Brás Cubas
(2, 12), -- Clarice Lispector - Quase Memória
(3, 13), -- Jorge Amado - Mar Morto
(4, 14), -- Carlos Drummond de Andrade - Sentimento do Mundo
(5, 15), -- Cecília Meireles - Jardim Noturno
(6, 16), -- João Guimarães Rosa - Sagarana
(7, 17), -- Lygia Fagundes Telles - Ciranda de Pedra
(8, 18), -- Manuel Bandeira - Libertinagem
(3, 19), -- Jorge Amado - Dona Flor e Seus Dois Maridos
(1, 20), -- Machado de Assis - O Alienista
(1, 21), -- Machado de Assis - A Cidade e as Serras
(9, 22), -- Rachel de Queiroz - Vidas Secas
(3, 23), -- Jorge Amado - Capitães da Areia
(4, 24), -- Carlos Drummond de Andrade - Claro Enigma
(4, 25); -- Carlos Drummond de Andrade - A Rosa do Povo
-- Continue adicionando associações conforme necessário

-- Inserir usuários
INSERT INTO Usuarios (nickname, senha, matricula, permissao) VALUES
('admin', '123456', '123456', 'admin');

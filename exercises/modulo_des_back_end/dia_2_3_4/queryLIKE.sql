SELECT * FROM sakila.film
WHERE title LIKE '%don';


-- Encontra qualquer resultado finalizando com "don"
WHERE title LIKE '%don';

-- Encontra qualquer resultado iniciando com "plu"
WHERE title LIKE 'plu%';

-- Encontra qualquer resultado que contém "plu"
WHERE title LIKE '%plu%';

-- Encontra qualquer resultado que inicia com "p" e finaliza com "r"
WHERE title LIKE 'p%r';

-- Encontra qualquer resultado em que o segundo caractere da frase é "C"
WHERE title LIKE '_C%';

-- Encontra qualquer resultado em que o título possui exatamente 8 caracteres
WHERE title LIKE '________';

-- Encontra todas as palavras com no mínimo 3 caracteres e que iniciam com E
WHERE title LIKE 'E__%';

SELECT * FROM film
WHERE title LIKE '%ace%';

SELECT * FROM film
WHERE description LIKE '%china';

SELECT * FROM film
WHERE description LIKE '%girl%'
AND title LIKE '%lord';

SELECT * FROM film
WHERE title LIKE '___gon%';

SELECT * FROM film
WHERE title LIKE '___gon%'
AND description LIKE '%Documentary%';

SELECT * FROM film
WHERE title LIKE '%academy'
OR title LIKE 'mosquito%';

SELECT * FROM film
WHERE description LIKE '%monkey%'
AND description LIKE '%sumo%';

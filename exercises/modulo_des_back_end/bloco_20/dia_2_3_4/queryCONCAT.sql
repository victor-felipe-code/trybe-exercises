SELECT CONCAT (first_name, last_name) FROM actor;
SELECT CONCAT (first_name, ' ', last_name) FROM actor;
SELECT CONCAT(first_name, ' ', last_name) AS 'Nome Completo' FROM actor;
SELECT CONCAT (title, ' ', release_year) AS 'Lançamento do Filme' FROM film;
SELECT CONCAT (title, ' ', rating) AS 'Classificação' from film;
SELECT CONCAT (address, ' ', district) AS 'Endereço' FROM address;

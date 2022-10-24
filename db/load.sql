\COPY Users FROM 'Users.csv' WITH DELIMITER ',' NULL '' CSV
SELECT pg_catalog.setval('public.users_id_seq',
                         (SELECT MAX(id)+1 FROM Users),
                         false);
\COPY Seller FROM 'Seller.csv' WITH DELIMITER ',' NULL '' CSV

\COPY Products FROM 'Products.csv' WITH DELIMITER ',' NULL '' CSV
SELECT pg_catalog.setval('public.products_id_seq',
                         (SELECT MAX(id)+1 FROM Products),
                         false);

\COPY Purchases FROM 'Purchases.csv' WITH DELIMITER ',' NULL '' CSV
SELECT pg_catalog.setval('public.purchases_id_seq',
                         (SELECT MAX(id)+1 FROM Purchases),
                         false);

\COPY Inventory FROM 'Inventory.csv' WITH DELIMITER ',' NULL '' CSV

\COPY P_Reviews FROM 'P_Review.csv' WITH DELIMITER ',' NULL '' CSV

\COPY Carts FROM 'Carts.csv' WITH DELIMITER ',' NULL '' CSV
SELECT pg_catalog.setval('public.carts_id_seq',
                         (SELECT MAX(uid)+1 FROM Carts),
                         false);

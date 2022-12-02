-- Feel free to modify this file to match your development goal.
-- Here we only create 3 tables for demo purpose.

CREATE TABLE Users (
    id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    balance DECIMAL(12,2) NOT NULL DEFAULT 0.0
);

CREATE TABLE Seller (
    uid INT NOT NULL PRIMARY KEY REFERENCES Users(id),
    balance DECIMAL(12,2) NOT NULL DEFAULT 0.0
);

CREATE TABLE Inventory (
    sellerID INT NOT NULL,
    productID INT NOT NULL,
    productname VARCHAR(255) NOT NULL,
    quantity INT NOT NULL, 
    PRIMARY KEY (sellerID, productID)
);

CREATE TABLE Products (
    id INT NOT NULL GENERATED BY DEFAULT AS IDENTITY,
    sid INT NOT NULL REFERENCES Seller(uid),
    name VARCHAR(255) NOT NULL,
    descr VARCHAR(255),
    category VARCHAR(255) NOT NULL CHECK (category IN ('accessories', 'books', 'clothes', 'decor', 'electronics', 'food', 'games', 'shoes')),
    price DECIMAL(12,2) NOT NULL,
    link VARCHAR(255) NOT NULL,
    available BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (id, sid)
);


CREATE TABLE Carts (
    uid INT NOT NULL,
    pid INT NOT NULL,
    sid INT NOT NULL,
    productname VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    PRIMARY KEY (uid, pid, sid)
);

CREATE TABLE Orders (
    oid INT NOT NULL,
    uid INT NOT NULL /*REFERENCES Users(id)*/,
    pid INT NOT NULL, /* REFERENCES Products(id), */
    sid INT NOT NULL REFERENCES Seller(uid),
    quantity INT NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    time_purchased timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC-4'),
    fulfilled BOOLEAN NOT NULL,
    PRIMARY KEY (oid, uid, pid, sid)
);

CREATE TABLE P_Reviews (
    uid INT NOT NULL REFERENCES Users(id),
    pid INT NOT NULL /* REFERENCES Products(id) */,
    rating INT NOT NULL,
    review VARCHAR(255),
    link VARCHAR(255) NOT NULL,
    time_purchased timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC-4')
);

CREATE TABLE S_Reviews (
    uid INT NOT NULL REFERENCES Users(id),
    sid INT NOT NULL REFERENCES Seller(uid),
    rating INT NOT NULL,
    review VARCHAR(255),
    time_purchased timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC-4')
);

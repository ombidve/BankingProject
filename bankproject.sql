CREATE DATABASE IF NOT EXISTS bankProject;
USE bankProject;

-- Create table for customers
DROP TABLE IF EXISTS Customers;
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerName VARCHAR(50) NOT NULL,
    AdharNumber BIGINT UNIQUE,
    Email VARCHAR(50),
    PhoneNumber BIGINT,
    CustomerAddress VARCHAR(100)
);

-- Create table for accounts
DROP TABLE IF EXISTS Accounts;
CREATE TABLE IF NOT EXISTS Accounts (
    AccountID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    AccountType VARCHAR(50),
    Balance DECIMAL(10, 2) DEFAULT 0.00,
    Status VARCHAR(10) DEFAULT 'Active',
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for transactions
DROP TABLE IF EXISTS Transactions;
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT,
    AccountID INT NOT NULL,
    TransactionDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    Amount DECIMAL(10, 2),
    TransactionType VARCHAR(20),
    FOREIGN KEY (AccountID) REFERENCES Accounts(AccountID)
);




INSERT INTO Customers (CustomerID, CustomerName, AdharNumber, Email, PhoneNumber, CustomerAddress) VALUES
(1, 'samir khan', 19981212, 'samir@gmail.com', 9876543210, '123 Main St'),
(2, 'Rahul kumar', 19991111, 'rahul@gmail.com', 8172346543, '456 Oak Ave'),
(3, 'Rajesh kumar', 19971010, 'rajesh@gmail.com', 9876543210, '789 Pine Rd');

INSERT INTO Accounts (AccountID, CustomerID, AccountType, Balance, Status) VALUES
(1, 1, 'Savings', 10000.00, 'Active'),
(2, 2, 'Current', 20000.00, 'Active'),
(3, 3, 'Savings', 30000.00, 'Active');

INSERT INTO Transactions (TransactionID, AccountID, TransactionDate, Amount, TransactionType) VALUES
(1, 1, '2021-01-01', 5000.00, 'Deposit'),
(2, 2, '2021-01-02', 10000.00, 'Withdrawal'),
(3, 3, '2021-01-03', 15000.00, 'Deposit');








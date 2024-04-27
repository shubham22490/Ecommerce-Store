truncate order_history;
truncate trial_history;
START TRANSACTION;
INSERT INTO trial_history(PHONE_NUMBER, Product_id) VALUES ('1234567890', 1);
SAVEPOINT before_conflict;
INSERT INTO trial_history(PHONE_NUMBER, Product_id) VALUES ('1234567890', 1);
ROLLBACK TO SAVEPOINT before_conflict;
INSERT INTO trial_history(PHONE_NUMBER, Product_id) VALUES ('4567890123', 2);
COMMIT;

START TRANSACTION;
INSERT INTO order_history(PHONE_NUMBER, Product_id,Quantity) VALUES ('1234567890', 1,2);
SAVEPOINT before_conflict;
INSERT INTO order_history(PHONE_NUMBER, Product_id,Quantity) VALUES ('1234567890', 1,2);
ROLLBACK TO SAVEPOINT before_conflict;
INSERT INTO order_history(PHONE_NUMBER, Product_id,Quantity) VALUES ('4567890123', 2,5);
COMMIT;



START TRANSACTION;
INSERT INTO trial_history (PHONE_NUMBER, Product_id) VALUES ('1112223334', 4);
COMMIT;

SELECT * from trial_history;


START TRANSACTION;
UPDATE trial_history SET Product_id = 3 WHERE PHONE_NUMBER = '1112223334';
COMMIT;


SELECT * from trial_history;


START TRANSACTION;
SELECT * FROM trial_history WHERE PHONE_NUMBER = '1112223334';
COMMIT;


START TRANSACTION;
DELETE FROM trial_history WHERE PHONE_NUMBER = '1112223334';
COMMIT;

SELECT * from trial_history;
                                                                  

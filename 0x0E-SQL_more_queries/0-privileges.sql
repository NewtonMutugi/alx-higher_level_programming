-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

SELECT * FROM mysql.user WHERE user = 'user_0d_1' OR user = 'user_0d_2';

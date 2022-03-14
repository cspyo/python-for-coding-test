SELECT a.first_name, a.last_name, b.room_no FROM customers a 
INNER JOIN reservations b
ON a.customer_id = b.customer_id
WHERE (MONTH(b.date_in) = 1 AND DAY(b.date_in) BETWEEN 1 AND 30)
OR (MONTH(b.date_out) = 1 AND DAY(b.date_out) BETWEEN 2 AND 31)
ORDER BY a.first_name, a.last_name, b.room_no



SELECT a.first_name, a.last_name, b.room_no FROM customers a 
INNER JOIN reservations b
ON a.customer_id = b.customer_id
WHERE (DATE(b.date_in) BETWEEN '2022-01-01' AND '2022-01-30')
OR (DATE(b.date_out) BETWEEN '2022-01-02' AND '2022-01-31')
ORDER BY a.first_name, a.last_name, b.room_no
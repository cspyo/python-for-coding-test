select c.first_name as 이름, c.last_name as 성,
sum(r.price * (datediff(res.date_out, res.date_in)+1)) as 누적숙박비
from rooms r
join reservations res
on res.room_no=r.room_no
join customers c
on res.customer_id = c.customer_id
group by c.customer_id
order by c.first_name, c.last_name
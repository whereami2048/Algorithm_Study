# select *
SELECT uu.USER_ID, uu.NICKNAME, sum(ub.price) as TOTAL_SALES
from used_goods_user as uu 
join used_goods_board as ub 
on uu.user_id = ub.writer_id
where ub.status = 'DONE'
group by uu.user_id
having sum(ub.price) >= 700000
order by sum(ub.price) asc

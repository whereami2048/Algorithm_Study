SELECT 
uu.USER_ID, 
uu.NICKNAME, 
CONCAT(uu.CITY, " ", uu.STREET_ADDRESS1, " ", STREET_ADDRESS2) as 전체주소, 
CONCAT(SUBSTR(uu.TLNO, 1, 3), '-', SUBSTR(uu.TLNO, 4, 4), '-', SUBSTR(uu.TLNO, 8, 4)) as 전화번호
from USED_GOODS_BOARD as ub
join USED_GOODS_USER as uu
on ub.writer_id = uu.user_id
group by ub.writer_id
having count(ub.writer_id) >= 3
order by uu.user_id desc
SELECT distinct cc.CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as CH 
join CAR_RENTAL_COMPANY_CAR as cc 
on ch.car_id = cc.car_id
where cc.car_type = '세단' and ch.start_date like '%-10-%'
order by cc.car_id desc
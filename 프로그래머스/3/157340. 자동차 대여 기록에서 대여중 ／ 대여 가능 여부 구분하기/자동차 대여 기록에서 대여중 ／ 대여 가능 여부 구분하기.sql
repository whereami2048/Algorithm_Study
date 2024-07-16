SELECT CAR_ID,
max(case 
when 
start_date <= Date('2022-10-16') and end_date >= Date('2022-10-16') 
then '대여중'
else '대여 가능'
end) as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by car_id desc
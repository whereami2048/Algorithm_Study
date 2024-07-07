SELECT ao.ANIMAL_ID, ao.NAME
from ANIMAL_OUTS as ao 
join ANIMAL_INS as ai 
on ao.animal_id = ai.animal_id
order by abs(ao.datetime - ai.datetime) desc
limit 2
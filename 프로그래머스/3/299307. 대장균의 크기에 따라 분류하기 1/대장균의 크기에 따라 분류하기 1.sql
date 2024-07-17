SELECT ID, 
CASE 
when SIZE_OF_COLONY <= 100 then 'LOW'
when SIZE_OF_COLONY > 100 and SIZE_OF_COLONY <= 1000 then 'MEDIUM'
else 'HIGH'
end as SIZE
from ECOLI_DATA
order by ID
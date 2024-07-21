SELECT places.ID, places.NAME, places.HOST_ID
from places
join (select host_id
    from places
    group by host_id 
    having count(host_id) >= 2
) as sp
on sp.host_id = places.host_id
order by id asc
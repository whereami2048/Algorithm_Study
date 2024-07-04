SELECT ai.animal_id, ai.name from animal_ins as ai
join animal_outs as ao
on ai.animal_id = ao.animal_id
where ao.datetime < ai.datetime
order by ai.datetime
select ID, COALESCE(ED_P.count, 0) as CHILD_COUNT
from ECOLI_DATA as ED
left join (select parent_id, count(*) as count
     from ECOLI_DATA
     group by parent_id
      having parent_id is not null
     ) as ED_P
on ED.id = ED_P.parent_id
order by ID asc
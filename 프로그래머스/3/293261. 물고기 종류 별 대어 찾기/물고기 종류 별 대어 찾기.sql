select fi.id as ID, fni.fish_name as FISH_NAME, fi.length as LENGTH
from fish_info as fi
join fish_name_info as fni
on fi.fish_type = fni.fish_type
where (fi.fish_type, fi.length) in (select fish_type, max(length)
                                 from fish_info
                                 group by fish_type)
order by fi.id asc
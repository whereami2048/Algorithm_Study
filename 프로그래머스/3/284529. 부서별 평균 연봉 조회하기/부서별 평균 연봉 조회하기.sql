select hd.DEPT_ID, hd.DEPT_NAME_EN, round(avg(he.SAL)) as AVG_SAL
from HR_DEPARTMENT as hd
join HR_EMPLOYEES as he
on hd.DEPT_ID = he.DEPT_ID
group by he.DEPT_ID
order by avg(he.SAL) desc
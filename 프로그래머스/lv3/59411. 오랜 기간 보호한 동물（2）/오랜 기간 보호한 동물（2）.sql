-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME
from animal_ins a, animal_outs b
where a.animal_id = b.animal_id
order by datediff(a.datetime,b.datetime)
limit 2
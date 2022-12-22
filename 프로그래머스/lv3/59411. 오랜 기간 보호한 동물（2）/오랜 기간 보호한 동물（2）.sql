-- 코드를 입력하세요
SELECT b.ANIMAL_ID,	b.NAME
from animal_ins a right join animal_outs b on a.ANIMAL_ID=b.ANIMAL_ID
order by b.datetime-a.datetime DESC
limit 2

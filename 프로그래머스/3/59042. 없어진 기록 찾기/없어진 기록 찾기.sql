-- 코드를 입력하세요
SELECT b.ANIMAL_ID,	b.NAME
from animal_ins a right join animal_outs b on a.ANIMAL_ID	=b.ANIMAL_ID	
where a.ANIMAL_ID	 is null
-- 코드를 입력하세요
# %가 앞뒤로 있으면 어딘가에 EL이 들어있음 된다.
SELECT ANIMAL_ID,	NAME
from ANIMAL_INS
where 	ANIMAL_TYPE='Dog' and NAME like '%EL%'
order by name
-- 코드를 입력하세요
SELECT mcdp_cd, count(PT_NO)
from APPOINTMENT
where APNT_YMD like '2022-05%' 
group by mcdp_cd
order by count(PT_NO), MCDP_CD
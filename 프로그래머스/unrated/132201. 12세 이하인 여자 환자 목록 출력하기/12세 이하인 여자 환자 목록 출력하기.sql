-- 코드를 입력하세요
SELECT PT_NAME,	PT_NO,	GEND_CD,AGE, ifnull(tlno,'NONE')
from PATIENT 
where AGE<=12 and gend_cd='W'
order by age desc, pt_name
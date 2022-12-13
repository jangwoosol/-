-- 코드를 입력하세요
SELECT a.INGREDIENT_TYPE,sum(b.TOTAL_ORDER)
from icecream_info a right join first_half b on a.flavor=b.flavor
group by a.INGREDIENT_TYPE
order by b.TOTAL_ORDER
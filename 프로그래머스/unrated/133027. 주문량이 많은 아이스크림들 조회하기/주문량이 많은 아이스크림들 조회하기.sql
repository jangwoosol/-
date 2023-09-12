-- 코드를 입력하세요
#같은 맛의 아이스크림이라도 다른 출하 번호를 갖게 된다.
select a.flavor
from (SELECT shipment_id, flavor, sum(total_order) as total
from july 
group by flavor) as a join (SELECT shipment_id, flavor, sum(total_order) as total from FIRST_HALF group by flavor) as b on a.flavor=b.flavor 
order by a.total+b.total desc
limit 3
-- 코드를 입력하세요
SELECT a.car_id
from CAR_RENTAL_COMPANY_CAR as a join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b on a.car_id=b.car_id
where month(b.start_date)=10 and a.car_type='세단'
group by a.car_id
order by a.car_id desc
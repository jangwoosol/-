-- 코드를 입력하세요
select car_id, k.car_type, round((daily_fee-(daily_fee*0.01*discount_rate))*30,0) as FEE
from (SELECT CAR_TYPE,	DAILY_FEE, a.car_id
from CAR_RENTAL_COMPANY_CAR as a join CAR_RENTAL_COMPANY_RENTAL_HISTORY as b on a.car_id=b.car_id
where a.car_type in ('세단','SUV') and a.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE > '2022-11-01' AND START_DATE < '2022-12-01')) as k join (select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where duration_type="30일 이상") as c on k.car_type=c.car_type
where round((daily_fee-(daily_fee*0.01*discount_rate))*30,0)>=500000 and round((daily_fee-(daily_fee*0.01*discount_rate))*30,0)<2000000
group by car_id
order by FEE desc, car_type , car_id desc

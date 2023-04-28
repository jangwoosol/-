SELECT car_id,
max(case when (date_format(START_DATE,'%Y-%m-%d')<='2022-10-16') and (date_format(END_DATE,'%Y-%m-%d')>='2022-10-16') then '대여중' else '대여 가능'
end) as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc
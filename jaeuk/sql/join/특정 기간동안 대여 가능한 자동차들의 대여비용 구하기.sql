select distinct c.CAR_ID, c.CAR_TYPE, ROUND(c.DAILY_FEE*30*(100-p.DISCOUNT_RATE)/100) AS FEE
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY h on c.car_id = h.car_id
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p on c.car_type = p.car_type
where c.car_id not in
        (select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where END_DATE >= '2022-11-01' and START_DATE <= '2022-12-01') and p.duration_type = '30일 이상'
group by c.car_id
having c.car_type in ('세단', 'SUV') and FEE >= 500000 and FEE <= 2000000
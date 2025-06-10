with history as (select 
    history_id,
    car_id,
    start_date,
    end_date,
    datediff(end_date, start_date) + 1 as 'period',
    case
        when datediff(end_date, start_date) + 1 >= 90 then '90일 이상'
        when datediff(end_date, start_date) + 1 >= 30 then '30일 이상'
        when datediff(end_date, start_date) + 1 >= 7 then '7일 이상'
        else 'NONE'
    end as duration_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY)

select 
    history_id,
    round(h.period * c.daily_fee * (100 - ifnull(p.discount_rate, 0)) / 100) as fee
from CAR_RENTAL_COMPANY_CAR c
join history h on c.car_id = h.car_id
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p on h.duration_type = p.duration_type and c.car_type = p.car_type
where c.car_type = '트럭'
order by fee desc, history_id desc
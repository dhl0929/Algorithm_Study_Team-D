select month(start_date) as MONTH, CAR_ID, count(history_id) as RECORDS
from car_rental_company_rental_history
where car_id in (select car_id
            from car_rental_company_rental_history
            where start_date >= '2022-08-01' and start_date <= '2022-10-31'
            group by car_id
            having count(history_id) >= 5) and start_date >= '2022-08-01' and start_date <= '2022-10-31'
group by MONTH, CAR_ID
order by MONTH, CAR_ID DESC
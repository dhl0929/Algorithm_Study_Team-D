WITH RECURSIVE hours AS (
  SELECT 0 AS hour, 0 AS count
  UNION ALL
  SELECT hour + 1, 0 FROM hours WHERE hour < 23
)

select 
    h.hour,
    ifnull(a.count, 0)
from hours h
left join (select hour(datetime) as HOUR, count(animal_id) as COUNT
            from animal_outs
            group by hour(datetime)) a on h.hour = a.hour


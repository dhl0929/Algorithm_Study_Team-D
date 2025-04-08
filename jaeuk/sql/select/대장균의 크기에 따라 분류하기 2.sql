with tmp as (
    select id, ntile(4) over (order by size_of_colony desc) as grade
    from ecoli_data
    order by id
)

select 
    id,
    case
        when grade = 1 then 'CRITICAL'
        when grade = 2 then 'HIGH'
        when grade = 3 then 'MEDIUM'
        else "LOW"
    end as colony_name
from tmp
select ai.animal_id, ao.name
from ANIMAL_OUTS ao
join ANIMAL_INS ai on ao.animal_id = ai.animal_id
order by datediff(ao.datetime, ai.datetime) desc
limit 2
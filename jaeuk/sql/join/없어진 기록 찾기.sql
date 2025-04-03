select animal_id, name
from animal_outs ao
where ao.animal_id not in (select animal_id from animal_ins)
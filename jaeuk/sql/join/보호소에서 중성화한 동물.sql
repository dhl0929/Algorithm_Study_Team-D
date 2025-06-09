select ANIMAL_ID, ANIMAL_TYPE, NAME
from animal_outs
where animal_id in (select ANIMAL_ID
                    from ANIMAL_INS
                    where sex_upon_intake like 'Intact%')
      and SEX_UPON_OUTCOME not like 'Intact%'
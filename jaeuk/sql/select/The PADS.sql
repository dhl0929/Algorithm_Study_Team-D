select concat(name, '(', substr(occupation, 1, 1), ')')
from occupations
order by name, substr(occupation, 1, 1);

select concat('There are a total of ', count(occupation), ' ', lower(occupation), 's.')
from occupations
group by occupation
order by count(occupation), occupation
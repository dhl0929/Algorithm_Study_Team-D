select 
    case
        when g.grade >= 8 then name
        else 'Null'
    end as name,
    g.grade, 
    s.marks
from students s
inner join grades g on s.marks between g.min_mark and g.max_mark
ORDER BY 
  g.grade DESC,
  CASE WHEN g.grade >= 8 THEN s.name END ASC,
  CASE WHEN g.grade < 8 THEN s.marks END ASC;

SELECT score1.score, count(distinct score2.score) AS 'rank' 
from scores score1 join scores score2
WhERE score1.score <= score2.score
GROUP BY score1.id
ORDER BY score1.score DESC;
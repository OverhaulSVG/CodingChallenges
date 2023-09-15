/*
In order to solve the problem, we need to first find the wands that costs the minimum, to do that, we create a 
table (CTE) to calculate this minimum, by using our wands table, joinin it with wands_property table by code, 
filtering the is_evil parameter, and grouping by code, age and power to get the appropiate aggregates.
Then we use this CTE to join the wands table again, so that we can indirectly filter the wands per price by 
joining on mw.min_coins and wands.coins_needed. This way we can obtain only the cheapest price for each  type 
of wand, we finish the query selecting the required fields, ordering by power and age.
*/

with min_wand as (
select 
    w1.code code, p1.age age, min(w1.coins_needed) min_coins,  w1.power power
from wands w1
    inner join wands_property p1
        on w1.code = p1.code
    where p1.is_evil <> 1
    group by w1.code, p1.age, w1.power
)
select w2.id, mw.age, mw.min_coins, mw.power from min_wand mw
inner join wands w2
    on mw.min_coins = w2.coins_needed and mw.code = w2.code
order by mw.power desc, mw.age desc

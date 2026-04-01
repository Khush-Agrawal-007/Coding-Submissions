-- # Write your MySQL query statement below
-- select  product_id ,
--         year as first_year,
--         quantity ,
--         price
--     from sales s
--     where s.year =  (select min(year) from sales s2 where s.product_id = s2.product_id )
--     ;



SELECT 
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales s
JOIN (
    SELECT 
        product_id, 
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) t
ON s.product_id = t.product_id
AND s.year = t.first_year;
# Write your MySQL query statement below
select s.product_id,product_name from  sales s inner join product p on p.product_id=s.product_id group by s.product_id having min(sale_date)>=CAST('2019-01-01' AS DATE) and max(sale_date)<=CAST('2019-03-31' AS DATE)

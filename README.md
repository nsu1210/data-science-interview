# Data Science Cheat Sheet

## MySQL Cheat Sheet

https://github.com/dennyzhang/cheatsheet.dennyzhang.com/tree/master/cheatsheet-mysql-A4

### Basic
- Alias, every derived table must have its own alias. `SELECT ... FROM (subquery) [AS] x`. NOTE: don't use alias in
 `WHERE` clause.
- `GROUP BY ... HAVING aggregate_func`, NOTE `WHERE` clause is before `GROUP BY`.
- `WHERE x = (SELECT MAX(...) FROM ...)`, NOTE: `WHERE x = MAX(...)` is wrong, aggregate function can't show in where
 clause.
- `WHERE column = value`, `WHERE column in (subquery)`, `WHERE (column1, column2) in (subquery)`.
- `LIMIT m, n` = `LIMIT n OFFSET m`, skip top m rows then top n rows.
- `COUNT(...)` & `COUNT(DISTINCT ...)`, can use count distinct for multiple columns. Conditional count `COUNT(IF
(condition, 1, NULL))` or `SUM(condition[x1 = x2])`, conditional ratio `AVG(condition)`.
- Round, `ROUND(..., decimals)`.
- Union, combine records from multiple columns into one. `UNION` = `UNION DISTINCT` -> remove duplicates, `UNION ALL
` -> keep duplicates.
- String, `SUBSTRING(str, num1, num2)`, extract a substring from str (start at position num1, length num2).
- Condition Judgement, `CASE WHEN <condition> THEN ... ELSE ... END`, `CASE <value> WHEN <value> THEN ... END`, note
 there're two ways expressions. Some other condition judgement method`IF(..., value if True, value if False)`, `IFNULL
 (value if not null, value if null)`. `COALESCE(value1, value2)` has same function with `IFNULL`, `COALESCE` is to
  choose the first not null value in list, so in application if `value1` is null then `value2` replaces it.
- Update, `UPDATE table SET column = value [WHERE]`.
- Delete, `DELETE FROM table [WHERE clause]`, [an classic example](https://leetcode.com/problems/delete-duplicate-emails/).  
`DROP` > `TRUNCATE` > `DELETE`. `DROP TABLE` drop entire table, `TRUNCATE TABLE` delete all records of table, both
 can't revise. `DELETE` delete specific records, can revise.
- Random, `RAND(seed=None)`, returns a random number between [0, 1). Get random int between [0, 10], `SELECT FLOOR
(RAND() * 11)`.

### Date
- Date, `DATE('2020-01-01')` is a date type. Query date in one year or one month, `YEAR(date) = 2020` or `MONTH(date
) = 4`. Change format of the date `DATE_FORMAT(date, '%m-%d-%Y')`, can use other format specifiers.
- `DATE_ADD(date, INTERVAL number type[DAY, WEEK, MONTH, YEAR])`, `DATE_SUB(date, INTERVAL number type[DAY, WEEK
, MONTH, YEAR])`.
- `DATEDIFF(date1, date2) = date1 - date2`.
- `CURRENT_DATE()` = `CURDATE()` get current date. `NOW()` get current datetime.

### Advanced
- Variable, `SELECT @variable := <some change> FROM table1, (SELECT @variable := original value) AS X`. NOTICE SPACE.
- `Rank() OVER(PARTITION BY ... ORDER BY ...)`. `ROW_NUMBER()` makes ordinal rank without tie. `DENSE_RANK()` doesn't
 take gap for tie.
- Some useful window function. `FIRST_VALUE()` get first value, `LEAD()` get next value, `LAG()` get previous value.
- Window Function, `Function() OVER(PARTITION BY ... ORDER BY ... ROWS [BETWEEN] <frame_start> [AND] <frame_end>)`.
    1. `frame_start`: 
        1. `UNBOUNDED PRECEDING`: frame starts at the first row of the partition.
        2. `N PRECEDING`: a physical N of rows before the first current row. N can be a literal number or an
         expression that evaluates to a number.
        3. `CURRENT ROW`: the row of the current calculation.
    2. `frame_end`
        1. `frame_start`: as mentioned previously.
        2. `UNBOUNDED FOLLOWING`: the frame ends at the final row in the partition.
        3. `N FOLLOWING`: a physical N of rows after the current row.
![alt text](https://sp.mysqltutorial.org/wp-content/uploads/2018/09/mysql-window-functions-frame-clause-bound.png)
- [Create Function](https://www.mysqltutorial.org/mysql-stored-function/)
```
DELIMITER $$

CREATE FUNCTION function_name(
    param1 datatype,
    param2 datatype,
    …
)
RETURNS datatype
[DETERMINISTIC]
BEGIN
 -- statements
END $$

DELIMITER ;
```

## Python Algorithms Cheat Sheet

### Python Standard Library
- `collections`
    - `Counter`. dict subclass for counting hashable objects. 
        - `most_common(n: int = None)`, get TOP N frequent `(elements, count)` list of tuple.


### Important Conception
- `assignment` & `shallow copy` & `deep copy`. [Link](https://songlee24.github.io/2014/08/15/python-FAQ-02/)


        




## Python Pandas Cheat Sheet

https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html

- IMPUTATION, `df.fillna(value=0), df.dropna(), df.drop_duplicates()`.
- NEW COLUMN, i.e. `df.assign(new=df.col1 + df.col2), df.assign(new=lambda x: x.col1 * 2)`.
- WHERE, i.e. `df[(df['col1'] == 1]) & (df['col2'] > 5)], df[(df['col1'] == 1]) | (df['col2'] > 5)], df[~df['col1'].isin(list)]`.
- IS NULL, i.e. `df['col1'].isna(), df['col1'].notna()`.
- FILL NULL, i.e. `df.fillna(value=0)`.
- GROUP BY, i.e. `df.groupby('col1').agg({'col2': np.mean, 'col3': np.size}), df.groupby(['col1', 'col2']).agg({'col3': [np.size, np.mean]})`.
- GROUP BY AGGREGATE, i.e. `df.groupby('col1')['col2'].apply(lambda x: x[x > 5].count())`.
- JOIN, i.e. `df.join(df, on=['col1', 'col2'], how='left'), df1.merge(df2, left_on='key1', right_on='key2', how='left')`.
- SORT, i.e. `df.sort_values(by='col1', ascending=True)`.
- CONCAT, i.e. `pd.concat([df1, df2], axis=0)`.
- RANK, i.e. `df['col1'].rank(method='first', ascending=False)`.
- SHIFT, i.e. shift down 3 rows `df.shift(periods=3)`.
- WINDOW, i.e. `df.rolling(window=5).mean()`.
- DATE, `date = datetime.now(), date = datetime(2020, 2, 18), date = datetime.strptime('2020-02-18', "%Y-%m-%d")`.
- DATE DIFF, `(datetime(2020, 2, 18) - datetime(2020, 2, 17)).days == 1, start_date = end_date - timedelta(days=7).`
- PIVOT, `df.pivot(index='col1', columns='col2', values='col3' | ['col3'. col4])`
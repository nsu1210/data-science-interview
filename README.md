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
- Create, `CREATE TABLE table_name (column_name1 column_type1, column_name2, column_type2, PRIMARY KEY (column_name1))`.
- Insert, `INSERT INTO table_name (field1, field2) VALUES (value11, value12), (value21, value22)`.
- Update, `UPDATE table SET column = value [WHERE]`.
- Delete, `DELETE FROM table [WHERE clause]`, [an classic example](https://leetcode.com/problems/delete-duplicate-emails/).  
`DROP` > `TRUNCATE` > `DELETE`. `DROP TABLE` drop entire table, `TRUNCATE TABLE` delete all records of table, both
 can't revise. `DELETE` delete specific records, can revise.
- Like, fuzzy query for string. `SELECT * FROM table WHERE column1 LIKE '%THIS`, `%` stands for any 0 or multiple
 chars, `_` stands for single chars, for other [regular expression](https://www.runoob.com/mysql/mysql-regexp.html).
- Random, `RAND(seed=None)`, returns a random number between [0, 1). Get random int between [0, 10], `SELECT FLOOR
(RAND() * 11)`.
- Index, index can boost query while need more space, which will slow down alter process(insert). `INDEX` could be
 duplicated and null. `Primary Key` will automatically generate `UNIQUE INDEX`(unique and not null). 
- Explain, `EXPLAIN query`, check SQL query plan. 

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

### Data Structure & Standard Library
- `collections`
    - `Counter`. Dict subclass for counting hashable objects. 
        - `most_common(n: int = None)`, get TOP N frequent `(elements, count)` list of tuple.
    - `defaultdict`. Dict subclass that calls a factory function to supply missing values.
        - `defaultdict(list)[key]` = `dict.setdefault(key, [])`, same for other data type: `int`, `set`.
    - `deque`. List-like container with fast appends and pops on either end. **Tips**: good choice for `BFS`.
        - `append(x)` & `appendleft(x)`. Append one element to right & left side.
        - `extend(l)` & `extendleft(l)`. Extend the iterable object (list) to right & left side. Note left one will be
         reversed.
        - `pop()` & `popleft()`.  Pop out one element from right & left side.
        - `count(x)`. Count the number of element x. `reverse()` & `remove(x)` are inplace methods same with `List`.
        - `rotate(n=1)`. Rotate the deque n steps to the right. If n is negative, rotate to the left, rotating one
         step to the right is equivalent to `d.appendleft(d.pop())`, and rotating one step to the left is equivalent to
          `d.append(d.popleft())`.
- `heapq`. `Heap` is a binary tree like data structure, with all parent nodes value less(more) than or equal to its
 own children. `Heapsort` is `O(nlogn)` sorting algorithm. In python `heaqp`, default is `min-heap`, which the
  smallest is always the root, `head[0]`.
    - `heapify(x)`. Transform list x into a heap (still a list type), in-place, in linear time.
    - `heappush(heap, item)`. Push the value item onto the heap, maintaining the heap invariant.
    - `heappop(heap)`. Pop and return the smallest item from the heap, maintaining the heap invariant.To access the
     smallest item without popping it, use `heap[0]`.
    - `heappushpop(heap, item)`. Push item on the heap, then pop and return the smallest item from the heap.
    - `heapreplace(heap, item)`. Pop and return the smallest item from the heap, then push the new item.
    - `merge(*iterables, key=None, reverse=False)`. Merge multiple sorted inputs into a single sorted output.
    - `nlargest(n, iterable, key=None)`. Return a list with the n largest elements from the `iterable`. Equivalent to
     `sorted(iterable, key=key, reverse=True)[:n]`.
    - `nsmallest(n, iterable, key=None)`. Return a list with the n smallest elements from the `iterable`.Equivalent to
     `sorted(iterable, key=key)[:n]`.

- `Trie`. `Trie` aka `prefix tree`, is a kind of search tree for strings. For all children of one node share the same
 prefix, each node represents one letter and usually has 26 children. In Python, `Trie` need to be manually defined. 
 `Trie` is constructed by `TrieNode`(two attributes `children: Dict` & `end: bool`). 
 [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
    - `__init__`. Initialize with empty root node.
    - `insert(String)`. Generate children of parent node recursively, if the letter key not in parent node then create
     one. In the final node, set `end = True`, meaning it's a completed word.
    - `search(String)`. Search if the word in the trie.
    - `word_suggest(String)`. Give out suggestion result when tying in a searching word. 
    [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)


- `copy`. Compare `assignment` & `shallow copy` & `deep copy`. [Link](https://songlee24.github.io/2014/08/15/python-FAQ-02/)

### Algorithm Summary
- `DFS` & `BFS`
    - `DFS` can reach the target, but might not take the optimal steps/route. Thus `BFS` is a good choice for optimal
     search problem. Example: [127. Word Ladder](https://leetcode.com/problems/word-ladder/)
    - **When searching, it would be better to change visit status value instead of storing in set.** Note `DFS` need to
     revert the value after recursion. Example: [200. Number of Islands](https://leetcode.com/problems/number-of-islands/), 
     [79. Word Search](https://leetcode.com/problems/word-search/).
    - `DFS` & `Topological Sort`. Unlike classic `DFS` change one status(visited), in graph problem, `Topological Sort
    ` has two status(visited & visiting) to detect cycle. Remember to change visiting to visited after recursion. 
    Example: [207. Course Schedule](https://leetcode.com/problems/course-schedule/).





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
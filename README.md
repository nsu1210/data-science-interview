# data-science-interview
Data Science interview collections 

## Python Cheat Sheet for Data Manipulation 

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
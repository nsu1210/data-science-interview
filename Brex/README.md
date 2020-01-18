# Data Science Challenge

<img src="https://brex.com/static/logo-5a9a377ec71868f4c94ae6788c3e0554.png" width="500">

We have attached a cleaned-up and redacted data set that simulates Brex financial
data.

There are four tables for you to work with:

1. Customer Accounts (id, name): a list of our customers with their names redacted
    and a unique identifier
2. Financial Accounts (id, customer_account_id, name): a list of bank accounts
    belonging to our customers
       a. customer_account_id: The ID of the customer that owns this bank account
          from Customer Accounts (table 1)
       b. id, name: Unique financial account identifier and redacted name of the
          account
3. Financials Balances (id, account_id, amount, accrual_date): a reading of the end-
    of-day balance per financial account
       a. account_id: the ID of the financial account (table 2) that the balance
          reading belongs to
       b. amount and accrual_date: The balance (in cents) reading and the date
          this reading was taken
4. Financials Transactions (id, account_id, amount, accrual_date): list of
    transactions in and out of each financial account
       a. account_id: the ID of the financial account (table 2) that the transaction
          reading belongs to
       b. amount and accrual_date: the amount (in cents) of each transaction and
          the date when the transaction occurred. Negative transactions are money
          leaving the bank account and positive transactions are money coming in

**Task:**

Calculate the approximate **total daily balance per customer**

1. The resulting table should have **one row per calendar day per customer**.
2. There are neither balance readings nor transactions for every calendar day per
    customer. This means you will need to **fill in missing calendar days** and
    interpolate a balance for those days (to make things simpler, we strongly
    recommend using the date range 2017 - 01 - 01 to 2018- 09 - 22 for every customer).


3. Be careful of other possible data integrity issues.
4. There are a few ways to calculate the daily balance and each one may give you
    slightly different daily values. Don’t worry about which one is most “correct”.
    Instead, just pick one method ( **make sure to use both financials_balances**
    **and financials_transactions tables** ) and tell us how you did it.

Whatever method you choose, try to make it reasonably performant. It should not be
taking more than a few minutes to re-derive the values. Take 2 hours max for the whole
challenge. However far you get is OK. The time limit should give you an idea of the level
of the solution we are looking for, so don’t go too far down the rabbit hole. Use whatever
database or scripting language you prefer. You may also use any online resources
freely.

**Submission**
Submit the following:

1. Table/CSV with customer_account_id, date, balance columns
2. A brief outline on the method (in-line comments are fine)
3. All code needed for us to replicate your results (Notebook, scripts, SQL code,
    etc.)



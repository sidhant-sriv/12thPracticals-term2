# 12thPracticals-term2
This is a repo for the solutions of the computer science practicals. 🙂

## For the contributer
- Please check q13 😛
- Please check if everything works because I didn't write any tests
- If there are any problems, make changes, write commit message, and make a PR. Do not tell me about it.
- Make sure to follow the naming convention

Note: If the code works, please leave it alone.

## How to run the sql scripts

1. open the mysql prompt in this directory.
2. ``source table-creation.sql;``
3. ``source data_initialisation.sql``

Notes:

- You would only need to run the table creation script once, unless you
changed the structure and want to reset it. In such a case, make sure
to drop the existing table before running the script.
- data_initialisation.sql removes all data from the records before
inserting. Highly recommend using transactions to deal with it.

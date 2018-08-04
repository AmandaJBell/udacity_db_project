# Project: Log Analysis
================================

This is the third project in the Udacity Full Stack Nanodegree. The purpose of this project is to build a mock internal reporting tool for a news website and in the process answer the following questions about the data in news database:

What are the most popular three articles of all time?

Who are the most popular article authors of all time?

On which days did more than 1% of requests lead to errors?

Required Libraries and Dependencies
-----------------------------------
This project requires Python v3.* and Psycopg v2.* to be installed. 

In addition Vagrant and VirtualBox are also required.

How to Run Project
------------------
**1.** After cloning the project, navigate to the repo in your terminal and unzip newsdata.zip.

**2.** Setup the VM by typing the following into terminal:
    ```vagrant up```

**3.** Login to the VM by typing the following into terminal:
    ```vagrant ssh```
    
**4.** Get to the right folder typing the following into terminal:
    ```cd /vagrant```

**5.** Setup the database by typing the following into terminal:
    ```psql -d news -f newsdata.sql;```

**6.** Finally run the project by typing the following into terminal:
    ```python newsdb.py```

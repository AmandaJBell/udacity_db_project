#!/usr/bin/python3

import datetime
import psycopg2


article_query_question = "What are the most popular three"\
                            "articles of all time?"
article_query = """select title, num from articles,
                  (select replace(path, '/article/', '') as slug,
                   count(*) as num from log
                    where status like '%200%'
                     group by path order by num desc) as subq
                  where articles.slug = subq.slug limit 3;"""

author_query_question = "Who are the most popular"\
                          "article authors of all time?"
author_query = """select sum(num) as views,
                   authors.name from articles, authors,
                  (select replace(path, '/article/', '')
                   as slug, count(*) as num from log
                    where status like '%200%' group by path
                     order by num desc) as subq
                  where authors.id = articles.author
                   and articles.slug = subq.slug
                  group by authors.id order by views desc;"""

error_query_question = "On which days did more than"\
                         "1% of requests lead to errors?"
error_query = """select time::date, p
                 from (select error_table.time::date,
                  error_count, table_count,
                  ((cast(error_count as float) /
                    cast( table_count as float)) * 100)
                   as p from (select time::date, count(*)
                    as error_count from log
                  where status='404 NOT FOUND' group by
                   time::date order by error_count desc) as error_table,
                  (select time::date, count(*) as table_count from
                   log group by time::date order by table_count desc)
                  as total_table where error_table.time = total_table.time)
                   as subq where p >= 1.0;"""


def execute_article_query():
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(article_query)
    content = c.fetchall()
    db.close()
    print(article_query_question)
    for article, views in content:
        print('"%s" -- %d views' % (article, views))
    print('\n')


def execute_author_query():
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(author_query)
    content = c.fetchall()
    db.close()
    print(author_query_question)
    for views, author in content:
        print('%s -- %d views' % (author, views))
    print('\n')


def execute_error_query():
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(error_query)
    content = c.fetchall()
    db.close()
    print(error_query_question)
    for date, error in content:
        print('%s -- %.2f%% errors' % (date.strftime("%B %d, %Y"), error))
    print('\n')


if __name__ == '__main__':
    execute_article_query()
    execute_error_query()
    execute_author_query()

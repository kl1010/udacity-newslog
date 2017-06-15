#!/usr/bin/env python2.7

import datetime
import time
import psycopg2
import bleach

DBNAME = "news"


def authors():
    for_data = []
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print "Connected"
    query = '''select authors.name as aun, count(authors.name) as cnt
     from log join articles on substring(log.path from 10) = articles.slug
      join authors on authors.id = articles.author where status = '200 OK'
       and path != '/' group by aun order by cnt desc'''
    c.execute(query)
    try:
        data = c.fetchall()
    except:
        data = None
    db.close()
    for x in data:
        for_data.append([x[0], int(x[1])])
    return for_data


def articles():
    for_data = []
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print "Connected"
    query = '''select count(path) as cnt, title from log
     join articles on substring(log.path from 10) = articles.slug
      where status = '200 OK' group by path,slug,title
       order by cnt desc limit 3'''
    c.execute(query)
    try:
        data = c.fetchall()
    except:
        data = None
    db.close()
    for x in data:
        for_data.append([int(x[0]), x[1]])
    return for_data


def errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    print "Connected"
    query = '''select date(time), round(100.0*sum(case
     log.status when '200 OK' then 0 else 1 end)/count(log.status),2)
     as PE from log group by date(time) order by PE desc limit 1'''
    c.execute(query)
    try:
        data = c.fetchall()
    except:
        data = None
    date = data[0][0].strftime('%B %d,%Y')
    percent = float(data[0][1])

    for_data = [date, percent]
    return for_data

# coding: utf8
from math import ceil
from django.db import connection

cmd_dict = {'billing_info': '''select bi.* ,sm.cust_user from billing_info bi
                               inner join sample_project_master sm on bi.project_id=sm.id
                               where sm.cust_user="%s"''',
           'receipt_info': '''select rt.* ,sm.cust_user from receipt_info rt
                              inner join sample_project_master sm on rt.project_id=sm.id
                              where sm.cust_user="%s"''',
           'cost_info': '''select ct.* ,sm.cust_user from cost_info ct
                           inner join sample_project_master sm on ct.project_id=sm.id
                           where sm.cust_user="%s"'''}
def get_expense_info(user, limit, sidx, sord, page, table):
    cmd1 =  cmd_dict[table] % (user)
    cursor = connection.cursor()
    cursor.execute(cmd1)
    results = cursor.fetchall()
    count = len(results)
    if count > 0:
        total_pages = ceil(float(count)/float(limit))
    else:
        total_pages = 0

    if page > total_pages:
        page = total_pages
    if page < 1:
        start = 0
    else:
        start = int(limit) * page - int(limit)
    cmd2 = cmd1 + " order by {sort_index} {sort_direct} limit {start}, {limit}".format(sort_index=sidx,
                                                                                      sort_direct=sord,
                                                                                      start=int(start),
                                                                                      limit=limit)
    cursor = connection.cursor()
    cursor.execute(cmd2)
    results = cursor.fetchall()

    return page, total_pages, count, results


def get_expense_total(user, table):
    cmd = cmd_dict[table] % (user)
    cursor = connection.cursor()
    cursor.execute(cmd)

    results = cursor.fetchall()
    total_expense = 0
    for result in results:
        total_expense += result[3]

    return total_expense

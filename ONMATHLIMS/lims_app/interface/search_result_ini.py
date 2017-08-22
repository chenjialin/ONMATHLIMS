# coding: utf8
from django.db import connection


def get_search_result(search_key):
    cursor = connection.cursor()
    sql = """SELECT
            m.project_name as "项目名称",
            m.project_number as "项目编码",
            m.status as "项目状态",
            m.create_time as "项目创建时间",
            m.cust_user as "客户",
            s.species as "物种",
            d.sample_name as "样品名称",
            d.sample_id as "样品ID",
            d.sendsample_time as "送样时间",
            d.downmachine_num as "下机时间"
             FROM sample_project_master m
             inner join sample_info_detail d on d.project_id=m.id
             inner join send_sample s on s.project_id=m.id
    """

    sql2 = """select
              ss.project_number as '项目编号',
              ss.sample_name as '样品名称',
              ss.species as '物种',
              qc.sample_id as '样品编号',
              qc.results as '判定结果',
              um.data_count as '上机数据量'
              from send_sample ss
              left join quality_check qc on ss.sample_name=qc.sample_name
              left join upmachine um on um.sample_name=ss.sample_name
    """
    condition = " where ss.project_number='{key}' or ss.sample_name='{key}' \
                or ss.species='{key}' or qc.sample_id='{key}'"
    sql2 += condition.format(key=search_key)
    cursor.execute(sql2)
    results = cursor.fetchall()

    table_header = ['项目编号', '样品名称', '物种', '样品编号', '判定结果', '上机数据量']
    table_values = results

    return table_header, table_values

# coding:utf-8
from models import SampleProjectMaster
from table import Table
from table.columns import Column

class ProjectViewTable(Table):
    id = Column(field='id', header='#')
    project_number = Column(field='project_number', header=u'项目编号')
    cust_user = Column(field='cust_user', header=u'客户名称')
    create_time = Column(field='create_time', header=u'创建时间')
    status = Column(field='status', header=u'状态')
    class Meta:
        model = SampleProjectMaster

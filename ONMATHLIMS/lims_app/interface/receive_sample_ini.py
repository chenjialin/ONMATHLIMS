# coding: utf8
def get_all_proj_info():

    return [('1', 'OMPJ-001'), ('2', 'OMPJ-002'), ('3', 'OMPJ-003'), ('4', 'OMPJ-004')]


def get_sample_by_project(project_id):
    """
    <th>样品编号</th>
                        <th>所属项目</th>
                        <th>快递编号</th>
                        <th>修改日期</th>
                        <!--<th>状态</th>-->
                        <th>样品备注</th>

    :param project_id:
    :return:
    """
    # smaple_id, project_name
    return [
        {'sample_id': 1, 'proj_name': 'OMPJ-001', 'express': '1111111', 'date': '11-7-2014', 'notes': '样品备注1'},
        {'sample_id': 2, 'proj_name': 'OMPJ-001', 'express': '22222', 'date': '11-7-2014', 'notes': '样品备注2'},
        {'sample_id': 3, 'proj_name': 'OMPJ-001', 'express': '33333', 'date': '11-7-2014', 'notes': '样品备注3'},
        {'sample_id': 4, 'proj_name': 'OMPJ-001', 'express': '4444', 'date': '11-7-2014', 'notes': '样品备注4'},

    ]


def get_sample_by_project2(project_id):
    """
    <th>样品编号</th>
                        <th>所属项目</th>
                        <th>快递编号</th>
                        <th>修改日期</th>
                        <!--<th>状态</th>-->
                        <th>样品备注</th>

    :param project_id:
    :return:
    """
    # smaple_id, project_name
    return [
        (1, 1, 'OMPJ-001', '1111111', '11-7-2014', '样品备注1'),
        (2, 2, 'OMPJ-002', '2222', '11-7-2014', '样品备注3'),
        (3, 3, 'OMPJ-003', '333', '11-7-2014', '样品备注2'),
        (4, 4, 'OMPJ-004', '4444', '11-7-2014', '样品备注2'),
    ]

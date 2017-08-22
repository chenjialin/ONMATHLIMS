class DbObjectDoesNotExist(Exception):
    pass


select_colums_dict = {'send_sample': ['sample_name', 'om_id', 'project_number', 'species', 'express_number', 'product_num', 'create_time', 'comment'],
                'quality_check': ['sample_name', 'om_id', 'sample_id', 'project_number', 'rin', 'concentration', 'volume', 'results', 'create_time', 'comment'],
                'build_lib': ['sample_id', 'om_id', 'sample_name', 'project_number', 'lib_id', 'create_time', 'comment'],
                'upmachine': ['sample_id', 'om_id', 'sample_name', 'project_number', 'upmachinetype', 'mode', 'data_count', 'create_time', 'comment'],
                'downmachine': ['sample_name', 'om_id', 'sample_id', 'project_number', 'data_count', 'q20', 'q30', 'create_time', 'comment']}

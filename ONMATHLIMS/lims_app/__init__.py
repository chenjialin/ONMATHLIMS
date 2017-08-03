class DbObjectDoesNotExist(Exception):
    pass


select_colums_dict = {'send_sample': ['sample_name', 'project_number', 'species', 'express_number', 'product_num', 'time', 'comment'],
                'quality_check': ['sample_name', 'sample_id', 'project_number', 'rin', 'concentration', 'volume', 'results', 'time', 'comment'],
                'build_lib': ['sample_id', 'sample_name', 'project_number', 'lib_id', 'time', 'comment'],
                'upmachine': ['sample_id', 'sample_name', 'project_number', 'upmachinetype', 'mode', 'data_count', 'time', 'comment'],
                'downmachine': ['sample_name', 'sample_id', 'project_number', 'data_count', 'q20', 'q30', 'time', 'comment']}

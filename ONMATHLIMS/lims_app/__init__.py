class DbObjectDoesNotExist(Exception):
    pass


select_colums_dict = {'receive_sample': ['sample_name', 'express_number', 'product_num', 'sendsample_time', 'sendsample_comment'],
                'quality_check': ['sample_id', 'sample_name', 'rin', 'concentration', 'volume', 'qualitycheck_results', 'qualitycheck_time', 'qualitycheck_comment'],
                'build_lib': ['sample_id', 'sample_name', 'lib_id', 'lib_time', 'lib_comment'],
                'upmachine': ['sample_id', 'sample_name', 'upmachine_type', 'upmachine_mode', 'upmachine_num', 'upmachine_time', 'upmachine_comment'],
                'downmachine': ['sample_id', 'sample_name', 'downmachine_num', 'q20', 'q30', 'downmachine_time', 'downmachine_comment']}

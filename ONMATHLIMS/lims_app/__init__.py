class DbObjectDoesNotExist(Exception):
    pass

comment_dict = {'receive_sample': 'sendsample_comment',
                'quality_check': 'qualitycheck_comment',
                'build_lib': 'lib_comment',
                'upmachine': 'upmachine_comment',
                'downmachine': 'downmachine_comment'}

import os, traceback, socketio
from datetime import datetime, timedelta
from flask import jsonify, json, send_file
from plugin import *

setting = {
    'filepath' : __file__,
    'use_db': True,
    'use_default_setting': True,
    'home_module': 'setting',
    'menu': {
        'uri': __package__,
        'name': 'RIDIRM',
        'list': [
            {'uri': 'setting', 'name': '설정'},
            {'uri': 'book_list', 'name': '책 목록'},
            {'uri': 'manage', 'name': '관리'},
            {'uri': 'log','name': '로그',},
        ]
    },
    'setting_menu': None,
    'default_route': 'single',
}

P = create_plugin_instance(setting)

DEFINE_DEV = False
if os.path.exists(os.path.join(os.path.dirname(__file__), 'logic.py')):
    DEFINE_DEV = True

try:
    if DEFINE_DEV:
        from .logic import Logic
    else:
        from support import SupportSC
        Logic = SupportSC.load_module_P(P, 'logic').Logic

    P.set_module_list([Logic])
except Exception as e:
    P.logger.error(f'Exception:{str(e)}')
    P.logger.error(traceback.format_exc())

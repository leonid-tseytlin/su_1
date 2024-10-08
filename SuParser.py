import json
import logging

ROOT = "root"
WORD_CLASS = "class"
GET_ROOTS = "get_roots"
ROOTS_LIST = "roots_list"
GET_FORM = "get_form"
FULL_FORM = "full_form"
TRANSLATE = "translate"
TRANS_RESULT = "translation"
EXIT_APP = "exit_app"

class SuParser():
    def __init__(self, key_list):
        self.key_list = key_list

    def parse(self, message):
#        logging.debug(message)
        msg_data = json.loads(message)
        logging.debug(msg_data)

        for key in self.key_list:
            if key in msg_data:
                return key, msg_data[key]

        return None
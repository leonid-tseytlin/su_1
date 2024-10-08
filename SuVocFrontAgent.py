import json
import logging
import threading
import SuParser


class SuVocFrontAgent():
    def __init__(self, inp_q, outp_q):
        self.inp_q = inp_q
        self.outp_q = outp_q

        self.parser = SuParser.SuParser((SuParser.ROOTS_LIST, SuParser.FULL_FORM, SuParser.TRANS_RESULT))

    def listenThreadFunc(self, inp_q, cbFn):
        logging.info('Thread running')
        msg = inp_q.get()
        logging.debug('Message "%s" received', msg)
        key, parsed_data = self.parser.parse(msg)
        logging.debug(key)
        logging.debug(parsed_data)
        cbFn(parsed_data)

    def get_roots_by_starting(self, starting, cbFn):
        self.createListener(cbFn)
        self.outp_q.put(json.dumps({SuParser.GET_ROOTS: starting}))

    def get_translation_by_root(self, root, cbFn):
        self.createListener(cbFn)
        self.outp_q.put(json.dumps({SuParser.TRANSLATE: root}))

    def get_full_form_by_root(self, root):
        self.outp_q.put(json.dumps({SuParser.GET_FORM: root}))

    def send_exit_app_to_voc(self):
        self.outp_q.put(json.dumps({SuParser.EXIT_APP: ""}))

    def createListener(self, cbFn):
        listen_thread = threading.Thread(target=self.listenThreadFunc, args=(self.inp_q, cbFn))
        listen_thread.start()

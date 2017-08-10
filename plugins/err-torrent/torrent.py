# coding: utf-8

import os
import requests
import bot_define
from errbot import BotPlugin, botcmd


class Torrent(BotPlugin):
    """
    Torrent Job only oNsemy
    """

    @botcmd  # flags a command
    def torrent(self, msg, args):  # a command callable with !tryme
        """
        url or magnet add (one by one)
        """
        if msg.frm != self.build_identifier(bot_define.BOT_ADMIN_ID):
            # deny!
            stream = self.send_stream_request(msg.to, open(os.getcwd() + '/resources/deny_new.jpg', 'rb'), name = 'deny_new.jpg', stream_type = 'photo')
            return

        self.log.info('args: ' + args)
        validations = ['http://', 'magnet:', 'https://', 'bc://bt/']
        if all(not (val in args) for val in validations):
            stream = self.send_stream_request(msg.to, open(os.getcwd() + '/resources/nooo.gif', 'rb'), name = 'nooo.gif', stream_type = 'document')
            return

        params = {'urls':args}
        # headers = {multipart/form-data; boundary=---------------------------6688794727912}
        yield "Request Torrent Job!"

        result = requests.post(bot_define.TORRENT_URL, params)

        if not result:
            yield "Something has wrong!"
            return

        yield "Result: " + result.status_code + " - " + result.reason

import schedule
import time
import itchat
import random

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
#	print(msg.User['RemarkName'])
	print(msg)
	if msg.User['RemarkName'] == 'XXX':
		return 'hello world'

itchat.auto_login(hotReload=True)
itchat.run()



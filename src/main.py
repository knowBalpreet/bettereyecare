import os,time,sys
ctr = int(sys.argv[1]) 
while True:
	print "Start"
	os.system('python2 stop.py {}'.format(ctr))
	print "Stop!"
	for i in range(2700):
		print i
		time.sleep(1)
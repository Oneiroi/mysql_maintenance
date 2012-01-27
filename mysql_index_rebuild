#!/usr/bin/env python

import os,sys,ConfigParser,getopt
import MySQLdb
from time import time,strftime,gmtime

'''
This utility is designed to be run as a crojob, it will run 'analyze table' on every table to force  a rebuild of indexes, ensure therefor that this is not done at peak times for your web app.
__author__="David Busby"
__copyright__="David Busby Saiweb.co.uk"
__license__="GNU v3 + part 5d section 7: Redistribution/Reuse of this code is permitted under the GNU v3 license, as an additional term ALL code must carry the original Author(s) credit in comment form."
__version__="0.2"
'''

def log(log,str):
    str = '[%s] %s\n' %((strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())),str)
    f = file(log, 'a+')
    f.write(str)
    f.close()

def usage():
	print 'Usage:',sys.argv[0],'-c /root/.my.cnf'
	print 'Note: -c is an optional overide, assumes default location if missing'
	sys.exit(0)

def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:],"hc:",["help","config="])
	except getopt.GetoptError,err:
		print str(err)
		usage()
	logfile = '/var/log/mysql_index_rebuild.log'
	cnf = '/root/.my.cnf'
	for o, a in opts:
		if o in ('-c','--config'):
			cnf = a
		else:
			assert False,"Unsupported option"

        if not os.path.isfile(cnf):
                print 'Configuration file does not exist!',cnf
                sys.exit(1)
        else:
                cfg = ConfigParser.ConfigParser()
                cfg.read(cnf)

		try:
                	usr = cfg.get('client','user')
                	pwd = cfg.get('client','password')
		except (ConfigParser.NoOptionError or ConfigParser.NoSectionError), e:
			print 'Missing a required configuration option'
                	print e
                	sys.exit(1)

                db = MySQLdb.connect(host="localhost",user=usr,passwd=pwd,db="information_schema")
                cursor = db.cursor()
                sql="SELECT CONCAT('`',TABLE_SCHEMA,'`','.','`',TABLE_NAME,'`') AS TABLE_NAME FROM TABLES WHERE TABLE_SCHEMA NOT IN ('information_schema','mysql','test') AND ENGINE IS NOT NULL;"
                cursor.execute(sql)
                res = cursor.fetchall()
		i = 0
                for row in res:
                        sql = 'analyze table %s' % row[0]
                        log(logfile,'Analyzing table %s' % (row[0]))
                        try:
				cursor.execute(sql)
				ares = cursor.fetchall()
                        	log(logfile,'Analyze complete for %s returned %s' %(row[0],ares))
			except:
				log(logfile,'Optimize for %s failed SQL(%s)'%(row[0],sql))
if __name__ == '__main__':
        main()


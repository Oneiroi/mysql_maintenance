#!/usr/bin/env python

import os,sys,ConfigParser,getopt
import MySQLdb
from time import time,strftime,gmtime

'''
This utility is designed to be run as a crojob, it will check for and optimize mySQL myISAM tables based on the configuration file in /etc/myisam_defrag/myisam_defrag.conf
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
	print 'Usage:',sys.argv[0],'-c /etc/myisam_defrag/myisam_defrag.conf'
	print 'Note: -c is an optional overide, assumes default location if missing'
	sys.exit(0)

def main():
	try:
		opts,args = getopt.getopt(sys.argv[1:],"hc:",["help","config="])
	except getopt.GetoptError,err:
		print str(err)
		usage()

	cnf = '/etc/myisam_defrag/myisam_defrag.conf'
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
                 logfile = cfg.get('myisam_defrag','logfile')
                 login_conf = cfg.get('myisam_defrag','login_conf')
                 frag_thresh = cfg.getint('myisam_defrag','frag_thresh')
	except (ConfigParser.NoOptionError or ConfigParser.NoSectionError), e:
		print 'Missing a required configuration option'
		print e
		sys.exit(1)

                if not os.path.isfile(login_conf):
                        print 'login_conf does not exist!',login_conf
                        sys.exit(1)
                else:
                        cfg.read(login_conf)
		try:
                         usr = cfg.get('client','user')
                         pwd = cfg.get('client','password')
		except (ConfigParser.NoOptionError or ConfigParser.NoSectionError), e:
			print 'Missing a required configuration option'
                        print e
                        sys.exit(1)

                        db = MySQLdb.connect(host="localhost",user=usr,passwd=pwd,db="information_schema")
                        cursor = db.cursor()
                        sql="SELECT CONCAT(TABLE_SCHEMA,'.',TABLE_NAME) AS TABLE_NAME, (DATA_FREE/DATA_LENGTH) AS FRAG_RATIO FROM TABLES WHERE ENGINE = 'MyISAM' AND DATA_LENGTH >=(1024*1024) AND (DATA_FREE/DATA_LENGTH) >=%s" % (1.00*frag_thresh/100)
                        cursor.execute(sql)
                        res = cursor.fetchall()
			i = 0
                        for row in res:
				i+=1
                                sql = 'optimize table %s' % row[0]
                                log(logfile,'%s found to be %s%% fragmented optimizing' % (row[0],(row[1]*100)))
                                cursor.execute(sql)
			if i == 0:
				log(logfile,'No tables to optimize on this run, try lowering your fragmentation threashold in %s?'%cnf)
if __name__ == '__main__':
        main()


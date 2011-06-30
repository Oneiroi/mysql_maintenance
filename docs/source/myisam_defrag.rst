.. sectionauthor:: David Busby <d.busby@saiweb.co.uk>
.. _myisam_defrag:

myisam_defrag
=============

SYNOPSIS
--------

myisam_defrag.py **[OPTION] [FILE]**

DESCRIPTION
-----------

myisam_defrag.py will run by default by loading the configuration file from /etc/myisam_defrag.conf, it may be optionaly overidden using
	**-c, --config**
		Load this configuration file 

logs will be written to /var/log/myisam_defrag.log

EXAMPLES
--------

myisam_defrag.py -c /path/to/alternate/config

REPORTING BUGS
--------------

Please raise an issue @ github https://github.com/Oneiroi/mysql_maintenance/issues/new


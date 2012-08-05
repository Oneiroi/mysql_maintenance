.. sectionauthor:: David Busby <oneiroi@fedoraproject.org>
.. _myisam_defrag.conf:

myisam_defrag
=============

SYNOPSIS
--------

myisam_defrag.conf

DESCRIPTION
-----------

Configuration file used with the myisam_defrag tool.


OPTIONS
-------

1. logfile=/path/to/logfile.log   - Used to define where to log output to, this contains details on the last run of the tool
2. login_conf=/my/private/.my.cnf - Used to define the .my.cnf file from which to read in user credentials, can be root or must be a used with sufficent privileges to run optimize across all tables.
3. frag_thresh=N                  - Used to define the percentage fragmentation above which a table will be optimized.

EXAMPLES
--------

This is the default configuration as found in /etc/myisam_defag.conf post install, note as the placement of this config can be overriden at runtime, you can place this config file anywhere the user executing it has access to.

[myisam_defrag]
logfile=/var/log/myisam_defrag.log
;login conf should be a standard .my.cnf containing login credentials for a user that can run optimize globally
login_conf=/root/.my.cnf
; fragementation percentage above which to run an optimization
frag_thresh=5


REPORTING BUGS
--------------

Please raise an issue @ github https://github.com/Oneiroi/mysql_maintenance/issues/new

SEE ALSO
--------

myisam_defrag(8)

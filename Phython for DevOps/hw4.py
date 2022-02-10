# Task:There is some rpm-file. 
# Create program that outputs header field rpm.RPMTAG_RELEASE of this file.

import sys
import rpmfile

with rpmfile.open(sys.argv[1]) as rpm:
    print(rpm.headers.get('name')).decode('ascii'),
    rpm.headers.get('release').decode('ascii'),
    rpm.headers.get('version').decode('ascii'),
        

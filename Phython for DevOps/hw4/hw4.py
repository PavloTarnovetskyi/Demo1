import sys, rpmfile

with rpmfile.open(sys.argv[1]) as rpm:
      print(rpm.headers.get('name').decode('ascii'), 
            rpm.headers.get('release').decode('ascii'),
            rpm.headers.get('version').decode('ascii'),
            sep='\n')

   
## Comand to execute this script:
## python3 hw4.py some_package.el6.x86_64.rpm
#--- Author : Ali Hojaji ---#

#--*------------------------*--#
#---> Copy Files By Python <---#
#--*------------------------*--#

import shutil
import os
import glob
from pathlib import Path
import time

#Step 0
#For connect vpn we use commad below
# os.system('rasdial "vpn_name" "username" "password"')
#if username and password are correct vpn will be connected 
# time.sleep(10)

#Step 1
#Now we are going to "E:/Test/*"  this location and we sort file by date of create (sort by descending mean the news file be first and ascending the oldest file be first one)
files = glob.glob(os.path.expanduser(r"\\192.168.1.10\Newfolder\test\*")) #(r"\\<ip>\Newfolder\test\*") Enter your IP and path here
sorted_by_mtime_ascending = sorted(files, key=lambda t: os.stat(t).st_mtime)
sorted_by_mtime_descending = sorted(files, key=lambda t: -os.stat(t).st_mtime)
first = sorted_by_mtime_descending[0]
print(first[39:]) #you must find your correct number by test

#Step 2
#after sorting file by date of create now we coppy file in new location
source_path = first
dest_path = r"\\192.168.1.11\Backup" # r"\\<ip>\Newfolder*" Enter your destination IP and Path here
Test = first[39:]
test2 = "\\" +  Test
file_name = test2
print(file_name)
shutil.copyfile(source_path , dest_path +file_name )


#Step 3
#after we coppy file we will disconnect the vpn
# os.system('rasdial "vpn_name" /disconnect')    #rasdial "vpn connection name" /disconnect
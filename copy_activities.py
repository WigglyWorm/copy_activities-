# Nicola Blackstock
#Assignment 4 Part 2
#Due Date: June 26th 2019
# UCBE Cyber Security 

import os
import shutil

def stu_activities():
    dest = "/Users/nicolablackstock/Desktop/CyberSecurity/homework/HW_week4_Python/CyberSecurity-Notes"
    src = "/Users/nicolablackstock/Desktop/UCBBMT201905CYBER4/Activities/"
    
    src_dir_list = os.listdir(src)
    print(src_dir_list)
    for dirname, dirs, files in os.walk(src):
        for a_dir in dirs:
            if("Stu_" in a_dir):
                pathHead, parentdir = (os.path.split(dirname))
                if(parentdir == 'Activities' and (os.path.split(pathHead)[1] == "03.1 Python1 Activities")):
                    pathHead, parentdir = os.path.split(pathHead)
                digit = 0
                for d in parentdir:
                    if d.isdigit():
                        break
                    digit += 1

                week = int (parentdir[digit : digit+2])
                day =  int (parentdir[digit+3 : digit+5])

                from_src = os.path.join(dirname, a_dir)
                new_dest = os.path.join(dest, ("Week " + str(week)), ("Day " + str(day)), a_dir)

                shutil.copytree (from_src, new_dest)
                print ("Copy '" + str(from_src) + "' directory to '" + str(new_dest) + "'")
              
stu_activities()
        
 
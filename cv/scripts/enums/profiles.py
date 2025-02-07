import enum
import os

# List of directories where profiles should be taken from
# /!\ if new directories are creates to hold profiles, they must be added here
base_dir =  "./../profiles/"
profile_dirs = [
    base_dir,
    f"{base_dir}examples/"
    ]

profiles = []
for dir in profile_dirs:
    # print(dir)
    profiles += [(name,dir.replace(base_dir,"")  + name) for name in os.listdir(dir)]

# Dinamically generate enum based on directory list contents
# this system is not perfect as it may included non-profile entries
Profile = enum.Enum('Profile', dict(profiles))
# print(list(Profile))
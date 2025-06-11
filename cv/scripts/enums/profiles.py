import enum
import os

# List of directories where profiles should be taken from
# /!\ if new directories are creates to hold profiles, they must be added here
base_dir = "./../../profiles/"
profile_dirs = [base_dir, f"{base_dir}examples/"]
excluded_dirs = ["examples"] # directories to exclude from the list of profiles, for example a folder containing example profiles 

profiles = []
for dir in profile_dirs:
    profile_names = [f for f in os.listdir(dir) 
                     if  os.path.isdir(os.path.join(dir, f))  # check that it is a directory
                     and f not in excluded_dirs # check that it is not in the excluded directories
                     ]
    profiles += [(name, dir.replace(base_dir, "") + name) for name in profile_names]

# Dinamically generate enum based on directory list contents
# this system is not perfect as it may included non-profile entries
Profile = enum.Enum("Profile", dict(profiles))
# print(list(Profile))

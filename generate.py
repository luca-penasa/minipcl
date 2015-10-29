#!/usr/bin/python3

import subprocess
import glob
import os
import fnmatch
from pip.commands.show import search_packages_info
import re

import shutil

pcl_dir = "pcl.git"

do_git = True


if do_git:
    if (os.path.exists(pcl_dir)):
        print ("found pcl git dir in: " + pcl_dir)
        print("Not cloning, just pulling!")
        pr = subprocess.Popen(["git", "pull", "origin", "master"], cwd=pcl_dir)
        (out, error) = pr.communicate()

    else:
        print("cannot find pcl git dir, going to do a shallow clone")
        pr = subprocess.Popen(["git", "clone", "https://github.com/PointCloudLibrary/pcl.git", pcl_dir, "--depth=1"])
        (out, error) = pr.communicate()



def locate(pattern, root_path):
    for path, dirs, files in os.walk(os.path.abspath(root_path)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

def readAllFiles(path):
    out = []
    for path, dirs, files in os.walk(os.path.abspath(path)):
        for filename in files:
            out.append(os.path.join(path, filename))

    return out;

def includePathToFullPath(include, search_dirs):
    matches = []

    for dir in search_dirs:
        files = readAllFiles(dir)
        for f in files:
            if re.match('.*' + include, f):
                matches.append(f)


    if len(matches) > 1:
        sys.exit("FOUND SEVERAL POTETENTIAL HEADERS!!!")


    if len(matches) == 0:
        print ("No matches found. returning None")
        return None

    return matches[0]



def getMatches(pattern, search_paths):
    matches  = []
    for p in search_paths:
        for m in locate(pattern, p):
            matches.append(m)

    return matches


source_origin = "auto_io.cpp"



search_mod = [pcl_dir + '/common' ,  pcl_dir + '/io', pcl_dir + '/filters']


full_source_origin = includePathToFullPath(source_origin, search_mod)



# source_origin_full = getMatches(source_origin, search_mod)

# if (len(found) != 1):
#     import sys
#     sys.exit("Too many matches!")


def extract_lines(exp, fname):
    matches = []
    f = open(fname, "r")
    regex = re.compile(exp)

    for line in f:
        print(line)
        if regex.match(line):
            matches.append(line)

    return matches

def extract_h(fname):
    with open(fname) as fp:
        lines = fp.read()

    return re.findall(r'\s*#include\s*[<"]\s*(.*.h)\s*[>"]\s*', lines)


def extract_hpp(fname):
    with open(fname) as fp:
        lines = fp.read()

    return re.findall(r'\s*#include\s*[<"]\s*(.*.hpp)\s*[>"]\s*', lines)

#
# def hasCPP(fname):
#     out = fname.replace('.h', '.cpp')
#     return os._exists(out)



tocheck = ["src/auto_io.cpp", "pcl/filters/passthrough.h"]
checked = []

full_list = []



while len(tocheck) != 0:
    file = tocheck.pop()

    if file in checked:
        continue


    filename, file_extension = os.path.splitext(file)

    if file_extension == ".h":
        splits = os.path.split(filename)
        ascpp = "src/" + splits[-1] + '.cpp'
        print("-->>> verifying: " + ascpp)
        full_cpp = includePathToFullPath(ascpp, search_mod)

        if full_cpp != None and ascpp not in checked:
            tocheck.append(ascpp)





    full_file = includePathToFullPath(file, search_mod)




    checked.append(file)

    if full_file == None:
        continue


    full_list.append([file, full_file])

    hs = extract_h(full_file)
    hpps = extract_hpp(full_file)


    print("For File: " + full_file + " found:")
    print("Headers: ")
    print(hs)
    print("hpp: ")
    print(hpps)
    print("\n\n")

    for h in hs:
        if re.match('pcl.*', h) and h not in checked:
            tocheck.append(h)

    for hpp in hpps :
        if re.match('pcl.*', hpp) and hpp not in checked:
            tocheck.append(hpp)

minipcl_name = "minipcl"

if os.path.exists(minipcl_name):
     shutil.rmtree(minipcl_name)
#     os.makedirs(minipcl_name)


for inc, file in full_list:
    print("Verify " + inc)
    if not os.path.exists(file):
        print("FILE NOT FOUND: " + file)
        continue
    else:
        print("OK")



    path, fname = os.path.split(inc)
    full = minipcl_name + "/" + path
    os.makedirs(full, exist_ok=True)

    full_with_name = full + "/" + fname

    shutil.copy(file, full_with_name)


additional_cpp = [pcl_dir + "/io/src/ply/ply_parser.cpp"]

for cpp in additional_cpp:
    shutil.copy(cpp, minipcl_name + "/src/")


shutil.copy("pcl_config.h", "minipcl/pcl/pcl_config.h")

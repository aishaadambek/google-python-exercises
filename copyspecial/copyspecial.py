#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):

  special_paths = []
  special_pat = r'__\w+__'

  for filename in os.listdir(dir):
    match = re.search(special_pat, filename)
    if match:
      special_paths.append(os.path.abspath(os.path.join(dir, filename)))

  for path in special_paths:
    print path

  return special_paths


def copy_to(special_paths, todir):
  if not os.path.exists(to_dir):
    os.system("sudo mkdir " + todir)
    os.system("sudo chmod 777 " + todir)
  todir_abs = os.path.abspath(todir)
  for path in special_paths:
    shutil.copy(path, todir_abs)


def zip_to(special_paths, tozip):
  string = ' '.join(special_paths)
  print "Command I am going to run: zip -j " + tozip + " " + string
  try:
    subprocess.check_output(['zip', '-j', tozip] + special_paths)
  except subprocess.CalledProcessError as e:
    print e.output, e.returncode
    sys.exit(e.returncode)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  dir = args[0]
  special_paths = get_special_paths(dir)

  if todir:
    copy_to(special_paths, todir)

  if tozip:
    zip_to(special_paths, tozip) 



if __name__ == "__main__":
  main()

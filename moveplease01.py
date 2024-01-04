#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
        Alta3 Research | rzfeeser@alta3.com"""


def main():
    #standard lib imports
    import shutil #shell utilies to move files
    import os


    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

#!/usr/bin/env python
#coding:utf-8

import os
import shutil

DESKTOP = "/home/emilio/Desktop/"
TARGET = "/home/emilio/Desktop/InBox"

def main():
	FILE_LIST = os.listdir(DESKTOP)
	for each in FILE_LIST:
		if os.path.isfile(DESKTOP+each):
			shutil.move(DESKTOP+each, TARGET)
	print "Done...!"


if __name__ == '__main__':
	main()

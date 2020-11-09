#!/usr/bin/env python3

import os
import sys
import subprocess

def run_cmd(cmd, stderr=None, stdout=None):
	if cmd[0] == "git":
		ret = subprocess.Popen(cmd, env=None, cwd=None, stderr=None, stdout=subprocess.PIPE)
	else:
		ret = subprocess.Popen(cmd, env=None, cwd=None, stderr=None, stdout=subprocess.PIPE)
	ret.wait()

def find_str_in_file_return_index(str, file):
	rc = -1
	with open(file, "r") as f:
		pos = f.read().find(str)
		f.close()
		rc = pos
	return rc

def find_str_in_file_return_line(str, file):
	with open(file, "r") as f:
		data_file = f.readlines()
		line_index = 0;
		for line in data_file:
			line_index = line_index + 1
			if str in line:
				f.close()
				return line_index
		f.close()
	return -1

def find_strip_str_in_file_return_line(str, file):
	with open(file, "r") as f:
		data_file = f.readlines()
		line_index = 0;
		for line in data_file:
			line_index = line_index + 1
			if str == line.strip():
				f.close()
				return line_index
		f.close()
	return -1

def get_last_line_in_file(file):
	with open(file, "r") as f:
		data_file = f.readlines()
		for last_line in data_file:
			pass
		f.close()
	return last_line

def get_line_count_in_file(file):
	line_count = 0
	with open(file, "r") as f:
		data_file = f.readlines()
		for last_line in data_file:
			line_count = line_count + 1
			pass
		f.close()
	return line_count

def write_str_to_end_of_file(str, file):
	line_count = 0
	with open(file, "a+") as f:
		f.write(str)
		f.close()


#!/usr/bin/env python3

import os
import sys

import utils

virtium_header = "# Add Virtium recipes support"
vt_append = "IMAGE_INSTALL_append = \" vttestcmd vtsecurecmd vtview dataretentiontest sanitizedemonstration\""

class Setup():
	def main(self, args):
		if args[1] == "-m":
			if args[2] == "x86-64":
				branch = "x86-64"
			elif args[2] == "arm":
				branch = "arm"
			else:
				print("Do not support this machine")
				return

			cmd = ["rm", "-rf", "layers/meta-virtium"]
			utils.run_cmd(cmd)

			url = "https://github.com/virtiumssd/meta-virtium.git"
			cmd = ["git", "-C", "layers", "clone", "-b", branch, url]
	    		utils.run_cmd(cmd)

			# modify bblayers.conf
			bblayers_path = os.getcwd() + "/build/conf/bblayers.conf"
			vt_layer_path = os.getcwd() + "/layers/meta-virtium \\"
			if 0 > utils.find_str_in_file_return_index(vt_layer_path, bblayers_path):
				line_index = utils.find_strip_str_in_file_return_line("\"", bblayers_path)
				if line_index > 0:
					line_index = line_index - 1
					with open(bblayers_path, "rw+") as f:
						contents = f.readlines()
						contents.insert(line_index, "  " + vt_layer_path + "\n")
						contents = "".join(contents)
						f.seek(0)
						f.write(contents)
						f.close()

			# modify local.conf
			local_path = os.getcwd() + "/build/conf/local.conf"
			if 0 > utils.find_str_in_file_return_index(virtium_header, local_path):
				append_str = virtium_header + "\n" + vt_append;
				if "" != utils.get_last_line_in_file(local_path):
					append_str = "\n" + append_str;
				utils.write_str_to_end_of_file(append_str, local_path)
		else:
			print("Do not support this argument")

if __name__ == '__main__':
    x = Setup()
    x.main(sys.argv)


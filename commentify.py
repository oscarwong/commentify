file_name = "input.txt"
output_name = "output.txt"
comment = "//"

with open(output_name, 'w') as out_file:
	with open(file_name, 'r') as in_file:
		for line in in_file:
			out_file.write(comment + ' ' + line)
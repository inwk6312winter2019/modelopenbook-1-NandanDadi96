def replace_ip():
	fout = open("running-config.cfg","r")
	for line in fout:
		if("address" in line and "." in line):
			line = line.split()
			temp_ip = line[2].split()
			temp_mask = line[3].split()
			if(temp_ip[0] == "192"):
				temp_ip[0]="10"
				temp_mask[0] = "255"
				temp_mask[1] = "0"
				temp_mask[2] = "0"
				temp_mask[3] = "0"
			elif(temp_ip[0] == "172"):
				temp_ip[0].replace("172","10")
				temp_mask[0] = "255"
				temp_mask[1] = "0"
				temp_mask[2] = "0"
				temp_mask[3] = "0"
				line = line[0]+line[1] + ".".join(temp_ip)+" "+".".join(temp_mask)
	print(line)
	print(temp_ip)
	print(temp_mask)



replace_ip()


soc1_registers = []
soc2_registers = []
mem1_registers = []
mem2_registers = []

with open('temp.txt','r') as file: # adjust the input file name/path
	for line in file:
		for word in line.split():
			if (word.split('/')[0] == 'mem1'):
				mem1_registers.append(word)
			if (word.split('/')[0] == 'mem2'):
				mem2_registers.append(word)
			if (word.split('/')[0] == 'soc1'):
				soc1_registers.append(word)
			if (word.split('/')[0] == 'soc2'):
				soc2_registers.append(word)

with open('out.txt','w') as file:
	file.write('macro boolean state_equivalence := \n')
	for i in range(len(mem1_registers)):
		file.write('\t'+mem1_registers[i]+'=='+mem2_registers[i]+' &&\n')

	for i in range(len(soc1_registers)-1):
		file.write('\t'+soc1_registers[i]+'=='+soc2_registers[i]+' &&\n')

	file.write('\t'+soc1_registers[len(soc1_registers)-1]+'=='+soc2_registers[len(soc1_registers)-1]+';\n')
	file.write('end macro;')
	file.write('\n\n\n')

	file.write('macro boolean state_uniqueness := \n')
	for i in range(len(mem1_registers)):
		file.write('\t'+mem1_registers[i]+'=='+mem2_registers[i]+' &&\n')

	for i in range(len(soc1_registers)-1):
		file.write('\t'+soc1_registers[i]+'=='+soc2_registers[i]+' &&\n')

	file.write('\t'+soc1_registers[len(soc1_registers)-1]+'=='+soc2_registers[len(soc1_registers)-1]+';\n')
	file.write('end macro;')


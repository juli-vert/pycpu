import subprocess
import json
cpus = {}
cpu = {}
t = subprocess.run(['cat', '/proc/cpuinfo'], capture_output=True).stdout
tmpcpu = "Not value"
for line in t.decode().split('\n'):
	if 'processor' in line:
		if not len(cpu):
			tmpcpu = line.split(':')[1].strip()
		else:
			cpus.update({tmpcpu:cpu})
			tmpcpu = line.split(':')[1].strip()
			cpu = {}
	elif line == '':
		pass
	else:
		print(line)
		(k,v) = line.split(':')
		v = v.strip()
		if 'flags' in k:
			v = v.strip().split(' ')
		cpu.update({k.strip('\t'):v})
cpus.update({tmpcpu:cpu})
j = json.dumps(cpus)
return j

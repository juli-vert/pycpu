from os import system
import json

def getcpuinfo():
	cpus = {}
	cpu = {}
	system('cat /proc/cpuinfo > cpuinfo.ini')
	tmpcpu = "Not value"
	with open('cpuinfo.ini', 'r') as f:
		for line in f.readlines():
			if 'processor' in line:
				if not len(cpu):
					tmpcpu = line.split(':')[1].strip()
				else:
					cpus.update({tmpcpu:cpu})
					tmpcpu = line.split(':')[1].strip()
					cpu = {}
			elif line == '\n':
				pass
			else:
				(k,v) = line.split(':')
				v = v.strip()
				if 'flags' in k:
					v = v.split(' ')
				cpu.update({k.strip('\t'):v})
	cpus.update({tmpcpu:cpu})
	j = json.dumps(cpus)
	return j

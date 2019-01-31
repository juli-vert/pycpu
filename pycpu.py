import json

def getcpuinfo():
    cores = {}
    core = {}
    total = 0
    cpus = {}
    tmpcore = "Not value"
    with open('/proc/cpuinfo', 'r') as f:
        for line in f.read().split('\n'):
            if 'processor' in line:
                total += 1
                if len(core):
                    cores.update({tmpcore:core})
                    core = {}
                tmpcore = line.split(':')[1].strip()
            elif line == '\n' or line == "":
                pass
            else:
                (k,v) = line.split(':')
                v = v.strip()
                if 'physical id' in k:
                    if v in cpus.keys():
                        cpus[v] = cpus[v]+1
                    else:
                        cpus.update({v:1})
                elif 'flags' in k:
                    v = v.split(' ')
                core.update({k.strip('\t'):v})
    cores.update({tmpcore:core})
    cores.update({'totals':total})
    cores.update({'real':len(cpus)})
    cors = 0
    for it in cpus:
        cors += cpus[it]
    cores.update({'cores':cors})
    return json.dumps(cores)

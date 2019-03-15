#just: srt.py filename.srt offset_seconds(like 6)
import re
import sys
w = open(sys.argv[1])
n = []
for line in w:
    if ':' in line:
        i = [m.start() for m in re.finditer(':', line)]
        ii = [m.start() for m in re.finditer(',', line)]

        s1 = line[i[1]+1:ii[0]]
        s2 = line[i[3]+1:ii[1]]
        si1 = int(s1) + int(sys.argv[2])
        si2 = int(s2) + int(sys.argv[2])
        
        m1 = line[i[0] + 1: i[1]]
        m2 = line[i[2] + 1: i[3]]
        mi1 = int(m1)
        mi2 = int(m2)
        if( not si1 < 60):
            mi1 += 1
            si1 %= 60
        if( not si2 < 60):
            mi2 += 1
            si2 %= 60
        line = line.replace(f':{m1}:{s1},', f':{mi1}:{si1},')
        line = line.replace(f':{m2}:{s2},', f':{mi2}:{si2},')
    n.append(line)
w.close()

with open(sys.argv[1],'w') as f:
        for line in n:
            f.write(f'{line}')

print("DONE")

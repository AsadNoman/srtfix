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
        ws1 = str(int(s1)+int(sys.argv[2]))
        ws2 = str(int(s2)+int(sys.argv[2]))
        line = line.replace(f':{s1},', f':{ws1},')
        line = line.replace(f':{s2},', f':{ws2},')
    n.append(line)
w.close()

with open(sys.argv[1],'w') as f:
    for line in n:
        f.write(f'{line}')

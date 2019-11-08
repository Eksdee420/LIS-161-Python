while True:
    fname = input('Enter a file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        continue
    break

counts = dict()

for line in fhand:
    if line.startswith('From '):
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender,0) + 1

masterlist = list()

for key, val in counts.items():
    masterlist.append((val, key))

masterlist.sort(reverse=True)

print(masterlist)
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
        max = sender



for person in counts:
    if counts[person] > counts[max]:
        max = person

print(max, counts[max])
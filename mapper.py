import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print
        '%S\t%s' % (word, 1)
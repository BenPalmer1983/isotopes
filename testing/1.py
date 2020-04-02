fh = open('1.txt', 'r')
d = ''
for row in fh:
  d = d + row.strip()
d = d.replace("array", "numpy.array")
fh.close()
fh = open('2.txt', 'w')
fh.write(d)
fh.close()



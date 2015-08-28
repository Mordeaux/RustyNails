import thread

x = 0

for i in xrange(50000000):
    x += 1

print "thread finished at count: {}".format(x)
print "python is done"

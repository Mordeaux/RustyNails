from multiprocessing import Process



def single_thread():
    count = 0
    for i in xrange(50000000): 
        count += 1

    print "thread finished at count: {}".format(count)
    print "python is done"


def multithread():
    def worker():
        count = 0
        for i in xrange(5000000): 
            count += 1
        print "thread finished at count: {}".format(count)

    threads = []
    for i in xrange(10):
        thread = Process(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print "python is done"

if __name__ == '__main__':
    multithread()

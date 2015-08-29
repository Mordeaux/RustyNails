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
        for i in xrange(50000000): 
            count += 1
        print "thread finished at count: {}".format(count)

    jobs = []
    for i in xrange(10):
        thread = Process(target=worker)
        jobs.append(thread)
        thread.start()

    for job in jobs:
        job.join()

    print "python is done"

if __name__ == '__main__':
    multithread()

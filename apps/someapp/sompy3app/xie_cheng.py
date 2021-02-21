def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSLMER] Consuming %s...' % n)
        input()
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        input()
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
        input()
    c.close()
c = consumer()
produce(c)
print(c)

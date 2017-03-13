def coroutine(fn):
    def func(*args, **kwargs):
        obj = fn(*args, **kwargs)
        next(obj)
        return obj
    return func


def cat(text, case_insensitive, child):
    if case_insensitive:
        process = lambda x: x.lower()
    else:
        process = lambda x: x
    for line in text:
        child.send(process(line))


@coroutine
def grep(pattern, case_insensitive, child):
    if case_insensitive:
        pattern = pattern.lower()
    text = (yield)
    child.send(text.count(pattern))


@coroutine
def count(substring):
    n = 0
    try:
        while True:
            n += (yield)
    except:
        print(substring, n)



if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('-i',action='store_true',dest='case_insensitive')
    parser.add_argument('pattern', type=str)
    parser.add_argument('infile',type=argparse.FileType('r'))
    args=parser.parse_args()

    cat(args.infile,args.case_insensitive,grep(args.pattern,args.case_insensitive, count(args.pattern)))

for case in range(int(input())):
    n_engines = int(input())
    engines = [input() for _ in range(n_engines)]
    n_queries = int(input())
    queries = [input() for _ in range(n_queries)]
    swaps = []
    

    for start_engine in range(n_engines):
        curr_engine = start_engine
        swapped = 0
        for query in queries:
            if query == engines[curr_engine]:
                swapped += 1
                curr_engine = (curr_engine)%n_engines
        swaps.append(swapped)
    print("Case #", case+1, ": ", min(swaps), sep="")

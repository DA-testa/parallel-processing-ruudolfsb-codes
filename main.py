# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [0]*n
    for value in data:
        threadIndex = threads.index(min(threads))
        output.append([threadIndex,threads[threadIndex]])
        threads[threadIndex]+= value
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    imp = list(map(int,input().split()))
    n = imp[0]
    m = imp[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for value in result:
        print(value[0], value[1])
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
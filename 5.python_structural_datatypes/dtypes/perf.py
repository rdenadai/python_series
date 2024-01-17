from time import perf_counter


def perf_list(l):
    return 999_999 in l


def perf_set(s):
    return 999_999 in s


def main():
    N = 1_000_000
    l = [i for i in range(N)]
    s = {i for i in range(N)}

    t = []
    for _ in range(20):
        start = perf_counter()
        perf_list(l)
        t.append(perf_counter() - start)

    print("Took", sum(t) / len(t), "seconds for list")

    t = []
    for _ in range(20):
        start = perf_counter()
        perf_set(s)
        t.append(perf_counter() - start)
    print("Took", sum(t) / len(t), "seconds for set")


if __name__ == "__main__":
    main()

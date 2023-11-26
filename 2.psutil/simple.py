import psutil


def main():
    print(psutil.cpu_times(percpu=True))


if __name__ == "__main__":
    main()

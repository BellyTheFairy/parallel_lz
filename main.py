import subprocess
import time
import threading

def main():
    time1 = ping_by_once(IP)
    time2 = parallel_ping(IP)
    compare_times(time1, time2)


if __name__ == "__main__":
    main()

import subprocess  
import time        
import threading   

IP = [
    "34.64.46.97",
    "245.46.242.42",
    "9.8.7.6",
    "208.67.222.222",
    "8.8.4.4",
    "1.0.9.1",
    "77.88.8.8",
    "11.22.33.44",
    "192.168.1.1",
    "10.255.255.1",
]

def ping(ip):
    result = subprocess.run(["ping", "-w", "1", ip], capture_output = True)
    print(f"{ip} is {'up' if result.returncode == 0 else 'down'}")              

def ping_by_once(ip_list):
    start = time.time()
    for ip in ip_list:
        ping(ip)
    elapsed = time.time() - start

    print(f"Время (пинг по очереди): {elapsed:.2f} сек")
    return elapsed

def parallel_ping(ip_list):
    start = time.time()
    threads = []
    for ip in ip_list:
        t = threading.Thread(target=ping, args=(ip,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    elapsed = time.time() - start
    print(f"Время (параллельный пинг): {elapsed:.2f} сек")
    return elapsed

def compare_times(time1, time2):
    
    print(f"Пинг по очереди:  {time1:.2f} сек")
    print(f"Параллельный пинг:   {time2:.2f} сек")
    print(f"Разница:     {time1 - time2:.2f} сек")

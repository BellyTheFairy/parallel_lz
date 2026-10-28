import threading
import queue
import time
import random

def producer(box, name):
    for i in range(10):
        item = f"data-{name}-{i}"
        box.put(item)                          
        print(f"[Производитель {name}] положил {item}. В очереди: {box.qsize()}")
        time.sleep(0.1)                        


def consumer(box, name):
    while True:
        try:
            item = box.get(timeout=0.5)    
        except queue.Empty:
            break
        print(f"[Потребитель {name}] обработал {item}. В очереди: {box.qsize()}")
        time.sleep(0.2)                        
        box.task_done()                        
      
box = queue.Queue(maxsize=10)
#производители/потребители 
producers = [threading.Thread(target=producer, args=(box, f"P{i}")) for i in range(1, 4)]
consumers = [threading.Thread(target=consumer, args=(box, f"C{i}")) for i in range(1, 3)]

for t in consumers:
    t.start()
for t in producers:
    t.start()

for t in producers:
    t.join()
box.join()

for t in consumers:
    t.join()

print("Обработка завершена.")

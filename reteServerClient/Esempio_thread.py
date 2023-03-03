from threading import Thread
import time
#ereditarietà
#classe che definisce un thread
class Mythread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
        self.running = True
    
    def run(self):
        while self.running:
            print(f"Sono il thread {self.name}")
            time.sleep(1)
    
    def stop(self):
        self.running = False


def main():
    t1 = Mythread("Alice")      #istanza
    t2 = Mythread("Bob")  
    t1.start()
    t2.start()
    for _ in range(5):
        print("Sono il main thread")
        time.sleep(1)
    t1.stop()       #stoppa il ciclo while
    t2.stop()
    t1.join()       #quando il ciclo dei thread finisce, riunisce i flussi
    t2.join()
    
if __name__=="__main__":
    main()
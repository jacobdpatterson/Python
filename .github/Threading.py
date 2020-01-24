import threading
class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10): #if you dont wanna use the variable
            print(threading.currentThread().getName())

x = BuckysMessenger(name='Send out messages')
y = BuckysMessenger(name='Receive messages')
x.start() # X and Y will run concurrently. Usually will want to go in order, but could be useful for chat
y.start() # X and Y will run concurrently. Usually will want to go in order, but could be useful for chat
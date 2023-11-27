class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def print_front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

q = QueueUsingStacks()
inp = input().split(',')
for i in inp:
    if(len(i)>1):
        x = list(map(int, i.split()))
        quer=x[0]
        val =x[1]
    elif(len(i)<=1):
        quer = int(i)
    if(quer==1):
        q.enqueue(val)
    elif(quer==2):
        q.dequeue()
    elif(quer==3):
        print(q.print_front())
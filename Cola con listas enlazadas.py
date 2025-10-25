class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        """Imprime la información del pedido."""
        print(f"     Customer: {self.customer}")
        print(f"     Quantity: {self.qtty}")
        print("     ------------")

    def getCustomer(self):
        return self.customer

    def getQtty(self):
        return self.qtty


class Node:
    def __init__(self, data):
        self.data = data     
        self.next = None    

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

    def getData(self):
        return self.data

class Queue:
    def __init__(self):
        self.front_node = None   
        self.rear_node = None   
        self.count = 0          

    
    def size(self):
        return self.count

    
    def isEmpty(self):
        return self.count == 0

    
    def front(self):
        if self.isEmpty():
            return None
        return self.front_node.getData()

    
    def enqueue(self, info):
        new_node = Node(info)
        if self.isEmpty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.setNext(new_node)
            self.rear_node = new_node
        self.count += 1

    
    def dequeue(self):
        if self.isEmpty():
            return None
        removed_data = self.front_node.getData()
        self.front_node = self.front_node.getNext()
        self.count -= 1
        if self.count == 0:
            self.rear_node = None
        return removed_data

    
    def getNth(self, pos):
        if pos < 1 or pos > self.count:
            return None
        current = self.front_node
        for _ in range(pos - 1):
            current = current.getNext()
        return current.getData()

    
    def printInfo(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.count}")
        node = self.front_node
        idx = 1
        while node is not None:
            print(f"   ** Element {idx}")
            node.getData().print()
            node = node.getNext()
            idx += 1
        print("******************************")
        print()


if __name__ == "__main__":
    
    queue = Queue()

    
    order1 = Order(20, "cust1")
    order2 = Order(30, "cust2")
    order3 = Order(40, "cust3")
    order4 = Order(50, "cust4")

    
    queue.enqueue(order1)
    queue.enqueue(order2)
    queue.enqueue(order3)
    queue.enqueue(order4)

    print("\nDespués de encolar 4 pedidos:")
    queue.printInfo()

    
    print("Elemento al frente (front):")
    front_order = queue.front()
    if front_order:
        front_order.print()

    
    print("Desencolando un pedido...")
    dequeued = queue.dequeue()
    if dequeued:
        dequeued.print()

    print("Después de desencolar:")
    queue.printInfo()

    
    print("Obteniendo el tercer elemento (getNth(3)):")
    third_order = queue.getNth(3)
    if third_order:
        third_order.print()

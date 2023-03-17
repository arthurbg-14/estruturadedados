class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def lenght(self):
        if self.head == None:
            return 0
        total = 0
        current_node = self.head

        while current_node:
            total += 1
            current_node = current_node.next

        return total

    def to_list(self):
        if self.head == None:
            return []
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next

        return node_data

    def __str__(self):
        if self.head == None:
            return ""
        return str(self.to_list())

    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node

    def get(self, index):
        if index >= self.lenght() or index < 0:
            return None
        current_index = 0
        current_node = self.head

        while current_node:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index += 1

    def search(self, data):
        current_node = self.head

        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False

    def remove_at_start(self):
        self.head = self.head.next

    def remove_at_end(self):
        current_node = self.head

        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_value(self, element):
        current_node = self.head

        while current_node.next:
            if current_node.data == element:
                new_node = Node(element)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_at_index(self, index, element):
        current_node = self.head
        current_index = 0

        while current_node.next:
            if current_index == index:
                new_node = Node(element)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_index += 1
            current_node = current_node.next

    def remove(self, element):
        current_node = self.head

        while current_node:
            if current_node.data == element:
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next


my_list = LinkedList()
print(my_list)

my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.insert_at_start("as")
my_list.insert_at_index(0, "x")

print(my_list)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def search(self, data):
        curr = self.head
        pos = 1
        while curr:
            if curr.data == data:
                return pos
            curr = curr.next
            pos += 1
        return -1

    def insert_head(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def insert_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = temp

    def insert_node(self, pos, data):
        temp = Node(data)

        if pos == 1:
            temp.next = self.head
            self.head = temp
            return

        curr = self.head
        for _ in range(pos - 2):
            if curr is None:
                return
            curr = curr.next

        if curr is None:
            return

        temp.next = curr.next
        curr.next = temp

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return

        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    def delete_node(self, pos):
        if self.head is None:
            return

        if pos == 1:
            self.head = self.head.next
            return

        curr = self.head
        for _ in range(pos - 2):
            if curr is None:
                return
            curr = curr.next

        if curr is None or curr.next is None:
            return

        curr.next = curr.next.next


if __name__ == "__main__":
    ll = SinglyLinkedList()

    ll.insert_end(78)
    ll.insert_end(65)
    ll.insert_end(45)
    ll.print_list()

    ll.insert_head(90)
    ll.print_list()

    ll.insert_end(19)
    ll.print_list()

    ll.insert_node(3, 36)
    ll.print_list()

    ll.delete_head()
    ll.print_list()

    ll.delete_end()
    ll.print_list()

    ll.delete_node(2)
    ll.print_list()
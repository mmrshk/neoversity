# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# - написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# - розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# - написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        current = self.head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    @staticmethod
    def _insert_sorted(sorted_head, node):
        if sorted_head is None or node.data < sorted_head.data:
            node.next = sorted_head
            return node

        cur = sorted_head
        while cur.next and cur.next.data < node.data:
            cur = cur.next

        node.next = cur.next
        cur.next = node

        return sorted_head

    def insertion_sort(self):
        sorted_head = None
        current = self.head

        while current:
            nxt = current.next
            current.next = None
            sorted_head = self._insert_sorted(sorted_head, current)
            current = nxt

        self.head = sorted_head

    def merge_list(self, other):
        dummy = Node()
        tail = dummy
        a = self.head
        b = other.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next

            tail = tail.next

        tail.next = a if a else b
        self.head = dummy.next
        other.head = None 



if __name__ == '__main__':
    llist = LinkedList()

    llist.insert_at_beginning(5)
    llist.insert_at_beginning(20)
    llist.insert_at_beginning(15)

    print("Зв'язний список:")
    llist.print_list()
    print("Реверснути список:")
    llist.reverse_list()
    llist.print_list()
    print("Відсортувати список:")
    llist.insertion_sort()
    llist.print_list()

    sllist = LinkedList()
    sllist.insert_at_beginning(3)
    sllist.insert_at_beginning(7)
    sllist.insert_at_beginning(90)
    sllist.insert_at_beginning(110)
    sllist.insertion_sort()
    sllist.print_list()

    llist.merge_list(sllist)
    print("Об'єднаний список:")
    llist.print_list()










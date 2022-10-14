class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    llist_set = set()
    current = llist_1.head
    while current:
        llist_set.add(current.value)
        current = current.next

    current = llist_2.head

    while current:
        llist_set.add(current.value)
        current = current.next

    result = LinkedList()
    for number in llist_set:
        result.append(number)
    return result


def intersection(llist_1, llist_2):
    llist_set1 = set()
    current = llist_1.head
    while current:
        llist_set1.add(current.value)
        current = current.next

    llist_set2 = set()
    current = llist_2.head

    while current:
        llist_set2.add(current.value)
        current = current.next

    llist_intersection = llist_set1.intersection(llist_set2)

    result = LinkedList()
    for number in llist_intersection:
        result.append(number)
    return result


# First Test
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

int_list1 = []
int_list2 = [8, 4, 6, 7]

for digit in int_list1:
    linked_list_1.append(digit)

for digit in int_list2:
    linked_list_2.append(digit)

print("\nTest Case 1")
print("Union: ", union(linked_list_1, linked_list_2))
print("Intersection: ", intersection(linked_list_1, linked_list_2))

# Second test
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

int_list3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
int_list4 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for digit in int_list3:
    linked_list_3.append(digit)

for digit in int_list4:
    linked_list_4.append(digit)

print("\nTest Case 2")
print("Union: ", union(linked_list_3, linked_list_4))
print("Intersection: ", intersection(linked_list_3, linked_list_4))

# Third Test

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

int_list5 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
int_list6 = [1, 7, 8, 9, 11, 21, 1]

for digit in int_list5:
    linked_list_5.append(digit)

for digit in int_list6:
    linked_list_6.append(digit)

print("\nTest Cast 3")
print("Union: ", union(linked_list_5, linked_list_6))
print("Intersection: ", intersection(linked_list_5, linked_list_6))

# Fourth Test
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

int_list7 = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
int_list8 = []

for digit in int_list7:
    linked_list_7.append(digit)

for digit in int_list8:
    linked_list_8.append(digit)

print("\nTest Cast 4")
print("Union: ", union(linked_list_7, linked_list_8))
print("Intersection: ", intersection(linked_list_7, linked_list_8))

# Final Test
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

int_list9 = [8, 8, 7, 9, 8, 6, 6, 2, 4, 8]
int_list10 = [8, 8, 7, 9, 8, 6, 6, 2, 4, 8]

for digit in int_list9:
    linked_list_9.append(digit)

for digit in int_list10:
    linked_list_10.append(digit)

print("\nTest Cast 5")
print("Union: ", union(linked_list_9, linked_list_10))
print("Intersection: ", intersection(linked_list_9, linked_list_10))

# Templanza, Kristine Joy F.
# BSCPE 2-4
# Merge Two Sorted Linked Lists

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        node = ListNode(value)
        node.next = self.top
        self.top = node
        
    def pop(self):
        if self.top is None:
            return None
        else:
            pop_node = self.top
            self.top = self.top.next
            pop_node.next = None
            return pop_node.value
        
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return float('inf')  # Return positive infinity for an empty stack
    
    def empty(self):
        return self.top is None

    def print_list(self):
        current = self.top
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        
    def size(self):
        current_node = self.top
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

def merge_sorted_lists(list1, list2):
    merged_list = Stack()
    while list1 is not None or list2 is not None:
        if list1 is None:
            merged_list.push(list2.value)
            list2 = list2.next
        elif list2 is None:
            merged_list.push(list1.value)
            list1 = list1.next
        elif list1.value < list2.value:
            merged_list.push(list1.value)
            list1 = list1.next
        else:
            merged_list.push(list2.value)
            list2 = list2.next
            
    reversed_stack = Stack()
    while not merged_list.empty():
        reversed_stack.push(merged_list.pop())

    return reversed_stack.top

# Example:
list1 = Stack()
list1.push(4)
list1.push(2)
list1.push(1)

list2 = Stack()
list2.push(4)
list2.push(3)
list2.push(1)

print("List 1:")
list1.print_list()

print("List 2:")
list2.print_list()

merged_list = merge_sorted_lists(list1.top, list2.top)

print("Merged list:")
current_node = merged_list
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
print("None")
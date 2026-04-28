# simulasi riwayat navigasi browser menggunakan stack (menggunakan class, linked list, dan list)
# wajib memiliki 5 operasi dasar stack:
# is_empyty: periksa apakah riawayat kosong (True or False)
# push(url): menambahkan url baru ke posisi teratas
# pop: menghapus dan mengembalikan url teratas
# peek: melihat url teratas tanpa menghapusnya
# size: menghitung total url yang tersimpan

class Node:
  def __init__(self, url):
    self.url = url
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, url):
    new_node = Node(url)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.url

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.url

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

  def traverseAndPrint(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.url, end=" -> ")
      currentNode = currentNode.next
    print()

myStack = Stack()
myStack.push('www.github.com')
myStack.push('www.medium.com')
myStack.push('www.w3schools.com')

print('=== Stack dengan Linked List ===')
print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
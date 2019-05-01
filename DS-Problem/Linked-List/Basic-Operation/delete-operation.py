# Code for Delete Operation.

class Node:
  """
    Node Definition of Linked List.

    Attributes:
      data(self): Data to be put in Node.
      next(self): Next of node of Linked List.
  """
  def __init__(self, data):
    """
      Function to initialize the node object.

      Args:
        data: Data to be contain in node.
    """
    self.data = data
    self.next = None


class LinkedList:
  """LinekedList Class."""

  def __init__(self):
    """Function to initialize the LinkedList obejct."""
    self.head = None

  def push(self, new_data):
    """
      Function to push element in LinkedList.
      
      Args:
        new_data: Data to be pushed.
    """
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def delete_node(self, data):
    """
      Function to delete node of given data.

      Args:
        data: data of node to be deleted of first occurence.
    """
    temp = self.head

    if temp is not None:
        if temp.data == data:
            self.head = temp.next
            temp = None
            return

    while temp is not None:
        if temp.data == data:
            break
        prev = temp
        temp = temp.next

    if temp == None:
      return

    prev.next = temp.next

    temp = None
  
  def delete_node_at_pos(self, pos):
    """
      Function to delete the Linked List node at given position.

      Args:
        pos: Position of node to be deleted.
    """
    if self.head is None:
      return

    temp = self.head
    if pos == 0:
        self.head = temp.next
        temp = None
        return

    count = 0
    while temp is not None:
      if count == pos:
        break
      prev = temp
      temp = temp.next
      count +=1

    if temp is None:
      return

    prev.next = temp.next
    temp = None


 
  def print_LinkedList(self):
    temp = self.head
    while temp is not None:
        print("%d " %temp.data)
        temp = temp.next
        

llist = LinkedList() 
llist.push(35) 
llist.push(21) 
llist.push(14) 
llist.push(28) 
llist.push(7)

print("Lineked List : ")
llist.print_LinkedList()
llist.delete_node(14)
print("After node value 14 is deleted : ")
llist.print_LinkedList()
llist.push(77)
llist.push(88)
print("New Linked List : ")
llist.print_LinkedList()
llist.delete_node_at_pos(3)
print("Linked List after position 3 element is deleted : ")
llist.print_LinkedList() 


    
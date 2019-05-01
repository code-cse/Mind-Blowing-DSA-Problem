# Code for linked-list insertion and deletion..!!!

class Node:
  """
    This is the class for Node used for Linked List.        
    
    Attributes: 
      data (self): The data part of Node. 
      next (self): The next part of Node. 
  """
  def __init__(self, data):
    """
      Function to initialize the node object.

      Args:
        data: Data contains in Node.
    """
    self.data = data
    self.next = None

class LinkedList:
  """LinkedList class"""
  def __init__(self):
    """
      Function to initialize LinkedList objects.
    """
    self.head = None


  def push(self, new_data):
    """
      Function to insert new node at beginning.
      
      Args:
        new_data: Data to contain in Node.
    """
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def insert_after(self, prev_node, new_data):
    """
      This function is to insert a new_node after given prev_node.
    
      Agrs:
        prev_node: Given Node after the node to be inserted.
        new_data: Data to put in new_node.
    """
    if prev_node is None:
      print("Node is not in Linked List")
      return
    
    # create a new node to put new data.
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node


  def append_node(self, new_data):
    """
      Function to append new node at the end of linked list.
      
      Args:
        new_data: Data to be put in new node.
    """

    #create a new node and put new data.
    new_node = Node(new_data)

    if self.head is None:
      self.head = new_node
      return

    end = self.head
    while end.next:
        end = end.next

    end.next = new_node

    
  def print_linked_list(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

if __name__ == '__main__':
  llist = LinkedList()

  llist.append_node(10)
  print("Linked List first element : ",10,)
  llist.print_linked_list()
  llist.append_node(43)
  llist.append_node(34)
  print("Linked List append at last : ",43,34,)
  llist.print_linked_list()
  llist.push(23)
  print("Linked List append element at first : ",23)
  llist.print_linked_list()
  llist.insert_after(llist.head.next, 90)
  print("Linked List insert after specific position : ",90)
  llist.print_linked_list()













# Single Linked List all basic operation.

class Node:
  """Class to form node structure."""

  def __init__(self, data):
  	self.data = data
  	self.next = next

class LinkedList:
  """Class to form linked list"""

  def __init__(self):
  	self.head = None

  def push(self, new_data):
  	"""
  	  Function to push the element in linked list.

  	  Args:
  	    new_data:  Data to be put in node.
  	"""
  	new_node = Node(new_data)
  	new_node.next = self.head
  	self.head = new_node

  def print_list(self):
  	"""
  	  Function to print Linked List.

  	  Args:
  	    node: Head node pf linked list.
  	"""
  	temp = self.head

  	while(temp is not None):
  	  print(temp.data)
  	  temp = temp.next

  def search_element(self, element):
  	"""
  	  Function to search element in linked list.

  	  Args:
  	    element: Element to be search in Linked List.
  	"""

  	temp = self.head

  	while temp is not None:
  	  if temp.data == element:
  	  	print("Element Found in Linked-List")
  	  	return
  	  else:
  	  	temp = temp.next

  def delete_node(self, element):
  	"""
  	  Function to delete node of a linked list.

  	  Args:
  	    element: data of node to be deleted
  	"""
  	temp = self.head

  	if temp is not None:
  	  if temp.data == element:
  	  	self.head = temp.next
  	  	temp = None
  	  	return

  	while temp is not None:
  	  if temp.data == element:
  	  	return
  	  prev = temp
  	  temp = temp.next

  	if temp == None:
  	  return

  	prev.next = temp.next
  	temp = None


  def delete_node_at_given_pos(self, pos):
  	"""
  	  Function to delete element of linked list at given position.

  	  Args:
  	    pos: Position of node to be deleted.
  	"""

  	if self.head == None:
  	  print("Invalid Linked-List")
  	  return

  	temp = self.head

  	if pos == 0:
  	  self.head = temp.next
  	  temp = None
  	  return;

  	count =0
  	while temp is not None:
  
  	  if pos-1 == count:
  	  	return
  	  
  	  count += 1
  	  temp = temp.next
  	
  	if temp is None:
  	  return

  	if temp.next is None:
  	  return

  	next = temp.next.next
  	
  	temp.next = None

  	temp.next = next



if __name__ == '__main__':
  llist = LinkedList()

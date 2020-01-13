class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  # Created method to facilitate confirming linked list contents
  def print_list(self):
    node = self.head
    print("list contents:")

    while node:
      print(node.value)
      node = node.next_node


  def reverse_list(self):
    prev_node = None
    curr_node = self.head
    end = self.head

    while curr_node:
      # Advance end to the next node
      end = end.next_node
      # Switch next_node pointers to prev_node variable
      curr_node.next_node = prev_node
      # Store current node in prev_node variable
      prev_node = curr_node
      # Move previous node value to top of the stack
      self.add_to_head(prev_node.value)
      # Assign end to curr_node variable
      curr_node = end

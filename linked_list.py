"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1


class Node:
  def __init__(self, value):
    self._value = value
    self._next = None


class LinkedList:
  def __init__(self):
    self._head = None
    self._tail = None
    self._length = 0

  def get_node(self, position):
    current = self._head
    count = 0

    while (current) :
      if count == position:
        return current
      count += 1
      current = current._next

    return None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self._head is None:
      self._head = new_node
    else:
      n = self._head
      while n._next != None:
        n = n._next
      n._next = new_node
    self._length += 1
    return self

  def add_to_head(self, value):
    new_node = Node(value)
    new_node._next = self._head
    self._head = new_node
    self._length += 1
    return self

  def remove_head(self):
    if self._head is None:
      return None
    else:
      self._head = self._head._next
      self._length -= 1
      if self._length == 0:
        self._tail = None
    return self

  def remove_tail(self):
    if self._head is None:
      return None
    elif self._length == 1:
      self._head = None
      self._tail = None
    else:
      n = self._head
      while n._next._next != None:
        n = n._next
      n._next = None
      self._length -= 1
    return self

  def __len__(self):
    return self._length

# Phase 2

  def contains_value(self, target):
    current = self._head

    while (current) :
      if current._value == target:
        return True
      else:
        current = current._next
    return False

  # TODO: Implement the insert_value method here
  def insert_value(self, position, value):
    if position > self._length:
      return False
    elif position == 0:
      self.add_to_head(value)
    elif position == self._length:
      self.add_to_tail(value)
    else:
      new_node = Node(value)
      prev_node = self._head
      # while prev_node._next != position:
      #   prev_node = prev_node._next
      # prev_node._next = node_to_move
      # new_node._next =
    self._length += 1
    return True



# Phase 1 Manual Testing:

# 1. Test Node and LinkedList initialization
node = Node('hello')
print(node)                                     # <__main__.Node object at ...>
print(node._value)                              # hello
linked_list = LinkedList()
print(linked_list)                              # <__main__.LinkedList object at ...>

# # # 2. Test getting a node by its position
print(linked_list.get_node(0))                # None

# # # 3. Test adding a node to the list's tail
linked_list.add_to_tail('new tail node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0)._value)         # `new tail node`

# # # # 4. Test adding a node to list's head
linked_list.add_to_head('new head node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0)._value)         # `new head node`

# # 5. Test removing the head node
linked_list.remove_head()
print(linked_list.get_node(0)._value)         # `new tail node` because `new head node` has been removed
print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# # # 6. Test removing the tail node
print(linked_list.get_node(0)._value)         # `new tail node`
linked_list.remove_tail()
print(linked_list.get_node(0))                # None

# # 7. Test returning the list length
print(len(linked_list))                                 # 2

# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
linked_list = LinkedList()
linked_list.add_to_head('new head node')
print(linked_list.contains_value('new head node'))      # True
print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
print(linked_list.get_node(0)._value)                   # `hello!`

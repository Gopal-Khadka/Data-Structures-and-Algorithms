class Node:
	def __init__(self,value):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self,value):
		"""Create new node with given value"""
		new_node = Node(value)
		self.head = new_node
		self.tail =  new_node
		self.length = 1

	def print_list(self):
		temp = self.head # assign head as first node
		values = []
		while temp is not None:
			values.append(str(temp.value))
			temp = temp.next # assign next value as new node
		print(", ".join(values))

	def append(self,value):
		"""Add the node with given value to end of the list and return boolean"""
		new_node = Node(value)
		if self.head is not None: # or check if length == 0
			# for non-empty list to insert next item
			self.tail.next = new_node
			self.tail = new_node
		else:
			# for empty list to insert first item
			self.head = new_node
			self.tail = new_node
		# self.tail = new_node
		self.length +=1
		return True

	def pop(self):
		"""Remove last node and return the node"""
		# The traversal to find the second-to-last node in pop() is a linear operation. 
		# You may want to consider optimizations like maintaining a pointer to the second-to-last node.
		
		# check if the list is empty
		if self.length == 0:
			return None

		temp = self.head
		# check if list has only 1 item
		if self.length==1:
			self.head = None
			self.tail = None
		else:
			prev_node = self.head
			while temp.next is not None:
				prev_node = temp
				temp = temp.next
			self.tail = prev_node # point tail to second last node
			self.tail.next = None # point next of present tail to None
		self.length -=1
		return temp
	
	def prepend(self,value):
		"""Add the given value node in the beginning of the linked list"""
		new_node  = Node(value)
		if self.length==0:
			self.head =  new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node
		self.length+=1
		return True

	def pop_first(self):
		"""Pop the first node of the list and return the node"""
		if self.length==0:
			return None

		temp = self.head
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head = temp.next
		temp.next = None
		self.length -=1
		return temp

	def get(self,index):
		"""Returns the value at given index of the linked list"""
		if index < 0 or index >= self.length :
			return None

		temp = self.head
		for _ in range(index):
			temp = temp.next

		return temp

	def set_value(self,index,value):
		"""Set the given value at the given index node"""
		temp = self.get(index)
		if temp:
			temp.value = value
			return True
		return False

	def insert(self,index,value):
		"""Insert the value at given index of the list"""
		if index > self.length or index < 0:
			return None

		if index==0:
			return self.prepend(value)
		if index==self.length:
			return self.append(value)

		new_node = Node(value)
		temp = self.get(index-1) # get previous node i.e. node at (index-1)
		new_node.next = temp.next
		temp.next = new_node

		self.length +=1
		return True

	def remove(self,index):
		""""Remove the node at given index and return boolean"""
		if index < 0 or index >= self.length:
			return None

		if index==0: # for first node
			return self.pop_first()
		if index==self.length-1: # for last node
			return self.pop()
		
		prev=self.get(index-1)
		temp = prev.next # get node at given index
		prev.next = temp.next
		temp.next = None
		self.length -= 1
		return temp

	def reverse(self):
		"""Reverse the linked list i.e change the direction of the connection"""
		# swap head and tail
		temp = self.head
		self.head = self.tail
		self.tail = temp

		# after (next node) and before(previous node)
		after = temp.next
		before = None 

		for _ in range (self.length):
			# changing the direction of linked list connection
			after = temp.next
			temp.next = before
			before = temp
			temp = after


	# Question 1: Find the middle node of the linked list without using length attribute
	def find_middle_node(self):
		# We use two pointers to traverse the list
		# "slow" pointer moves one step at a time
		# "fast" pointer movies two step at a time
		# when "fast" pointer reaches the end, "slow" pointer must be at middle of the list
		slow = self.head
		fast = self.head
		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next
		return slow

	#Question 2: Write a method called has_loop that is part of the linked list class.
	# The method should be able to detect if there is a cycle or
	#loop present in the linked list.(circular linked list) The method should
	#utilize Floyd's cycle-finding algorithm("tortoise and hare" algorithm)
	#to determine the presence of a loop efficiently.

	def has_loop(self):
		slow = self.head
		fast = self.head

		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				return True

		return False

	# Question 3: implement a method called remove_duplicates() within the
	# LinkedList class that removes all duplicate values from the integers list

	def remove_duplicates(self):
		prev= None
		current = self.head
		values = set()
		while current is not None:
			if current.value in values:
				prev.next = current.next
				self.length -= 1
			else:
				values.add(current.value)
				prev = current
			current = current.next

# Question 4: Write function to find the node that is k steps away from the end without using length
def find_kth_from_end(ll:LinkedList,k:int):
	slow = fast = ll.head
	for _ in range(k):
		# check if the k is more than length of the list
		# i.e the value "None" / end of the list arrives before the end of the loop
		if fast.next is None:
			return None
		fast = fast.next # move "fast" k steps away from "slow"
	
	while fast.next:
		# move both "fast" and "slow" one step at a time till end of the list
		slow = slow.next
		fast = fast.next

	return slow.value # return the node that is k steps away from the node


if __name__ == '__main__':
	my_list = LinkedList(0)

	my_list.append(20)
	my_list.append(30)
	# my_list.append(20)
	# my_list.append(30)

	my_list.print_list()
	print(my_list.length)

	my_list.remove_duplicates()
	print(find_kth_from_end(my_list,0))
	my_list.print_list()
	print(my_list.length)
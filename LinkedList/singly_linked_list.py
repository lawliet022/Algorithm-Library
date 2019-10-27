# create nodes
# create linked list
# add nodes to the linked list
# print the linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def add_node_head(self, newNode):
		newNode.next = self.head
		self.head = newNode
	def add_node_end(self, newNode):
		if(self.head is None):
			self.head = newNode
		else:
			current_node = self.head
			while(current_node.next is not None):
				current_node = current_node.next
			current_node.next = newNode
	def add_node_at(self, newNode, pos):
		# pass
		count = 0
		current_node = self.head
		if(pos == 0):
			self.add_node_head(newNode)
			return
		while(True):
			if(current_node is None):
				print("The position does not exists")
				return 
			if(count == pos-1):
				prev_node = current_node
				break
			current_node = current_node.next
			count += 1
		newNode.next = prev_node.next
		prev_node.next = newNode
	def print_list(self):
		print("-----------------------")
		current_node = self.head
		if(current_node is None):
			print("List is empty")
			return 
		count = 0
		while(current_node is not None):
			print(count, current_node.data, current_node.next)
			count += 1
			current_node = current_node.next
	def remove_node_end(self):
		current_node = self.head
		while(current_node.next.next is not None):
			current_node = current_node.next
		last_node = current_node.next
		del(last_node)
		current_node.next = None
	def remove_node_head(self):
		if(self.head is None):
			print("The list is already empty")
		else:
			first_node = self.head
			self.head = first_node.next
			del	first_node
	def remove_node_at(self, pos):
		if(pos == 0):
			self.remove_node_head()
		else:
			count = 0
			current_node = self.head
			while(True):
				if(current_node is None):
					print("The position does not exists")
					return
				if(count == pos-1):
					prev_node = current_node
					current_node = current_node.next
					prev_node.next = current_node.next
					del current_node
					break
				count+=1
				current_node = current_node.next
	def delete_complete_list(self):
		current_node=self.head
		while(self.head is not None):
			print("deleting ",self.head.data)
			self.remove_node_head()			
# Node=>data,next
n1 = Node("n1")
n2 = Node("n2")
ll = LinkedList()
ll.print_list()
ll.add_node_end(n1)
ll.print_list()
ll.add_node_end(n2)
ll.print_list()
n3 = Node("n3")
n4 = Node("n4")
ll.add_node_head(n3)
ll.print_list()
ll.add_node_head(n4) 
ll.print_list()
n5 = Node("n5")
ll.add_node_at(n5,2)
ll.print_list()
n6 = Node("n6")
ll.add_node_at(n6,-1)
ll.print_list()
n7 = Node("n7")
ll.add_node_at(n7,100)
ll.print_list()
ll.remove_node_end()
ll.print_list()
ll.remove_node_head()
ll.print_list()
# ll.remove_node_at(0)
# ll.print_list()
# ll.remove_node_at(0)
# ll.print_list()
# ll.remove_node_at(0)
# ll.print_list()
ll.delete_complete_list()
# ll.print_list()
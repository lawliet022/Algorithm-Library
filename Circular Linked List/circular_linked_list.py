class Node:
	def __init__(self,data):
		self.data=data
		self.next=self
class CircularLinkedList:
	def __init__(self):
		self.head=None
	
	def add_node_end(self,newNode):
		if(self.head is None):
			self.head=newNode
		else:
			current=self.head
			while(current.next!=self.head):
				current=current.next
			if(current.next==self.head):
				tail=current
			newNode.next=self.head
			tail.next=newNode

	def add_node_head(self,newNode):
		if(self.head is None):
			self.head=newNode
		else:
			tail=self.head
			while(tail.next!=self.head):
				tail=tail.next
			firstNode=self.head
			newNode.next=firstNode
			self.head=newNode
			tail.next=self.head
	
	def add_node_at(self,newNode,pos):
		if(pos==0):
			self.add_node_head(newNode)
		else:
			count=0
			current=self.head
			while(True):
				if(count==pos):
					newNode.next=prev.next
					prev.next=newNode
					break
				if(current==self.head and count>0):
					print("Index out of range")
					break
				prev=current
				count+=1
				current=current.next

	def __str__(self):
		s="---------------------\n"
		if(self.head is None):
			s+="Lsit is empty"
		else:
			current=self.head
			while(True):
				s+=str(current.data)+"\n"
				current=current.next
				if(current==self.head):
					break
		return s

	def del_node_head(self):
		if(self.head is None):
			print("List is already empty")
		elif(self.head==self.head.next):
			node=self.head
			del(node)
			self.head=None
		else:
			current=self.head
			while(current.next!=self.head):
				current=current.next
			if(current.next==self.head):
				tail=current
			current.next=self.head.next
			node=self.head
			self.head=node.next
			del(node)

	def del_node_end(self):
		if(self.head is None):
			print("List is already empty")
		elif(self.head.next==self.head):
			del(self.head)
			self.head=None
		else:
			current=self.head
			while(current.next!=self.head):
				prev=current
				current=current.next
			if(current.next==self.head):
				tail=current
				prev.next=self.head
				del(tail)

	def del_node_at(self,pos):
		if(self.head is None):
			print("Lsit empty")
		elif(pos==0):
			self.del_node_head()
		else:
			count=0
			current=self.head
			while(True):
				if(count==pos):
					prev.next=current.next
					del(current)
					break
				if(count>0 and current==self.head):
					print("Index out of range")
					return
				prev=current
				count+=1
				current=current.next






ll=CircularLinkedList()
ll.add_node_end(Node(1))
ll.add_node_end(Node(2))
# print(ll)
ll.add_node_head(Node(-1))
# print(ll)
ll.add_node_at(Node(9),1)
# print(ll)
# ll.add_node_at(Node(9),0)
# print(ll)
# ll.add_node_at(Node(9),5)
# print(ll)
print(ll)
# ll.del_node_head()
# ll.del_node_end()
# ll.del_node_end()
ll.del_node_at(0)
print(ll)

ll.del_node_at(0)
print(ll)

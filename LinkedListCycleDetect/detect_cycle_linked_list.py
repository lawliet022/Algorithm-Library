class Node:
	def __init__(self, val):
		self.val=val
		self.next=None
class LL:
	def __init__(self, node):
		self.head=node

	def print(self):
		start=self.head
		while(start!=None):
			print(start.val)
			start=start.next

	def has_cycle(self):
		slow=self.head
		fast=self.head
		while(slow and fast and fast.next):
			slow=slow.next
			fast=fast.next.next
			if(slow==fast):
				return True
		return False
	
	def cycle_point(self):
		if(self.has_cycle()):
			slow=self.head
			fast=self.head
			ans=False
			while(slow and fast and fast.next):
				slow=slow.next
				fast=fast.next.next
				if(slow==fast):
					ans=True
					break
			if(ans):
				slow=self.head
				while(slow!=fast):
					slow=slow.next
					fast=fast.next
				return slow
	
	def cycle_length(self):
		point=self.cycle_point()
		if(point!=None):
			start=point.next
			count=1
			while(start!=point):
				count+=1
				start=start.next
			return count

		

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n8=Node(8)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n8
n8.next=n8

l=LL(n1)

print(l.has_cycle())
print(l.cycle_point().val)
print(l.cycle_length())
class Node(object):
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	def __str__(self):
		return str(self.data)
	def __repr__(self):
		return str(self.data)
	

class BinaryTree(object):
	def __init__(self,root):
		self.root=root
	def dfs_preorder(self, start=None, ans=""):
		if(start is None):
			return ""
		ans+=str(start.data)+"-"
		ans+=str(self.dfs_preorder(start.left))
		ans+=str(self.dfs_preorder(start.right))
		return ans
	def dfs_preorder_non_recursive(slef,start=None,ans=""):
		# dlr
		queue=[]
		root=start	
		if(root is not None):
			while(True):
				while(root!=None):
					ans+=str(root.data)+"-"
					queue.append(root)
					root=root.left
				if(root is None):
					if(len(queue)==0):
						break
					root=queue.pop()
					root=root.right
		return ans
	def dfs_inorder(self,start=None,ans=""):
		if(start is None):
			return ""
		ans+=str(self.dfs_inorder(start.left))
		ans+=str(start.data)+"-"
		ans+=str(self.dfs_inorder(start.right))
		return ans
	def dfs_inorder_non_recursive(slef,start=None,ans=""):
		# dlr
		queue=[]
		root=start	
		if(root is not None):
			while(True):
				while(root!=None):
					queue.append(root)
					root=root.left
				if(root is None):
					if(len(queue)==0):
						break
					root=queue.pop()
					ans+=str(root.data)+"-"
					root=root.right
		return ans
	def dfs_postorder(self,start=None,ans=""):
		if(start is None):
			return ""
		ans+=str(self.dfs_postorder(start.left))
		ans+=str(self.dfs_postorder(start.right))
		ans+=str(start.data)+"-"
		return ans

	def dfs_postorder_non_recursive(self,start=None,ans=""):
		# lrd
		root=start
		stack=[]
		count=0
		while(True):
			# count+=1
			# print(stack)
			if(root is not None):
				stack.append(root)
				root=root.left
			else:
				if(len(stack)==0):
					break
				if(stack[-1].right is None):
					root=stack.pop()
					print(root)
					while(len(stack)>0 and stack[-1].right==root):
						root=stack.pop()
						print(root)
				if(len(stack)>0):
					root=stack[-1].right
				else:
					root=None

		return ans
tree=BinaryTree(Node(1))
tree.root.left=Node(2)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right=Node(3)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

ans=tree.dfs_preorder(tree.root)
print(ans)

ans=tree.dfs_inorder(tree.root)
print(ans)

ans=tree.dfs_postorder(tree.root)
print(ans)

ans=tree.dfs_preorder_non_recursive(tree.root)
print(ans)

ans=tree.dfs_inorder_non_recursive(tree.root)
print(ans)

print("---------------------------------")
ans=tree.dfs_postorder_non_recursive(tree.root)
print(ans)


# Tree Traversal
# Pre-order, In-order, Post-order
LEFT, RIGHT = 0, 1

N = int(input())
tree = dict()

for i in range(N):
    key, left, right = list(input().split())
    tree[key] = [left, right]

def preorder(tree: dict, root: str):
    if root == ".":
        return
    
    print(root, end="")
    preorder(tree, tree[root][LEFT])
    preorder(tree, tree[root][RIGHT])

def inorder(tree, root):
    if root == ".":
        return
    
    inorder(tree, tree[root][LEFT])
    print(root, end="")
    inorder(tree, tree[root][RIGHT])

def postorder(tree, root):
    if root == ".":
        return
    
    postorder(tree, tree[root][LEFT])
    postorder(tree, tree[root][RIGHT])
    print(root, end='')

preorder(tree, 'A')
print()
inorder(tree, 'A')
print()
postorder(tree, 'A')

# Solved 11m06s
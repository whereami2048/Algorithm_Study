import sys
sys.setrecursionlimit(10000)

class Node():
    def __init__(self, info):
        self.num = info[2]
        self.x = info[0]
        self.y = info[1]
        self.left = None
        self.right = None
    
    def __str__(obj):
        return f'x: {obj.x}, y: {obj.y}'

def preorder(parent, order):
    order.append(parent.num)
    
    if parent.left:
        preorder(parent.left, order)
    
    if parent.right:
        preorder(parent.right, order)
    
    return order

def postorder(parent, order):
    if parent.left:
        postorder(parent.left, order)
    
    if parent.right:
        postorder(parent.right, order)
    
    order.append(parent.num)
    return order
    
def add_node(parent, info):
    if parent.x > info[0]:
        if parent.left:
            add_node(parent.left, info)
        else:
            parent.left = Node(info)
    else:
        if parent.right:
            add_node(parent.right, info)
        else:
            parent.right = Node(info)
    
    
def solution(nodeinfo):
    answer = []
    
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    
    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    
    tree = Node(nodeinfo[0])
    
    for info in nodeinfo[1:]:
        add_node(tree, info)
    
    answer.append(preorder(tree, []))
    answer.append(postorder(tree, []))
    
    
    
    return answer
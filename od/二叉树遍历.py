'''
题目描述

根据给定的二叉树结构Q描述字符串，输出该二叉树按照中序遍历结果字符串。中序遍历顺序为：左子树，根结点，右子树。

输入描述

由大小写字母、左右大括号、逗号组成的字符串：

1、字母代表一个节点值，左右括号内包含该节点的子节点。
2、左右子节点使用逗号分隔，逗号前为空则表示左子节点为空，没有逗号则表示右子节点为空。
3、二又树节点数最大不超过100。注：输入字符串Q格式是正确的，无需考虑格式错误的情况。

输出描述
输出一个字符串，为二叉树中序遍历各节点值的拼接结果。

补充说明
中序遍历是二又树遍历的一种，遍历方式是首先遍历左子树，然后访问根结点，最后遍历右子树。

input
a{b{d,e{g,h{,i}}},c{f}}
output
dbgehiafc
'''
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def create_tree_node(input_str):
    stack = []
    root = None
    current_node =None
    is_left_child =False

    for char in input_str:
        if char == '{':
            stack.append(current_node)
            is_left_child = True
        elif char == ',':
            is_left_child = False
        elif char == '}':
            stack.pop()
        else:
            current_node = TreeNode(char)
            if root is None:
                root = current_node
            else:
                if is_left_child:
                    stack[-1].left = current_node
                else:
                    stack[-1].right =current_node
    return root

def inorder(root, res):
    if root is None:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

input_str = input()
root = create_tree_node(input_str)
res = []
inorder(root, res)
print(''.join(res))

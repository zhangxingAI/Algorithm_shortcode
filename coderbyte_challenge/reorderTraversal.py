from Tree import Node
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, TreeNode):
        if not root: return []
        res=[root.val]
        st=[root]
        node=root
        while st:
            if node.left == None and node.right ==None:  # 如果节点的左右都是空的，证明这个节点被遍历完了，返回上一个节点
                st.pop()
                if not st: break
                node=st[-1]  # 第一次返回的时候把左侧置为None，第二次返回的时候把右侧置为None
                if node.left==None:
                    node.right=None
                else:
                    node.left=None

            elif node.left:  # 遍历左边
                node = node.left
                res.append(node.val)
                st.append(node)
                if node.left == None and node.right ==None:  # 如果下个节点到头了，返回上一个节点
                    st.pop()
                    node=st[-1]
                    node.left = None  # 因为我们是从左侧返回的上一个节点，所以把左侧到头的节点置为None
            elif node.right:  # 遍历右边
                node = node.right
                res.append(node.val)
                st.append(node)
                if node.left == None and node.right ==None:  # 如果下个节点到头了，返回上一个节点
                    st.pop()
                    node=st[-1]
                    node.right = None  # 因为我们是从右侧返回的上一个节点，所以把右侧到头的节点置为None
        return res


print(preorderTraversal(["4", "1", "5", "2", "#", "#", "#"]))


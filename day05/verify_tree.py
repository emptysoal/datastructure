"""
    【1】题目描述
        输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果

    【2】试题解析
        2.1) 注意题中二叉搜索树，左子树中节点值都小于根，右子树中节点值都大于根
        2.2) 后序遍历结果: 左右根
        2.3) 后序遍历后最后一个元素为二叉树根节点, 根据这个元素将传入的数组分为两部分
             左侧部分: 都比根节点小
             右侧部分: 都比根节点大

    【3】解题思路
        3.1) 先找到数组的最后一个元素: 即为二叉树的根节点
        3.2) 左子树节点都比根节点小,右子树节点都比根节点大
             所以我们以根节点为标准,将数组分为左右两个小数组,分别存放左右子树的节点
        3.3) 递归思想: 左右子树又必须得满足后序遍历的规则,使用递归重新调用此方法
"""


class Solution:
    def verify_sort_tree(self, li):
        if not li:
            return False
        root_val = li[-1]
        left = []
        right = []
        length = len(li) - 1
        for i in range(length):
            if li[i] > root_val:
                left.extend(li[:i])
                right.extend(li[i:length])
                break

        # 确定：left中所有元素都比根小
        # 未确定：right中不一定所有元素都比根大
        for r in right:
            if r < root_val:
                return False

        # 递归思想：左子树和右子树都按照上述方法进行判断
        is_left = True
        is_right = True
        if left:
            is_left = self.verify_sort_tree(left)
        if right:
            is_right = self.verify_sort_tree(right)

        return is_left and is_right

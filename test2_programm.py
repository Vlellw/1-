class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def get_min(self):
        runner = self.root
        if runner is None:
            return None

        while runner.left is not None:
            runner = runner.left
        return runner.value

    def get_max(self):
        runner = self.root
        if runner is None:
            return None

        while runner.right is not None:
            runner = runner.right
        return runner.value

    def find(self, elem):
        return self.__find(elem) is not None

    def __find(self, elem):
        runner = self.root
        while runner is not None and runner.value != elem:
            if runner.value > elem:
                runner = runner.left
            else:
                runner = runner.right

        return runner

    def push(self, elem):
        if self.root is None:
            self.root = Node(elem)
            return

        runner = self.root
        while True:
            if runner.value > elem:
                if runner.left is None:
                    runner.left = Node(elem)
                    runner.left.parent = runner
                    return
                else:
                    runner = runner.left
            elif runner.value < elem:
                if runner.right is None:
                    runner.right = Node(elem)
                    runner.right.parent = runner
                    return
                else:
                    runner = runner.right
            else:
                return

    def pop(self, elem):
        item = self.__find(elem)
        if item is None:
            return

        if (item.left is None) and (item.right is None):
            self.__pop_childless(item)
            return

        if (item.right is not None) and (item.left is None):
            self.__pop_left_childless(item)
            return

        if (item.right is None) and (item.left is not None):
            self.__pop_right_childless(item)
            return

        runner = item.right
        while runner.left is not None:
            runner = runner.left
        item.value = runner.value
        if runner.right is None:
            self.__pop_childless(runner)
        else:
            self.__pop_left_childless(runner)

    def __pop_childless(self, item):
        if item == self.root:
            self.root = None
            return

        if item.parent.left == item:
            item.parent.left = None
        else:
            item.parent.right = None

    def __pop_left_childless(self, item):
        if item == self.root:
            self.root = item.right
            return

        if item.parent.left == item:
            item.parent.left = item.right
        else:
            item.parent.right = item.right

    def __pop_right_childless(self, item):
        if item == self.root:
            self.root = item.left
            return

        if item.parent.left == item:
            item.parent.left = item.left
        else:
            item.parent.right = item.left


n = int(input())
tree = Tree()
lst = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        tree.push(int(cmd[1]))
        lst.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        tree.pop(int(cmd[1]))
        if int(cmd[1]) in lst:
            lst.remove(int(cmd[1]))
    elif cmd[0] == 'find':
        assert tree.find(int(cmd[1])) == (int(cmd[1]) in lst)
    elif cmd[0] == 'get_min':
        assert tree.get_min() == min(lst)
    elif cmd[0] == 'get_max':
        assert tree.get_max() == max(lst)
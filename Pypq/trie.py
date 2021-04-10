# 定义路由表存储结构--树
class Node(object):
    def __init__(self,part='', isWild=0 ,pattern=''):
        self.pattern = pattern
        self.part = part
        self.isWild = isWild
        self.children = []

    def __str__(self):
        return "node:pattern={}, part={}, isWild={}".format(self.pattern,self.part,self.isWild)

    def matchChild(self,part):
        for child in self.children:
            if child.part == part or child.isWild:
                return child
        return None

    def matchChildren(self, part):
        nodes = []
        for child in self.children:
            if child.part == part or child.isWild:
                nodes.append(child)
        return nodes

    # insert an address to router table
    def insert(self,pattern, parts, height):
        if len(parts) == height:
            self.pattern = pattern
            return
        
        part = parts[height]
        child = self.matchChild(part)
        if child == None:
            isWild = 0
            if part[0] == ':' or part[0] == '*':
                isWild = 1
            child = Node(part=part,isWild=isWild)
            self.children.append(child)
        child.insert(pattern, parts, height + 1)

    # search for a certain pattern
    def search(self, parts, height):
        if len(parts) == height or self.part.startswith("*"):
            if self.pattern == "":
                return None
            return self
        
        part = parts[height]
        children = self.matchChildren(part)

        for child in children:
            result = child.search(parts,height + 1)
            if result is not None:
                return result
        return None

    #  traversal the tree's leaves
    def travel(self, list):
        if self.pattern != "":
            list.append(self)
        
        for child in self.children:
            child.travel(list)

# debug
if __name__ == '__main__':
    print(1)
    tr = Node()
    print(1)
    tr.insert('1/2/3/4',['1','2','3','4'],0)
    print(1)
    print(tr.search (['1','2','3','4'],0))
    a = []
    tr.travel(a)
    print(a[0])
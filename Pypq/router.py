# 定义router类，封装路由添加与查询等功能
from trie import Node

class router(object):
    def __init__(self,roots,handlers):
        self.roots = roots
        self.handlers = handlers

    # 添加路由
    def addRoute(self,method,pattern,handler):
        parts = parsePattern(pattern)
        key = method + '-' + pattern

        if method not in self.roots.keys():
            roots[method] = Node()

        self.roots[method].insert(pattern,parts,0)
        # add handler map
        self.handlers[key] = handler

    # 查找路由
    def getRoute(self,method,path):
        searchParts = parsePattern(path)
        params = {}
        if method not in self.roots.keys():
            return None,None
        root = self.roots[method]

        n = root.search(searchParts,0)
        if n == None:
            return None,None
        
        parts = parsePattern(n.pattern)
        for index,part in enumerate(parts):
            if part[0] == ':':
                params[part[1:]] = searchParts[index]
            if part[0] == '*' and len(part) > 1:
                params[params[1:]] = "/".join(searchParts[index:])
                break
        return n,params

    def getRoutes(self,method):
        if method not in roots.keys():
            return None
        nodes = []
        root.travel(nodes)
        return nodes

    def handle(self, c):
        n,params = self.getRoute(c.Method, c.Path)

        if n != None:
            key = c.Method + "-" + self.pattern
            c.Params = params
            c.handlers.append(self.handlers[key])
        else :
            def func(c):
                c.String("404 NOT FOUND: {}\n".format(c.Path))
            c.handlers.append(func)

        c.Next()


def newRouter():
    router = router({},{})

#  将pattern转化为列表
def parsePattern(pattern ):
    vs = "/".split(pattern)
    parts = []

    for item in vs:
        if item != "":
            parts.append(item)
            if item[0] == '*':
                break
    return parts


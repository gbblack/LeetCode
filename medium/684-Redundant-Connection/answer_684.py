class Solution(object):
    def findRedundantConnection(self, edges):
        self.parent = dict()
        
        for e in edges:
            
            e0 = self.find_node(e[0])
            e1 = self.find_node(e[1])
            if e0 == e1:
                print("e0")
                print(e0)
                print("e1")
                print(e1)
                return e
            
            self.parent[e0] = e1
            
    def find_node(self, x):
        if x not in self.parent:
            return x
    
        return self.find_node(self.parent[x])
class PrefixTree:
    def __init__(self, string=""):
        self.root = {}

    def insert(self, word):
        current = self.root
        for i in word:
            if i not in current:
                current[i] = {}
            current = current[i]
        current['--'] = 1

    def search(self, word):
        current = self.root
        for i in word:
            if i not in current:
                return False
            current = current[i]
        return '--' in current

    def startsWith(self, prefix):
        current = self.root
        for i in prefix:
            if i not in current:
                return False
            current = current[i]
        return True

    def deepestNode(self):
        current = [self.root]
        depth = 0
        end = 0
        while end != 1:
            for cur in range(0, len(current)):
                for i in current[0]:
                    if current[0][i] is not None and current[0][i] != 1:
                        current.append(current[0][i])

                current.pop(0)
            depth += 1
            if len(current) == 0:
                end = 1
        return depth - 1


if __name__ == "__main__":
    ob = PrefixTree()
    ob.insert("Hello")
    ob.insert("Because")
    print(ob.search("Hello"))
    print(ob.search("Because"))
    print(ob.search("Hell"))
    print()
    print(ob.startsWith("Hell"))
    print(ob.startsWith("Be"))
    print(ob.startsWith("Becas"))
    print()
    print(ob.deepestNode())

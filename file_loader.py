import os


class fileTree:
    def __init__(self, path):
        self.trunk = branch(path, 0)
        self.minName = self.trunk.nameVal
        self.maxName = self.trunk.nameVal
        self._buildtree(self.trunk)
        self.trunk.sizeRatio = 1.0

    def _buildtree(self, br):
        branchSize = 0
        for p in os.listdir(br.path):
            b = branch(os.path.join(br.path, p), br.level + 1)
            if b.nameVal < self.minName:
                self.minName = b.nameVal
            if b.nameVal > self.maxName:
                self.maxName = b.nameVal
            if not b.isFile:
                self._buildtree(b)
            branchSize += b.size
            br.branches.append(b)
        br.size = branchSize
        if br.size > 0:
            for p in br.branches:
                p.sizeRatio = p.size / br.size

        
class branch:
    def __init__(self, path, level):
        self.path = os.path.abspath(path)
        self.name = os.path.basename(self.path)
        self.isFile = os.path.isfile(self.path)
        self.level = level
        self.nameVal = 0.0
        self.sizeRatio = 1
        try:
            for n in range(len(self.name)):
                self.nameVal += ord(self.name[n])/(1000.0**n)
        except:
            pass

        if self.isFile:
            self.size = os.stat(path).st_size
        else:
            self.size = 0
        self.branches = []
    def __iter__(self):
        return branch_iter(self)


class branch_iter:
    def __init__(self, branch):
        self._branch = [branch] + self._makebranch(branch)
        self._index = 0

    def _makebranch(self, branch):
        ret = branch.branches
        for x in range(len(branch.branches)-1, -1, -1):
            n = branch.branches[x]
            if not n.isFile:
                br = self._makebranch(n)
                ret = ret[0:(x+1)] + br + ret[(x+1):]
        return ret
        
    def __next__(self):
        if (self._index < len(self._branch)):
            self._index += 1
            return self._branch[self._index - 1]
        raise StopIteration

def printTree(outputFile, tree):
    leaves = 0
    branches = 0
    f = open(outputFile, 'w')
    for a in tree.trunk:
        if a.isFile:
            leaves += 1
        else:
            branches += 1
        toprint = ""
        for b in range(a.level):
            toprint += "\t"
        nameRatio = (a.nameVal-tree.minName)/(tree.maxName-tree.minName)
        toprint += ','.join([a.name, str(format(a.size, '.30f')), str(format(a.sizeRatio, '.30f')), str(format(nameRatio, '.30f')), a.path])
        f.write(toprint + "\n")
    f.close()
    print("Branches: " + str(branches))
    print("Leaves: " + str(leaves))

if __name__ == "__main__":
    print("Start")
    x = fileTree("C:\\Users\\Shay\\Desktop")
    printTree("output.txt", x)
    print("Done")
'''

python -m venv venv
.\venv\Scripts\Activate.ps1

1) Load all the files of the directories into a tree
    file_loader.py
2) Organize branches of the tree by sizes of the files
3) Draw tree, length of branch/leaf by file size or folder contents sizes

Output as text document, indented by level, with the following information as csv:
    Branch Name, Branch Size (in bytes), Branch Size Ratio relative to parent (0.0 to 1.0),
        Branch Name Ratio relative to whole tree (0.0 to 1.0), Branch Full Path

How to run:

Python main.py <Location to directory or file>... out:<outputfilename>
Output will be in separate output files as "<outputfilename>_<Location to directory basename>.txt"
The default <outputfilename> is "output"
There was very little testing done.

'''

from graphics_modified import *
import sys
from file_loader import fileTree, printTree

def makeTree(path, output):
    tree = fileTree(path)
    printTree(output, tree)

output = "output"
trees = []

if len(sys.argv) > 0:
    for path in sys.argv:
        if path.startswith("out:"):
            output = path[4:]
        if os.path.isdir(path):
            if os.path.exists(path):
                trees.append(path)
if len(trees) == 0:
    trees.append('./')

for n in trees:
    makeTree(n, output + "_" + os.path.basename(n) + ".txt")




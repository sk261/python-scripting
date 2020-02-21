'''

python -m venv venv
.\venv\Scripts\Activate.ps1

1) Load all the files of the directories into a tree
    file_loader.py
2) Organize branches of the tree by sizes of the files
3) Draw tree, length of branch/leaf by file size or folder contents sizes



'''

from graphics_modified import *
import sys
from file_loader import fileTree

def makeTree(path):
    tree = fileTree(path)

if len(sys.argv) > 0:
    for path in sys.argv:
        if os.path.isdir(path):
            if os.path.exists(path):
                makeTree(path)
else:
    makeTree('./')
    




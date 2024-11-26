"""
File: main.py
Creation Date: 2024-11-25
Last Update: 2024-11-25
Creator: eis-x
Github: https://github.com/eis-x/pytreebuilder
"""

from pytreebuilder.pytreebuilder import PyTreeBuilder

if __name__=='__main__':
    PyTreeBuilder("trees/any_project_tree.txt").create_project_structure()
"""
File: any_project_tree.py
Creation Date: 2024-11-25
Last Update: 2024-11-25
Creator: eis-x
Github: https://github.com/eis-x/pytreebuilder
"""
import sys 
import os # Add the parent directory to the PYTHONPATH 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pytreebuilder.pytreebuilder import PyTreeBuilder

if __name__ == '__main__':
    PyTreeBuilder(tree_file_path="trees/any_project_tree.txt", update_mode=False).create_project_structure()
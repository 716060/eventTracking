from util import read

class TreeNode:
    def __init__(self, key=None, value=None, children=None):
        self.key = key
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.key) + ": " + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

def dict_to_tree(d, parent_key=None):
    if isinstance(d, dict):
        node = TreeNode(key=parent_key)
        for key, value in d.items():
            if isinstance(value, (dict, list)):
                child_node = dict_to_tree(value, key)
                node.add_child(child_node)
            else:
                node.add_child(TreeNode(key=key, value=value))
        return node
    elif isinstance(d, list):
        root = TreeNode(key=parent_key)
        for item in d:
            if isinstance(item, dict):
                child_node = dict_to_tree(item)
                root.add_child(child_node)
            else:
                pass
        return root
    else:
        return TreeNode(value=d)


if __name__ == '__main__':
    data = read.Read().readYaml("/Users/koolearn/cuijianwei/PyProject/eventTracking/resources/applicationContext.yaml")

    tree = dict_to_tree(data, 'page_id')

    print(tree)
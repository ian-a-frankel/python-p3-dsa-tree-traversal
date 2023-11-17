class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    found = None
    if self.root['id'] == id:
      found = self.root
    else:
      for child in self.root['children']:
        child_tree = Tree(child)
        print(child_tree)
        return child_tree.get_element_by_id(id)
    return found

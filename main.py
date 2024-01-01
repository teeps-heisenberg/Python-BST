from binary_tree import BinarySearchTree

my_tree = BinarySearchTree()

my_tree.insert(21)

my_tree.insert(16)

my_tree.insert(42)

print('Root: ',my_tree.root.value)
print('Left: ',my_tree.root.left.value)
print('Root: ',my_tree.root.right.value)


is_present = my_tree.contains(16)
print('Is 16 present? ', is_present)

is_present = my_tree.contains(18)
print('Is 18 present? ', is_present)
from binary_tree import BinarySearchTree

my_tree = BinarySearchTree()

my_tree.insert(47)

my_tree.insert(21)

my_tree.insert(76)

my_tree.insert(18)
my_tree.insert(27)

my_tree.insert(52)
my_tree.insert(89)

# print('Root: ',my_tree.root.value)
# print('Left: ',my_tree.root.left.value)
# print('Root: ',my_tree.root.right.value)


#Recursive Search
is_present = my_tree.r_contains(27)
print('Is 27 present? ', is_present)

is_present = my_tree.r_contains(15)
print('Is 15 present? ', is_present)
print()

my_tree.print_tree()

print()
my_tree.delete_node(76)
my_tree.print_tree()
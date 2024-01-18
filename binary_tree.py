from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None
    

    def insert(self,value):
        new_node = Node(value=value);
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


    def print_tree(self):
        self.__print_tree_recursive(self.root,"Root")

    def __print_tree_recursive(self, current_node, direction):
        if current_node:
            # Print the current node's value and its position
            print(f"{direction}: {current_node.value}")
            
            # Recursively print the left subtree
            self.__print_tree_recursive(current_node.left, "Left of " + str(current_node.value))
            
            # Recursively print the right subtree
            self.__print_tree_recursive(current_node.right, "Right of " + str(current_node.value))


    def __r_contains(self,current_node,value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left,value)
        if value > current_node.value:
            return self.__r_contains(current_node.right,value)


    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    def __r_insert(self,current_node,value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node

    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root,value)


    def __delete_node(self,current_node,value):
        #If value not in BST
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left,value)

        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right,value)
        
        else:
            # Leaf Node Removed
            if current_node.left == None and current_node.right == None:
                return None

            # Node to be Removed has a node to the left
            elif current_node.right == None:
                current_node = current_node.left

            # Node to be Removed has a node to the right
            elif current_node.left == None:
                current_node = current_node.right

            # Node to be removed has nodes to right and left
            else:
                subtree_min = self.min_value(current_node.right)
                current_node.value = subtree_min
                current_node.right = self.__delete_node(current_node.right, subtree_min)
        
        return current_node
    
    
    def delete_node(self,value):
        self.__delete_node(self.root,value)

    def min_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
from BinarySearchTree import BinarySearchTree;

bst = BinarySearchTree();

bst.insert(10);
bst.insert(-5);
bst.insert(3);
bst.insert(345);
bst.insert(678);

bst.traverseInOrder();

bst.remove(678);

bst.traverseInOrder();


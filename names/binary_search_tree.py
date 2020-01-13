class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Edge case check for root node
        if self.value is None:
            self.value = value

        # Edge case to address duplicate values
        elif self.value == value:
            print(f"{value} exists")
            return

        # Evaluate left nodes
        elif self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # Evaluate right nodes
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        # Base case
        if self.value is None:
            return False

        # Evaluate left nodes
        if self.value > target:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        # Evaluate right nodes
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check for right nodes
        if self.right is None:
            return self.value

        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

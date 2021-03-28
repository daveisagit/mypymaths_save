class Node:
    dice_A: list
    dice_B: list
    child_nodes: list

    def __init__(self):
        self.dice_A = []
        self.dice_B = []
        self.child_nodes = []

    def clone(self):
        new_node = Node()
        new_node.dice_A = self.dice_A.copy()
        new_node.dice_B = self.dice_B.copy()
        return new_node

    def get_distribution(self) -> dict:
        d = {}
        for n_A in self.dice_A:
            for n_B in self.dice_B:
                total = n_A + n_B
                count = d.get(total, 0)
                d[total] = count + 1
        return d

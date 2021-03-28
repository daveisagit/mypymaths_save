from node import Node

SIDES = 12

min_A = 1
min_B = 1

max_A = 14
max_B = 10

target_d = {}


def create_target_distribution(sides: int):
    tn = Node()
    tn.dice_A = list(range(1, sides + 1))
    tn.dice_B = list(range(1, sides + 1))
    return tn.get_distribution()


def add_x_lots_of_n(dice: list, x, n) -> int:
    while x > 0 and len(dice) < SIDES:
        dice.append(n)
        x -= 1
    return x

def add_child_nodes(node: Node, n: int):
    d = node.get_distribution()

    next_num = n + 1
    next_num_target = target_d.get(next_num, 0)
    next_num_count = d.get(next_num, 0)

    amount_of_n = next_num_target - next_num_count

    for i in range(0, amount_of_n + 1):
        new_node = node.clone()
        r = add_x_lots_of_n(new_node.dice_A, i, n)
        r = add_x_lots_of_n(new_node.dice_A, r, n)

        node.child_nodes.append(new_node)
        print(new_node)

    # for child_node in node.child_nodes:
    #     add_child_nodes(child_node, n + 1)


if __name__ == '__main__':
    print('Find Solutions')
    target_d = create_target_distribution(SIDES)
    print(target_d)
    node = Node()
    node.dice_A = [1]
    node.dice_B = [1]

    add_child_nodes(node, 2)
    for n in node.child_nodes:
        print("Node")
        print(n.dice_A)
        print(n.dice_B)

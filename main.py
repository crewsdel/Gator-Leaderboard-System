from AVLTree import Node, AVLTree, pre_order, _get_height, _get_size
import gator_leaderboard_system
from gator_leaderboard_system import initialize, insert_player, remove_player, get_rank, get_player_with_rank

if __name__ == '__main__':

    leaderboard = AVLTree()

    # # LL case insertion test
    # leaderboard.insert(30, 3333)
    # leaderboard.insert(20, 2222)
    # leaderboard.insert(10, 1111)
    # pre_order(leaderboard.root)
    #
    # # RR case insertion test
    # leaderboard.insert(10, 1111)
    # leaderboard.insert(20, 2222)
    # leaderboard.insert(30, 3333)
    # pre_order(leaderboard.root)
    #
    # ## LR case insertion test
    # leaderboard.insert(30, 3333)
    # leaderboard.insert(10, 1111)
    # leaderboard.insert(20, 2222)
    # pre_order(leaderboard.root)

    # # RL case insertion test
    # leaderboard.insert(20, 2222)
    # leaderboard.insert(10, 1111)
    # leaderboard.insert(30, 3333)
    # pre_order(leaderboard.root)

    # # Tie test case
    # leaderboard.insert(50, 2222)
    # leaderboard.insert(50, 1111)
    # pre_order(leaderboard.root)
    # print(leaderboard.root.left.key)

    # Tie test case
    # leaderboard.insert(50, 1111)
    # leaderboard.insert(50, 2222)
    # leaderboard.insert(40, 4444)
    # leaderboard.insert(20, 2222)
    # leaderboard.insert(30, 3333)
    # pre_order(leaderboard.root)
    # print(leaderboard.root.right.key)
    # print(_get_height(leaderboard.root))
    # print(_get_size(leaderboard.root))

    tree = AVLTree()
    tree.insert(50, 222222)
    tree.insert(40, 333333)

    # print(tree.rank((50, 222222)))
    # print(tree.select(1))



    initialize()
    insert_player(30, 333333)
    insert_player(10, 111111)
    insert_player(40, 444444)
    insert_player(60, 666666)

    get_rank(666666)
    get_rank(22222)
    get_player_with_rank(1)




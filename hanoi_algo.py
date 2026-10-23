
def hanoi_solver(total_number):
    list1 = list(range(total_number, 0, -1))
    list2 = []
    list3 = []

    moves = [f"{list1} {list2} {list3}"]

    def move_disks(n, source, helper, destination):
        if n == 1:
            disk = source.pop()
            destination.append(disk)
            moves.append(f"{list1} {list2} {list3}")
            return

        move_disks(n - 1, source, destination, helper)

        disk = source.pop()
        destination.append(disk)
        moves.append(f"{list1} {list2} {list3}")

        move_disks(n - 1, helper, source, destination)

    move_disks(total_number, list1, list2, list3)

    return "\n".join(moves)
hanoi_solver(5)

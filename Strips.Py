blocks = ["A", "B", "C"]

def move(block, destination):
    print("Move", block, "to", destination)

move("A", "Table")
move("B", "A")
move("C", "B")
print("Goal Achieved")

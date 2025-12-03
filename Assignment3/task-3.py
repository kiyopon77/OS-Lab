# TASK 3: Indexed File Allocation

total_blocks = int(input("Enter total number of blocks: "))
block_status = [0] * total_blocks

n = int(input("Enter number of files: "))

for i in range(n):
    index = int(input(f"\nEnter index block for file {i+1}: "))

    if block_status[index] == 1:
        print("Index block already allocated.")
        continue

    count = int(input("Enter number of data blocks required: "))
    data_blocks = list(map(int, input("Enter block numbers: ").split()))

    if len(data_blocks) != count:
        print("Incorrect number of blocks entered.")
        continue

    if any(block_status[b] == 1 for b in data_blocks):
        print("One or more blocks already allocated.")
        continue

    block_status[index] = 1
    for b in data_blocks:
        block_status[b] = 1

    print(f"File {i+1} allocated with index block {index} -> {data_blocks}")

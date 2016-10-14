file_BC = open("1k_digest_BC.txt", "r")
file_array = file_BC.readline()[1:-1].split(", ")
for line in file_array:
    print line

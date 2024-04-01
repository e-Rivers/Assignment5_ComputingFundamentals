# Testing
for listType in ["randomScrambled", "orderedDescending", "orderedAscending"]:
    for exp in range(2, 7):
        with open(f".\InputFiles\TextFiles\{listType}_10to{exp}.txt") as inputFile:
            inputArr = [int(i) for i in "".join(inputFile.readlines()).split(",")]
            print(f"{listType}, list size 10^{exp}")
            print("ORIGINAL")
            print(inputArr)
            print("\nSORTED")
            print(mergeSort(inputArr, 0, len(inputArr)-1))
            print("\n\n\n")

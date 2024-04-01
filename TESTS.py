#
# NOTE. Some print() functions are commented (the ones that print the unsorted and sorted arrays)
# because they take additional time with tampers the evaluation of the runtime and other metrics.
#

import time
from HeapSort import *
from MergeSort import *
from QuickSort import *

testType = int(input("Enter the type of test (0 - Stability, 1 - Runtime):"))

if testType == 0:
    # Stability Testing (Verifying if the algorithm keeps the relative order of data)
    def isStableSort(algorithm, inputData, extraArgs):
        indexedData = [(val, idx) for idx, val in enumerate(inputData)]
        
        # Sort the data using the provided sorting algorithm
        sortedData = algorithm(indexedData) if not extraArgs else algorithm(indexedData, 0, len(indexedData)-1)

        # Check if the relative order of equal elements is preserved
        for i in range(1, len(sortedData)):
            if sortedData[i][0] == sortedData[i - 1][0]:
                if sortedData[i][1] < sortedData[i - 1][1]:
                    return False
        return True

    for listType in ["randomScrambled"]:#["randomScrambled", "orderedDescending", "orderedAscending"]:
        print("#####################################################################")
        with open(f".\\InputFiles\\TextFiles\\scalabilityTestFile.txt") as inputFile:
            arr = [int(i) for i in "".join(inputFile.readlines()).split(",")]
            for algorithm in ["Merge", "Quick", "Heap"]:
                print("=============================================")
                print(f"{algorithm} Sort")
                inputArr = list(arr)
                if algorithm == "Merge":
                    print(f"Runtime: {isStableSort(mergeSort, inputArr, True)}")
                elif algorithm == "Quick": 
                    print(f"Runtime: {isStableSort(quickSort, inputArr, True)}")
                else:
                    print(f"Runtime: {isStableSort(heapSort, inputArr, False)}")
                print("\n\n")
else:
    # Runtime Testing
    for listType in ["randomScrambled", "orderedDescending", "orderedAscending"]:
        for exp in range(2, 7):
            print("#####################################################################")
            with open(f".\\InputFiles\\TextFiles\\{listType}_10to{exp}.txt") as inputFile:
                arr = [int(i) for i in "".join(inputFile.readlines()).split(",")]
                for algorithm in ["Merge", "Quick", "Heap"]:
                    print("=============================================")
                    print(f"{algorithm} Sort")
                    
                    # MEASUREMENT VARIABLES INITIALIZATION
                    startTime = time.time()

                    # CALCULATIONS
                    inputArr = list(arr)
                    print(f"{listType}, list size 10^{exp}")
                    #print("ORIGINAL")
                    #print(inputArr)
                    #print("\nSORTED")
                    if algorithm == "Merge":
                        mergeSorted = mergeSort(inputArr, 0, len(inputArr)-1)
                        #print(mergeSorted)
                    elif algorithm == "Quick":
                        #quickSorted = quickSort(inputArr, 0, len(inputArr)-1)
                        #print(quickSorted)
                        pass
                    else:
                        heapSorted = heapSort(inputArr)
                        #print(heapSorted)

                    # MEASUMENT FINALIZATION
                    runtime = time.time() - startTime

                    #print("\nREPORT")
                    print(f"Runtime: {runtime:.4f}")
                    print("\n\n")

                




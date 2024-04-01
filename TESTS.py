#
# NOTE. Some print() functions are commented (the ones that print the unsorted and sorted arrays)
# because they take additional time with tampers the evaluation of the runtime and other metrics.
#

import time
from HeapSort import *
from MergeSort import *
from QuickSort import *

# Testing
for listType in ["orderedDescending"]:#["randomScrambled", "orderedDescending", "orderedAscending"]:
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

            




from time import time as detak
from random import shuffle as kocok
import time
from Lat_5_1 import bubbleSort, selectionSort, insertionSort
from Lat_6_1 import mergeSort, quickSort
from Tug_6_5 import mergeSortNew
from Tug_6_6 import quickSortNew

k = [i for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]
u_mrg2 = k[:]
u_qck2 = k[:]

aw = detak(); bubbleSort(u_bub); ak = detak(); print('bubble: %g detik' %(ak-aw));
aw = detak(); selectionSort(u_sel); ak = detak(); print('selection: %g detik' %(ak-aw));
aw = detak(); insertionSort(u_ins); ak = detak(); print('insertion: %g detik' %(ak-aw));
aw = detak(); mergeSort(u_mrg); ak = detak(); print('merge: %g detik' %(ak-aw));
aw = detak(); quickSort(u_qck); ak = detak(); print('quick: %g detik' %(ak-aw));
aw = detak(); mergeSortNew(u_mrg2); ak = detak(); print('merge2: %g detik' %(ak-aw));
aw = detak(); quickSortNew(u_qck2); ak = detak(); print('quick2: %g detik' %(ak-aw));
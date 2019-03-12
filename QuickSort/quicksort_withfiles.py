import xml.etree.ElementTree as et
#from multiprocessing import Process
from threading import Thread
import unittest

class QuickSort:
    def __init__(self, filename):
        self.array = self.parser(filename)
    
    def qsort(self,left,right):
        
        if left<right:
            splitPoint = self.partition(left, right) 
            #introduce concurrency here
            
            #self.qsort(left, splitPoint-1)
            #self.qsort(splitPoint+1, right)
            t1 = Thread(target=self.qsort, args=(left,splitPoint-1,))
            t2 = Thread(target=self.qsort, args=(splitPoint+1,right,))
            
            t1.start()
            t2.start()
            
            t1.join()        
            t2.join()
            
        return self.array
            
            
        
    def parser(self, filename):
        #parsing from the XML file
        tree = et.parse(filename)
        root = tree.getroot()
        array = []
               
        for child in root:
            array.append(int(child.text))
        
        return array
    
    def swap(self,index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp
    
    def partition(self, left, right):
            
        '''taking middle element as pivot
        can also be the first, the last or 
        the median of first, last and middle'''
        
        '''for pivot = array[left]
        leftmark = left+1
        rightmark = right
        
        for pivot = array[right]
        leftmark = left
        rightmark = right - 1
        ''' 
        pivotvalue = self.array[left]
        leftmark = left+1
        rightmark = right

        while True:
            while leftmark <= rightmark and self.array[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
                
            while self.array[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1
                
            if rightmark < leftmark:
                break
            else:
                temp = self.array[leftmark]
                self.array[leftmark] = self.array[rightmark]
                self.array[rightmark] = temp

        temp = self.array[left]
        self.array[left] = self.array[rightmark]
        self.array[rightmark] = temp

        return rightmark
    
    def displaySortedArray(self):
        print "Sorted Array is :",self.array
        

def driverFunction(filename):
    qsortObj = QuickSort(filename)
    sortedArray = qsortObj.qsort(0, len(qsortObj.array)-1)
    qsortObj.displaySortedArray()  
    return sortedArray  
    

class Testing(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(driverFunction("positiveInput.xml"), [-5,-1,0,1,2,6,8,8])
        
    def test_negative(self):
        self.assertEqual(driverFunction("negativeInput1.xml"), [-5,-1,0,1,2,6,8,8])
        
if __name__=="__main__":
    unittest.main()

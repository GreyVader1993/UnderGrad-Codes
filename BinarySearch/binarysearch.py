import unittest

class MyTestCases(unittest.TestCase):
    def test_positive(self):
        binSearchObj = BinarySearch([10, 15, 30, 20, 19], 19) #Test case with element present in list
        self.assertEqual(binSearchObj.perform_binary_search(), 2)
        binSearchObj = BinarySearch([90, 12, 34, 65, 23, 10], 65)
        self.assertEqual(binSearchObj.perform_binary_search(), 4)
        
    def test_negative(self):
        binSearchObj = BinarySearch([80, 70, 60, 50, 65, 90, 100], 20) #Test case with element not present in list
        self.assertEqual(binSearchObj.perform_binary_search(), 7)
        
class BinarySearch:
    def __init__(self, a, elem_to_search):
        self.a = a
        self.elem_to_search = elem_to_search
        self.sort_for_binary_search()
        self.display_list()
        
    def display_list(self):
        print "The created list is: ", self.a

    #Function to sort the list for Binary Search
    #Add any sorting method necessary, according to your convenience
    def sort_for_binary_search(self):
        self.a.sort()

    #Recursive call for binary search
    def binary_search(self, a, left, right):
        mid = (left + right)/2
        
        #Element not found
        if(mid > right or mid < left):
            return len(self.a)

        #Element is in the middle of the list
        elif(a[mid] == self.elem_to_search):
            return mid

        #Element should be present in the second half of the list 
        elif(a[mid] < self.elem_to_search):
            left = mid+1
            
        #Element should be present in the first half of the list
        elif(a[mid] > self.elem_to_search):
            right = mid-1
            
        return self.binary_search(a, left, right)

    #Function to call the binary search function 
    def perform_binary_search(self):
        a = self.a
        left = 0
        right = len(self.a) - 1

        index = self.binary_search(a, left, right)

        if(index >= len(self.a)):
            print "Element not found"
        else:
            print "Element is present at position ", index, "in the array ", self.a

        return index

def main():
    
    print "Enter the elements: "
    a = map(int, raw_input().split())
    print "The list has been created.\n"
    elem_to_search = int(raw_input("Enter the element to be searched: ").strip())

    binSearchObj = BinarySearch(a, elem_to_search)
    binSearchObj.perform_binary_search()

print "Executing code here"
main()

print "\nTesting begins here"
unittest.main()

import math
import argparse

class Sort:
    def __init(input_list):
        self.input = input_list

    def bubble_sort():
        for size in range(len(self.input)):
            for item in range(size):
               if self.input[item] > self.input[item+1]:
                   self.input[item] = self.input[item] + self.input[item+1]
                   self.input[item+1] = self.input[item] - self.input[item+1]
                   self.input[item] = self.input[item] - self.input[item+1]

        return self.input

    def insertion_Sort():
        for index in range(1, len(self.input)):
            key = self.input(index)
            holder = index -1
            while holder > 0 and key < self.input[holder]:
                self.input[holder + 1],holder  = self.input[holder], holder-1
                self.input[holder + 1] = key

        return self.input

    def quick_sort():

        list_size = len(self.input)

        #Base case
        if list_size < 2:
            return self.input

        current_position = 0 #Position of the partitioning element

        for i in range(1, list_size): #Partitioning loop
             if self.input[i] <= self.input[0]:
                  current_position += 1
                  self.input[i] =  self.input[i] + self.input[current_position]
                  self.input[current_position] = self.input[i] - self.input[current_position]
                  self.input[i] = self.input[i] - self.input[current_position]

        self.input[0] = self.input[0] + self.input[current_position]
        self.input[current_position] = self.input0] - self.input[current_position] #Brings pivot to it's appropriate position
        self.input[0] = self.input[0] -self.input[current_position]

        left = quick_sort(self.input[0:current_position]) #Sorts the elements to the left of pivot
        right = quick_sort(self.input[current_position+1:elements]) #sorts the elements to the right of pivot

        self.input = left + [self.input[current_position]] + right #Merging everything together

        return self.input


    def Merge_Sort():
    def merge_sort(self.input, left_index, right_index):
        if left_index >= right_index:
            return

        middle = (left_index + right_index)//2
        merge_sort(self.input, left_index, middle)
        merge_sort(self.input, middle + 1, right_index)
        merge(self.input, left_index, right_index, middle)
        return self.input_list

    def merge(aself.input, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = self.input[left_index:middle + 1]
    right_copy = self.input[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            self.input[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            self.input[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        self.input[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        aself.input[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('--input_list', required=True, help='unsorted list of input')

    if len(sys.argv) == 1:
         parser.print_help(sys.stderr)
         sys.exit(1)

    args = parser.parse_args()

    sorter = Sort(args.input_list)
    sorted_output = sorter.quick_sort()
    print("Sorted Output is:", sorted_output)

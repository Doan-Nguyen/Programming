
from logging import raiseExceptions
from time import sleep


class DynamicArrays:
    def __init__(self) -> None:
        self.size = 0 
        self.capacity = 1
        self.arr = self.mar

    def check_index(self, idx):
        if idx < 0 or idx >= len(self.arr):
            return False
        return True            

    def get(self, idx):
        '''
        This function gets element at i-th.
        Error : idx < 0 or idx >= arr'size
        '''
        if self.check_index(idx):
            return self.arr[idx]
        else:
            raise Exception("Index out of range")            

    def set(self, idx, val):
        '''
        This function sets element i-th to val
        '''
        if self.check_index(idx):
            self.arr[idx] = val
            return self.arr
        else:
            raise Exception("Index out of range")

    def pushBack(self, val):
        '''
        
        '''

        



if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    dy_arr = DynamicArrays(input_arr=arr)
    idx = dy_arr.get(-1)
    print(idx)
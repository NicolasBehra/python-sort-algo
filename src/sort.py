# -*-coding:Latin-1 -*

import array

IntArray = array.array('i')

class MySort:
    def is_sorted(self, t: IntArray) -> bool:
        for i in range(0, len(t)-1):
            if (t[i] > t[i+1]):
                return False
        return True

    def get_index(self, sorted_t: IntArray, elem: int) -> int:
        if (len(sorted_t) > 0):
            if (len(sorted_t) > 1):
                sorted_half_t_left, sorted_half_t_right = self.split_array(sorted_t)
                if (sorted_half_t_left[-1] < elem): # -1 get last elem
                    index = self.get_index(sorted_half_t_right, elem)
                    if (index > -1):
                        return index + len(sorted_half_t_left)
                    else:
                        return index
                else:
                    return self.get_index(sorted_half_t_left, elem)
            else:
                if (sorted_t[0] == elem):
                    return 0
        return -1

    def split_array(self, t: IntArray) -> (IntArray, IntArray):
        if (len(t) > 0):
            if (len(t) > 1):
                half = int(round(len(t)/2))
                return t[:half], t[half:]
            else:
                return t, IntArray
        return IntArray, IntArray

    def get_index_of_minimum(self, t: IntArray) -> int:
        if (len(t) > 0):
            if (len(t) > 1):
                (minus, index) = (t[0], 0)
                for i in range(1, len(t)):
                    if (t[i] < minus):
                        (minus, index) = (t[i], i)
                return index
            return 0
        return -1

    def selection_sort(self, t: IntArray) -> IntArray:
        if (len(t) > 0):
            if (len(t) > 1):
                for i in range(0, len(t)-1):
                    index_of_minimum = self.get_index_of_minimum(t[i:]) + i
                    t = self.invert_two_values(t, i, index_of_minimum)
            return t
        return IntArray

    def invert_two_values(self, t: IntArray, pos_val_1: int, pos_val_2: int) -> IntArray:
        val_1 = t[pos_val_1]
        t[pos_val_1] = t[pos_val_2]
        t[pos_val_2] = val_1
        return t

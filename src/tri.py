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

        # for i in range(0, len(sorted_t)):
        #     if (sorted_t[i] == elem):
        #         return i
        # return -1

    def split_array(self, t: IntArray) -> (IntArray, IntArray):
        if (len(t) > 0):
            if (len(t) > 1):
                half = int(round(len(t)/2))
                return t[:half], t[half:]
            else:
                return t, IntArray
        return IntArray, IntArray



        # if (len(sorted_t) > 0):
        #     if (sorted_t[0] == elem):
        #         return 0
        #     elif (len(sorted_t) > 1):
        #         if (sorted_t[1] == elem):
        #             return 1
        #         elif (len(sorted_t) > 2):
        #             if (sorted_t[2] == elem):
        #                 return 2
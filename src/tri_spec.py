# -*-coding:Latin-1 -*

import unittest
import array

from tri import MySort as MySortClass
from tri import IntArray

class TestMySort(unittest.TestCase):

    def setUp(self):
        self.my_sort = MySortClass()

    # is_sorted

    def test_is_sorted_1_empty_array_true(self):
        my_tab = IntArray
        self.assertEqual(self.my_sort.is_sorted(my_tab), True)

    def test_is_sorted_2_array_init__return_true(self):
        my_tab = array.array('i', (0 for i in range(0, 10)))
        self.assertEqual(self.my_sort.is_sorted(my_tab), True)

    def test_is_sorted_3_array_one_elem__return_true(self):
        my_tab = array.array('i', [1])
        self.assertEqual(self.my_sort.is_sorted(my_tab), True)

    def test_is_sorted_4_array_two_elem__return_true(self):
        my_tab = array.array('i', [1, 2])
        self.assertEqual(self.my_sort.is_sorted(my_tab), True)

    def test_is_sorted_5_array_two_elem__return_false(self):
        my_tab = array.array('i', [2, 1])
        self.assertEqual(self.my_sort.is_sorted(my_tab), False)

    def test_is_sorted_6_array_two_elem__return_false(self):
        my_tab = array.array('i', [6, 0])
        self.assertEqual(self.my_sort.is_sorted(my_tab), False)

    def test_is_sorted_7_array_three_elem__return_true(self):
        my_tab = array.array('i', [1, 2, 3])
        self.assertEqual(self.my_sort.is_sorted(my_tab), True)

    def test_is_sorted_8_array_three_elem__return_false(self):
        my_tab = array.array('i', [1, 4, 3])
        self.assertEqual(self.my_sort.is_sorted(my_tab), False)

    def test_is_sorted_9_array_four_elem__return_true(self):
        my_tab = array.array('i', [1, 2, 3, 4])
        self.assertEqual(self.my_sort.is_sorted(my_tab), True)

    def test_is_sorted_10_array_four_elem__return_false(self):
        my_tab = array.array('i', [1, 2, 4, 3])
        self.assertEqual(self.my_sort.is_sorted(my_tab), False)

    # get_index

    def test_get_index_1_empty_array__return_minus_1(self):
        my_sorted_tab = IntArray
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 1), -1)

    def test_get_index_2_array_init__return_minus_1(self):
        my_sorted_tab = array.array('i', (0 for i in range(0, 10)))
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 1), -1)

    def test_get_index_3_array_one_elem__return_minus_1(self):
        my_sorted_tab = array.array('i', [1])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 2), -1)

    def test_get_index_4_array_one_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 1), 0)

    def test_get_index_5_array_two_elem__return_minus_1(self):
        my_sorted_tab = array.array('i', [1, 2])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 3), -1)

    def test_get_index_6_array_two_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1, 2])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 1), 0)

    def test_get_index_7_array_two_elem__return_one(self):
        my_sorted_tab = array.array('i', [1, 2])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 2), 1)

    def test_get_index_8_array_three_elem__return_minus_1(self):
        my_sorted_tab = array.array('i', [1, 2, 3])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 4), -1)

    def test_get_index_9_array_three_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1, 2, 3])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 1), 0)

    def test_get_index_10_array_three_elem__return_one(self):
        my_sorted_tab = array.array('i', [1, 2, 3])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 2), 1)

    def test_get_index_11_array_three_elem__return_two(self):
        my_sorted_tab = array.array('i', [1, 2, 3])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 3), 2)

    def test_get_index_12_array_test__return_one(self):
        my_sorted_tab = array.array('i', [1, 3, 3, 5, 6, 7, 7])
        self.assertEqual(self.my_sort.get_index(my_sorted_tab, 3), 1)

    # split_array

    def test_split_array_1_empty_array__return_empty(self):
        my_tab = IntArray
        self.assertEqual(self.my_sort.split_array(my_tab), (IntArray, IntArray))

    def test_split_array_2_array_init__return_empty(self):
        my_tab = array.array('i', (0 for i in range(0, 10)))
        my_half_tab = array.array('i', [0, 0, 0, 0, 0])
        self.assertEqual(
            self.my_sort.split_array(my_tab), (my_half_tab, my_half_tab))

    def test_split_array_3_array_one_elem__return_self_array_and_empty(self):
        my_tab = array.array('i', [1])
        self.assertEqual(
            self.my_sort.split_array(my_tab), (my_tab, IntArray))

    def test_split_array_4_array_two_elem__return_two_arrays_of_one_elem(self):
        my_tab = array.array('i', [1, 2])
        my_half_tab_1 = array.array('i', [1])
        my_half_tab_2 = array.array('i', [2])
        self.assertEqual(
            self.my_sort.split_array(my_tab), (my_half_tab_1, my_half_tab_2))

    def test_split_array_5_array_three_elem__return_two_arrays_two_and_one_elem(self):
        my_tab = array.array('i', [1, 2, 3])
        my_half_tab_1 = array.array('i', [1, 2])
        my_half_tab_2 = array.array('i', [3])
        self.assertEqual(
            self.my_sort.split_array(my_tab), (my_half_tab_1, my_half_tab_2))

    # get_index_of_minimum

    def test_get_index_of_minimum_1_empty_array__return_minus_1(self):
        my_sorted_tab = IntArray
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), -1)

    def test_get_index_of_minimum_2_array_one_elem__return_zero(self):
        my_sorted_tab = array.array('i', [2])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 0)

    def test_get_index_of_minimum_3_array_two_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1, 2])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 0)

    def test_get_index_of_minimum_4_array_two_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1, 1])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 0)

    def test_get_index_of_minimum_5_array_two_elem__return_one(self):
        my_sorted_tab = array.array('i', [2, 1])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 1)

    def test_get_index_of_minimum_6_array_three_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1, 2, 3])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 0)

    def test_get_index_of_minimum_7_array_three_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1, 3, 2])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 0)

    def test_get_index_of_minimum_8_array_three_elem__return_zero(self):
        my_sorted_tab = array.array('i', [1, 1, 1])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 0)

    def test_get_index_of_minimum_9_array_three_elem__return_one(self):
        my_sorted_tab = array.array('i', [2, 1, 3])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 1)

    def test_get_index_of_minimum_10_array_three_elem__return_one(self):
        my_sorted_tab = array.array('i', [3, 1, 2])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 1)

    def test_get_index_of_minimum_11_array_three_elem__return_two(self):
        my_sorted_tab = array.array('i', [2, 3, 1])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 2)

    def test_get_index_of_minimum_12_array_three_elem__return_two(self):
        my_sorted_tab = array.array('i', [3, 2, 1])
        self.assertEqual(self.my_sort.get_index_of_minimum(my_sorted_tab), 2)

    # selection_sort

    def test_selection_sort_1_empty_array__return_empty(self):
        my_tab = IntArray
        self.assertEqual(self.my_sort.selection_sort(my_tab), IntArray)

    def test_selection_sort_2_array_init__return_self_array(self):
        my_tab = array.array('i', (0 for i in range(0, 10)))
        self.assertEqual(
            self.my_sort.selection_sort(my_tab), my_tab)

    def test_selection_sort_3_array_one_elem__return_self_array(self):
        my_tab = array.array('i', [1])
        self.assertEqual(
            self.my_sort.selection_sort(my_tab), my_tab)

    def test_selection_sort_4_sorted_array__return_self_array(self):
        my_tab = array.array('i', [1, 2])
        self.assertEqual(
            self.my_sort.selection_sort(my_tab), my_tab)

    def test_selection_sort_5_array_two_elem__return_sorted_array(self):
        my_tab = array.array('i', [2, 1])
        sorted_array = array.array('i', [1, 2])
        self.assertEqual(
            self.my_sort.selection_sort(my_tab), sorted_array)

    def test_selection_sort_6_array_three_elem__return_sorted_array(self):
        my_tab = array.array('i', [3, 2, 1])
        sorted_array = array.array('i', [1, 2, 3])
        self.assertEqual(
            self.my_sort.selection_sort(my_tab), sorted_array)

    def test_selection_sort_7_array_three_elem__return_sorted_array(self):
        my_tab = array.array('i', [3, 1, 2])
        sorted_array = array.array('i', [1, 2, 3])
        self.assertEqual(
            self.my_sort.selection_sort(my_tab), sorted_array)

    def test_selection_sort_7_array_five_elem__return_sorted_array(self):
        my_tab = array.array('i', [3, 1, 2, 8, 4])
        sorted_array = array.array('i', [1, 2, 3, 4, 8])
        self.assertEqual(
            self.my_sort.selection_sort(my_tab), sorted_array)



    # get_minus_of_two_elem

    def test_get_minus_of_two_elem_1_lower__return_first(self):
        elem_1 = 2
        elem_2 = 3
        self.assertEqual(
            self.my_sort.get_minus_of_two_elem(elem_1, elem_2), 2)

    def test_get_minus_of_two_elem_1_lower__return_first(self):
        elem_1 = 2
        elem_2 = -1
        self.assertEqual(
            self.my_sort.get_minus_of_two_elem(elem_1, elem_2), 2)

    def test_get_minus_of_two_elem_1_lower__return_second(self):
        elem_1 = 3
        elem_2 = 2
        self.assertEqual(
            self.my_sort.get_minus_of_two_elem(elem_1, elem_2), 2)

    def test_get_minus_of_two_elem_1_lower__return_second(self):
        elem_1 = -1
        elem_2 = 2
        self.assertEqual(
            self.my_sort.get_minus_of_two_elem(elem_1, elem_2), 2)

    def test_get_minus_of_two_elem_1_lower__return_minus_one(self):
        elem_1 = -1
        elem_2 = -1
        self.assertEqual(
            self.my_sort.get_minus_of_two_elem(elem_1, elem_2), -1)


if __name__ == '__main__':
    unittest.main()
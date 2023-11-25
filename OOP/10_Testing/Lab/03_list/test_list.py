from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList("50", 1, False, 3.6, 2, 3)
    
    def test_get_data_returns_list(self):
        self.assertIsInstance(self.integer_list.get_data(), list)
    
    def test_correct_integer_and_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())
    
    def test_add_operation_adds_int_to_list(self):
        expected_data = self.integer_list.get_data() + [5]
        actual_data = self.integer_list.add(5)
        self.assertListEqual(expected_data, actual_data)
    
    def test_add_operation_with_wrong_data(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(5.5)
        
        self.assertEqual("Element is not Integer", str(ve.exception))
    
    def test_remove_index_operation_without_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(100)
        
        self.assertEqual("Index is out of range", str(ie.exception))
    
    def test_remove_index_with_valid_index_removes_element(self):
        deleted_element = 2
        expected = [1, 3]
        
        actual_deleted_element = self.integer_list.remove_index(1)
        
        self.assertEqual(expected, self.integer_list.get_data())
        self.assertEqual(deleted_element, actual_deleted_element)
    
    def test_get_test_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(100)
        
        self.assertEqual("Index is out of range", str(ie.exception))
    
    def test_get_test_with_valid_index_returns_element(self):
        actual_element = self.integer_list.get(1)
        expected_element = 2
        
        self.assertEqual(expected_element, actual_element)
    
    def test_insert_integer_at_valid_index_expect_inserted_element(self):
        expected_list = [1, 2, 4, 3]
        self.integer_list.insert(len(self.integer_list.get_data()) - 1, 4)
        self.assertEqual(expected_list, self.integer_list.get_data())
    
    def test_insert_integer_with_invalid_index_expected_rises_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(100, 4)
        
        self.assertEqual("Index is out of range", str(ie.exception))
    
    def test_insert_invalid_element_on_valid_index_rises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(2, 5.6)
        
        self.assertEqual("Element is not Integer", str(ve.exception))
    
    def test_get_biggest_successful(self):
        self.assertEqual(3, self.integer_list.get_biggest())
    
    def test_get_index_successful(self):
        self.assertEqual(1, self.integer_list.get_index(2))


if __name__ == "__main__":
    main()

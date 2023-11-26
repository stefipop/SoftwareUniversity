from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student1 = Student("Stefi")
        self.student2 = Student("Stefi", {"Python": [100]})
    
    def test_correct_initialization_with_empty_list(self):
        self.assertEqual("Stefi", self.student1.name)
        self.assertEqual({}, self.student1.courses)
    
    def test_correct_initialization_with_courses_in_list(self):
        self.assertEqual("Stefi", self.student2.name)
        self.assertEqual({"Python": [100]}, self.student2.courses)
    
    def test_enroll_existing_course(self):
        result = self.student2.enroll("Python", [90, 85, 100], )
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python": [100, 90, 85, 100]}, self.student2.courses)
    
    def test_enroll_new_course_with_notes_and_add_course_notes(self):
        result = self.student1.enroll("JS", [90, 85, 100])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"JS": [90, 85, 100]}, self.student1.courses)
    
    def test_enroll_existing_course_with_notes_and_no_add_course_notes(self):
        result = self.student2.enroll("DB", [100], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Python": [100], "DB": []}, self.student2.courses)
    
    def test_enroll_existing_course_with_notes_and_add_course_notes(self):
        result = self.student2.enroll("JS", [100], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python": [100], "JS": [100]}, self.student2.courses)
    
    def test_add_notes_in_existing_course(self):
        self.student1.enroll("DB", [80, 100], "N")
        result = self.student1.add_notes("DB", 50)
        self.assertEqual("Notes have been updated", result)
        self.assertEqual([50], self.student1.courses.get("DB"))
    
    def test_add_notes_in_non_existing_course(self):
        with self.assertRaises(Exception) as e:
            result = self.student1.add_notes("DB", 50)
        self.assertEqual("Cannot add notes. Course not found.", str(e.exception))
    
    def test_leave_existing_course(self):
        result = self.student2.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student2.courses)
    
    def test_leave_nonexistent_course(self):
        with self.assertRaises(Exception) as e:
            self.student1.leave_course("DB")
        self.assertEqual("Cannot remove course. Course not found.", str(e.exception))


if __name__ == '__main__':
    main()

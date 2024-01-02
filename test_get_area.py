import unittest
from get_area import get_rectangle_area, get_bbox_area


class TestGetRectangleArea(unittest.TestCase):
  def test_get_rectangle_area(self):
    # Test case 1: width = 5, height = 10
    self.assertEqual(get_rectangle_area(5, 10), 50)

    # Test case 2: width = 3, height = 7
    self.assertEqual(get_rectangle_area(3, 7), 21)

    # Test case 3: width = 0, height = 5
    self.assertEqual(get_rectangle_area(0, 5), 0)


class TestGetBboxArea(unittest.TestCase):
  def test_get_bbox_area(self):
    # Test case 1: bbox = (0, 0, 5, 5)
    self.assertEqual(get_bbox_area((0, 0, 5, 5)), 25)

    # Test case 2: bbox = (2, 3, 7, 9)
    self.assertEqual(get_bbox_area((2, 3, 7, 9)), 30)

    # Test case 3: bbox = (0, 0, 0, 0)
    self.assertEqual(get_bbox_area((0, 0, 0, 0)), 0)


if __name__ == '__main__':
  unittest.main()

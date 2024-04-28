from unittest import TestCase

from src.pytemplate.domain.models import Operands


class TestOperands(TestCase):
  def test_init_valid_operands(self):
    operands = Operands(10, 5)
    self.assertEqual(operands.first_operand, 10)
    self.assertEqual(operands.second_operand, 5)

  def test_init_invalid_type(self):
    with self.assertRaises(TypeError):
      Operands("hello", 5)

  def test_init_invalid_type2(self):
    with self.assertRaises(TypeError):
      Operands(10, "world")

if __name__ == "__main__":
  unittest.main()
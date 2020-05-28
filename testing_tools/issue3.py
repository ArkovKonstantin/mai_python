import unittest
from testing_tools import one_hot_encoder


class TestEncoder(unittest.TestCase):

    def test_args(self):
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        res_args = one_hot_encoder.fit_transform('Moscow', 'New York', 'Moscow', 'London')
        res_list = one_hot_encoder.fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        self.assertEqual(expected, res_args)
        self.assertEqual(expected, res_list)

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform()

    def test_empty_arglist(self):
        res = one_hot_encoder.fit_transform([])
        self.assertEqual([], res)

    def test_not_string_input(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform(1)

    def test_res_type(self):
        res = one_hot_encoder.fit_transform('Moscow', 'New York', 'Moscow')
        self.assertIsInstance(res, list)
        [self.assertIsInstance(x, tuple) for x in res]


if __name__ == '__main__':
    unittest.main()

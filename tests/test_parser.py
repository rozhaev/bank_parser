import shutil
import unittest

from app.core.csv_application import CSVApplication


class ParametrizedCSVTestCase(unittest.TestCase):

    def setUp(self):
        self.test_data = [
            {
                'input': './tests/data/bank1',
                'output': 'test_result/bank1',
                'expected_value': 'date,transaction_type,amount,from,to\n'
                                  '2019-10-01,remove,99.20,198,182\n'
                                  '2019-10-02,add,2000.10,188,198\n'
            },
            {
                'input': './tests/data/bank2',
                'output': 'test_result/bank2',
                'expected_value': 'date,transaction_type,amount,from,to\n'
                                  '2019-10-03,remove,99.40,198,182\n'
                                  '2019-10-04,add,2123.50,188,198\n',
            },
            {
                'input': './tests/data/bank3',
                'output': 'test_result/bank3',
                'expected_value': 'date,transaction_type,amount,from,to\n'
                                  '2019-10-05,remove,5.07,198,182\n'
                                  '2019-10-06,add,1060.08,188,198\n',
            },
            {
                'input': './tests/data/bank4',
                'output': 'test_result/bank4',
                'expected_value': 'date,transaction_type,amount,from,to\n'
                                  '2019-10-05,remove,5.07,198,182\n'
                                  '2019-10-06,add,1060.08,188,198\n'
                                  '2019-10-01,remove,99.20,198,182\n'
                                  '2019-10-02,add,2000.10,188,198\n'
                                  '2019-10-03,remove,99.40,198,182\n'
                                  '2019-10-04,add,2123.50,188,198\n'
            },
            {
                'input': './tests/data/bank5',
                'output': 'test_result/bank5',
                'expected_value': 'date,transaction_type,amount,from,to\n'
            },
            {
                'input': './tests/data/bank6',
                'output': 'test_result/bank6',
                'expected_value': 'date,transaction_type,amount,from,to\n'
            }
        ]

    def test_parser(self):
        for params in self.test_data:
            with self.subTest(test_value=params):
                self.app = CSVApplication(params['input'], params['output'], 'test_banks')
                self.app.run()
                checked_value = self.get_result_from_file(f'{params["output"]}/test_banks.csv')
                self.assertEqual(params['expected_value'], checked_value)

    @staticmethod
    def get_result_from_file(file_name: str):
        with open(file_name, mode="r", encoding="UTF-8") as csv_file:
            return csv_file.read()

    def tearDown(self):
        shutil.rmtree('test_result', ignore_errors=True)


if __name__ == '__main__':
    unittest.main()

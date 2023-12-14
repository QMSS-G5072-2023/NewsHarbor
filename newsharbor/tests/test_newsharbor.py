from newsharbor import newsharbor
import unittest

class TestNewsharborAPI(unittest.TestCase):

    def setUp(self):
        self.api = NewsharborAPI()

    def test_get_section_list(self):
        result = self.api.get_section_list()
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'OK')

    def test_get_latest_news(self):
        result = self.api.get_latest_news('world')
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'OK')

    def test_search_news(self):
        result = self.api.search_news('technology')
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'OK')

)

    def test_analyze_news_data(self):
        result = self.api.analyze_news_data('world')
    

if __name__ == '__main__':
    unittest.main()

# import unittest
# from aggregator import Aggregator



# class TestAggregator(unittest.TestCase):
#     def test_fetch(self):
#         aggr = Aggregator()
#         articles = aggr.get_combined_data()
#         self.assertIsInstance(articles, list)
#         if articles:
#             self.assertIn('title', articles[0])
#             self.assertIn('full_content', articles[0])

# if __name__ == "__main__":
#     unittest.main()



import unittest
from aggregator import Aggregator

class TestAggregator(unittest.TestCase):
    def test_fetch(self):
        aggr = Aggregator()
        articles = aggr.get_combined_data()
        self.assertIsInstance(articles, list)
        if articles:
            self.assertIn('title', articles[0])
            self.assertIn('full_content', articles[0])

if __name__ == "__main__":
    unittest.main()

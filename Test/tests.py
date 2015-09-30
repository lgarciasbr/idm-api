from Account import main_app

import unittest
import json


class StunticonTest(unittest.TestCase):

  def test_index(self):

    tester = main_app.app.test_client(self)

    response = tester.get('/')

    self.assertEqual(response.status_code, 200)
    self.assertEqual(
        response.data,
        json.dumps([
            "Motormaster",
            "Dead End",
            "Breakdown",
            "Wildrider",
            "Drag Strip"
        ])
    )

if __name__ == '__main__':
    unittest.main()
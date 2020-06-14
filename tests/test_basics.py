# %%

import unittest
import yaml


from logparser import parser

# %%

class TestMe(unittest.TestCase):
    def test_existence(self):
       assert parser.my_string == 'whoa, this is so kewl'
    
    def test_parsing(self):
       assert parser.my_string == 'whoa, this is so kewl'


if __name__ == '__main__':
    unittest.main()

# %%

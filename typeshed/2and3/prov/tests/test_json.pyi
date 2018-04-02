# Stubs for prov.tests.test_json (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import unittest
from prov.tests.test_model import AllTestsBase
from prov.tests.utility import RoundTripTestCase
from typing import Any

logger: Any

class TestJSONSerializer(unittest.TestCase):
    def test_decoding_unicode_value(self): ...

class RoundTripJSONTests(RoundTripTestCase, AllTestsBase):
    FORMAT: str = ...

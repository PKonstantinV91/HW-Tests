from unittest import TestCase
from main1 import filter_russia, unicum_id, max_value, geo_logs, ids, stats


class TestFilterRussia(TestCase):

    def test_geologs_list(self):
        res = filter_russia(geo_logs)
        self.assertIsInstance(res, list)


class TestUnicumId(TestCase):

    def test_ids(self):
        res = unicum_id(ids)
        self.assertEqual(res, list(set(res)))


class TestMaxValue(TestCase):

    def test_stats(self):
        res = max_value(stats)
        self.assertIn('yandex', res)
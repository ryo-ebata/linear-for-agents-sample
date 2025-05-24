"""
Tests for the JRA data collector module.
"""
import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock

import pandas as pd

from src.data_collection.jra_collector import JRADataCollector


class TestJRADataCollector(unittest.TestCase):
    """
    Test cases for the JRADataCollector class.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        self.temp_dir = tempfile.TemporaryDirectory()
        
        # Create a collector with a temporary data directory
        with patch('os.makedirs'):
            with patch('os.path.dirname', return_value=self.temp_dir.name):
                self.collector = JRADataCollector(start_year=2020, end_year=2021)
                self.collector.data_dir = self.temp_dir.name
    
    def tearDown(self):
        """
        Tear down test fixtures.
        """
        self.temp_dir.cleanup()
    
    def test_init(self):
        """
        Test initialization of the JRADataCollector.
        """
        self.assertEqual(self.collector.start_year, 2020)
        self.assertEqual(self.collector.end_year, 2021)
        self.assertIsNotNone(self.collector.session)
    
    @patch('requests.Session.get')
    def test_make_request(self, mock_get):
        """
        Test the _make_request method.
        """
        mock_response = MagicMock()
        mock_get.return_value = mock_response
        
        url = "https://example.com"
        params = {"param1": "value1"}
        
        with patch('time.sleep'):  # Skip the sleep delay for testing
            response = self.collector._make_request(url, params)
        
        mock_get.assert_called_once_with(url, params=params)
        self.assertEqual(response, mock_response)
    
    @patch('pandas.DataFrame.to_csv')
    def test_collect_race_calendar(self, mock_to_csv):
        """
        Test the collect_race_calendar method.
        """
        df = self.collector.collect_race_calendar(2020, save=True)
        
        self.assertIsInstance(df, pd.DataFrame)
        mock_to_csv.assert_called_once()
    
    @patch('pandas.DataFrame.to_csv')
    def test_collect_race_results(self, mock_to_csv):
        """
        Test the collect_race_results method.
        """
        df = self.collector.collect_race_results(2020, save=True)
        
        self.assertIsInstance(df, pd.DataFrame)
        mock_to_csv.assert_called_once()
    
    @patch('pandas.DataFrame.to_csv')
    def test_collect_horse_data(self, mock_to_csv):
        """
        Test the collect_horse_data method.
        """
        df = self.collector.collect_horse_data(2020, save=True)
        
        self.assertIsInstance(df, pd.DataFrame)
        mock_to_csv.assert_called_once()
    
    @patch('pandas.DataFrame.to_csv')
    def test_collect_track_condition_data(self, mock_to_csv):
        """
        Test the collect_track_condition_data method.
        """
        df = self.collector.collect_track_condition_data(2020, save=True)
        
        self.assertIsInstance(df, pd.DataFrame)
        mock_to_csv.assert_called_once()
    
    @patch('src.data_collection.jra_collector.JRADataCollector.collect_race_calendar')
    @patch('src.data_collection.jra_collector.JRADataCollector.collect_race_results')
    def test_collect_all_data(self, mock_collect_race_results, mock_collect_race_calendar):
        """
        Test the collect_all_data method.
        """
        mock_collect_race_calendar.return_value = pd.DataFrame()
        mock_collect_race_results.return_value = pd.DataFrame()
        
        data_types = ["race_calendar", "race_results"]
        all_data = self.collector.collect_all_data(data_types=data_types)
        
        self.assertIsInstance(all_data, dict)
        self.assertEqual(set(all_data.keys()), set(data_types))
        
        # Check that the collect methods were called for each year
        self.assertEqual(mock_collect_race_calendar.call_count, 2)  # 2020 and 2021
        self.assertEqual(mock_collect_race_results.call_count, 2)  # 2020 and 2021
    
    @patch('json.dump')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('os.listdir')
    def test_export_data_summary(self, mock_listdir, mock_open, mock_json_dump):
        """
        Test the export_data_summary method.
        """
        mock_listdir.return_value = [
            "race_calendar_2020.csv",
            "race_results_2020.csv",
            "horse_data_2020.csv",
            "track_condition_2020.csv",
        ]
        
        self.collector.export_data_summary()
        
        mock_open.assert_called_once()
        mock_json_dump.assert_called_once()


if __name__ == '__main__':
    unittest.main()


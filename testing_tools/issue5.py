import pytest
from unittest.mock import patch
from testing_tools import what_is_year_now
import io


@pytest.mark.parametrize('date, exp', [
    ('{"currentDateTime": "2001-03-01"}', 2001),
    ('{"currentDateTime": "01.03.9999"}', 9999),
])
def test_all(date, exp):
    date_io = io.StringIO(date)
    with patch('urllib.request.urlopen') as mock:
        mock.return_value.__enter__.return_value = date_io
        res = what_is_year_now.what_is_year_now()
    assert res == exp


def test_wrong_format():
    date = '{"currentDateTime": "2001.03.01"}'
    date_io = io.StringIO(date)
    with patch('urllib.request.urlopen') as mock:
        mock.return_value.__enter__.return_value = date_io
        with pytest.raises(ValueError):
            what_is_year_now.what_is_year_now()
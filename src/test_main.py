import os
import sys
import pytest
from unittest.mock import patch

# Ensure that the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from main import main

@pytest.fixture
def mock_display_header():
    with patch('main.display_header') as mock:
        yield mock

@pytest.fixture
def mock_update_contract_content():
    with patch('main.update_contract_content') as mock:
        yield mock

@pytest.fixture
def mock_input():
    with patch('builtins.input', side_effect=[
        "contract_test",   # contract_name
        "Service Provider",# service_provider_name
        "Client",          # client_name
        "1000.0",          # service_fee
        "100.0",           # hourly_rate
        "30"               # estimated_days
    ]) as mock:
        yield mock

def test_main(mock_display_header, mock_update_contract_content, mock_input):
    main()

    # Check that display_header was called once
    mock_display_header.assert_called_once()

    # Check that update_contract_content was called once with the correct arguments
    mock_update_contract_content.assert_called_once_with(
        "Service Provider",
        "Client",
        1000.0,
        30,
        "contract_test",
        100.0
    )

    # Check that input was called the expected number of times
    assert mock_input.call_count == 6
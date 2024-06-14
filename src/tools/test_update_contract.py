import os
import pytest
from datetime import datetime
from unittest.mock import patch, mock_open, MagicMock
from update_contract import update_contract_content

@pytest.fixture
def mock_datetime_now():
    with patch('update_contract.datetime') as mock_date:
        mock_date.now.return_value = datetime(2024, 1, 1)
        mock_date.strptime = datetime.strptime
        yield mock_date

@pytest.fixture
def mock_open_file():
    mock = mock_open(read_data="Contract Template with {Execution_Date} and other placeholders")
    with patch('builtins.open', mock):
        yield mock

@pytest.fixture
def mock_os_system():
    with patch('os.system') as mock:
        yield mock

@pytest.fixture
def mock_os_makedirs():
    with patch('os.makedirs') as mock:
        yield mock

@pytest.fixture
def mock_fpdf():
    with patch('update_contract.FPDF') as mock:
        mock_instance = mock.return_value
        mock_instance.add_page = MagicMock()
        mock_instance.set_font = MagicMock()
        mock_instance.multi_cell = MagicMock()
        mock_instance.output = MagicMock()
        yield mock

def test_update_contract_content(mock_datetime_now, mock_open_file, mock_os_system, mock_os_makedirs, mock_fpdf):
    # Call the function
    service_provider_name = "Service Provider"
    client_name = "Client"
    service_fee = 1000.0
    estimated_days = 30
    contract_name = "contract_test"
    hourly_rate = 100.0

    update_contract_content(service_provider_name, client_name, service_fee, estimated_days, contract_name, hourly_rate)

    # Check that the file was read
    mock_open_file.assert_called_once_with(os.path.join("src", "templates", "demo-service-agreement.txt"), "r", encoding="utf-8")

    # Check that the PDF was created correctly
    mock_fpdf().add_page.assert_called_once()
    mock_fpdf().set_font.assert_called_once_with("Arial", size=11)
    mock_fpdf().multi_cell.assert_called_once()

    # Check that the PDF was saved to the correct path
    output_path = os.path.join("src", "output", f"{contract_name}.pdf")
    mock_fpdf().output.assert_called_once_with(output_path)

    # Check that the directory was created
    mock_os_makedirs.assert_called_once_with(os.path.join("src", "output"), exist_ok=True)

    # Check that the system call to open the PDF was made
    mock_os_system.assert_called_once_with(f"open {output_path}")

    # Validate that the correct substitutions were made in the contract text passed to FPDF
    expected_text = (
        "Contract Template with 2024-01-01 and other placeholders"
        .replace("{Execution_Date}", "2024-01-01")
        .replace("{Post_Deployment_End_Date}", "2029-12-31")
        .replace("{Service_Provider_Name}", service_provider_name)
        .replace("{Client_Name}", client_name)
        .replace("{Service_Fee}", "{:.2f}".format(service_fee))
        .replace("{Upfront_Fee}", "{:.2f}".format(service_fee * 0.5))
        .replace("{Development_Fee}", "{:.2f}".format(service_fee * 0.5))
        .replace("{Estimated_Days_for_Completion}", str(estimated_days))
        .replace("{Hourly_Rate}", "{:.2f}".format(hourly_rate))
    )

    # Check the content passed to multi_cell
    written_content = mock_fpdf().multi_cell.call_args[0][2]
    assert written_content == expected_text.encode('utf-8').decode('latin1')
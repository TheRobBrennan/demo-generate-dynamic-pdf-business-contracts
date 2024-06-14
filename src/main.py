# Inspired by Caden Chen's Medium article 
# https://medium.com/pythoneers/generate-a-custom-business-contract-in-just-10-seconds-with-this-python-script-963bdc64280f

from tools.display_header import display_header
from tools.update_contract import update_contract_content

def main():
    display_header()

    # Ask user for input
    contract_name = input("Enter the Contract Name / File Name (No Spacing): ")
    service_provider_name = input("Enter the Service Provider Name: ")
    client_name = input("Enter the Client Name: ")
    service_fee = float(input("Enter the Service Fee (USD): "))
    hourly_rate = float(input("Enter the Hourly Rate (USD): "))
    estimated_days = int(input("Enter the Estimated Days for Completion: "))

    # Call the function to update and generate the contract
    update_contract_content(service_provider_name, client_name, service_fee, estimated_days, contract_name, hourly_rate)

if __name__ == "__main__":  # pragma: no cover
    main()
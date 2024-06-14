# Inspired by Caden Chen's Medium article 
# https://medium.com/pythoneers/generate-a-custom-business-contract-in-just-10-seconds-with-this-python-script-963bdc64280f

import os
from fpdf import FPDF
from datetime import datetime, timedelta

def display_header():
    # Generate your own ASCII art at https://patorjk.com/software/taag/
    header = """
    
    
    

   /$$$$$$            /$$                               /$$            /$$$$$$  /$$$$$$
 /$$__  $$          | $$                              | $$           /$$__  $$|_  $$_/
| $$  \__/  /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$     | $$  \ $$  | $$  
|  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$_____/| $$__  $$    | $$$$$$$$  | $$  
 \____  $$| $$  \ $$| $$| $$  \ $$| $$  \ $$|  $$$$$$ | $$  \ $$    | $$__  $$  | $$  
 /$$  \ $$| $$  | $$| $$| $$  | $$| $$  | $$ \____  $$| $$  | $$    | $$  | $$  | $$  
|  $$$$$$/| $$$$$$$/| $$|  $$$$$$/|  $$$$$$/ /$$$$$$$/| $$  | $$ /$$| $$  | $$ /$$$$$$
 \______/ | $$____/ |__/ \______/  \______/ |_______/ |__/  |__/|__/|__/  |__/|______/
          | $$                                                                        
          | $$                                                                        
          |__/                                                                                                                                                                

     
    
    

     
    """
    print(header)

def update_contract_content(service_provider_name, client_name, service_fee, estimated_days, contract_name, hourly_rate):
    # Get today's date
    execution_date = datetime.now().strftime("%Y-%m-%d")

    # Calculate deployment end date
    deployment_end_date = datetime.strptime(execution_date, "%Y-%m-%d") + timedelta(days=5*365)

    # Use relative path to load the template
    template_path = os.path.join("src", "templates", "demo-service-agreement.txt")
    with open(template_path, "r", encoding="utf-8") as file:
        contract_text = file.read()

    # Replace placeholders with user input and calculated dates
    updated_contract_text = contract_text.replace("{Execution_Date}", execution_date)
    updated_contract_text = updated_contract_text.replace("{Post_Deployment_End_Date}", deployment_end_date.strftime("%Y-%m-%d"))
    updated_contract_text = updated_contract_text.replace("{Service_Provider_Name}", service_provider_name)
    updated_contract_text = updated_contract_text.replace("{Client_Name}", client_name)
    updated_contract_text = updated_contract_text.replace("{Service_Fee}", "{:.2f}".format(service_fee))
    updated_contract_text = updated_contract_text.replace("{Upfront_Fee}", "{:.2f}".format(upfront_fee))
    updated_contract_text = updated_contract_text.replace("{Development_Fee}", "{:.2f}".format(development_fee))
    updated_contract_text = updated_contract_text.replace("{Estimated_Days_for_Completion}", str(estimated_days))
    updated_contract_text = updated_contract_text.replace("{Hourly_Rate}", "{:.2f}".format(hourly_rate))

    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font for the text
    pdf.set_font("Arial", size=11)

    # Add the updated contract text to the PDF
    pdf.multi_cell(0, 6, updated_contract_text.encode('utf-8').decode('latin1'))  # Encode as UTF-8 and decode as latin1

    # Use relative path for output
    output_dir = os.path.join("src", "output")
    os.makedirs(output_dir, exist_ok=True)
    pdf_output_path = os.path.join(output_dir, f"{contract_name}.pdf")
    pdf.output(pdf_output_path)

    print(f"Contract updated successfully and saved as {pdf_output_path}!")

    # Automatically open the generated PDF file
    os.system(f"open {pdf_output_path}")

if __name__ == "__main__":

    display_header()

    # Ask user for input
    contract_name = input("Enter the Contract Name / File Name (No Spacing): ")
    service_provider_name = input("Enter the Service Provider Name: ")
    client_name = input("Enter the Client Name: ")
    service_fee = float(input("Enter the Service Fee (USD): "))
    hourly_rate = float(input("Enter the Hourly Rate (USD): "))
    upfront_fee = service_fee * 0.5
    development_fee = service_fee * 0.5
    estimated_days = int(input("Enter the Estimated Days for Completion: "))

    # Call the function to update and generate the contract
    update_contract_content(service_provider_name, client_name, service_fee, estimated_days, contract_name, hourly_rate)
import os
from fpdf import FPDF
from datetime import datetime, timedelta

def update_contract_content(service_provider_name, client_name, service_fee, estimated_days, contract_name, hourly_rate):
    # Get today's date
    execution_date = datetime.now().strftime("%Y-%m-%d")

    # Calculate deployment end date
    deployment_end_date = datetime.strptime(execution_date, "%Y-%m-%d") + timedelta(days=5*365)

    # Calculate upfront fee and development fee
    upfront_fee = service_fee * 0.5
    development_fee = service_fee * 0.5

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
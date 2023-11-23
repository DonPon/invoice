import fpdf
import datetime
import yaml
import os

#names = ["FRANCISCO SANCHEZ GALEANA", "MARIA PEREZ", "JUAN GONZALEZ"]



def create_pdf(subject, text, month, name):
    # Create a new PDF document.
    pdf = fpdf.FPDF()

    # Set slightly larger margins
    pdf.set_margins(left=30, top=20, right=30)

    # Add a new page.
    pdf.add_page()

    # Set font for title
    pdf.set_font('Arial', 'B', 20)

    # Add the title text
    pdf.cell(0, 8, 'RECIBO', align='C')

    # Add a newline
    pdf.ln(20)

    # Reset font for body text
    pdf.set_font('Arial', '', 14)

    # Add the subject text
    pdf.multi_cell(0, 8, subject, align='R')

    # Add a newline
    pdf.ln(20)

    # Add the body text
    pdf.multi_cell(0, 8, text, align='J')

    # Add 5 new lines
    for i in range(7):
        pdf.ln(8)

    # Draw a signature line
    pdf.set_line_width(0.4)
    pdf.line(pdf.get_x() + 30, pdf.get_y(), pdf.get_x() + 120, pdf.get_y())

    # Add a newline
    pdf.ln(1)

    # Add signature text
    pdf.set_font('Arial', '', 14)
    pdf.multi_cell(0, 8, f'SRA. GABRIELA SEGURA\nLEYVA', align='C')

    # Save the document.
    # Specify the folder path
    folder_path = "C:/Users/4PF26LA_RS5/Desktop/Recibos/"
    # Check if the folder exists
    if not os.path.exists(folder_path):
        # Create the folder if it doesn't exist
        os.makedirs(folder_path)

    filename = f"C:/Users/4PF26LA_RS5/Desktop/Recibos/Recibo_{month.upper()}_{name}.pdf"
    pdf.output(filename)


# Get the month from the user.
month = input("ENTER THE MONTH: ")

# Open the YAML file
with open("tenants.yaml") as f:
    tenants = yaml.load(f, Loader=yaml.FullLoader)

# Get the current year
current_year = datetime.datetime.now().year

# Iterate over the tenants and generate PDFs
for tenant_name, tenant_data in tenants.items():
    # Extract tenant information from the YAML data
    day = tenant_data["day"]
    price = tenant_data["price"]
    price_letters = tenant_data["price_letters"]
    servicios = tenant_data["servicios"]
    local = tenant_data["local"]

    # Generate the PDF content
    subject = f"CDMX, a {day} de {month}\nde {current_year}"
    text = f"Recibí de parte del SR. {tenant_name}, la cantidad de ${price} ({price_letters.upper()} PESOS 00/100 M.N.), por concepto de {servicios} del local {local}, del inmueble ubicado en Calle Noche de Paz # 14 Colonia Granjas Navidad, Delegación Cuajimalpa, C.P. 05219, correspondiente al mes de {month.upper()} de {current_year}."

    # Create and save the PDF
    create_pdf(subject, text, month, tenant_name)


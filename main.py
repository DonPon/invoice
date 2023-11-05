import os
import jinja2
import pdfkit


def replace_text_in_pdf(input_docx_path, output_pdf_path, context):
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template(input_docx_path)
    output_text = template.render(context)
    print(output_text)

    # Specify the correct path to wkhtmltopdf.exe
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files (x86)/wkhtmltopdf/bin/wkhtmltopdf.exe')

    # Convert the HTML content to PDF
    pdfkit.from_string(output_text, output_pdf_path, configuration=config)



if __name__ == '__main__':

    # List of names and their corresponding Word document files
    # names = ['Francisco_Galeana', 'Irwing_Pena', 'Jose_Antonio_Hurtado']
    names = ['Jose_Antonio_Hurtado']
    month = input('Escribe el mes: ')

    for name in names:
        input_docx_path = f'pdf_templates/Recibo_{name}_4.html'
        output_pdf_path = f'C:/Users/4PF26LA_RS5/Desktop/Recibo_{month.upper()}_{name}_edited.pdf'

        context = {'_mes_': month, '_MES_': month.upper()}


        replace_text_in_pdf(input_docx_path, output_pdf_path, context)

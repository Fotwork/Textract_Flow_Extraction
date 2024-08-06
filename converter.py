import os
from pdf2image import convert_from_path

# Path to the folder containing the PDF files
pdf_folder = 'Data/real_images/Weird_invoices'
# Path to the output folder for the images
output_folder = 'Data/Weird_invoices_images'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to convert PDF to images
def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image_file = os.path.join(output_folder, f"{os.path.basename(pdf_path).replace('.pdf', '')}_page_{i+1}.png")
        image.save(image_file, 'PNG')
        print(f"Saved: {image_file}")

# Main function
def main():
    # Convert all PDF files to images
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            convert_pdf_to_images(pdf_path, output_folder)

    print("Conversion completed.")

if __name__ == '__main__':
    main()
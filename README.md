# OCR Evaluation

This project uses AWS Textract to extract text from images stored in an S3 bucket and visualizes the OCR performance distribution based on the normalized Levenshtein distance of product names extracted from invoices.

## Prerequisites

1. **Boto3**: The AWS SDK for Python. Install it using pip:

    ```bash
    pip install boto3
    ```

2. **Pandas**: Install pandas for data manipulation:

    ```bash
    pip install pandas
    ```

3. **Matplotlib**: Install matplotlib for plotting:

    ```bash
    pip install matplotlib
    ```

4. **AWS Account**: Ensure you have an AWS account.
5. **AWS CLI**: Install and configure the AWS CLI.

### Configuring the AWS CLI

**Run the AWS Configure Command**

   Open a terminal or command prompt and enter the following command:

   ```bash
   aws configure

## Configuration

1. **S3 Bucket Name**: Specify the name of your S3 bucket by modifying the following line in the script:

    ```python
    s3_bucket_name = 'textract-intern'  # Replace 'textract-intern' with your bucket name
    ```

2. **Folders**: Specify the folders you want to process by modifying the following line in the script:

    ```python
    folders = ['Weird_invoices']  # Replace 'Weird_invoices' with the names of the folders you want to process
    ```

3. **Product Database Path**: Specify the path to your product database by modifying the following line in the script:

    ```python
    file_path = 'Data/real_images/Products.xlsm'  # Replace with your actual file path
    ```

4. **Sheet Name**: Specify the sheet name of your database by modifying the following line in the script:

    ```python
    sheet_name = 'Base_de_Donnees'  # Replace with your actual sheet name
    ```

5. **Total Number of Products**: Specify the total number of products in your invoices by modifying the following line in the script:

    ```python
    total_products_count = 1600  # Replace with the actual total number of products
    ```
    
## Using the PDF to Image Converter

To convert PDF files to images before processing them with AWS Textract, follow these steps:

1. **Ensure Prerequisites are Met**:
    - Install the required library `pdf2image`:

      pip install pdf2image

    - Additionally, you need to install Poppler:
      - **For Windows**: Download the Poppler binaries from this link: http://blog.alivate.com.au/poppler-windows/, extract the contents, and add the `bin` folder to your system's PATH.
      - **For macOS**: Install Poppler via Homebrew:

        brew install poppler

      - **For Linux**: Install Poppler using your package manager:

        sudo apt-get install poppler-utils

2. **Specify Paths in the Script**:
    - Open the `coverter.py` script and specify the paths:

    ```python
    # Path to the folder containing the PDF files
    pdf_folder = 'Data/real_images/Weird_invoices'
    # Path to the output folder for the images
    output_folder = 'Data/Weird_invoices_images'
    ```

3. **Run the Script**:

      python converter.py

    - The script will convert all PDF files in the specified `pdf_folder` to images and save them in the `output_folder`.

By following these steps, you can convert PDF files to images, which can then be processed using AWS Textract for OCR and further analysis.
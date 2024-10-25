# CHIAQADownloader

CHIAQADownloader is a Python tool designed to download all PDF documents from the CHIA (Center for Health Information and Analysis) question and answer sessions and merge them into a single PDF file. This project aims to simplify access to important CHIA presentations by aggregating them for easier review.

## Features

- Downloads all relevant PDF files from specified CHIA web pages.
- Merges downloaded PDFs into one consolidated PDF document.
- Saves the PDFs in a dedicated directory for organization.

## Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `BeautifulSoup4`
  - `PyPDF2`

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 PyPDF2
```
## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.

```bash
git clone <repository-url>
cd CHIAQADownloader
```

## Usage

## Step 1: Download PDFs
Run the scraper.py script to download the PDFs:
```bash
python scraper.py
```

This script will create a directory named chiafiles and download all PDF files into it from the following pages:

- [CHIA Data User Workgroup Information](https://www.chiamass.gov/chia-data-user-workgroup-information/)
- [Previous CHIA Data User Workgroup Presentations](https://www.chiamass.gov/previous-chia-data-user-workgroup-presentations/)

## Step 2: Merge PDFs
After downloading the PDFs, run the mergepdf.py script to merge them into a single PDF:

```bash
python mergepdf.py
```

The merged PDF will be saved as combined.pdf in the project directory.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the LICENSE file for more details.

## Acknowledgments

- BeautifulSoup for HTML parsing.
- PyPDF2 for PDF manipulation.











# PubMed Scraper

## Overview
PubMed Scraper is a Python-based command-line tool that fetches articles from PubMed using the Entrez API. It retrieves articles based on a user-defined search query and provides details such as the PMID, title, publication date, author affiliations, and contact emails. The results can be saved as a CSV file or displayed in the terminal.

## Installation

### Prerequisites
Ensure you have Python 3.13 or later installed.

### Setup
1. Clone the repository:
   git clone <repository-url>
   cd pubmed_scraper

2. Install Poetry:
   curl -sSL https://install.python-poetry.org | python3 -
   
3. Verify Poetry installation:
   poetry --version

4. Install dependencies:
   poetry lock
   poetry install

5. To fetch PubMed articles, run:
   poetry run get-papers-list "search query" 


# Usage

### Running the Script
To fetch PubMed articles, run:
poetry run get-papers-list "search query" 


Optional arguments:
- `-d` or `--debug`: Enable debug mode for detailed logs.
- `-f filename.csv` or `--file filename.csv`: Save results to a CSV file instead of printing to the terminal.

Example:
poetry run get-papers-list "cancer" -d -f cancer.csv


## Files and Functionalities

### 1. `main.py`
- Entry point for the program.
- Parses command-line arguments.
- Calls `fetch_pubmed_articles` and processes results.

### 2. `fetcher.py`
- Handles API requests to the PubMed Entrez API.
- Retrieves PMIDs and fetches article details in XML format.
- Calls `parse_pubmed_articles` to extract relevant data.

### 3. `parser.py`
- Parses XML responses.
- Extracts article metadata (PMID, title, publication date, author affiliations, emails).
- Filters non-academic and company-affiliated authors.

### 4. `utils.py`
- Saves fetched articles to a CSV file.
- Prints articles in a formatted structure.

## Dependencies
- `requests` (>=2.32.3,<3.0.0) – For making HTTP requests to the PubMed API.
- `xml.etree.ElementTree` – For parsing XML responses.

## Important Links
### 1️⃣ PubMed API (Entrez E-utilities)
- [API Documentation](https://www.ncbi.nlm.nih.gov/books/NBK25500/)
- [E-utilities Overview](https://www.ncbi.nlm.nih.gov/books/NBK25499/)
- [Search API (esearch.fcgi)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi)
- [Fetch API (efetch.fcgi)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi)

### 2️⃣ Poetry (Dependency Management)
- [Official Poetry Documentation](https://python-poetry.org/docs/)
- [Installing Poetry](https://python-poetry.org/docs/#installation)
- [Managing Dependencies](https://python-poetry.org/docs/dependency-specification/)
- [Pyproject.toml Guide](https://python-poetry.org/docs/pyproject/)

### 3️⃣ Requests Library (Used for API Calls)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [How to Use Requests](https://realpython.com/python-requests/)

### 4️⃣ XML Parsing (ElementTree)
- [Python XML Parsing with ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)

## License
This project is licensed under the MIT License.

## Author
- **Vamsi Mohan Krishna**
  - Email: mohanvamsikrishna0828@gmail.com


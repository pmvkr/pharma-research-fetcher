import requests
import xml.etree.ElementTree as ET
from pubmed_scraper.parser import parse_pubmed_articles

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_pubmed_articles(query, max_results=50, debug=False):
    """Fetch PubMed articles from NCBI using Entrez API."""
    if debug:
        print(f"Searching PubMed for: {query}")

    search_url = f"{BASE_URL}/esearch.fcgi"
    fetch_url = f"{BASE_URL}/efetch.fcgi"

    # Search for PMIDs
    search_params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": max_results}
    response = requests.get(search_url, params=search_params).json()
    pmids = response.get("esearchresult", {}).get("idlist", [])

    if not pmids:
        print("No results found.")
        return []

    if debug:
        print(f"Found {len(pmids)} articles.")

    # Fetch details
    fetch_params = {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"}
    root = ET.fromstring(requests.get(fetch_url, params=fetch_params).text)

    return parse_pubmed_articles(root)

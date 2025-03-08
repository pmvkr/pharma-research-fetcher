import re
import xml.etree.ElementTree as ET

def get_text(element, path, default="Unknown"):
    """Extracts text from XML with a default fallback."""
    node = element.find(path)
    return node.text.strip() if node is not None and node.text else default

def parse_pubmed_articles(root):
    """Parses PubMed XML and extracts article details."""
    articles = []

    for article in root.findall(".//PubmedArticle"):
        pmid = get_text(article, ".//PMID")
        title = get_text(article, ".//ArticleTitle", "No Title Available")
        pub_date = " ".join(filter(None, [get_text(article, f".//PubDate/{tag}", "") for tag in ["Day", "Month", "Year"]]))

        non_academic, company_affiliations, emails = set(), set(), set()
        for author in article.findall(".//Author"):
            name = " ".join(filter(None, [get_text(author, "ForeName", ""), get_text(author, "LastName", "")]))
            affiliation = get_text(author, "AffiliationInfo/Affiliation", "").lower()

            if any(word in affiliation for word in ["pharma", "biotech", "inc", "ltd", "gmbh", "corporation"]):
                company_affiliations.add(name)
            if "university" not in affiliation and "institute" not in affiliation:
                non_academic.add(name)

            email_match = re.search(r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}", affiliation)
            if email_match:
                emails.add(email_match.group())

        articles.append([pmid, title, pub_date, ", ".join(non_academic) or "None",
                         ", ".join(company_affiliations) or "None", ", ".join(emails) or "Not Available"])

    return articles

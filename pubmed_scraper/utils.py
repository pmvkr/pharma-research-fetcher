import csv

def save_to_csv(filename, articles):
    """Save articles to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["PMID", "Title", "Publication Date", "Non-Academic Authors", "Company Affiliations", "Emails"])
        writer.writerows(articles)
    print(f"Results saved to {filename}")

def print_articles(articles):
    """Print articles in a readable format."""
    for article in articles:
        print(f"\nPMID: {article[0]}\nTitle: {article[1]}\nPublication Date: {article[2]}")
        print(f"Non-Academic Authors: {article[3]}\nCompany Affiliations: {article[4]}\nEmails: {article[5]}")
        print("-" * 80)

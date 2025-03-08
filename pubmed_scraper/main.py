import argparse
from pubmed_scraper.fetcher import fetch_pubmed_articles
from pubmed_scraper.utils import save_to_csv, print_articles

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed articles based on a search query.")
    parser.add_argument("query", help="Search query for PubMed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument("-f", "--file", help="Specify the output filename for saving results.")
    args = parser.parse_args()

    articles = fetch_pubmed_articles(args.query, debug=args.debug)

    if articles:
        save_to_csv(args.file, articles) if args.file else print_articles(articles)

if __name__ == "__main__":
    main()

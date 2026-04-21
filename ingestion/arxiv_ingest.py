import requests
import feedparser
from db.connect import SessionLocal
from db.tables import Author, Category, Paper
from datetime import datetime

# Fetch data from arxiv 
def fetch_arxiv_data(category='cs.AI', max_results=20):
    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}+OR+cat:cs.LG&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"
    response = requests.get(url)

    feed = feedparser.parse(response.text) 

    return feed.entries

# Store data in PostgreSQL

def store_in_db(entries):
    db = SessionLocal()

    for entry in entries:
        exists = db.query(Paper).filter(Paper.arxiv_id == entry.id).first()
        if exists:
            print(f"Paper with arXiv ID {entry.id} already exists. Skipping.")
            continue

        author_objs = []
        for author in entry.authors:
            name = author.name.strip()

            existing_author = db.query(Author).filter_by(name=name).first()
            if not existing_author:
                existing_author = Author(name=name)
                db.add(existing_author)
                db.flush()

            author_objs.append(existing_author)

        category_objs = []
        if hasattr(entry, 'tags'):
            for tag in entry.tags:
                cat_name = tag['term']

                existing_cat = db.query(Category).filter_by(name=cat_name).first()
                if not existing_cat:
                    existing_cat = Category(name=cat_name)
                    db.add(existing_cat)
                    db.flush()

                category_objs.append(existing_cat)


        # Exract data   
        paper = Paper(                                                                                                                                                                                                        
                arxiv_id=entry.id,
                title=entry.title,
                abstract=entry.summary,
                publication_date= parse_date(entry.published),
                pdf_url=entry.link
            )

        paper.authors = author_objs
        paper.categories = category_objs   

        db.add(paper)

    db.commit()
    db.close()


# Parse Date
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None

if __name__ == "__main__":
    print("Fetching data from arXiv...")
    entries = fetch_arxiv_data()
    print(f"Fetched {len(entries)} entries. Storing in database...")
    store_in_db(entries)
    print("Data ingestion complete.")



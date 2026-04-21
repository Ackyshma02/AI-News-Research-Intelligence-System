from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from db.connect import Base
from datetime import datetime


# Papers Table
class Paper(Base):
    __tablename__ = 'papers'
    
    id = Column(Integer, primary_key=True, index=True) # internal id
    arxiv_id = Column(String, unique=True, index=True) # arXiv ID
    title = Column(Text)
    abstract = Column(Text)

    publication_date = Column(DateTime)
    pdf_url = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    chunks = relationship("Chunk", back_populates="paper")
    authors = relationship("Author", secondary="paper_authors", backref="papers")
    categories = relationship("Category", secondary="paper_categories", backref="papers")


# Author Table
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)


# Paper-Author Relationship
class PaperAuthor(Base):
    __tablename__ = 'paper_authors'

    paper_id = Column(Integer, ForeignKey('papers.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'), primary_key=True)


# Category Table
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)


# Paper-Category Relationship
class PaperCategory(Base):
    __tablename__ = 'paper_categories'

    paper_id = Column(Integer, ForeignKey('papers.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)


# Chunks Table
class Chunk(Base):
    __tablename__ = 'chunks'
    
    id = Column(Integer, primary_key=True, index=True)
    paper_id = Column(Integer, ForeignKey('papers.id'))
    content = Column(Text)  # The actual text content of the chunk


    chunk_index = Column(Integer)  # To maintain order of chunks
    section = Column(String)  # e.g., Introduction, Methods, results, etc.
    token_count = Column(Integer)  # Number of tokens in the chunk
    
    
    # Relationships
    paper = relationship("Paper", back_populates="chunks")
    embedding = relationship("Embedding", uselist=False, back_populates="chunk")



# Embeddings Table
class Embedding(Base):
    __tablename__ = 'embeddings'
    
    id = Column(Integer, primary_key=True, index=True)
    chunk_id = Column(Integer, ForeignKey('chunks.id'))
    embedding_vector = Column(Text)  # Store as JSON string or use a separate table for vectors
    
    # Relationships
    chunk = relationship("Chunk", back_populates="embedding")



# Paper Insights Table
class PaperInsight(Base):
    __tablename__ = 'paper_insights'
    
    id = Column(Integer, primary_key=True, index=True)
    paper_id = Column(Integer, ForeignKey('papers.id'))

    summary= Column(Text)
    keywords = Column(Text)  
    methods = Column(Text)
    results = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
    

#Relations Table
class Relation(Base):
    __tablename__ = 'relations'
    
    id = Column(Integer, primary_key=True, index=True)
    paper_id = Column(Integer, ForeignKey('papers.id'))
    related_paper_id = Column(Integer, ForeignKey('papers.id'))

    score = Column(Float) #To indicate strength of relation 


# Ingestion State Table
class IngestionState(Base):
    __tablename__ = 'ingestion_state'

    id = Column(Integer, primary_key=True)
    last_ingested_at = Column(DateTime)
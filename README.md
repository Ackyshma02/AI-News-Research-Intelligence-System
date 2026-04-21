# AI News & Research Intelligence System

> 🚧 **Work in Progress** – This project is actively being developed as part of an AI/ML research-focused pipeline.

## 📌 Overview

This project aims to build an **AI-powered system for ingesting, storing, and processing research papers** (primarily from arXiv).
The long-term goal is to enable **semantic search, retrieval, and intelligent question-answering** over research documents using modern AI techniques.

## 🎯 Objectives

* Automate ingestion of research papers from arXiv
* Store structured metadata and content in a database
* Enable downstream AI tasks such as:

  * Semantic search
  * Document understanding
  * Retrieval-Augmented Generation (RAG)

## 🚧 Project Status

### ✅ Completed

* Database connection module
* Database schema design (`tables.py`)
* Script to initialize database (`create_tables.py`)
* arXiv ingestion pipeline (`arxiv_ingest.py`)

### 🔄 In Progress

* Data preprocessing and cleaning
* Error handling and pipeline robustness
* Integration with ML/AI models

### 📌 Planned

* Embedding generation (vector databases)
* Semantic search functionality
* RAG-based question answering system
* API development (FastAPI/Flask)
* Frontend interface (optional)

---

## 📂 Project Structure

AI_INSIGHTS/
│
├── db/
│   ├── __init__.py
│   ├── connect.py        # Handles database connection
│   ├── tables.py         # Defines database schema
│
├── ingestion/
│   ├── arxiv_ingest.py   # Fetches and processes arXiv papers
│
├── create_tables.py      # Initializes database tables


## ▶️ Running the Project

### Step 1: Initialize Database

```bash
python create_tables.py
```

### Step 2: Run Ingestion Pipeline

```bash
python ingestion/arxiv_ingest.py
```


## ⚠️ Notes

* This project is under active development and may change frequently
* Some modules are experimental and not fully optimized
* Error handling and scalability improvements are ongoing

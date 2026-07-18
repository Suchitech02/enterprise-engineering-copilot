# Enterprise Engineering Copilot

Enterprise Engineering Copilot is an AI-powered engineering assistant designed to help engineers build, modernize, and troubleshoot enterprise data platforms.

## Vision

Instead of acting as a generic chatbot, Enterprise Engineering Copilot understands enterprise engineering concepts including:

- Databricks
- Apache Spark
- Delta Live Tables
- Medallion Architecture
- Azure Data Factory migration
- REST API ingestion
- PySpark
- SQL
- Enterprise Lakehouse Patterns

The assistant is being built incrementally using modern AI engineering practices including Retrieval-Augmented Generation (RAG), structured outputs, and agentic workflows.

## Current Status

🚧 In Development

## Planned Features

- Natural language → Databricks SQL
- PySpark code generation
- Spark error analysis
- Delta Live Tables generation
- Medallion Architecture recommendations
- Enterprise RAG
- ADF → Databricks migration assistant
- Multi-agent engineering workflows

## Tech Stack

- Python
- FastAPI
- Streamlit
- OpenAI API
- ChromaDB
- LangGraph (planned)
- Docker
- GitHub Actions

## Roadmap

- [x] Project initialization
- [ ] FastAPI backend
- [ ] Streamlit frontend
- [ ] OpenAI integration
- [ ] SQL Generator
- [ ] PySpark Generator
- [ ] RAG
- [ ] Multi-agent system

## Development

Start the development server:

```bash
make dev
```

Run tests:

```bash
make test
```

Run linting:

```bash
make lint
```

Format the code:

```bash
make format
```

## Running with Docker

### Build

```bash
docker build -t enterprise-engineering-copilot .
```

### Run

```bash
docker run -p 8000:8000 enterprise-engineering-copilot
```

Open:

```
http://localhost:8000/docs
```
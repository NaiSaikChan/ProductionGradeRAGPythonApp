# Production Grade RAG Python App

A production-ready Retrieval-Augmented Generation (RAG) application built with Python, designed for scalable document processing and intelligent question answering.

## Features

- **Document Processing**: Support for multiple file formats (PDF, TXT, DOCX)
- **Vector Database Integration**: Efficient document embedding and retrieval
- **LLM Integration**: Compatible with popular language models
- **API Endpoints**: RESTful API for easy integration
- **Monitoring & Logging**: Comprehensive logging and metrics
- **Docker Support**: Containerized deployment ready

## Prerequisites

- Python 3.8+
- Docker (optional)
- OpenAI API key or other LLM provider credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ProductionGradeRAGPythonApp.git
cd ProductionGradeRAGPythonApp
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

### Local Development
```bash
python app.py
```

### Inngest Deployment
```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```

### Streamlit Interface
```bash
uv run streamlit run streamlit_app.py --server.port 8501
```

### FastAPI Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Qdrant Vector DB
```bash
docker run -d --name qdrantRAG -p 6333:6333 -v "D:/QdrantDB:/qdrant/storage" qdrant/qdrant:latest
```

### Docker Deployment
```bash
docker build -t rag-app .
docker run -p 8000:8000 rag-app
```


## API Endpoints

- `POST /upload` - Upload documents
- `POST /query` - Submit questions
- `GET /health` - Health check

## Configuration

Configure the application through environment variables or `config.py`:

- `OPENAI_API_KEY`: Your OpenAI API key
- `VECTOR_DB_URL`: Vector database connection string
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
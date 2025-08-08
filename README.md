# 🚀 Aarini - RAG-Powered Question Answering App

A smart AI-powered question answering system leveraging Retrieval-Augmented Generation (RAG) to deliver precise and context-rich answers._

---

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24-orange.svg)
![Docker](https://img.shields.io/badge/Docker-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-purple.svg)
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-yellow.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub--Actions-blue.svg)
---

## ✨ Features

- 🧠 Generate embeddings with OpenAI's `text-embedding-ada-002`.
- 🔍 Fast semantic search using Pinecone vector database.
- 📝 Contextual prompt augmentation for better answer generation.
- 🤖 Detailed answer generation with OpenAI GPT-3.5.
- ⚡ FastAPI backend serving intelligent query responses.
- 🎨 Streamlit frontend for smooth and interactive user experience.
- 🐳 Dockerized deployment with AWS ECR & ECS.
- 🔄 Automated CI/CD via GitHub Actions.

---

##🏗️ Architecture Overview

1. User inputs question in the Streamlit UI.
2. FastAPI backend generates an embedding vector via OpenAI.
3. Pinecone performs vector similarity search to find relevant documents.
4. Retrieved context is embedded into a prompt.
5. Prompt is sent to OpenAI GPT for a detailed answer.
6. The answer is sent back to the frontend and displayed to the user.

---

## 🛠️ Tech Stack
| Technology      | Description                           |
|-----------------|-----------------------------------|
| Python 3.11     | Core programming language          |
| FastAPI         | Backend API framework              |
| Streamlit       | Frontend UI framework              |
| OpenAI API      | Embeddings and language generation |
| Pinecone        | Vector similarity search database  |
| Docker          | Containerization                   |
| AWS ECR & ECS   | Container registry & deployment    |
| GitHub Actions  | CI/CD automation                   |

## 🚀 Setup & Usage
### Prerequisites

- Docker installed  
- AWS account with ECR/ECS setup  
- OpenAI API key  
- Pinecone API key  

### Environment Variables

Create a `.env` file with:

```bash
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
ECR_REPOSITORY_NAME=your_ecr_repo_name
```
---

### Running Locally (Without Docker)

```bash
pip install -r requirements.txt
uvicorn api:app --host 0.0.0.0 --port 8000
streamlit run Streamlit_main.py --server.port=8501

```

---

## 🚀 Docker Usage

```bash
docker build -t aarini-app .
docker run -p 8000:8000 -p 8501:8501 aarini-app
```
---

## 🥪 CI/CD Pipeline

Triggered on pushes to main branch.
Runs linting and unit tests.
Builds and pushes Docker image to AWS ECR.
Deploys container to ECS or self-hosted runner.
Cleans up old Docker images to save space.

---

## Project Structure
```bash
/backend/                # Core backend modules (embeddings, prompt augmentation, data loading, etc.)
api.py                  # FastAPI application entrypoint
Streamlit_main.py       # Streamlit frontend UI
Dockerfile              # Docker build instructions
start.sh                # Script to run backend + frontend
main.yaml               # GitHub Actions workflow configuration
requirements.txt        # Python dependencies
.env.example            # Sample environment variables file
README.md               # Project documentation
```
---


## 📝 License

MIT License

---


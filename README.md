# StudyMate AI

StudyMate AI is a simple university study assistant built with Python, the Strands Agents SDK, Ollama, and Amazon S3.

It helps students find information in their lecture notes by asking questions in simple English.

## Features

- Answers study questions using a local AI model.
- Retrieves lecture notes from a private Amazon S3 bucket.
- Searches notes for relevant information.
- Reports when the notes do not contain matching information.
- Includes automated tests for the search tool.

## Technologies

- Python
- Strands Agents SDK
- Ollama with Qwen 2.5 3B
- Amazon S3
- Boto3

## How It Works

1. A student asks StudyMate a question.
2. The AI agent calls the `search_notes` tool when the question concerns lecture notes.
3. The tool retrieves `notes.txt` from Amazon S3.
4. The tool searches for relevant lines and returns them to the agent.
5. The agent generates an answer based on the retrieved information.

## Requirements

- Python
- Ollama
- AWS CLI or another supported way to configure AWS credentials
- An AWS account with access to the configured S3 bucket
- The `qwen2.5:3b` Ollama model

## Setup

### 1. Download the project

Clone this repository or download its source code.

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Prepare the local AI model

Install Ollama, then run:

```powershell
ollama pull qwen2.5:3b
```

Make sure Ollama is running before starting StudyMate.

### 5. Configure AWS access

Configure AWS credentials using a supported AWS authentication method.

The configured AWS identity must have permission to read the required S3 object.

Check `search_notes.py` and confirm that `BUCKET_NAME`, `FILE_NAME`, and `AWS_REGION` match your AWS setup.

### 6. Run StudyMate

```powershell
python agent.py
```

Enter a question when prompted.

## Run Tests

```powershell
python test_studymate.py
```

The tests check a matching question, a vague question, and a question with no matching information.

## Current Limitations

- Search uses keyword matching rather than semantic search.
- Answers depend on the content available in the configured notes file.
- An internet connection and valid AWS access are needed to retrieve notes from S3.
- The AI model runs locally through Ollama.

## Security

- Keep AWS credentials and secret keys out of the repository.
- Use a private S3 bucket and grant only the permissions required.
- Do not upload private lecture materials without permission.

## Project Status

Version 1: Basic AI study assistant with Amazon S3 lecture-note retrieval.

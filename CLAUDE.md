# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Run from repository root. Requires Python 3.12; root dependencies are declared in `requirements.txt`.

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

# Build/load persistent Chroma vector store from docs/*.txt
python ingestion_pipeline.py

# Current app entry point (prints Hello World)
python app.py

# Start optional Docker development services
 docker compose -f .docker/compose.yaml up -d
# Run ingestion in container
 docker exec -it python_pg python ingestion_pipeline.py
```

Set `OPENROUTER_API_KEY` in local environment or `.env` before running ingestion; `python-dotenv` loads `.env`. Embeddings use OpenRouter endpoint `https://openrouter.ai/api/v1` and model `openai/text-embedding-3-small`. Do not commit `.env`.

No test suite, test configuration, linter, or build configuration is currently defined. If pytest is installed and tests are added, run all with `python -m pytest`; run one test with `python -m pytest path/to/test_file.py::test_name`.

## Architecture

This is a Python RAG tutorial project using LangChain, OpenAI embeddings/chat models, and Chroma.

- Root `ingestion_pipeline.py` is the main implemented pipeline: load top-level `docs/*.txt`, split into character chunks, embed with `text-embedding-3-small`, and persist a cosine-similarity Chroma store under `db/chroma_db`. If that directory already exists, ingestion reuses it instead of rebuilding it.
- Root `app.py` is only a placeholder; it does not yet query the vector store or generate answers.
- `dev/reference/` contains tutorial/example implementations for retrieval, answer generation, chat history, and advanced RAG strategies. Treat these as learning references, not as modules imported by the root application.
- `.docker/compose.yaml` starts a Python development container and a PostgreSQL/pgvector service. The current root pipeline uses local Chroma and does not connect to PostgreSQL; the Python container remains idle until commands are run with `docker compose exec`.

The README currently contains only a project title. Note: `.gitignore` excludes `docs/` and `dev/`; local changes under those directories are not tracked unless ignore rules change.

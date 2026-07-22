# Eminem Lyrics GPT — Live API

A character-level GPT language model, **built and trained from scratch in PyTorch**, trained on Eminem lyrics and deployed as a containerized REST API.

**Live demo:** https://eminem-lyrics-api.onrender.com/docs

> Note: hosted on a free tier that sleeps after inactivity — the first request may take ~50 seconds to wake up, then responds normally.

## What this is

I implemented a GPT-style transformer from the ground up — no high-level model libraries — following the architecture from *Attention Is All You Need*, then trained it on a corpus of Eminem lyrics to generate new verses. The trained model is served over HTTP through a FastAPI application, packaged with Docker, and deployed to Render via GitHub.

## Try it

Open the [interactive docs](https://eminem-lyrics-api.onrender.com/docs), expand `POST /generate`, click **Try it out**, and send:

​```json
{"prompt": "started from", "max_tokens": 100}
​```

Or from the terminal:

​```bash
curl -X POST https://eminem-lyrics-api.onrender.com/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "started from", "max_tokens": 100}'
​```

## Model architecture

Implemented from scratch: token + positional embeddings, multi-head self-attention, feed-forward layers, residual connections, and layer normalization.

| Parameter | Value |
|---|---|
| Type | Character-level GPT |
| Layers | 6 |
| Attention heads | 8 |
| Embedding dim | 128 |
| Context length (block size) | 128 |
| Vocabulary | 34 characters |
| Final validation loss | ~1.52 |
| Training hardware | Apple M4 (MPS) |

## Tech stack

- **PyTorch** — model implementation and training
- **FastAPI + Pydantic** — API layer with request validation
- **Uvicorn** — ASGI server
- **Docker** — containerization (slim CPU-only image)
- **Render** — cloud hosting with auto-deploy from GitHub

## API endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/generate` | Generate text from a prompt |

`POST /generate` accepts a JSON body with `prompt` (string) and `max_tokens` (integer, 1–500).

## Running locally

​```bash
# with Docker
docker build -t eminem-gpt .
docker run -p 8000:8000 eminem-gpt

# then open http://localhost:8000/docs
​```
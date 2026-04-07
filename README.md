# Learn LangChain

This repository is a hands-on sandbox for learning LangChain and the surrounding GenAI concepts that matter in real applications. The codebase currently covers core areas such as chat models, prompts, embeddings, and conversational state. The goal should not be just to call an LLM API, but to understand how to design reliable, observable, and cost-aware GenAI systems.

## What You Should Learn To Become Good At GenAI With LangChain

### 1. Foundation Concepts

Before going deep into LangChain, be comfortable with these fundamentals:

- Python basics: functions, classes, virtual environments, file handling, JSON, APIs.
- LLM basics: tokens, context window, temperature, system vs user prompts, deterministic vs creative generation.
- Prompt engineering: clear instructions, constraints, examples, structured output.
- Embeddings: semantic similarity, vector representation, cosine similarity, retrieval.
- Chat applications: message history, role-based messages, state, memory.

### 2. LangChain Concepts You Should Master

- Models: how to use chat models and text generation models.
- Prompt templates: reusable prompts with variables and validation.
- Output handling: parsing model responses into reliable formats.
- Chains: combining prompts, models, and post-processing into workflows.
- Runnables: the modern LangChain pattern for composing steps.
- Message history: building multi-turn chat behavior.
- Embeddings and retrieval: semantic search and document similarity.
- Document loading and splitting: preparing external knowledge for retrieval.
- Vector stores: storing and querying embeddings efficiently.
- RAG: retrieval-augmented generation for grounded answers.
- Memory and state: preserving context across user interactions.
- Agents and tools: letting models call external functions or APIs.
- Observability: tracing, debugging, prompt inspection, latency and token usage.

### 3. GenAI Topics Related To LangChain That Are Equally Important

To become effective, LangChain alone is not enough. You should also understand:

- Model selection: OpenAI, Anthropic, Google, Hugging Face, local models.
- Cost and latency tradeoffs: smaller vs larger models, caching, batching.
- Evaluation: correctness, hallucination rate, groundedness, relevance, consistency.
- Guardrails: prompt injection risk, unsafe output, structured validation.
- Production design: retries, rate limits, error handling, secrets management.
- UX for GenAI apps: streaming, responsiveness, feedback, transparency.
- Retrieval quality: chunking strategy, embedding choice, reranking.
- Data privacy: what data is sent to hosted APIs and what should stay local.
- Deployment: APIs, Streamlit apps, background jobs, monitoring.

## Current Repository Coverage

This repository already includes learning examples in the following areas:

### Chat Models

- [chat-models/demo.py](chat-models/demo.py): basic `ChatOpenAI` invocation and temperature behavior.
- [chat-models/hf-demo.py](chat-models/hf-demo.py): Hugging Face hosted model experimentation.
- [chat-models/hf-demo-local.py](chat-models/hf-demo-local.py): local Hugging Face model usage.

### Prompts

- [prompt/prompt_generator.py](prompt/prompt_generator.py): creates and saves a `PromptTemplate` as JSON.
- [prompt/prompt_ui.py](prompt/prompt_ui.py): Streamlit UI that loads a saved prompt template and sends it to an LLM.
- [prompt/nobel_prize_prompt.json](prompt/nobel_prize_prompt.json): stored prompt definition.

### Embeddings

- [embeddings/openai_query.py](embeddings/openai_query.py): generate embeddings for a single query.
- [embeddings/openai_docs.py](embeddings/openai_docs.py): document embedding workflow.
- [embeddings/document_similarity.py](embeddings/document_similarity.py): semantic similarity using cosine similarity.
- [embeddings/hf_local.py](embeddings/hf_local.py): local embedding experimentation.

### Chatbot and Conversation State

- [chatbot/chatbot.py](chatbot/chatbot.py): simple chatbot pattern.
- [chatbot/chatbot_with_memeory.py](chatbot/chatbot_with_memeory.py): multi-turn chat using accumulated history.
- [chatbot/chat_prompt_template.py](chatbot/chat_prompt_template.py): prompt structure for chat applications.
- [chatbot/message_placeholder.py](chatbot/message_placeholder.py): working with message placeholders.
- [chatbot/messages.py](chatbot/messages.py): role-based chat message usage.

### LLM Basics and Python Recap

- [llms/demo.py](llms/demo.py): basic LLM usage.
- [recap](recap): Python recap files for foundational practice.

## Learning Path Recommended For This Repo

Follow this order instead of jumping randomly between examples:

1. Learn basic model invocation from [chat-models/demo.py](chat-models/demo.py).
2. Study prompt templates with [prompt/prompt_generator.py](prompt/prompt_generator.py) and [prompt/prompt_ui.py](prompt/prompt_ui.py).
3. Understand embeddings with [embeddings/openai_query.py](embeddings/openai_query.py) and [embeddings/document_similarity.py](embeddings/document_similarity.py).
4. Move to chat state and message handling in [chatbot/chatbot.py](chatbot/chatbot.py) and [chatbot/chatbot_with_memeory.py](chatbot/chatbot_with_memeory.py).
5. Compare hosted and local model usage in [chat-models/hf-demo.py](chat-models/hf-demo.py) and [chat-models/hf-demo-local.py](chat-models/hf-demo-local.py).
6. After that, build a small RAG project with document loading, chunking, embeddings, retrieval, and answer generation.

## Important Gaps To Cover Next

If your goal is to become strong in GenAI with LangChain, add these topics to this repository next:

- RAG pipeline with a vector store such as FAISS or Chroma.
- Document loaders for PDF, web pages, and text files.
- Text splitters and chunking strategies.
- Structured output parsing with JSON or Pydantic.
- LangChain Expression Language and runnables.
- LangSmith or equivalent tracing for debugging chains.
- Evaluation scripts for answer quality and retrieval quality.
- Tool calling and agent workflows.
- Streaming responses in the UI.
- Basic guardrails and validation for unsafe or malformed model output.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add the keys required by the examples you want to run. Typical variables include:

```env
OPENAI_API_KEY=your_key_here
HUGGINGFACEHUB_API_TOKEN=your_token_here
GOOGLE_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

## How To Run Examples

Run a Python script directly:

```bash
python chat-models/demo.py
python embeddings/document_similarity.py
python chatbot/chatbot_with_memeory.py
```

Run the Streamlit prompt app:

```bash
streamlit run prompt/prompt_ui.py
```

## Practical Advice

- Start simple and understand each abstraction before stacking more layers.
- Do not treat LangChain as magic; inspect prompts, messages, and model outputs.
- Compare different providers and models for the same task.
- Measure output quality, latency, and cost together.
- Build small end-to-end projects, not only isolated demos.
- Learn where plain Python is enough and where LangChain adds real value.

## Good End Goal Projects

Once you finish the basics in this repo, you should be able to build:

- A question-answering app over your own documents.
- A chatbot with conversation history and prompt templates.
- A semantic search tool using embeddings.
- A Streamlit-based GenAI assistant.
- A tool-using agent that can call APIs or search documents.

## Summary

To become good at GenAI with LangChain, focus on both sides:

- LangChain abstractions: prompts, models, chains, runnables, retrieval, agents.
- GenAI engineering: model behavior, evaluation, cost, latency, safety, and product design.

This repository already gives you a solid starting point. The next major milestone is to add RAG, structured output, evaluation, and observability so your learning moves from demos to real GenAI system design.

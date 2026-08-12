# Complete GenAI Interview Preparation Roadmap
## LLM · LangChain · LangGraph · RAG · Production Engineering
### v3.0 Final — 2–4 YOE, Service-Based Company Edition

---

## How to Use This File

1. Save the **Teaching Prompt** (next section) somewhere permanent — Claude Project, Notion, sticky note.
2. Work through topics in order. Each is a copy-paste block for the prompt's `{PASTE TOPIC HERE}` slot.
3. Do NOT skip prerequisites — each phase builds on the one before.
4. Topics marked `★ HIGH PRIORITY` are the most frequently asked in service-company interviews.
5. Topics marked `◆ RAG` are from the RAG handbook. Topics marked `◆ EXTRA` are beyond the standard handbooks but still get asked.

**Coverage:** LLM Fundamentals · Embeddings · Vector Databases · RAG (Basic → Expert) ·
LangChain Core · Agents · LangGraph · Multi-Agent Systems · Production Engineering ·
Fine-tuning Concepts · Cloud LLM Services · System Design · Responsible AI

---

## Teaching Prompt (Use This Every Time)

```
You are an expert AI/GenAI instructor, RAG architect, LangChain/LangGraph engineer,
and interview mentor. Your task is to teach AI application development concepts — covering
LLMs, Embeddings, Vector Databases, RAG systems, LangChain, LangGraph, and agentic AI —
in a way that prepares me for AI/backend interviews at service-based companies for
2–4 years of experience.

I want:
- Clear understanding from basics → advanced
- Interview-ready knowledge
- Short but powerful notes
- Real-world production perspective, especially from service-company project contexts
  (document Q&A systems, chatbots, enterprise RAG pipelines, AI agents)

---

STRICT TEACHING RULES
1. Start from absolute basics — no assumptions about prior knowledge on this topic
2. Move step-by-step from basics to advanced
3. Explain WHY before WHAT — motivation first, then mechanism
4. Use simple English first, then technical explanation
5. Use a real-world analogy to build intuition
6. Add architecture / flow diagrams using text arrows (e.g. Query → Embed → Search → Rerank → LLM → Answer)
7. Explain the internal working — how it actually works under the hood
8. Use comparison tables for related concepts (e.g. this vs that, old way vs new way)
9. Include real production use-cases that service companies actually build
10. Highlight the top common mistakes and pitfalls (especially the ones candidates get wrong in interviews)
11. Add 5–8 interview questions with crisp, confident answers
12. End with a quick revision summary (bullet points, max 10 lines)
13. End with one "Most Important Takeaway" sentence

---

OUTPUT FORMAT — use this structure every time, no exceptions:

### 1. Basic Understanding (Simple English + Analogy)
### 2. Technical Deep Dive
### 3. Internal Working / Architecture (with text diagram)
### 4. Real-World Example (service-company context)
### 5. Code Example (Python — current LangChain/LangGraph syntax where applicable)
### 6. Comparison Table (if applicable)
### 7. Common Mistakes & Pitfalls
### 8. Interview Questions & Answers (5–8 Q&As)
### 9. Quick Revision Summary (bullet points)
### 10. Most Important Takeaway

---

Topic to teach:
👉 {PASTE TOPIC HERE}
```

---

## PHASE 1 — LLM Foundations
**Why first:** You cannot understand LangChain, RAG, or agents without knowing how LLMs work.
**Timeline:** Week 1–2

---

### Topic 1
```
Python Type Hints & Async  ★ HIGH PRIORITY
Subtopics: type hints (typing module — List, Dict, Optional, Union, Tuple), Pydantic
BaseModel and Field (used everywhere in LangChain), async/await syntax, coroutines vs
threads vs processes, the Python event loop, asyncio.gather() for parallel async calls,
why async is mandatory in production LangChain/LangGraph code (non-blocking API calls),
common mistakes with sync code inside async functions
```

### Topic 2
```
How LLMs Work  ★ HIGH PRIORITY
Subtopics: transformer architecture overview (self-attention at a high level, why it
replaced RNNs), encoder vs decoder vs encoder-decoder models, what a language model
actually does (probability distribution over next tokens), autoregressive generation
(the next-token prediction loop), context window (what it is, why it has a limit),
what happens inside one API call end-to-end, difference between base model vs
instruction-tuned vs RLHF model
```

### Topic 3
```
Tokens & Tokenisation  ★ HIGH PRIORITY
Subtopics: what a token is (not a word — a subword unit), Byte Pair Encoding (BPE)
intuition, why "1 word ≠ 1 token" (special chars, spaces, non-English text), cost
implications (tokens = money), context limit = token limit, how to count tokens with
tiktoken, tokenisers across providers (OpenAI vs Anthropic vs open-source differ),
practical rule of thumb: 1 token ≈ 0.75 English words
```

### Topic 4
```
Temperature, Top-p, Top-k — Sampling Strategies
Subtopics: what sampling means in LLM generation, temperature (0 = greedy/deterministic,
high = random/creative), top-k (consider only top k tokens each step), top-p nucleus
sampling (consider tokens whose cumulative prob ≥ p), frequency_penalty and
presence_penalty, when to use temperature=0 (structured output, factual Q&A),
when to use high temperature (creative writing, brainstorming), combining these in
production prompts
```

### Topic 5
```
Prompt Engineering  ★ HIGH PRIORITY
Subtopics: anatomy of a good prompt (role, context, task, output format, constraints),
system prompt vs user message vs assistant turn, instruction clarity techniques
(be specific, use examples, specify format), output format control (JSON, markdown,
bullet points, XML tags), negative instructions ("do not..."), prompt iteration workflow,
why prompt engineering is a skill not a trick, common prompt anti-patterns
```

### Topic 6
```
Zero-Shot & Few-Shot Prompting  ★ HIGH PRIORITY
Subtopics: zero-shot (no examples, relies on instruction clarity), few-shot (provide
input-output examples to guide behavior), when to use each, how many examples work
best (3–8 typically), example selection strategy (diverse, representative, edge cases),
ordering of examples (latest/hardest last works well), role of examples in steering
output format not just content, few-shot vs fine-tuning trade-off
```

### Topic 7
```
Chain of Thought (CoT)
Subtopics: why LLMs make arithmetic/logic errors without CoT, step-by-step reasoning
prompting ("let's think step by step"), zero-shot CoT vs few-shot CoT, why CoT helps
(forces intermediate reasoning tokens), self-consistency (run CoT N times, take
majority vote), Tree of Thought (branching reasoning paths), when NOT to use CoT
(simple factual lookup, latency-critical paths)
```

### Topic 8
```
LLM APIs & Function Calling Internals  ★ HIGH PRIORITY
Subtopics: OpenAI API request/response structure (messages array, role/content format),
how to make a direct API call (before touching any framework), Anthropic API structure,
OpenAI Function Calling vs Tool Use (the difference), how the LLM "signals" it wants
to call a tool (the response format), tool call → tool result → LLM continues loop,
what LangChain actually wraps so you aren't flying blind, parallel tool calls
```

---

## PHASE 2 — Embeddings & Vector Search  ◆ RAG
**Why second:** Pre-requisite for everything in RAG. Without embeddings, RAG is magic words.
**Timeline:** Week 2–3

---

### Topic 9
```
What are Embeddings?  ★ HIGH PRIORITY  ◆ RAG
Subtopics: what an embedding is (a dense numerical vector representing meaning),
why similar meaning → similar vectors (the key insight), embedding space as a map of
meaning, cosine similarity (angle between vectors), dot product similarity, Euclidean
distance — which to use when, embedding dimensions (384, 768, 1536, 3072 — what they
mean, bigger ≠ always better), why embeddings enable semantic search (vs keyword
search), real-world analogy: embedding = GPS coordinates for meaning
```

### Topic 10
```
Embedding Models & Selection  ★ HIGH PRIORITY  ◆ RAG
Subtopics: OpenAI text-embedding-3-small vs text-embedding-3-large vs ada-002
(speed, cost, quality trade-offs), sentence-transformers (all-MiniLM-L6-v2,
all-mpnet-base-v2, bge-large-en-v1.5), HuggingFace MTEB leaderboard for choosing
models, bi-encoder architecture (query and doc embedded separately — fast but less
accurate), cross-encoder architecture (query+doc together — accurate but slow),
WHY you must use the same model for indexing and querying (critical interview question),
domain-specific embedding models (legal, medical, code)
```

### Topic 11
```
HNSW & ANN Algorithms — How Vector Search Works  ★ HIGH PRIORITY  ◆ RAG
Subtopics: why brute-force search over millions of vectors is too slow (O(N) problem),
Approximate Nearest Neighbour (ANN) — trade a little accuracy for huge speed gain,
HNSW (Hierarchical Navigable Small World) — the dominant algorithm: layer-based graph,
how HNSW builds and searches the graph (intuition), HNSW parameters (M, ef_construction,
ef_search) and what they control, IVF (Inverted File Index) — alternative approach,
FAISS and which index to choose (Flat, IVFFlat, HNSW), recall vs latency trade-off
```

### Topic 12
```
BM25 Algorithm — Sparse Retrieval  ★ HIGH PRIORITY  ◆ RAG
Subtopics: what BM25 is (a keyword-based ranking function, successor to TF-IDF),
TF-IDF intuition (term frequency × inverse document frequency), BM25 improvements
over TF-IDF (document length normalisation, saturation), why BM25 is still relevant
despite embeddings (exact keyword match, no training needed, fast), BM25 in Python
(rank_bm25 library), when sparse search beats dense search (rare terms, product codes,
proper nouns, IDs), BM25 as the "sparse" in hybrid search
```

### Topic 13
```
Vector Databases — Selection & Internals  ★ HIGH PRIORITY  ◆ RAG
Subtopics: what a vector database does (store + index + search vectors at scale),
FAISS (Meta, local, in-memory, no persistence — good for dev and learning),
Chroma (open-source, local, easy to use, persistent — good for prototypes),
Pinecone (managed cloud, serverless, production-ready, expensive),
Weaviate (open-source, hybrid search built-in, self-hosted or cloud),
Qdrant (open-source, Rust-based, fast, production-ready),
pgvector (Postgres extension — add vector search to your existing DB),
how to choose: dev vs prod, scale, hybrid search need, cost, team familiarity,
metadata filtering alongside vector search (how it works with pre-filtering vs post-filtering)
```

### Topic 14
```
LangChain Embeddings & VectorStore Integration  ★ HIGH PRIORITY
Subtopics: OpenAIEmbeddings and HuggingFaceEmbeddings in LangChain, embedding text
with .embed_query() and .embed_documents(), creating a Chroma vectorstore from documents,
FAISS vectorstore creation, adding documents, similarity_search(query, k=5),
similarity_search_with_score(), persisting a vectorstore to disk, loading it back,
from_documents() shortcut, end-to-end flow: raw text → chunk → embed → store → query
→ retrieve → pass to LLM
```

---

## PHASE 3 — RAG Fundamentals  ◆ RAG
**Why third:** Core of what service companies build and interview on. This phase alone covers 40% of interview questions.
**Timeline:** Week 3–5

---

### Topic 15
```
RAG Architecture End-to-End  ★ HIGH PRIORITY  ◆ RAG
Subtopics: what RAG is and why it exists (LLMs have knowledge cutoff + hallucination +
no private data access), the two pipelines: Ingestion Pipeline (offline: load → chunk →
embed → store) vs Query Pipeline (online: query → embed → retrieve → rerank → prompt
→ LLM → answer), end-to-end text diagram of both pipelines, naive RAG vs advanced RAG
vs modular RAG, where RAG fits in enterprise AI architecture, what RAG does NOT solve
(hallucination on retrieved content, bad chunking, wrong retrieval)
```

### Topic 16
```
Document Ingestion Pipeline  ★ HIGH PRIORITY  ◆ RAG
Subtopics: the full offline pipeline in detail: Document Source → Loader → Cleaner →
Chunker → Embedder → Vector DB, handling multiple document formats (PDF, DOCX, HTML,
CSV, code), text cleaning (remove headers/footers, fix encoding, strip HTML tags),
document metadata (filename, page number, section, date — preserved through the pipeline),
deduplication (why and how to detect duplicate or near-duplicate documents),
batch embedding optimisation (embed in batches not one-by-one), incremental updates
(adding new docs to an existing index without rebuilding from scratch)
```

### Topic 17
```
Document Loaders & Text Splitters in LangChain  ★ HIGH PRIORITY
Subtopics: LangChain document loaders (PyPDFLoader, WebBaseLoader, CSVLoader,
TextLoader, UnstructuredFileLoader, DirectoryLoader), the Document object
(page_content + metadata), RecursiveCharacterTextSplitter (most important — how it
tries paragraph → sentence → word → character splits), CharacterTextSplitter,
TokenTextSplitter (split by token count — best for LLM context management),
SemanticChunker (embeds sentences, splits at meaning shifts), chunk_size and
chunk_overlap explained with numbers, practical tuning: larger chunks = more context
but less precise retrieval, smaller chunks = precise but may lose context
```

### Topic 18
```
Chunking Strategies & Trade-offs  ★ HIGH PRIORITY  ◆ RAG
Subtopics: WHY chunking matters (LLM has a context limit, retrieval needs focused chunks),
fixed-size chunking (simple, fast, loses context at boundaries — the bad default),
recursive character chunking (respects document structure: paragraphs first, then
sentences, then words), semantic chunking (detect topic shifts by embedding similarity —
most accurate, slowest), sentence-window chunking (chunk per sentence, but retrieve
surrounding window), parent-child chunking (small chunks for retrieval accuracy +
return large parent chunks for context — best of both worlds), late chunking,
document structure-aware chunking (use headings/sections), chunk_size rule of thumb
by document type: legal=512, technical=256, FAQ=128
```

### Topic 19
```
Metadata Filtering  ★ HIGH PRIORITY  ◆ RAG
Subtopics: what metadata filtering is (filter by attributes before/alongside vector
search), why metadata filtering is critical in enterprise RAG (filter by department,
date, document type, user permissions, language), pre-filtering vs post-filtering vs
in-query filtering, how to attach metadata when ingesting documents, metadata filtering
in Chroma (where clause), in Pinecone (filter dict), in Weaviate (GraphQL filter),
SelfQueryRetriever in LangChain (LLM generates the metadata filter from natural
language query), real-world example: "Show only HR policy docs from 2024"
```

### Topic 20
```
Hybrid Search — Dense + Sparse + RRF  ★ HIGH PRIORITY  ◆ RAG
Subtopics: why neither pure semantic search nor pure keyword search is enough,
dense retrieval (embedding-based — good for semantic/conceptual queries),
sparse retrieval (BM25 keyword-based — good for exact terms, product codes, names),
hybrid = combine both, Reciprocal Rank Fusion (RRF) — how it merges ranked lists
from multiple retrievers (formula: score = Σ 1/(k + rank_i)), why RRF is better than
score averaging (no score normalisation needed), EnsembleRetriever in LangChain
(weights for each retriever), Weaviate built-in hybrid search, when hybrid is
significantly better than pure dense (product search, legal search, technical docs)
```

### Topic 21
```
Retriever Types in LangChain  ★ HIGH PRIORITY
Subtopics: VectorStoreRetriever (basic — similarity_search wrapper, with k and search_type),
MultiQueryRetriever (generates N rephrased queries, retrieves for each, deduplicates —
reduces single-query bias), ContextualCompressionRetriever (wraps any retriever, then
compresses/filters retrieved docs using an LLM or compressor — only return relevant
parts), EnsembleRetriever (hybrid search — combine multiple retrievers with weights),
ParentDocumentRetriever (stores small chunks, but retrieves and returns their large
parent chunk — best for precision + context), SelfQueryRetriever (LLM converts
natural language query to filter + semantic query automatically),
when to use each: simple → VectorStore, quality → MultiQuery + Rerank,
structured data → SelfQuery, precision + context → ParentDocument
```

### Topic 22
```
Reranking with Cross-Encoders  ★ HIGH PRIORITY  ◆ RAG
Subtopics: why initial vector retrieval ranking is imperfect (bi-encoder trades speed
for accuracy), cross-encoder: takes (query, doc) pair together → more accurate relevance
score but O(k) inference calls, the standard pipeline: retrieve top-20 → rerank →
return top-5 to LLM, Cohere Rerank API in LangChain (CohereRerank), BGE reranker
(local, free), FlashrankRerank (lightweight, fast, local), ContextualCompressionRetriever
+ CohereRerank combination, typical parameters: retrieve_k=20, top_n=5,
latency vs accuracy trade-off in reranking, when reranking is worth the extra latency
```

### Topic 23
```
Prompt Engineering for RAG  ★ HIGH PRIORITY  ◆ RAG
Subtopics: how RAG prompts differ from general prompts (must inject retrieved context),
standard RAG prompt template structure (system role + context block + question),
instructing the LLM to answer ONLY from context (groundedness), handling no-answer
case ("I don't know" instruction), citation instructions in prompt ("reference the
source"), context placement (put context before question — better attention),
prompt compression (remove irrelevant parts of context before injecting), RAG-specific
prompt pitfalls, LangChain RAG prompt templates (hub.pull("rlm/rag-prompt")),
create_retrieval_chain() and create_stuff_documents_chain()
```

### Topic 24
```
Conversational RAG (Chat History + Retrieval)  ★ HIGH PRIORITY
Subtopics: the problem — user says "what did it say about that?" and the retriever has
no context for "that", solution: history-aware retrieval (rephrase question using chat
history BEFORE retrieval), create_history_aware_retriever() in LangChain, the two-step
pipeline: (1) reformulate query using history → (2) retrieve with reformulated query
→ (3) generate answer with history + retrieved context, storing chat history (in-memory
vs database), managing history length (trim or summarise old turns), end-to-end
conversational RAG chain, real-world example: enterprise document Q&A chatbot
```

### Topic 25
```
Context Window Management in RAG  ★ HIGH PRIORITY  ◆ RAG
Subtopics: the challenge — retrieved chunks + chat history + system prompt must all fit
within the LLM's context window, how to budget tokens (assign max tokens per component),
truncation strategies (cut oldest history first, cut least-relevant chunks), map-reduce
for very long context (split, process each, combine results), stuff vs map-reduce vs
refine strategies for document processing, context stuffing pitfalls (too many chunks
→ "lost in the middle"), LLM context window comparison (GPT-4o: 128K, Claude: 200K,
Gemini: 1M — does bigger always help?), tiktoken for counting tokens before calling LLM
```

### Topic 26
```
RAG Evaluation — RAGAS Deep Dive  ★ HIGH PRIORITY  ◆ RAG
Subtopics: why evaluating RAG is hard (no single correct answer), RAGAS framework
introduction, the 4 core RAGAS metrics:
  (1) Faithfulness — is the answer supported by the retrieved context? (0–1)
  (2) Answer Relevancy — does the answer address the user's question? (0–1)
  (3) Context Precision — are retrieved chunks relevant to the question? (0–1)
  (4) Context Recall — were all the necessary chunks retrieved? (0–1),
how RAGAS uses an LLM to compute these scores, building an evaluation dataset
(question + ground truth + context + answer), LLM-as-judge evaluation pattern,
running RAGAS with LangSmith integration, what scores to target in production,
common evaluation pitfalls, end-to-end evaluation pipeline setup
```

---

## PHASE 4 — Advanced RAG  ◆ RAG
**Why fourth:** Differentiates mid-level from senior candidates. Service companies building real RAG products ask these.
**Timeline:** Week 5–7

---

### Topic 27
```
Query Transformation — HyDE & Multi-Query  ★ HIGH PRIORITY  ◆ RAG
Subtopics: the problem — user queries are often vague, short, or use different vocabulary
than documents, MultiQueryRetriever (generate 3–5 rephrased versions of the query,
retrieve for each, deduplicate results — covers query ambiguity), HyDE — Hypothetical
Document Embeddings (generate a fake "ideal answer" to the query, embed THAT, search
for similar real docs — bridges vocabulary gap), step-back prompting (abstract the
question to a more general one, retrieve for that, then answer the specific), query
decomposition (break complex multi-part question into sub-questions, answer each,
combine), RAG Fusion (multi-query + RRF), when each technique helps vs adds latency
```

### Topic 28
```
RAG Failure Modes & Debugging  ★ HIGH PRIORITY  ◆ RAG
Subtopics: the 3 layers where RAG fails — (1) Retrieval failures, (2) Generation
failures, (3) Pipeline failures. Retrieval failures: wrong chunks retrieved (bad chunking,
wrong embedding model, no reranking), missing chunks (poor recall — need hybrid search),
irrelevant chunks returned (no metadata filtering). Generation failures: LLM ignores
retrieved context, LLM adds information not in context (hallucination), answer too long
or too short. Pipeline failures: embedding model mismatch, stale index, slow latency.
Debugging checklist for each layer. How to diagnose with LangSmith traces. The top 10
mistakes candidates make when describing RAG in interviews (from the handbook).
```

### Topic 29
```
Lost-in-the-Middle Problem  ◆ RAG
Subtopics: research finding — LLMs pay more attention to content at the START and END
of the context, content in the MIDDLE is underweighted (especially beyond 20 chunks),
why this matters for RAG (the most relevant chunk might be ranked 5th in the context),
mitigation strategies: (1) reranking first, then place most relevant at start/end,
(2) reduce number of retrieved chunks (top-3 not top-20), (3) use LLMs with better
long-context handling, (4) map-reduce instead of stuffing, experimental evidence,
how to test for this issue in your RAG system
```

### Topic 30
```
Parent-Child & Hierarchical Chunking  ◆ RAG
Subtopics: the core trade-off — small chunks = precise retrieval but lack context,
large chunks = rich context but imprecise retrieval, parent-child solution: index small
child chunks for retrieval, return their large parent chunk to the LLM,
ParentDocumentRetriever in LangChain implementation step by step, hierarchical chunking
(paragraph → sentence levels, retrieve sentence, return paragraph),
document summary indexing (index a summary of each document + chunks, retrieve at
both levels), when parent-child significantly outperforms flat chunking (long structured
documents, reports, legal docs, technical manuals)
```

### Topic 31
```
Contextual Retrieval — Anthropic's Approach  ◆ RAG
Subtopics: the problem — chunks lose context when extracted (e.g. "the company
reported revenue of $X" without knowing WHICH company), Anthropic's solution: for each
chunk, prepend a short LLM-generated context explaining its role in the document,
then embed the enriched chunk, contextual BM25 + contextual embeddings combined,
why this reduces retrieval failure rate significantly, cost consideration (need to call
LLM per chunk during ingestion), implementation approach, when it's worth the extra
cost vs simple chunking
```

### Topic 32
```
RAG vs Long Context LLMs  ★ HIGH PRIORITY  ◆ RAG
Subtopics: long context LLMs (GPT-4o 128K, Claude 200K, Gemini 1M) — can you just
stuff the whole document? When long context replaces RAG (small doc collection,
real-time updates, latency not critical), when RAG still wins (massive document corpus,
cost efficiency at scale, precise attribution, latency budget constraints), the "lost
in the middle" problem with long context, cost comparison: RAG vs long context at
scale (token cost math), hybrid approach (use RAG for retrieval, long context for
final generation), interview-ready decision framework: which to use when
```

### Topic 33
```
Agentic RAG & Tool Use in RAG  ◆ RAG
Subtopics: what makes RAG "agentic" (agent decides WHEN and HOW to retrieve, not
a fixed pipeline), routing agent (decide which retriever/knowledge base to query),
iterative retrieval (retrieve → answer partial → retrieve more if needed),
CRAG — Corrective RAG (evaluate retrieved docs, fall back to web search if poor),
Self-RAG (LLM generates retrieval tokens to decide when to retrieve),
tool-calling RAG (retriever as a tool in a ReAct agent loop),
LangGraph RAG agent implementation, when agentic RAG is worth the added complexity
vs a simple fixed RAG pipeline
```

### Topic 34
```
GraphRAG  ◆ RAG
Subtopics: limitation of standard RAG (misses relationships and connections between
documents), what a knowledge graph is (nodes = entities, edges = relationships),
GraphRAG by Microsoft — build a knowledge graph from documents, traverse the graph
during retrieval, local vs global search in GraphRAG (entity-level vs community-level),
LlamaIndex PropertyGraphIndex, Neo4j integration with LangChain, when GraphRAG
outperforms standard RAG (multi-hop questions, relationship-heavy domains like legal,
medical, financial), implementation complexity and cost trade-offs
```

### Topic 35
```
RAG for Tabular Data & SQL  ◆ RAG
Subtopics: the problem — standard RAG fails on structured/tabular data (embedding a
CSV row is not meaningful), approaches: (1) Text-to-SQL (LLM generates SQL from
natural language question — query the actual database), (2) Table Q&A (embed table
as text, use LLM to reason over it), (3) Pandas agent (LLM writes Python/pandas code),
LangChain create_sql_query_chain() and SQLDatabaseChain, SQLDatabase tool in agents,
nl2sql pitfalls (schema awareness, ambiguity, security — SQL injection via prompt),
combining SQL agent + vector RAG for hybrid enterprise data
```

### Topic 36
```
Multi-Modal RAG  ◆ RAG
Subtopics: what multi-modal RAG handles (PDFs with images, charts, diagrams, tables,
scanned documents), approaches: (1) image captioning then embed captions,
(2) multi-modal embeddings (CLIP, nomic-embed-vision — embed image and text in same
space), (3) multi-modal LLM for both retrieval and generation (GPT-4V, Claude Vision),
LlamaIndex multi-modal index, handling PDFs with figures (pdfplumber, unstructured.io),
OCR integration (Tesseract, AWS Textract) for scanned documents,
limitations and when multi-modal RAG is vs is not worth the complexity
```

### Topic 37
```
RAG Latency Optimization  ★ HIGH PRIORITY  ◆ RAG
Subtopics: measuring RAG latency (P50, P95 per component: embed query, vector search,
rerank, LLM call), where latency comes from in each component, optimization strategies:
(1) query embedding caching, (2) async retrieval (retrieve from multiple sources in
parallel), (3) reduce k (fewer retrieved chunks), (4) skip reranking for simple queries,
(5) use a fast/cheap LLM for routing and slow/expensive for final answer,
(6) streaming LLM response to user while other processing happens,
latency budget design (assign ms budgets to each component), SLA targets for
production RAG (aim for < 3s end-to-end for document Q&A)
```

### Topic 38
```
RAG Monitoring & Observability  ★ HIGH PRIORITY  ◆ RAG
Subtopics: what to monitor in production RAG (retrieval quality, answer quality,
latency, cost, errors), LangSmith tracing for RAG pipeline visibility, metrics to
track: retrieval hit rate, RAGAS scores over time, latency per component, cost per
query, error rates, user feedback signals (thumbs up/down), alerting on quality
degradation, logging for debugging (log query, retrieved chunks, final prompt, answer),
OpenTelemetry integration, Langfuse as alternative to LangSmith, stale index detection
(when vector DB is out of sync with source documents)
```

### Topic 39
```
RAG Security — Multi-Tenant Architecture & Prompt Injection  ★ HIGH PRIORITY  ◆ RAG
Subtopics: multi-tenant RAG challenge (users from different organizations/roles must
not see each other's data), isolation strategies: (1) separate vectorstore per tenant
(simplest but expensive), (2) shared vectorstore with strict metadata filtering by
tenant_id (efficient but filtering must be enforced), (3) namespace per tenant in
Pinecone/Qdrant, RBAC (Role-Based Access Control) in RAG (filter docs by user role),
prompt injection attacks in RAG (malicious content in retrieved docs that hijacks LLM),
indirect prompt injection (document contains "ignore previous instructions..."),
defenses: input sanitization, output validation, privilege separation, trust levels
```

### Topic 40
```
Faithfulness, Source Citation & Hallucination Control in RAG  ★ HIGH PRIORITY  ◆ RAG
Subtopics: RAG reduces but does NOT eliminate hallucination (LLM can still ignore
context or add to it), faithfulness = answer is fully supported by retrieved context,
techniques to improve faithfulness: (1) explicit "only answer from context" instruction,
(2) structured output with citations (force LLM to quote source), (3) faithfulness
scoring with RAGAS, (4) NLI-based post-generation check (Natural Language Inference:
does the context entail the answer?), source citation implementation in LangChain
(cite Document metadata: source, page), displaying citations in UI (with links),
evaluating citation accuracy, hallucination rate as a production KPI
```

### Topic 41
```
RAG Cost Optimization & Semantic Caching  ◆ RAG
Subtopics: where RAG costs come from (embedding API, LLM API, vector DB hosting,
reranker API), cost per query math (how to calculate at scale), optimization strategies:
(1) use cheaper embedding model for high-volume, (2) semantic caching — cache LLM
responses for semantically similar queries (not just exact match), Redis + vector
similarity for semantic cache, GPTCache library, (3) batch embeddings during ingestion
(not one at a time), (4) model routing (cheap LLM for simple queries, expensive for
complex), (5) reduce k (each extra retrieved chunk = extra tokens = extra cost),
GDPR and data retention in RAG (PII in documents, right to be forgotten = index update)
```

---

## PHASE 5 — LangChain Core
**Why fifth:** Now you understand what LangChain is abstracting. You'll learn it with full context.
**Timeline:** Week 7–8

---

### Topic 42
```
ChatModels vs LLMs  ★ HIGH PRIORITY
Subtopics: legacy LLM class (string in → string out), ChatModel class (message list in
→ AIMessage out), message types: SystemMessage, HumanMessage, AIMessage,
ToolMessage, FunctionMessage, why ChatModel is the modern standard (all frontier
models use chat format), ChatOpenAI, ChatAnthropic, ChatGoogleGenerativeAI —
initialisation patterns, model parameter (gpt-4o, claude-3-5-sonnet-20241022),
temperature, max_tokens, invoking with .invoke(), .stream(), .batch()
```

### Topic 43
```
PromptTemplates  ★ HIGH PRIORITY
Subtopics: ChatPromptTemplate.from_messages() (list of tuples or message objects),
variable placeholders with {variable_name}, FewShotChatMessagePromptTemplate
(structured few-shot examples), FewShotPromptTemplate (legacy but still asked),
example selectors: SemanticSimilarityExampleSelector, LengthBasedExampleSelector,
partial prompt templates (pre-fill some variables), MessagesPlaceholder (dynamically
inject conversation history), format_messages() and format(), hub.pull() for
community prompts
```

### Topic 44
```
Output Parsers & Structured Output  ★ HIGH PRIORITY
Subtopics: StrOutputParser (simplest — just gets the text content), JsonOutputParser
(parse JSON output — fragile if LLM doesn't follow format), PydanticOutputParser
(define a Pydantic schema, get a validated Python object), format_instructions
(inject schema description into prompt), with_structured_output() — the modern
preferred approach (uses function calling / tool use internally — much more reliable),
designing Pydantic schemas for structured LLM output, handling parsing failures with
OutputFixingParser, when to use with_structured_output vs output parsers
```

### Topic 45
```
LCEL — Pipe Operator & Runnables  ★ HIGH PRIORITY (MUST KNOW)
Subtopics: what LCEL is and why it was created (composability, streaming, async, batch
all built-in), the pipe operator syntax: chain = prompt | llm | parser,
how the | operator chains Runnables, the Runnable interface (all LangChain components
implement it: invoke, stream, batch, ainvoke, astream, abatch),
invoke() for single call, stream() for token streaming, batch() for parallel calls,
the config object (callbacks, tags, metadata), why LCEL replaced LLMChain
(deprecated), composability: chain1 | chain2 | chain3 is still one Runnable
```

### Topic 46
```
Runnables Deep Dive  ★ HIGH PRIORITY
Subtopics: RunnableParallel (run multiple sub-chains simultaneously, merge into a dict
output — use for retrieving from multiple sources in parallel),
RunnablePassthrough (pass input through unchanged — used to inject original question
alongside retrieved context with {"context": retriever, "question": RunnablePassthrough()}),
RunnableLambda (wrap ANY Python function as a Runnable — custom preprocessing/postprocessing),
RunnableBranch (conditional routing — route to different chains based on a condition),
RunnableWithMessageHistory (attach memory/history to any chain without modifying it),
itemgetter() for extracting dict keys, combining multiple Runnables in complex chains
```

### Topic 47
```
with_retry & Fallbacks
Subtopics: why retries are necessary (API rate limits, transient network failures,
LLM service outages), .with_retry() on any Runnable (stop_after_attempt,
wait_exponential_jitter, retry_if_exception_type), .with_fallbacks() for model fallback
(primary: gpt-4o, fallback: gpt-3.5-turbo — useful for cost management and outage
handling), exceptions_to_handle parameter, combining retry and fallback in a production
chain, testing fallback behavior, .with_config() for runtime configuration override
```

### Topic 48
```
Memory — All Types  ★ HIGH PRIORITY
Subtopics: WHY memory matters (LLM has no memory between calls — each API call is
stateless), ConversationBufferMemory (store full history — simple but grows unbounded),
ConversationBufferWindowMemory (last k messages only — simple context control),
ConversationSummaryMemory (LLM summarises old turns — slow but compact),
ConversationSummaryBufferMemory (keep recent turns verbatim + summarise old ones —
best balance), ConversationEntityMemory (tracks named entities and their attributes),
using memory in LCEL with RunnableWithMessageHistory vs manual history management,
when to use each type, external memory store (Redis, DynamoDB for production)
```

### Topic 49
```
Tools & Tool Design  ★ HIGH PRIORITY
Subtopics: what a tool is (a Python function that an LLM can call via tool-calling API),
@tool decorator (simplest way to define a tool), tool name and description — the
description IS the prompt that tells the LLM when to use this tool (critical),
args_schema with Pydantic (validates inputs before calling the function),
StructuredTool.from_function() for complex tools, BaseTool subclass for full control,
returning tool errors gracefully (ToolException), tools with side effects (write to DB,
send email — security and confirmation considerations), tool naming conventions
```

### Topic 50
```
Chains (Legacy vs LCEL) & LangChain Versioning  ★ HIGH PRIORITY
Subtopics: legacy chain classes (LLMChain, StuffDocumentsChain, MapReduceDocumentsChain,
RefineDocumentsChain, MapRerankDocumentsChain) — what each does and their LCEL
equivalents, why these are deprecated (no streaming, no async, harder to compose),
the 3 document chain strategies and LCEL implementations:
  Stuff (put all docs in one context — simple, limited by context window),
  Map-Reduce (process each doc separately, then combine — handles many docs),
  Refine (iteratively improve answer with each doc — best quality, slowest),
LangChain v0.1 vs v0.2 vs v0.3 key breaking changes, what to use in new projects
today (langchain-core + langchain-community)
```

### Topic 51
```
LangSmith — Tracing, Debugging & Callbacks  ★ HIGH PRIORITY
Subtopics: what LangSmith does (full observability: every LLM call, tool call, chain
invocation is logged with inputs, outputs, latency, token cost), enabling with 3 env
vars (zero code changes), reading a trace (the tree structure of a chain execution),
filtering and searching traces, LangChain Callbacks system (BaseCallbackHandler,
on_llm_start, on_llm_end, on_chain_start, on_tool_start etc.), custom callback for
logging to your own system, using LangSmith for debugging agent loops that go wrong,
LangSmith projects for organizing traces by environment
```

### Topic 52
```
Caching Strategies in LangChain
Subtopics: why caching matters (same prompt → cached response → zero latency + zero
cost), InMemoryCache (for dev — lost on restart), SQLiteCache (persistent, simple),
set_llm_cache() to enable globally, Exact-Match Caching (identical prompts only —
limited use), Semantic Caching (similar meaning → return cached response, embed the
query, compare with cached queries, return if above similarity threshold), Redis
SemanticCache in LangChain, when NOT to cache (non-deterministic tasks, real-time
data queries, user-specific personalization)
```

---

## PHASE 6 — Agents & LangGraph
**Why sixth:** LangGraph is the current industry standard for building production agents. High interview frequency.
**Timeline:** Week 8–10

---

### Topic 53
```
Agent Concepts & ReAct Pattern  ★ HIGH PRIORITY
Subtopics: what an agent is vs a chain (chain = fixed steps, agent = LLM decides steps
at runtime), why agents are needed (dynamic multi-step problems that can't be
predetermined), ReAct pattern: Reasoning + Acting (the dominant agent architecture),
the loop: Thought (LLM reasons) → Action (LLM calls a tool) → Observation (tool result
returned) → repeat until done, how the LLM "decides" to call a tool (via tool-calling
API in the message), agent vs chain trade-offs (flexibility vs predictability),
when NOT to use an agent (predictable tasks, latency-critical, high-stakes)
```

### Topic 54
```
LangGraph Core Concepts  ★ HIGH PRIORITY
Subtopics: why LangGraph was built (LangChain agents lacked controllability —
hard to add HITL, branching, cycles, persistence), LangGraph as a directed graph
where nodes are Python functions and edges are transitions, StateGraph as the main
abstraction, compiled graph = an executable (graph.compile()), the three primitives:
nodes (do work), edges (connect nodes), state (shared data that flows through the graph),
difference from LCEL (LCEL = linear chains, LangGraph = cyclic stateful graphs),
when to use LangGraph vs plain LCEL vs simple agent
```

### Topic 55
```
StateGraph & State Schema  ★ HIGH PRIORITY
Subtopics: defining State as a TypedDict (keys = pieces of data, values = their types),
Annotated fields with reducer functions (how state is updated — not overwritten),
add_messages reducer (appends new messages to list instead of replacing),
custom reducers (e.g. keep only unique items, aggregate numbers),
how state flows between nodes (each node receives full state, returns partial update),
accessing state inside a node (state["key"]), the START and END virtual nodes,
add_node() and add_edge() syntax, compile() to get an executable graph
```

### Topic 56
```
Conditional Edges & Routing  ★ HIGH PRIORITY
Subtopics: why conditional edges are LangGraph's superpower (enables dynamic routing
unlike fixed LCEL pipelines), defining a routing function (takes state, returns node
name string or END), add_conditional_edges(source_node, routing_fn, mapping_dict),
routing based on LLM output (does the last message contain a tool call?),
routing based on state field values (e.g. state["error_count"] > 3 → END),
tools_condition (pre-built router: tool call detected → ToolNode, else → END),
building decision trees and loops in graphs
```

### Topic 57
```
ToolNode & tools_condition  ★ HIGH PRIORITY
Subtopics: ToolNode (pre-built LangGraph node that executes tool calls from the last
AIMessage), how ToolNode works internally (reads tool_calls from AIMessage, calls each
tool, returns ToolMessages), tools_condition (pre-built routing function that checks
for tool calls), wiring a complete minimal ReAct agent: START → agent_node →
(tools_condition) → ToolNode → agent_node → END loop, binding tools to the LLM with
.bind_tools(tools), why ToolNode handles parallel tool calls automatically
```

### Topic 58
```
Checkpointing & Persistence  ★ HIGH PRIORITY
Subtopics: why checkpointing is critical (resume after failure, multi-turn conversation,
enable HITL, time-travel debugging), MemorySaver (in-memory — lost on restart, for dev),
SqliteSaver (file-based, persistent, good for single-server production),
PostgresSaver (cloud production, scalable), how to compile with a checkpointer:
graph.compile(checkpointer=SqliteSaver.from_conn_string("db.sqlite")),
thread_id in config — each conversation is a separate thread,
resuming a graph from checkpoint (just invoke with same thread_id),
checkpoint structure (checkpoint_id, state snapshot, next nodes)
```

### Topic 59
```
Human-in-the-Loop (HITL)  ★ HIGH PRIORITY
Subtopics: why HITL is critical in production (approve before sending email, confirm
before deleting records, review generated code before executing), interrupt_before
(pause BEFORE a node executes) and interrupt_after (pause AFTER), how execution
pauses at the interrupt point (graph returns, stores checkpoint),
how to resume: graph.invoke(None, config) with same thread_id,
passing human feedback back into state (update state before resuming),
combined HITL + checkpointing pattern, real-world use cases: document approval
workflow, sensitive data handling, agentic email/calendar tools
```

### Topic 60
```
Streaming in LangGraph  ★ HIGH PRIORITY
Subtopics: why streaming matters (show partial results while LLM is generating —
critical for UX), graph.stream() for full node-level output streaming (get output
after each node completes), graph.astream_events() for fine-grained event streaming
(individual LLM tokens, tool call events, node start/end events),
event types in astream_events (on_llm_stream, on_tool_start, on_chat_model_stream),
filtering events by type and tags, streaming in a FastAPI endpoint (StreamingResponse),
async streaming with ainvoke vs astream, displaying token-by-token in UI
```

### Topic 61
```
Agent Termination Conditions & LangGraph Debugging
Subtopics: how an agent loop ends (reaching END node, explicit condition in routing
function, or hitting recursion limit), infinite loop risks in agents (LLM keeps calling
tools without progress), recursion_limit in compile config (default 25 — raise for
complex tasks), max_iterations pattern (track in state, route to END when exceeded),
LangGraph time-travel debugging — what it is (replay graph from any past checkpoint),
how to list checkpoints and step back to a prior state, using LangSmith to debug
agent traces (see every node execution, tool call, LLM response in order)
```

---

## PHASE 7 — Multi-Agent & Production
**Why seventh:** Senior-level topic. Shows you can design complex systems, not just build single agents.
**Timeline:** Week 10–12

---

### Topic 62
```
Multi-Agent Supervisor Pattern  ★ HIGH PRIORITY
Subtopics: why multi-agent (single agent becomes too complex, token limit, need
specialisation), supervisor architecture: one LLM supervisor routes to specialist
sub-agents (researcher, coder, summariser, data analyst etc.),
implementing supervisor as a LangGraph node (LLM decides which agent to call next),
each sub-agent as a node or subgraph, returning results back to supervisor,
supervisor deciding when work is complete (route to END), real-world example:
enterprise research assistant (web search agent + document agent + synthesis agent),
how to structure state for multi-agent systems
```

### Topic 63
```
Swarm Pattern  ◆ EXTRA
Subtopics: alternative to supervisor — no central controller, agents hand off to each
other directly, handoff tool (an agent calls a "transfer_to_X" tool that routes
execution to agent X), when swarm is better than supervisor (peer-to-peer,
no natural "boss", more flexible routing), implementing handoff in LangGraph,
risk of infinite handoff loops and how to prevent them, LangGraph prebuilt swarm
utilities, real-world example: customer support swarm (billing agent → technical agent
→ escalation agent)
```

### Topic 64
```
Plan-and-Execute Pattern  ◆ EXTRA
Subtopics: limitation of ReAct for long-horizon tasks (makes greedy local decisions,
no global plan), Plan-and-Execute: (1) Planner LLM creates a structured plan (list of
steps) upfront, (2) Executor runs each step with tools, (3) Replanner adapts the plan
based on intermediate results, why this handles complex multi-step tasks better,
implementing in LangGraph: planner node → executor loop → replanner node → END,
task list in state, when plan-and-execute outperforms ReAct
```

### Topic 65
```
Reflection & Self-Correction  ◆ EXTRA
Subtopics: agent generates output → reflection/critic node evaluates it → agent revises
based on feedback → loop, implementing reflection as a LangGraph loop (generate →
reflect → revise → check → END), self-reflection vs external critic (a second LLM),
stopping conditions: N max iterations OR quality threshold OR "approved" in state,
Reflexion pattern, use cases: code generation with testing, report writing with
quality check, data extraction with validation, combining reflection with tool use
```

### Topic 66
```
LangGraph Subgraphs & Modular Architecture  ◆ EXTRA
Subtopics: what a subgraph is (a full compiled graph used as a single node inside
a parent graph), why subgraphs enable modularity and reusability (each sub-team
owns one subgraph), state schema compatibility rules (parent state must include all
subgraph state keys, or use input/output transformers), how to add a subgraph as a
node, nested subgraphs (subgraph of subgraphs), real-world example: parent graph
orchestrates [RAG subgraph, SQL subgraph, web search subgraph], testing subgraphs
independently before integrating
```

### Topic 67
```
LangGraph Send API — Parallel Fan-out
Subtopics: the problem — you want to process N items in parallel inside a graph
(e.g. analyse 10 documents simultaneously), Send object (routes to a node with a
specific input — multiple Sends = parallel execution), map-reduce pattern in LangGraph:
fan-out with Send → parallel node executions → aggregate results in a reduce node,
how Send differs from RunnableParallel (Send works within graph cycles, between
arbitrary nodes), state design for fan-out (list of pending tasks), collecting
parallel results back into state, when Send is the right tool
```

### Topic 68
```
LangSmith Evaluation & CI/CD for LLM Apps
Subtopics: why evaluation pipelines matter (can't manually check every LLM response
in production), creating evaluation datasets in LangSmith (question + ground truth
answer pairs), defining evaluators (correctness, hallucination, relevance — use a
grader LLM), running client.evaluate() against a dataset, comparing two model versions
(before/after prompt change), custom evaluator functions, integrating LangSmith
evaluation into CI/CD (run on every PR, fail pipeline if score drops), human annotation
pipeline in LangSmith, tracking model performance over time
```

### Topic 69
```
Cost & Token Optimisation  ★ HIGH PRIORITY
Subtopics: where cost comes from in LLM apps (prompt tokens, completion tokens, per API
call), calculating cost per conversation (track tokens in LangSmith), model routing:
classify query complexity → use cheap model (gpt-3.5, claude-haiku) for simple, expensive
(gpt-4o, claude-sonnet) for complex, prompt compression (remove redundant context,
summarise rather than include raw history), response caching (LangSmith shows hit rate),
batching API calls (abatch() for parallel processing), reducing k in RAG (each extra
chunk = extra prompt tokens), token budget enforcement in chains
```

### Topic 70
```
Guardrails & Safety  ★ HIGH PRIORITY
Subtopics: input validation (detect and block harmful/off-topic queries before they
reach the LLM), output validation (check LLM response before sending to user — contains
PII? Toxic content? Off-brand?), prompt injection attacks (user input hijacks system
instructions), indirect prompt injection in RAG (retrieved document contains malicious
instructions), PII detection (regex for emails/phones, spaCy NER for names, AWS
Comprehend, Azure PII), PII scrubbing before embedding, Constitutional AI (LLM
self-critiques against a set of rules), NeMo Guardrails and Llama Guard (overview),
OWASP Top 10 for LLMs — the list with brief explanation of each item
```

### Topic 71
```
Deployment — LangServe, LangGraph Platform, FastAPI  ★ HIGH PRIORITY
Subtopics: LangServe (FastAPI-based serving for LangChain chains — /invoke, /stream,
/batch, /playground endpoints, add_routes() in FastAPI), LangGraph Platform (managed
deployment of LangGraph agents — persistence, streaming, human-in-the-loop built in),
self-hosting a LangGraph agent as a FastAPI endpoint (async endpoint for streaming),
environment variable management (LangSmith API key, model API keys — use .env + dotenv
or AWS Secrets Manager), Docker containerisation for LLM apps (Dockerfile patterns),
horizontal scaling for stateless chains vs stateful agents (agents need sticky sessions
or shared checkpointer), health checks and graceful shutdown
```

---

## PHASE 8 — Beyond the Frameworks: What Else Gets Asked
**Why eighth:** Interview rounds 2 and 3 at service companies frequently go outside the framework knowledge into fundamentals, decision-making, architecture, and industry context.
**Timeline:** Week 12–14

---

### Topic 72
```
LLM Hallucination — What It Is, Why It Happens, How to Reduce It  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: what hallucination is (LLM generating confident but false information),
WHY it happens (LLM is a token predictor, not a truth verifier — plausible ≠ true),
types: factual hallucination, attribution hallucination (wrong source), temporal
hallucination (outdated info), intrinsic (contradicts context) vs extrinsic
(adds information not in context), why RAG REDUCES but does NOT eliminate hallucination,
mitigation strategies: temperature=0 for factual tasks, RAG with strict grounding
prompt, citation enforcement, RLHF training, output verification,
NLI-based factual consistency checking, hallucination rate as a production KPI
```

### Topic 73
```
Fine-tuning vs RAG vs Prompt Engineering — Decision Framework  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: the three approaches and when each is the right tool:
Prompt Engineering (when: well-defined task, LLM already knows the domain, fast
iteration needed, prototyping — start here always),
RAG (when: private/proprietary knowledge, knowledge changes frequently, large document
corpus, need source citations, can't retrain model — most common at service companies),
Fine-tuning (when: specific output style/format, domain vocabulary adaptation, latency
critical and want to reduce prompt length, teach the model a new behavior not knowledge),
Fine-tune + RAG hybrid (fine-tune for style, RAG for knowledge),
cost and timeline comparison, interview-ready decision matrix, common mistake:
"fine-tuning is the solution to hallucination" (it is not)
```

### Topic 74
```
Fine-tuning Concepts — LoRA, PEFT, Instruction Tuning  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: what fine-tuning means (adjust model weights on your task-specific data),
full fine-tuning (update all weights — expensive, requires significant GPU, risk of
catastrophic forgetting), PEFT — Parameter Efficient Fine-Tuning (update only a small
fraction of parameters), LoRA — Low-Rank Adaptation (add small trainable adapter
matrices alongside frozen original weights, merge at inference),
WHY LoRA is the industry standard (1–10% of parameters, near full fine-tuning quality,
much cheaper), QLoRA (quantise the base model to 4-bit + LoRA — run on consumer GPUs),
instruction tuning (fine-tune on instruction-response pairs — how ChatGPT was trained),
SFT (Supervised Fine-Tuning) vs RLHF, HuggingFace PEFT library overview,
when to call a fine-tuning vendor (OpenAI fine-tuning, Together AI, Modal) vs DIY
```

### Topic 75
```
HuggingFace & Local LLMs with Ollama  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: why local/open-source LLMs matter (cost at scale, data privacy, compliance,
offline deployment), HuggingFace Hub (find and load models: Llama 3, Mistral, Phi-3,
Gemma, Qwen), HuggingFacePipeline in LangChain (wrap transformers pipeline as ChatModel),
sentence-transformers for free high-quality local embeddings (all-MiniLM, bge-small),
Ollama (run models locally with one command: ollama run llama3), ChatOllama in LangChain,
OllamaEmbeddings, GPU vs CPU inference (quantised models: GGUF format for CPU,
4-bit for GPU), when to use local vs API (privacy requirements, >100K requests/day
cost tipping point, offline deployment), LM Studio as a desktop alternative
```

### Topic 76
```
Cloud LLM Services — AWS Bedrock, Azure OpenAI, GCP Vertex AI  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: why cloud LLM services matter for service companies (clients run on cloud,
compliance, enterprise contracts), AWS Bedrock (managed LLM service — Claude, Llama,
Mistral, Titan — pay-per-token, IAM integration, VPC support, no data training by default),
LangChain ChatBedrock integration, Azure OpenAI Service (same GPT models hosted on Azure,
GDPR compliant, enterprise SLAs, private networking), ChatAzureOpenAI in LangChain,
GCP Vertex AI (Gemini models, palm2, open-source models via Model Garden),
how to choose between direct API vs cloud service (compliance, data residency,
existing cloud relationship, network egress costs), LangChain integration patterns for each
```

### Topic 77
```
LLM Application Design Patterns  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: the 5 core LLM application patterns service companies build repeatedly:

(1) Document Q&A / RAG Chatbot (most common) — architecture, challenges, production tips

(2) Document Summarisation — Stuff strategy (all docs in one context), Map-Reduce
(summarise each doc → combine summaries), Refine (iteratively improve answer),
MapRerank (score each chunk, return top) — when to use each strategy

(3) Information Extraction Pipeline (extract structured data from unstructured text —
invoices, contracts, emails) — use Pydantic + with_structured_output, batch processing

(4) LLM-based Classification (sentiment, intent, topic, priority) — zero-shot vs
few-shot classification, confidence scores, multi-label classification

(5) Code Generation Assistant — system prompt with coding rules, test generation,
code review, explain code patterns

For each: architecture diagram, LangChain approach, production pitfalls
```

### Topic 78
```
LLM System Design for Production  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: this is the ARCHITECTURE ROUND topic — most asked in senior/round-3 interviews.
The question: "Design a document Q&A chatbot for 10,000 concurrent users."

Walk through EACH layer and justify decisions:
  (1) API Gateway / Load Balancer (rate limiting, auth, routing)
  (2) LLM Orchestration Service (FastAPI + LangGraph, stateless for chains, stateful for agents)
  (3) Vector Database (Pinecone/Weaviate for scale, pgvector for simplicity)
  (4) Caching Layer (Redis for semantic cache, exact-match cache for FAQs)
  (5) LLM Provider (primary + fallback, model routing by query complexity)
  (6) Monitoring (LangSmith, OpenTelemetry, Grafana dashboards)
  (7) Storage (S3 for raw documents, RDS for metadata, Redis for sessions)

Key design decisions to discuss: sync vs async, streaming vs batch, multi-tenancy,
data isolation, cost per request estimation, P99 latency target (< 5s end-to-end),
scaling the embedding pipeline separately from the query pipeline,
GDPR compliance (data residency, right to be forgotten)

Also cover: LLM Evaluation Metrics — BLEU/ROUGE (older NLP, still asked), RAGAS scores,
LLM-as-judge (G-Eval pattern), pairwise evaluation (A vs B), reference-free evaluation,
human evaluation vs automated, what metrics to track in production dashboards,
Responsible AI: bias in LLMs (training data bias, demographic disparities),
fairness auditing, EU AI Act awareness (high-risk AI systems), model cards
```

---

## Quick-Access Priority Guide

### Crash Mode — Only 2 Weeks Available:
Focus exclusively on these (roughly in order):
Topics 2, 3, 5, 9, 10, 11, 13, 15, 16, 18, 20, 22, 23, 26, 27, 28, 42, 44, 45, 46,
48, 49, 53, 54, 55, 56, 57, 58, 59, 62, 72, 73, 77, 78

### Standard Mode — 10–14 Weeks:
Work through all 78 topics in order, spending 2–4 hours per topic.

### Topic Count by Phase:

| Phase | Focus Area | Topics | Count |
|---|---|---|---|
| Phase 1 | LLM Foundations | 1–8 | 8 |
| Phase 2 | Embeddings & Vector Search | 9–14 | 6 |
| Phase 3 | RAG Fundamentals | 15–26 | 12 |
| Phase 4 | Advanced RAG | 27–41 | 15 |
| Phase 5 | LangChain Core | 42–52 | 11 |
| Phase 6 | Agents & LangGraph | 53–61 | 9 |
| Phase 7 | Multi-Agent & Production | 62–71 | 10 |
| Phase 8 | Beyond the Frameworks | 72–78 | 7 |
| **Total** | | | **78 topics** |

### Top 10 Interview Questions Service Companies Ask That Candidates Get Wrong:
1. "RAG eliminates hallucination" — WRONG. It reduces it, not eliminates.
2. Cannot explain chunking trade-offs beyond "I used 512 tokens"
3. Doesn't know what hybrid search is — only mentions vector search
4. Cannot explain WHY the same embedding model must index and query
5. No knowledge of any RAG evaluation framework by name
6. Treats fine-tuning as the solution to hallucination
7. Can't explain the lost-in-the-middle problem
8. Knows LangChain but can't explain what LCEL replaced and why
9. Can't design a multi-tenant RAG system (data isolation)
10. No answer for "how do you know your RAG system is working in production?"
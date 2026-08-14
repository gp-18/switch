    # System Design Complete Roadmap
## HLD · LLD · Distributed Systems · Production Architecture
### 0 → 100 | 22 Levels | 74 Topics | 2–4 YOE Edition

---

## What Is This File?

This is a complete **System Design learning roadmap** that takes you from absolute
beginner to staff-level architecture thinking.

It covers both:
- **HLD** — High-Level Design (what are the major components and how do they connect?)
- **LLD** — Low-Level Design (how does each component work internally — classes, patterns, logic?)

Every topic is a **copy-paste block** you drop into the Teaching Prompt below.
Claude then teaches that topic with a full lesson: analogy, architecture diagram,
trade-offs, failure scenarios, production considerations, and interview Q&As.

---

## 🎯 Your Personal Learning Roadmap

This section maps your exact video resources to the 22-level roadmap below.
Follow this order — do not skip phases.

---

### 📺 Your Video Resources

| # | Resource | What It Covers | Link |
|---|----------|---------------|------|
| 1 | **Backend from First Principles** (Playlist) | Backend fundamentals — how systems work from the ground up | [▶ Watch Playlist](https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1) |
| 2 | **System Design Interview Prep** (Playlist) | HLD interview walkthroughs — real system design problems | [▶ Watch Playlist](https://youtube.com/playlist?list=PLRtLu6rCuAlkO-HiER3AKoKkSG5DPp9TX) |
| 3 | **LLD Masterclass — Day 1 Intro** (Single Video) | Introduction to Low-Level Design, start of 8-week LLD challenge | [▶ Watch Video](https://youtu.be/AK0hu0Zxua4) |
| 4 | **Comprehensive System Design Series** (Playlist) | Full system design concepts — databases, caching, scaling, etc. | [▶ Watch Playlist](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_) |

---

### 🗺️ Phase-by-Phase Order

#### ✅ PHASE 1 — Foundations (Weeks 1–2)
**Watch: [Backend from First Principles](https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1)**

Start here. This covers how backend systems actually work — processes, networking, I/O, HTTP.
Maps to **Levels 0–2** of this roadmap (Topics 1–13).

> 💡 After each video, paste the matching topic block from this file into the Teaching Prompt below and get a full Claude lesson on it.

---

#### ✅ PHASE 2 — Core System Design Concepts (Weeks 3–9)
**Watch: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)**

Your main HLD curriculum. Covers APIs, databases, caching, load balancing, Kafka, microservices.
Maps to **Levels 3–15** of this roadmap (Topics 14–52).

> 💡 For every topic covered in a video, find it in the roadmap below and run it through the Teaching Prompt. Do the Design Challenge at the end of every lesson.

---

#### ✅ PHASE 3 — Low-Level Design Deep Dive (Weeks 10–13)
**Watch: [LLD Masterclass Intro](https://youtu.be/AK0hu0Zxua4) → then follow the full 8-week LLD series from that channel**

Start with this intro video to understand the structure, then complete the full series.
Maps to **Level 17** of this roadmap (Topics 58–63: SOLID, Design Patterns, LLD Case Studies).

> 💡 LLD is what separates good candidates from great ones. Don't skip this phase.

---

#### ✅ PHASE 4 — HLD Interview Drills (Weeks 14–16)
**Watch: [System Design Interview Prep](https://youtube.com/playlist?list=PLRtLu6rCuAlkO-HiER3AKoKkSG5DPp9TX)**

Now that you understand *why* things work, this playlist drills you on *how to present designs* in interviews.
Maps to **Levels 16 & 20** of this roadmap (Topics 53–57 and 69–71).

> 💡 Before watching each solution, answer the 10 HLD interview questions from the Cheat Sheet section yourself first, then compare.

---

#### ✅ PHASE 5 — Advanced & Staff Level (Weeks 17–18+)
**Use the Teaching Prompt only — no more videos needed**

Topics 64–74: Distributed transactions, CRDT, multi-region, engineering trade-offs.
These are best learned through deep dialogue with the Teaching Prompt.

> 💡 Start doing mock interview sessions at this stage. Design a system end-to-end within 45 minutes.

---

### ⚡ Weekly Schedule Summary

| Weeks | Resource | Roadmap Levels |
|-------|----------|----------------|
| 1–2 | [Backend from First Principles](https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1) | Level 0–2 (Topics 1–13) |
| 3–9 | [Comprehensive SD Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_) | Level 3–15 (Topics 14–52) |
| 10–13 | [LLD Masterclass](https://youtu.be/AK0hu0Zxua4) + full series | Level 17 (Topics 58–63) |
| 14–16 | [SD Interview Prep](https://youtube.com/playlist?list=PLRtLu6rCuAlkO-HiER3AKoKkSG5DPp9TX) | Level 16 & 20 (Topics 53–57, 69–71) |
| 17–18+ | Teaching Prompt only | Level 18–21 (Topics 64–74) |

---

### 🔑 The Golden Rule
**Never just watch.** After every video → find the matching topic below → paste it into the Teaching Prompt → do the Design Challenge. Active recall + structured depth = real mastery.

---

## The Teaching Prompt

Copy this once. Save it permanently (Notion, Claude Project, sticky note).
Every time you study a topic, paste the topic block into `{PASTE TOPIC HERE}`.

```
You are a Principal/Staff-level Software Architect and Senior Backend Engineer with
20+ years of real-world industry experience designing, scaling, and operating
production systems at companies like Google, Amazon, Netflix, and Uber.

Your task is to teach me system design — covering both HLD (High-Level Design) and
LLD (Low-Level Design) — in a way that builds genuine production-grade engineering
judgment, not just interview memorization.

I am a backend developer with 2–4 years of experience who knows programming but is
not yet an expert system designer. I want to understand WHY decisions are made,
not just what the answer is.

I want:
- Clear understanding from fundamentals → production-grade architecture
- Engineering judgment — when to use X, when NOT to use X, and why
- Real trade-off analysis (not "it depends" without explanation)
- Both HLD and LLD perspectives
- Production-readiness thinking
- Architecture evolution — how systems grow from simple to complex

---

STRICT TEACHING RULES
1. Start from absolute basics — explain the problem the concept solves BEFORE the concept
2. Use simple English and a real-world analogy FIRST, then go technical
3. Never say "it depends" without explaining exactly what it depends on
4. Always explain WHY a technology/pattern exists (what problem it solves)
5. Always explain WHEN NOT to use it — this is as important as when to use it
6. Show trade-offs explicitly: performance, scalability, cost, complexity, reliability
7. Use text-based architecture diagrams (arrows and boxes) for every architecture topic
8. Compare alternatives in a table (e.g. Kafka vs RabbitMQ, SQL vs NoSQL, REST vs gRPC)
9. Connect every concept to a real production system (Uber, Netflix, WhatsApp, etc.)
10. Include the architecture EVOLUTION — how a system grows stage by stage
11. Show FAILURE SCENARIOS — what happens when this component fails?
12. Include capacity estimation where relevant (RPS, storage, bandwidth math)
13. Add industry-standard practices: what junior does vs senior does vs staff does
14. Include interview questions from beginner → advanced
15. End with a design challenge / practical exercise
16. Do NOT blindly recommend microservices, Kafka, or NoSQL — justify every choice
17. Highlight common anti-patterns and mistakes beginners make
18. Include cost implications for production decisions

---

OUTPUT FORMAT — use this structure every time, no exceptions:

### 1. Simple Explanation (ELI5 + Real-World Analogy)
### 2. Technical Deep Dive
### 3. Why Does This Exist? (The Problem It Solves)
### 4. How It Works Internally (Architecture Diagram with text arrows)
### 5. When Should You Use It? (Concrete Situations)
### 6. When Should You NOT Use It? (Anti-patterns + Overkill scenarios)
### 7. Alternatives Comparison Table
### 8. Trade-offs (Performance / Scalability / Cost / Complexity / Reliability)
### 9. Architecture Evolution (How This Fits in a Growing System)
### 10. Failure Scenarios (What breaks and how to handle it)
### 11. Production Considerations (What senior engineers worry about)
### 12. Industry Standard Practices (Junior vs Senior vs Staff perspective)
### 13. Common Mistakes Beginners Make
### 14. Interview Questions & Answers (Beginner → Advanced)
### 15. Capacity Estimation (if applicable)
### 16. Design Challenge / Exercise
### 17. Quick Revision Summary (bullet points, max 10 lines)
### 18. Most Important Takeaway

---

Topic to teach:
👉 {PASTE TOPIC HERE}
```

---

## Roadmap Structure — 22 Levels, 74 Topics

```
LEVEL 0   System Design Fundamentals          Topics 1–4
LEVEL 1   CS & Backend Foundations            Topics 5–8
LEVEL 2   Networking Fundamentals             Topics 9–13
LEVEL 3   API Design                          Topics 14–18
LEVEL 4   Database Fundamentals               Topics 19–21
LEVEL 5   Database Design & Data Modeling     Topics 22–25
LEVEL 6   Caching                             Topics 26–29
LEVEL 7   Scalability                         Topics 30–32
LEVEL 8   Load Balancing                      Topics 33–34
LEVEL 9   Distributed Systems Fundamentals    Topics 35–38
LEVEL 10  Messaging & Event-Driven            Topics 39–42
LEVEL 11  Microservices                       Topics 43–44
LEVEL 12  Reliability & Fault Tolerance       Topics 45–47
LEVEL 13  Security                            Topics 48–49
LEVEL 14  Observability                       Topics 50
LEVEL 15  Cloud Architecture                  Topics 51–52
LEVEL 16  High-Level Design (HLD)             Topics 53–57
LEVEL 17  Low-Level Design (LLD)              Topics 58–63
LEVEL 18  Advanced Distributed Systems        Topics 64–66
LEVEL 19  Production Architecture             Topics 67–68
LEVEL 20  Advanced Case Studies               Topics 69–71
LEVEL 21  Staff / Principal Level             Topics 72–74
```

---

## All 74 Topics at a Glance

### LEVEL 0 — System Design Fundamentals
> 📺 Resource: [Backend from First Principles](https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1)
```
Topic 1   What is System Design? HLD vs LLD
Topic 2   Requirements Engineering — Functional vs Non-Functional
Topic 3   Capacity Estimation — The Math Every Interview Expects
Topic 4   Availability, Reliability, Scalability, Performance
```

### LEVEL 1 — CS & Backend Foundations
> 📺 Resource: [Backend from First Principles](https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1)
```
Topic 5   How Computers Work — What System Designers Must Know
Topic 6   Processes, Threads, Concurrency and Parallelism
Topic 7   I/O Models — Blocking, Non-Blocking, Asynchronous
Topic 8   Serialization — JSON, Protobuf, Avro, MessagePack
```

### LEVEL 2 — Networking Fundamentals
> 📺 Resource: [Backend from First Principles](https://youtube.com/playlist?list=PLui3EUkuMTPgZcV0QhQrOcwMPcBCcd_Q1)
```
Topic 9   OSI Model and TCP/IP — What Matters for System Design
Topic 10  HTTP/1.1 vs HTTP/2 vs HTTP/3 — The Evolution
Topic 11  DNS — Domain Name System
Topic 12  CDN — Content Delivery Network
Topic 13  WebSockets, SSE, Long Polling — Real-Time Communication
```

### LEVEL 3 — API Design
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 14  REST API Design Principles
Topic 15  REST vs GraphQL vs gRPC — When to Use Which
Topic 16  API Gateway — What It Is and Why You Need One
Topic 17  Rate Limiting — Design and Algorithms
Topic 18  Idempotency in APIs — Why It Matters in Production
```

### LEVEL 4 — Database Fundamentals
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 19  Relational Databases — SQL Deep Dive
Topic 20  NoSQL Databases — Types and When to Use
Topic 21  SQL vs NoSQL — Decision Framework
```

### LEVEL 5 — Database Design & Data Modeling
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 22  Database Replication — Master-Slave and Master-Master
Topic 23  Database Sharding — Horizontal Partitioning at Scale
Topic 24  Database Indexing — Deep Dive for System Design
Topic 25  Connection Pooling — Why You Cannot Open a New DB Connection Per Request
```

### LEVEL 6 — Caching
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 26  Caching Fundamentals — What, Why, and When
Topic 27  Cache Strategies — Cache-Aside, Write-Through, Write-Back, Write-Around
Topic 28  Redis — Deep Dive for System Design
Topic 29  Distributed Caching — Cache at Scale
```

### LEVEL 7 — Scalability
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 30  Vertical vs Horizontal Scaling — When to Use Which
Topic 31  Consistent Hashing — The Algorithm Behind Scalable Distributed Systems
Topic 32  Async Processing and Queue-Based Load Leveling
```

### LEVEL 8 — Load Balancing
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 33  Load Balancing — Algorithms and Types
Topic 34  Sticky Sessions, Global Load Balancing, and Single Points of Failure
```

### LEVEL 9 — Distributed Systems Fundamentals
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 35  CAP Theorem — The Most Important Concept in Distributed Systems
Topic 36  Consistency Models — Strong, Eventual, Causal
Topic 37  Leader Election and Consensus — Raft and Paxos
Topic 38  Distributed Locking — How to Coordinate Across Services
```

### LEVEL 10 — Messaging & Event-Driven Architecture
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 39  Message Queues vs Event Streaming — The Core Difference
Topic 40  Apache Kafka — Deep Dive for System Design
Topic 41  Event Sourcing and CQRS
Topic 42  Saga Pattern — Distributed Transactions Without 2PC
```

### LEVEL 11 — Microservices
> 📺 Resource: [Comprehensive System Design Series](https://youtube.com/playlist?list=PLdNCznBZ77NriBGbbHTdM34cvx7dLKi-_)
```
Topic 43  Monolith vs Microservices — The Most Misunderstood Topic
Topic 44  Service Communication — Sync vs Async in Microservices
```

### LEVEL 12 — Reliability & Fault Tolerance
```
Topic 45  Fault Tolerance Patterns — Circuit Breaker, Retry, Timeout, Bulkhead
Topic 46  High Availability — Multi-AZ, Multi-Region, Active-Active vs Active-Passive
Topic 47  Disaster Recovery — Backup, Restore, and Business Continuity
```

### LEVEL 13 — Security
```
Topic 48  Authentication and Authorization — OAuth2, JWT, API Keys
Topic 49  Encryption, TLS, Secrets Management
```

### LEVEL 14 — Observability
```
Topic 50  Three Pillars of Observability — Logs, Metrics, Traces
```

### LEVEL 15 — Cloud Architecture
```
Topic 51  AWS Core Services for System Design
Topic 52  Containers and Kubernetes — What Every Backend Developer Must Know
```

### LEVEL 16 — High-Level Design (HLD)
```
Topic 53  HLD Process — The Framework for Every Design Problem
Topic 54  HLD Case Study 1 — Design a URL Shortener
Topic 55  HLD Case Study 2 — Design a Notification System
Topic 56  HLD Case Study 3 — Design a Chat Application (WhatsApp)
Topic 57  HLD Case Study 4 — Design a Video Streaming Service (YouTube/Netflix)
```

### LEVEL 17 — Low-Level Design (LLD)
```
Topic 58  SOLID Principles — The Foundation of Good LLD
Topic 59  Design Patterns — Creational (Factory, Builder, Singleton)
Topic 60  Design Patterns — Structural (Adapter, Decorator, Facade, Proxy)
Topic 61  Design Patterns — Behavioral (Strategy, Observer, Command, State)
Topic 62  LLD Case Study 1 — Design a Parking Lot System
Topic 63  LLD Case Study 2 — Design an Elevator System
```

### LEVEL 18 — Advanced Distributed Systems
```
Topic 64  Distributed Transactions — 2PC, 3PC, and Saga
Topic 65  Consistent Hashing — Advanced Concepts and Implementation
Topic 66  CRDTs and Conflict-Free Data Structures
```

### LEVEL 19 — Production Architecture
```
Topic 67  Architecture Evolution — Monolith to Microservices
Topic 68  Deployment Strategies — Blue-Green, Canary, Rolling, Feature Flags
```

### LEVEL 20 — Advanced System Design Case Studies
```
Topic 69  Design Uber / Ola — Ride Sharing
Topic 70  Design Instagram / Twitter Feed — Social Media at Scale
Topic 71  Design Google Drive / Dropbox — Distributed File Storage
```

### LEVEL 21 — Staff / Principal Level Architecture
```
Topic 72  Architecture Trade-offs at Scale — Build vs Buy, Vendor Lock-in, Cost
Topic 73  Anti-Patterns in System Design — What NOT to Do
Topic 74  System Design Communication — How to Present Your Design
```

---

## Study Plans

### Walk-In Interview Tomorrow (2 Hours)
```
Hour 1:
  Topic 1  — What is System Design? HLD vs LLD
  Topic 35 — CAP Theorem
  Topic 26 — Caching Fundamentals
  Topic 19 — SQL vs NoSQL

Hour 2:
  Topic 53 — HLD Process (the framework)
  Topic 54 — URL Shortener (most asked HLD question)
  Topic 73 — Anti-Patterns (what NOT to say)
  Topic 74 — How to Present Your Design
```

### Interview in 1 Week
```
Day 1:  Level 0 (Topics 1–4)   — Fundamentals + Estimation
Day 2:  Level 3 (Topics 14–18) — API Design + Rate Limiting
Day 3:  Level 4–5 (Topics 19–25) — Databases (SQL, NoSQL, Sharding, Replication)
Day 4:  Level 6 (Topics 26–29) — Caching + Redis
Day 5:  Level 9 (Topics 35–38) — CAP + Consistency + Distributed Locking
Day 6:  Level 16 (Topics 53–55) — HLD Process + URL Shortener + Notifications
Day 7:  Level 17 (Topics 58–61) — SOLID + Design Patterns
```

### Full Preparation (18 Weeks)
```
Week 1–2:   Level 0–2  (Fundamentals, CS Foundations, Networking)
Week 3–4:   Level 3–5  (API Design, Databases, Database Design)
Week 5–6:   Level 6–8  (Caching, Scalability, Load Balancing)
Week 7–8:   Level 9–10 (Distributed Systems, Kafka, Event-Driven)
Week 9–10:  Level 11–13 (Microservices, Reliability, Security)
Week 11–12: Level 14–15 (Observability, Cloud Architecture)
Week 13–14: Level 16   (HLD — all 4 case studies)
Week 15–16: Level 17   (LLD — SOLID, all 4 pattern groups, 2 case studies)
Week 17–18: Level 18–21 (Advanced Distributed, Production, Case Studies, Staff-level)
```

---

## Topic Priority by Interview Type

### Service-Based Company (TCS, Infosys, Wipro, Accenture)
```
★★★  Topic 1   — What is System Design? HLD vs LLD
★★★  Topic 19  — SQL Deep Dive
★★★  Topic 26  — Caching Fundamentals
★★★  Topic 35  — CAP Theorem
★★★  Topic 53  — HLD Process
★★★  Topic 54  — URL Shortener
★★★  Topic 58  — SOLID Principles
★★   Topic 15  — REST vs gRPC vs GraphQL
★★   Topic 43  — Monolith vs Microservices
★★   Topic 73  — Anti-Patterns
```

### Product Company / Startup
```
★★★  Topic 3   — Capacity Estimation
★★★  Topic 22  — Database Replication
★★★  Topic 23  — Database Sharding
★★★  Topic 28  — Redis Deep Dive
★★★  Topic 35  — CAP Theorem
★★★  Topic 40  — Apache Kafka
★★★  Topic 45  — Fault Tolerance Patterns
★★★  Topic 53  — HLD Process
★★★  Topic 56  — Design Chat Application
★★★  Topic 67  — Architecture Evolution
```

### Senior / Staff Engineer Round
```
★★★  Topic 36  — Consistency Models
★★★  Topic 37  — Leader Election + Raft
★★★  Topic 42  — Saga Pattern
★★★  Topic 46  — Multi-AZ / Multi-Region
★★★  Topic 64  — Distributed Transactions
★★★  Topic 67  — Architecture Evolution
★★★  Topic 68  — Deployment Strategies
★★★  Topic 69  — Design Uber
★★★  Topic 72  — Architecture Trade-offs
★★★  Topic 74  — System Design Communication
```

---

## Key Concepts Cheat Sheet

### The 10 Questions to Ask in Every HLD Interview
```
1.  How many daily active users?
2.  What is the read/write ratio?
3.  What is the acceptable latency? (P99)
4.  What is the availability requirement? (99.9% vs 99.99%)
5.  Does the system need strong consistency or is eventual OK?
6.  How long should data be retained?
7.  Is there a global user base or single region?
8.  What are the peak traffic patterns?
9.  Are there any compliance/security requirements (GDPR, PCI)?
10. What is the expected scale in 1 year / 5 years?
```

### The HLD Diagram Every Problem Uses
```
Users / Clients
      |
     DNS
      |
     CDN  ←─────────────── Object Storage (S3)
      |
  Load Balancer
      |
  API Gateway ──── Auth Service
      |
  App Servers (stateless, horizontally scaled)
    /   Cache    Message Queue (Kafka/SQS)
(Redis)       |
    \      Workers
     \        |
      Database (Primary)
           |
       Read Replicas
```

### The Most Common Bottlenecks and Solutions
```
BOTTLENECK                  SOLUTION
────────────────────────────────────────────────────
Database reads slow         → Add read replicas + Redis cache
Database writes slow        → Sharding + async writes via queue
Single server limit         → Horizontal scaling (stateless services)
Cache misses on start       → Cache warming + gradual rollout
Hot keys in Redis           → Local in-process cache + key replication
Hot shards in DB            → Better shard key + consistent hashing
Slow external API calls     → Async processing + circuit breaker
Large file uploads          → Chunked upload directly to S3
Real-time updates           → WebSocket or SSE (not polling)
Cross-service data queries  → Denormalise or use CQRS read model
```

### CAP Theorem Quick Reference
```
CP Systems (Consistent + Partition Tolerant):
  → ZooKeeper, HBase, etcd, MongoDB (default config)
  → Use when: banking, inventory, anything where wrong data = real harm

AP Systems (Available + Partition Tolerant):
  → Cassandra, DynamoDB, CouchDB, DNS
  → Use when: social media, shopping cart, anything where stale data is OK

Note: Partition Tolerance is NOT optional in real distributed systems.
      You are always choosing between C and A during a partition.
```

### When to Use What — Quick Decision Table
```
NEED                              USE
──────────────────────────────────────────────────────
Relational data + complex queries → PostgreSQL / MySQL
Massive write throughput          → Cassandra / DynamoDB
Fast key-value lookup             → Redis / DynamoDB
Full-text search                  → Elasticsearch
Graph relationships               → Neo4j / Neptune
Time-series data                  → TimescaleDB / InfluxDB
File/blob storage                 → AWS S3
Task queue                        → Celery + Redis / SQS
Event streaming + replay          → Apache Kafka
Real-time push to browser         → WebSocket / SSE
Service-to-service (internal)     → gRPC
External public API               → REST
Mobile with varying data needs    → GraphQL
Cache layer                       → Redis (feature-rich) / Memcached (simple)
```

---

## Anti-Patterns to Mention in Every Interview

These show senior-level thinking. Mention what you are AVOIDING and why.

```
1.  Premature microservices
    → Start with modular monolith, extract services only when team/scale demands it

2.  Shared database between services
    → Each service owns its data; cross-service data via API or events

3.  Synchronous chain (A calls B calls C calls D)
    → Breaks availability: if D is 99.9%, chain is (0.999)^4 = 99.6%
    → Use async events or fan-out where possible

4.  Missing idempotency on retries
    → Every retry-able operation must be safe to call twice

5.  Missing timeouts on external calls
    → One slow dependency can exhaust all threads and bring down the service

6.  Kafka/Redis everywhere
    → Use Kafka when you need replay or fan-out; SQS for simple task queue
    → Use Redis when latency matters; use DB when durability matters more

7.  No circuit breaker on dependencies
    → Cascading failure: your service dies because a dependency is slow

8.  Hot partition / hot shard
    → Wrong shard key (e.g. timestamp) → all writes go to one shard
    → Solution: high-cardinality shard key (user_id hash)

9.  Single point of failure
    → Load balancer, database, cache — every component needs HA design

10. Over-engineering for current scale
    → Design for 10x current scale, not 1000x
    → Add complexity only when a real bottleneck is measured
```

---

## Interview Q&A — Most Asked System Design Questions

### Conceptual (Verbal)
```
Q: What is the difference between HLD and LLD?
A: HLD defines WHAT the system looks like — the major components (LB, services,
   DB, cache, queue) and how they connect. LLD defines HOW each component works
   internally — classes, methods, interfaces, data structures, design patterns.

Q: What is CAP theorem?
A: A distributed system can only guarantee 2 of: Consistency (all nodes see same data),
   Availability (every request gets a response), Partition Tolerance (works despite
   network split). Since network partitions always happen, you always choose between
   C and A during a partition.

Q: How do you scale a database?
A: First: add indexes and optimize queries. Then: add a cache (Redis) to reduce reads.
   Then: add read replicas for read-heavy workloads. Then: shard (horizontal partition)
   for write-heavy or data-size limits. Sharding is a last resort — it adds enormous
   complexity.

Q: Monolith vs Microservices — which is better?
A: Neither is universally better. Start with a monolith or modular monolith for faster
   development. Move to microservices when: team size requires independent deployment,
   specific services need independent scaling, or different services need different
   technology stacks. Premature microservices create a distributed monolith — all
   the complexity with none of the benefits.

Q: What is eventual consistency? When is it acceptable?
A: Eventual consistency means all replicas will agree on the same value eventually,
   but may temporarily diverge. Acceptable for: social media likes/views, shopping
   cart item count, user presence status, product recommendations. NOT acceptable
   for: bank balance, inventory count, payment processing.
```

### Design (Practical)
```
Q: Design a URL Shortener
A: APIs: POST /shorten → short_code, GET /{code} → 302 redirect
   Data model: (short_code PK, original_url, created_at, user_id, expires_at)
   Short code: base62(auto_increment_id) — unique, compact, no collision
   Storage: PostgreSQL for URLs, Redis for hot URL cache
   Scale: 1K writes/sec → single DB fine; 100K reads/sec → Redis cache is critical
   CDN: cache 301 redirects at edge for most popular URLs
   Analytics: async via Kafka → click consumer → analytics DB

Q: Design a Rate Limiter
A: Algorithm: Token Bucket (allows burst) or Sliding Window Counter (accurate)
   Storage: Redis (shared counter across all app server instances)
   Key: rate_limit:{user_id} or rate_limit:{ip} with TTL = window size
   Response: 429 Too Many Requests + Retry-After header
   Distributed challenge: Redis atomic INCR + EXPIRE for thread-safe counting
   Bypass prevention: check at API Gateway level, not just app layer
```

---

## Notes on SQL Syntax Used in Diagrams

All architecture diagrams in this roadmap use plain text arrows:
```
Component A
    |
    ↓
Component B ──── Side Component
    |
    ↓
Component C
```

Mermaid diagrams are used where the prompt response generates them.
ASCII diagrams work in any text editor, Notion, GitHub, or chat window.

---

*74 topics · 22 levels · Complete 0 → 100 System Design path*
*Built for 2–4 YOE engineers targeting service-based and product companies*

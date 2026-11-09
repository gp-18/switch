# System Design Master Roadmap (HLD + LLD)
 
A dependency-ordered roadmap for learning High-Level Design (HLD) and Low-Level Design (LLD), from internet fundamentals to real-world case studies and interview preparation.
 
Each topic builds on the ones before it. Follow the order, and don't mark a topic as interview-ready until you can explain it without notes, draw it, and answer follow-up questions about failures and alternatives.
 
---
 
## Table of Contents
 
- [How to Use This Roadmap](#how-to-use-this-roadmap)
- [Learning Path](#learning-path)
- [HLD Curriculum](#hld-curriculum)
  - [Part 1: Internet and Networking](#part-1-internet-and-networking)
  - [Part 2: Application Architecture](#part-2-application-architecture)
  - [Part 3: Databases and Data Storage](#part-3-databases-and-data-storage)
  - [Part 4: Caching](#part-4-caching)
  - [Part 5: Messaging and Event-Driven Architecture](#part-5-messaging-and-event-driven-architecture)
  - [Part 6: Distributed Systems](#part-6-distributed-systems)
  - [Part 7: Security](#part-7-security)
  - [Part 8: Reliability, Observability, and Operations](#part-8-reliability-observability-and-operations)
  - [Part 9: System Design Fundamentals](#part-9-system-design-fundamentals)
  - [Part 10: End-to-End Architecture](#part-10-end-to-end-architecture)
  - [Part 11: HLD Case Studies](#part-11-hld-case-studies)
- [LLD Curriculum](#lld-curriculum)
  - [Part 1: Object-Oriented Programming](#part-1-object-oriented-programming)
  - [Part 2: UML](#part-2-uml)
  - [Part 3: SOLID and Design Principles](#part-3-solid-and-design-principles)
  - [Part 4: Design Patterns](#part-4-design-patterns)
  - [Part 5: Machine Coding](#part-5-machine-coding)
  - [Part 6: LLD Case Studies](#part-6-lld-case-studies)
- [Interview Preparation](#interview-preparation)
- [Notes Generation Prompt](#notes-generation-prompt)
- [Progress Tracker](#progress-tracker)
- [Repository Structure](#repository-structure)
---
 
## How to Use This Roadmap
 
1. Study topics in order; each one lists only what the next one needs.
2. Generate in-depth notes for each topic using the [Notes Generation Prompt](#notes-generation-prompt), then save them in the matching folder.
3. After every topic, draw its diagram from memory and explain it out loud.
4. Update the [Progress Tracker](#progress-tracker) honestly.
5. Start case studies only after the fundamentals they depend on are complete.
---
 
## Learning Path
 
````mermaid
flowchart TD
    A[Internet Fundamentals] --> B[DNS]
    A --> C[TCP / UDP]
    C --> D[HTTP]
    B --> E[HTTPS / TLS]
    D --> E
    E --> F[CDN]
    E --> G[Proxies]
    G --> H[Load Balancers]
    H --> I[API Gateway]
    I --> J[Application Architecture]
    J --> K[Databases]
    J --> L[Caching]
    K --> L
    J --> M[Messaging]
    K --> N[Distributed Systems]
    L --> N
    M --> N
    N --> O[Security]
    N --> P[Reliability and Observability]
    O --> Q[System Design Fundamentals]
    P --> Q
    Q --> R[HLD Case Studies]
 
    S[OOP] --> T[UML]
    S --> U[SOLID and Design Principles]
    T --> V[Design Patterns]
    U --> V
    V --> W[Machine Coding Framework]
    W --> X[LLD Case Studies]
 
    R --> Y[Interview Preparation]
    X --> Y
````
 
HLD and LLD can be studied in parallel. LLD does not depend on HLD, but both meet at interview preparation.
 
---
 
# HLD Curriculum
 
## Part 1: Internet and Networking
 
### Topic 1: How the Internet Works
 
1. What the internet is
2. Client and server
3. IP addresses
4. Public vs private IP addresses
5. IPv4 vs IPv6
6. NAT
7. Ports
8. Packets
9. Routers and routing
10. ISPs
11. The OSI and TCP/IP models
12. Domain names
13. What happens when you enter a URL in a browser (overview)
### Topic 2: DNS (Domain Name System)
 
1. Why DNS exists
2. DNS hierarchy
3. Recursive resolver
4. Root DNS servers
5. TLD DNS servers
6. Authoritative DNS servers
7. Recursive vs iterative queries
8. DNS records: A, AAAA, CNAME, MX, NS, TXT
9. DNS caching: browser, OS, resolver
10. TTL
11. End-to-end DNS resolution flow
12. DNS propagation
13. DNS failures
14. DNS load balancing
15. GeoDNS
16. Anycast
17. DNS security: spoofing, cache poisoning, DNSSEC
18. DNS over HTTPS and DNS over TLS
19. Route 53 in practice
### Topic 3: TCP and UDP
 
1. Why transport protocols exist
2. TCP vs UDP
3. Three-way handshake
4. Connection termination
5. Sequence numbers and acknowledgements
6. Retransmission and timeouts
7. Flow control
8. Congestion control
9. Packet loss
10. Connections, sockets, and ports
11. UDP characteristics
12. When to use TCP vs UDP
13. QUIC
14. TCP vs QUIC
### Topic 4: HTTP
 
1. HTTP fundamentals
2. Request and response structure
3. Methods
4. Headers and body
5. Status codes
6. Statelessness
7. Cookies and sessions
8. HTTP/1.0 vs HTTP/1.1
9. Persistent connections and keep-alive
10. HTTP/2 and multiplexing
11. Head-of-line blocking
12. HTTP/3
13. Compression
14. Safe and idempotent methods
15. HTTP caching and Cache-Control
16. Conditional requests and ETags
17. REST basics
### Topic 5: HTTPS and TLS
 
1. Why plain HTTP is insecure
2. Confidentiality, integrity, and authentication
3. Hashing
4. Symmetric encryption
5. Asymmetric encryption
6. Public and private keys
7. Digital signatures
8. Certificates and certificate authorities
9. Certificate chains and validation
10. Browser trust stores
11. Key exchange: Diffie-Hellman and ECDHE
12. Session keys
13. TLS 1.2 handshake (message by message)
14. TLS 1.3 handshake (message by message)
15. SSL vs TLS
16. TLS termination: CDN, load balancer, reverse proxy
17. Transport encryption vs end-to-end encryption
18. Mutual TLS (mTLS)
19. TLS failure scenarios
### Topic 6: CDN (Content Delivery Network)
 
1. Why CDNs exist
2. Origin server, edge server, and PoP
3. CDN routing and DNS integration
4. Cache hit and cache miss
5. Cache keys
6. TTL and Cache-Control headers
7. Cache invalidation
8. Static vs dynamic content delivery
9. Origin shielding
10. Browser cache vs CDN cache
11. TLS termination at the edge
12. DDoS protection and WAF integration
13. CloudFront architecture
14. CDN vs reverse proxy vs load balancer vs API gateway
15. Real-world request flow through a CDN
### Topic 7: Proxies
 
1. Why proxies exist
2. Forward proxy
3. Reverse proxy
4. Transparent proxy
5. Forward vs reverse proxy
6. Proxy authentication
7. Proxy caching
8. Reverse proxy routing
9. TLS termination at the proxy
10. NGINX architecture
11. Proxy request lifecycle
12. Reverse proxy vs load balancer
### Topic 8: Load Balancers
 
1. Why load balancing exists
2. Single-server bottlenecks
3. Vertical vs horizontal scaling
4. Load balancer architecture
5. Layer 4 vs Layer 7 load balancing
6. Algorithms: Round Robin, Weighted Round Robin
7. Algorithms: Least Connections, Weighted Least Connections, Least Response Time
8. Algorithms: IP Hash and Consistent Hashing
9. Active and passive health checks
10. Failover
11. Sticky sessions and session persistence
12. Stateless application servers
13. Load balancing across availability zones
14. Load balancing across regions
15. High availability of the load balancer itself
16. Load balancer bottlenecks and failures
17. AWS ALB vs NLB
18. Load balancer vs reverse proxy vs CDN vs API gateway
### Topic 9: API Gateway
 
1. Why API gateways exist
2. Request routing
3. Authentication at the gateway
4. Rate limiting and throttling
5. Request and response transformation
6. Aggregation
7. Backend for Frontend (BFF)
8. AWS API Gateway
9. API gateway vs load balancer vs service mesh
10. Gateway as a single point of failure
---
 
## Part 2: Application Architecture
 
### Topic 10: Architecture Styles
 
1. Client-server architecture
2. Monolithic architecture
3. Modular monolith
4. Service-oriented architecture (SOA)
5. Microservices architecture
6. Serverless architecture
7. Choosing an architecture style
### Topic 11: Servers, Runtimes, and Concurrency
 
1. Web servers vs application servers
2. Runtime environments (WSGI, ASGI)
3. Process vs thread
4. Concurrency vs parallelism
5. Asynchronous programming
6. Synchronous vs asynchronous communication
7. Stateless vs stateful services
### Topic 12: Scaling and Service Infrastructure
 
1. Horizontal vs vertical scaling
2. Auto scaling
3. Service discovery
4. Configuration management
5. Secrets management
6. Service mesh
### Topic 13: API Design and Communication
 
1. API design principles
2. REST APIs
3. GraphQL
4. gRPC
5. WebSockets
6. Server-Sent Events
7. Long polling
8. Webhooks
9. API versioning
10. Pagination
11. API authentication and authorization
12. Rate limiting vs throttling
### Topic 14: Resilience Patterns
 
1. Timeouts
2. Retries with exponential backoff and jitter
3. Circuit breakers
4. Bulkheads
5. Graceful degradation
---
 
## Part 3: Databases and Data Storage
 
### Topic 15: Database Fundamentals
 
1. What a database is and why it exists
2. Database servers
3. Storage engines
4. Data persistence
5. CRUD
6. Query processing
7. Transactions and ACID
8. Primary keys, foreign keys, and constraints
9. Indexes
10. Normalization
11. Denormalization
### Topic 16: SQL Databases
 
1. Relational model: tables, rows, columns
2. Relationships and joins
3. B-tree indexes
4. Query execution plans
5. Query optimization
6. Isolation levels
7. Locking
8. Deadlocks
9. MVCC
10. Connection pooling
11. Read replicas
12. Partitioning
13. PostgreSQL in practice
### Topic 17: NoSQL Databases
 
1. Why NoSQL exists
2. Key-value databases
3. Document databases
4. Wide-column databases
5. Graph databases
6. DynamoDB: partition keys, sort keys, GSIs
7. MongoDB
8. Cassandra
9. Redis as a database
10. SQL vs NoSQL: when to use which
### Topic 18: Distributed Database Concepts
 
1. Replication
2. Leader-follower replication
3. Multi-leader replication
4. Leaderless replication
5. Replication lag
6. Strong consistency vs eventual consistency
7. Read-after-write consistency
8. Quorum reads and writes
9. CAP theorem
10. PACELC
11. Partitioning and sharding
12. Consistent hashing
13. Hot partitions
14. Data locality
15. Database failover
### Topic 19: Database Scaling
 
1. Scaling path: vertical, replicas, sharding
2. Choosing a shard key
3. Resharding
4. CQRS
5. Materialized views
6. Data aggregation
7. OLTP vs OLAP
---
 
## Part 4: Caching
 
### Topic 20: Caching Fundamentals
 
1. Why caching exists
2. Cache hierarchy: browser, CDN, reverse proxy, application, distributed, database buffer
3. Cache hit, miss, and hit ratio
4. Cache keys
5. Eviction policies: LRU, LFU, FIFO
6. TTL
7. Cache-aside
8. Write-through
9. Write-back
10. Write-around
11. Cache invalidation
12. Cache consistency
### Topic 21: Distributed Caching and Redis
 
1. Distributed caching
2. Redis architecture
3. Redis data structures
4. Redis persistence: RDB and AOF
5. Redis replication
6. Redis Cluster
7. Redis failover and Sentinel
8. Memcached vs Redis
9. Cache stampede
10. Cache penetration
11. Cache avalanche
12. Hot keys
13. Cache failure scenarios
---
 
## Part 5: Messaging and Event-Driven Architecture
 
### Topic 22: Message Queue Fundamentals
 
1. Why queues exist
2. Producer, consumer, message, broker
3. Message acknowledgement
4. Visibility timeout
5. Retries
6. Dead-letter queues
7. Message ordering and FIFO queues
8. Delivery guarantees: at-most-once, at-least-once, exactly-once
9. Idempotent consumers
10. Backpressure
### Topic 23: Pub/Sub and Event-Driven Architecture
 
1. Point-to-point vs pub/sub
2. Fan-out
3. Event-driven architecture
4. Event streaming
5. AWS SQS
6. AWS SNS
7. AWS EventBridge
8. RabbitMQ
### Topic 24: Kafka
 
1. Kafka architecture
2. Topics and partitions
3. Offsets
4. Consumer groups
5. Replication and ISR
6. Ordering guarantees
7. Kafka vs RabbitMQ vs SQS
### Topic 25: Distributed Workflow Patterns
 
1. Transactional outbox pattern
2. Inbox pattern
3. Saga pattern: choreography and orchestration
4. Eventual consistency in workflows
5. Asynchronous workflows end to end
---
 
## Part 6: Distributed Systems
 
### Topic 26: Foundations and Failures
 
1. What distributed systems are and why they exist
2. Core challenges
3. Network partitions
4. Partial failures
5. Clock synchronization and logical clocks
6. Timeouts and failure detection
7. Retries and duplicate requests
8. Idempotency
### Topic 27: Coordination
 
1. Race conditions and concurrency
2. Distributed locks
3. Fencing tokens
4. Leader election
5. Quorum
6. Consensus
7. Raft
8. Split brain
### Topic 28: Consistency and Transactions
 
1. Consistency models
2. CAP and PACELC revisited
3. Distributed transactions
4. Two-phase commit
5. Saga vs two-phase commit
6. Exactly-once processing
### Topic 29: Failure Handling at Scale
 
1. Fault tolerance
2. Backpressure
3. Load shedding
4. Graceful degradation
5. Circuit breakers and bulkheads
6. Retry storms
7. Thundering herd
---
 
## Part 7: Security
 
### Topic 30: Authentication and Authorization
 
1. Authentication vs authorization
2. Sessions
3. JWT
4. Access tokens and refresh tokens
5. OAuth 2.0
6. OpenID Connect
7. RBAC
8. ABAC
9. IAM
### Topic 31: Data and Infrastructure Security
 
1. Encryption in transit
2. Encryption at rest
3. KMS
4. Secrets management
5. Least privilege
6. Zero trust
7. Security boundaries
8. Network isolation and private networking (VPC)
9. Firewalls and security groups
10. VPN
11. TLS and mTLS between services
### Topic 32: Web and API Attacks
 
1. API security
2. Rate limiting
3. WAF
4. DDoS protection
5. SQL injection
6. XSS
7. CSRF
8. SSRF
---
 
## Part 8: Reliability, Observability, and Operations
 
### Topic 33: Reliability and Disaster Recovery
 
1. Availability, reliability, durability
2. Fault tolerance, resilience, redundancy
3. Multi-AZ
4. Multi-region
5. Failover
6. Backup and restore
7. RTO and RPO
8. Disaster recovery strategies
### Topic 34: Observability
 
1. Monitoring
2. Logging
3. Metrics
4. Distributed tracing
5. OpenTelemetry
6. Health checks
7. Alerting
### Topic 35: SLIs, SLOs, and Incidents
 
1. SLI
2. SLO
3. SLA
4. Error budgets
5. Incident management
### Topic 36: Testing and Deployment
 
1. Capacity planning
2. Performance testing
3. Load testing
4. Stress testing
5. Chaos engineering
6. Rolling deployments
7. Blue-green deployments
8. Canary deployments
9. Infrastructure as Code
---
 
## Part 9: System Design Fundamentals
 
### Topic 37: Requirements and Quality Attributes
 
1. Functional requirements
2. Non-functional requirements
3. Scalability
4. Availability
5. Reliability
6. Consistency
7. Latency
8. Throughput
9. Bandwidth
### Topic 38: Estimation and Trade-offs
 
1. Back-of-the-envelope calculations
2. QPS and peak QPS
3. Storage estimation
4. Memory estimation
5. Network and bandwidth estimation
6. Bottleneck analysis
7. Single points of failure
8. Cost optimization
9. Making and justifying trade-offs
---
 
## Part 10: End-to-End Architecture
 
### Topic 39: The Complete Request Lifecycle
 
1. User enters a URL
2. DNS resolution
3. TCP or QUIC connection
4. TLS handshake
5. CDN
6. WAF
7. Load balancer
8. API gateway
9. Authentication
10. Application server
11. Cache
12. Database
13. Message queue and background workers
14. Notifications
15. Response to the client
16. Which components are optional, combinable, or reorderable
17. Monolithic reference architecture
18. Microservices reference architecture
19. Serverless reference architecture
20. Cloud-native reference architecture
---
 
## Part 11: HLD Case Studies
 
Ordered from simplest to most complex. Each case study covers: requirements, capacity estimation, API design, data model, architecture, request flow, caching, queues, scaling, failures, security, bottlenecks, trade-offs, and follow-up questions.
 
### Level 1: Core Building Blocks
 
1. URL Shortener
2. Pastebin
3. Rate Limiter
4. Distributed Cache
5. Leaderboard
### Level 2: Async and Real-Time Systems
 
6. Notification System
7. Chat Application
8. WhatsApp
9. Distributed Job Scheduler
10. Logging Platform
11. Metrics Monitoring Platform
### Level 3: Content and Social Platforms
 
12. News Feed
13. Twitter/X
14. Instagram
15. File Upload System
16. Google Drive
17. Dropbox
18. Google Photos
### Level 4: Media and Discovery
 
19. Video Streaming Platform
20. YouTube
21. Netflix
22. Web Crawler
23. Search Engine
24. Recommendation System
### Level 5: Transactions and Location
 
25. Ticket Booking System
26. Payment System
27. E-commerce Platform
28. Location Tracking System
29. Food Delivery System
30. Uber
---
 
# LLD Curriculum
 
## Part 1: Object-Oriented Programming
 
### Topic 1: OOP Basics
 
1. Classes and objects
2. Attributes and methods
3. Constructors
4. Instance, class, and static methods
5. Access modifiers (and Python conventions)
6. Object lifecycle
### Topic 2: OOP Pillars
 
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
5. Method overloading vs overriding
6. Interfaces and abstract classes
### Topic 3: Object Relationships
 
1. Association
2. Aggregation
3. Composition
4. Dependency
5. Composition vs aggregation vs inheritance
---
 
## Part 2: UML
 
### Topic 4: UML Diagrams
 
1. Class diagrams
2. UML notation and arrows
3. Multiplicity
4. Sequence diagrams
5. Activity diagrams
6. State diagrams
7. Use-case diagrams
8. Translating requirements into class diagrams
---
 
## Part 3: SOLID and Design Principles
 
### Topic 5: SOLID Principles
 
1. Single Responsibility Principle
2. Open/Closed Principle
3. Liskov Substitution Principle
4. Interface Segregation Principle
5. Dependency Inversion Principle
### Topic 6: Design Principles
 
1. Separation of concerns
2. Loose coupling and high cohesion
3. Dependency injection
4. Composition over inheritance
5. Programming to interfaces
6. Immutability
7. DRY, KISS, YAGNI
8. Clean code and refactoring
9. Extensibility, testability, maintainability
### Topic 7: Domain Modeling
 
1. Object responsibilities
2. Domain-driven design fundamentals
3. Entities and value objects
4. Aggregates
5. Repositories
6. Domain services vs application services
---
 
## Part 4: Design Patterns
 
Each pattern covers: problem, when to use, when not to use, UML, bad vs refactored Python implementation, trade-offs, common mistakes, related patterns, and how to recognize it in a problem.
 
### Topic 8: Creational Patterns
 
1. Singleton
2. Factory Method
3. Abstract Factory
4. Builder
5. Prototype
### Topic 9: Structural Patterns
 
1. Adapter
2. Decorator
3. Facade
4. Proxy
5. Composite
6. Bridge
7. Flyweight
### Topic 10: Behavioral Patterns
 
1. Strategy
2. Observer
3. State
4. Command
5. Template Method
6. Chain of Responsibility
7. Iterator
8. Mediator
9. Memento
10. Visitor
11. Interpreter
---
 
## Part 5: Machine Coding
 
### Topic 11: Concurrency for LLD
 
1. Threads in Python and the GIL
2. Locks, RLocks, and semaphores
3. Condition variables
4. Producer-consumer problem
5. Thread-safe data structures
### Topic 12: Machine Coding Framework
 
1. Clarify requirements and use cases
2. Identify actors
3. Identify entities
4. Define responsibilities
5. Define relationships
6. Identify interfaces
7. Apply SOLID
8. Select design patterns
9. Draw UML
10. Implement core logic
11. Handle edge cases
12. Add extensibility
13. Test
14. Explain trade-offs
---
 
## Part 6: LLD Case Studies
 
Each case study covers: requirements, actors, entities, UML class and sequence diagrams, patterns used, Python code, edge cases, concurrency, extensibility, testing, and follow-up questions.
 
### Level 1: Data Structures and Games
 
1. LRU Cache
2. LFU Cache
3. Tic-Tac-Toe
4. Snake and Ladder
5. Chess
### Level 2: State Machines
 
6. Vending Machine
7. Coffee Machine
8. ATM
9. Elevator System
10. Parking Lot
### Level 3: Frameworks and Infrastructure
 
11. Logging Framework
12. Rate Limiter
13. Notification Framework
14. Pub/Sub Framework
15. Thread-Safe Queue
16. Job Scheduler
17. File System
### Level 4: Business Systems
 
18. Library Management System
19. Task Management System
20. Inventory Management
21. Shopping Cart
22. Coupon System
23. Wallet
24. Bank Account System
25. Splitwise
### Level 5: Booking and Payments
 
26. Payment Gateway
27. Food Ordering
28. Ride Booking
29. Hotel Booking
30. Movie Ticket Booking
---
 
# Interview Preparation
 
### HLD Interview Framework
 
1. Clarify requirements
2. Define functional requirements
3. Define non-functional requirements
4. Estimate scale
5. Define APIs
6. Design the data model
7. Draw the high-level architecture
8. Walk through the request flow
9. Identify bottlenecks
10. Scale the system
11. Discuss reliability and consistency
12. Discuss security
13. Discuss trade-offs
14. Handle follow-up questions
### LLD Interview Framework
 
1. Clarify requirements
2. Identify entities
3. Define responsibilities
4. Create UML
5. Define interfaces
6. Apply SOLID
7. Select patterns
8. Implement
9. Test
10. Extend the design
11. Discuss trade-offs
### Revision Strategy
 
1. Day 1: learn the topic and write notes
2. Day 3: redraw diagrams from memory
3. Day 7: answer interview questions out loud
4. Day 21: revise using only the revision notes
5. Before interviews: run through the final checklist
### Final Interview Checklist
 
- [ ] Can explain what happens when you type a URL into a browser, end to end
- [ ] Can do back-of-the-envelope estimation without hesitation
- [ ] Can compare SQL vs NoSQL for a given use case
- [ ] Can explain caching strategies and their failure modes
- [ ] Can explain CAP, consistency models, and replication trade-offs
- [ ] Can design at least 15 HLD case studies on a whiteboard
- [ ] Can apply SOLID and pick design patterns for an unseen LLD problem
- [ ] Can solve at least 15 LLD case studies in 60–90 minutes
---
 
# Notes Generation Prompt
 
Use this prompt with any AI tool to learn one subtopic in depth and get the notes as a GitHub-ready Markdown file.
 
**How to use it**
 
1. Copy the prompt below.
2. Replace only the last two lines with the topic and subtopic from this README:
````text
   Topic: How the Internet Works
   Subtopic: Client and server
````
3. Paste it into any AI tool.
4. If the response stops partway, reply `continue`.
5. Save the output in the topic's folder, for example `hld/01-how-the-internet-works/02-client-and-server.md`.
Do one subtopic per prompt. Asking for a whole topic at once makes the explanation shallow.
 
````text
Act as a senior system design instructor, staff-level backend engineer,
distributed systems architect, and product-company interview mentor.
 
I will give you a TOPIC and one SUBTOPIC from my system design learning
roadmap. Teach me that subtopic completely, from beginner level to
interview level, so that I do not need any other tutorial, blog, or
video to understand it. Write the result as a single GitHub-ready
Markdown file.
 
About me:
- I am a developer preparing for system design interviews at
  product-based companies.
- Do not assume I already know advanced concepts. Assume I know only
  the subtopics that come before this one in a normal learning order.
  If you must use a concept I have not learned yet, explain it in one
  or two lines.
- Use Python for code examples unless another language is clearly
  better suited.
 
=== REQUIRED STRUCTURE ===
 
Start the file with:
# <Topic> — <Subtopic>
 
Then cover ALL of the following sections, in this order. If a section
truly does not apply to this subtopic, write one line explaining why
instead of skipping it silently.
 
## 1. What is it?
Explain the concept in beginner-friendly language first, then give a
technically precise definition. Use an analogy if it helps.
 
## 2. Why does it exist?
Explain the actual problem that caused this concept to be introduced.
What was the world like without it?
 
## 3. What problem does it solve?
Explain the exact problem it addresses and what would break without it.
 
## 4. Prerequisites
List what I must already understand, and give a one-line refresher
for each.
 
## 5. Internal Working
Explain how it works internally, step by step. Do not skip
intermediate steps. Start simple and gradually go technically deep.
 
## 6. Complete End-to-End Flow
Use numbered steps: what happens first, second, third, and so on.
Add a Mermaid diagram (flowchart or sequenceDiagram) that matches
the steps.
 
## 7. Component Responsibilities
For every component involved, explain:
- What it does
- What information it receives
- What information it stores
- What information it returns
- Why it exists
- What happens if it fails
Use a table if there are several components.
 
## 8. Architecture Diagram
A Mermaid diagram showing where this fits in a real system. The
diagram must explain the actual system, not just decorate the page.
Explain the diagram in text below it.
 
## 9. Real-World Example
How this works in an actual production system. Use AWS or well-known
companies where useful.
 
## 10. Example Scenario
Walk through one concrete scenario step by step, with realistic
values (IP addresses, ports, headers, numbers, timings).
 
## 11. Failure Scenarios
For each realistic failure:
- What can fail and why
- What happens when it fails
- How the failure is detected
- How it is recovered
- The trade-offs of the recovery approach
 
## 12. Alternatives
Compare alternative approaches in a table and explain when to use each.
 
## 13. Advantages and Disadvantages
Meaningful technical trade-offs, not generic points.
 
## 14. Common Misconceptions
Incorrect assumptions beginners often make, and the correct
understanding for each.
 
## 15. Interview Questions
Group into: Beginner, Intermediate, Advanced, Scenario-based,
and Follow-up questions.
 
## 16. Interview-Ready Answers
Give complete answers to the questions above that I can explain out
loud in an interview. Each answer should be a full paragraph, not
one line.
 
## 17. Practical Implementation
Where appropriate, provide Python, SQL, CLI commands (e.g. dig, curl,
netstat), AWS, or configuration examples. Code must be correct and
runnable, with comments explaining what it shows.
 
## 18. Revision Notes
- Key takeaways (bullet points)
- Important terminology (table: Term | Meaning)
- Things to remember
- A concise 5-line revision summary
 
## 19. Connections
- How this subtopic connects to other system design concepts
  (e.g. DNS connects to CDN, load balancing, failover, TLS).
- What I should already understand before this.
- What I will learn next, and why it becomes easier after this one.
 
=== QUALITY RULES ===
- Technical accuracy over simplicity. No simplifications that become
  wrong. If behavior varies by implementation or version, say so.
- No unexplained terminology. Explain every term the first time it
  appears.
- No unexplained diagrams.
- No isolated definitions without practical context.
- No repetitive filler or motivational text.
- Explain the reasoning behind every design decision.
- Use clean Markdown: headings, numbered steps, tables, fenced code
  blocks with language tags, and Mermaid blocks that render on GitHub.
- Output only the Markdown file content, starting with the # heading.
- If you run out of space, stop at the end of a complete section and
  write: Continued in next response — reply "continue".
 
=== MY INPUT ===
Topic: How the Internet Works
Subtopic: Client and server
````
 
### Prompt for Case Studies
 
When you reach the case studies, use this prompt and change only the last two lines.
 
````text
Act as a senior system design instructor, staff-level backend engineer,
and product-company interview mentor.
 
I will give you a case study from my system design roadmap. Teach me
how to design it completely, as if I were solving it in an interview,
and write the result as a single GitHub-ready Markdown file. Use Python
for code. Explain every term and every design decision. Use Mermaid
diagrams that render on GitHub, and explain each diagram in text.
Output only the Markdown file content.
 
For an HLD case study, cover:
1. Problem statement
2. Clarifying questions to ask the interviewer
3. Functional requirements
4. Non-functional requirements
5. Capacity estimation (show every calculation)
6. API design
7. Database schema and database choice (with reasoning)
8. High-level architecture (Mermaid diagram)
9. Complete request flow and data flow for each main use case
10. Component responsibilities
11. Cache strategy
12. Queue strategy
13. Scaling strategy
14. Failure scenarios and reliability strategy
15. Security
16. Bottlenecks and how to fix them
17. Trade-offs and alternative architectures
18. Interview follow-up questions with full answers
19. Revision summary
 
For an LLD case study, cover:
1. Requirements (functional and non-functional)
2. Clarifying questions
3. Actors and core entities
4. Class responsibilities and relationships
5. UML class diagram (Mermaid classDiagram)
6. Sequence diagram for the main flow (Mermaid sequenceDiagram)
7. Design patterns used and why
8. SOLID principles applied
9. Complete runnable Python code
10. Complete execution flow with a demo run
11. Edge cases
12. Concurrency considerations
13. Extensibility
14. Testing with sample tests
15. Common mistakes and alternative designs
16. Interview follow-up questions with full answers
 
If you run out of space, stop at the end of a complete section and
write: Continued in next response — reply "continue".
 
=== MY INPUT ===
Track: HLD
Case study: URL Shortener
````
 
---
 
# Progress Tracker
 
Statuses: ⬜ Not started · 📖 Learning · ✅ Completed · 🔁 Revised · 🎯 Interview-ready
 
**Interview-ready** means you can explain it without notes, draw it, answer follow-ups, explain failure scenarios, and compare alternatives.
 
### HLD
 
| # | Topic | Depends on | Status |
|---|-------|------------|--------|
| 1 | How the Internet Works | — | ⬜ |
| 2 | DNS | 1 | ⬜ |
| 3 | TCP and UDP | 1 | ⬜ |
| 4 | HTTP | 3 | ⬜ |
| 5 | HTTPS and TLS | 2, 4 | ⬜ |
| 6 | CDN | 2, 5 | ⬜ |
| 7 | Proxies | 4, 5 | ⬜ |
| 8 | Load Balancers | 7 | ⬜ |
| 9 | API Gateway | 8 | ⬜ |
| 10 | Architecture Styles | 9 | ⬜ |
| 11 | Servers, Runtimes, Concurrency | 10 | ⬜ |
| 12 | Scaling and Service Infrastructure | 8, 11 | ⬜ |
| 13 | API Design and Communication | 4, 11 | ⬜ |
| 14 | Resilience Patterns | 13 | ⬜ |
| 15 | Database Fundamentals | 11 | ⬜ |
| 16 | SQL Databases | 15 | ⬜ |
| 17 | NoSQL Databases | 15 | ⬜ |
| 18 | Distributed Database Concepts | 16, 17 | ⬜ |
| 19 | Database Scaling | 18 | ⬜ |
| 20 | Caching Fundamentals | 6, 15 | ⬜ |
| 21 | Distributed Caching and Redis | 18, 20 | ⬜ |
| 22 | Message Queue Fundamentals | 11 | ⬜ |
| 23 | Pub/Sub and Event-Driven Architecture | 22 | ⬜ |
| 24 | Kafka | 23 | ⬜ |
| 25 | Distributed Workflow Patterns | 18, 24 | ⬜ |
| 26 | Distributed Systems Foundations | 18, 22 | ⬜ |
| 27 | Coordination | 26 | ⬜ |
| 28 | Consistency and Transactions | 25, 27 | ⬜ |
| 29 | Failure Handling at Scale | 14, 26 | ⬜ |
| 30 | Authentication and Authorization | 5, 9 | ⬜ |
| 31 | Data and Infrastructure Security | 30 | ⬜ |
| 32 | Web and API Attacks | 30 | ⬜ |
| 33 | Reliability and Disaster Recovery | 18, 29 | ⬜ |
| 34 | Observability | 29 | ⬜ |
| 35 | SLIs, SLOs, and Incidents | 34 | ⬜ |
| 36 | Testing and Deployment | 33 | ⬜ |
| 37 | Requirements and Quality Attributes | 33 | ⬜ |
| 38 | Estimation and Trade-offs | 37 | ⬜ |
| 39 | Complete Request Lifecycle | 1–38 | ⬜ |
 
### LLD
 
| # | Topic | Depends on | Status |
|---|-------|------------|--------|
| 1 | OOP Basics | — | ⬜ |
| 2 | OOP Pillars | 1 | ⬜ |
| 3 | Object Relationships | 2 | ⬜ |
| 4 | UML Diagrams | 3 | ⬜ |
| 5 | SOLID Principles | 2 | ⬜ |
| 6 | Design Principles | 5 | ⬜ |
| 7 | Domain Modeling | 6 | ⬜ |
| 8 | Creational Patterns | 4, 5 | ⬜ |
| 9 | Structural Patterns | 8 | ⬜ |
| 10 | Behavioral Patterns | 9 | ⬜ |
| 11 | Concurrency for LLD | 2 | ⬜ |
| 12 | Machine Coding Framework | 7, 10 | ⬜ |
 
### Case Studies
 
| Track | Completed | Interview-ready |
|-------|-----------|-----------------|
| HLD (30) | 0 / 30 | 0 / 30 |
| LLD (30) | 0 / 30 | 0 / 30 |
 
---
 
# Repository Structure
 
One folder per topic, one file per subtopic.
 
````text
system-design/
├── README.md
├── hld/
│   ├── 01-how-the-internet-works/
│   │   ├── 01-what-the-internet-is.md
│   │   ├── 02-client-and-server.md
│   │   └── ...
│   ├── 02-dns/
│   ├── ...
│   └── case-studies/
│       ├── 01-url-shortener.md
│       └── ...
├── lld/
│   ├── 01-oop-basics/
│   ├── ...
│   └── case-studies/
├── interview/
└── diagrams/
````
 
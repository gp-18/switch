# Master DevOps from 0 → 100: Complete Production Infrastructure Engineering Program
## Linux · Docker · Kubernetes · Terraform · AWS · CI/CD · SRE · Security · Observability
### 0 → 100 | 38 Levels | 120 Topics | Junior → Principal DevOps / SRE / Platform Engineer Edition

---

## What Is This File?

This is a complete **DevOps mastery learning roadmap** that takes you from absolute
beginner to principal-level DevOps, SRE, and Platform Engineer.

It covers the full stack of concerns a real infrastructure engineer must own:
- **Foundations** — Linux, OS internals, Networking, DNS, HTTP, TLS, Shell Scripting
- **Source Control & CI/CD** — Git internals, GitHub Actions, Deployment strategies
- **Containers** — Docker internals, Dockerfiles, Container security, Docker Compose
- **Infrastructure as Code** — Terraform, State, Modules, AWS provisioning
- **Cloud** — AWS compute, networking, storage, IAM, databases, serverless, HA
- **Kubernetes** — Architecture, Workloads, Networking, Storage, Security, Scaling
- **Observability** — Logs, Metrics, Traces, Prometheus, Grafana, OpenTelemetry
- **SRE & Reliability** — SLOs, Error Budgets, Incident Management, Disaster Recovery
- **Security** — DevSecOps, Secrets, Container security, Supply chain, IAM least privilege
- **Production** — Platform Engineering, System Design, Debugging, Chaos Engineering

Every topic is a **copy-paste block** you drop into the Teaching Prompt below.
Claude then teaches that topic with a full lesson: analogy, internal architecture,
infrastructure diagrams, failure scenarios, security implications, trade-offs,
production considerations, and interview Q&As.

---

## The Teaching Prompt

Copy this once. Save it permanently (Notion, Claude Project, sticky note).
Every time you study a topic, paste the topic block into `{PASTE TOPIC HERE}`.

```
You are a Principal DevOps Engineer, Platform Engineer, SRE, Cloud Architect,
and Infrastructure Engineer with 20+ years of real-world production experience
designing, securing, scaling, and operating production systems on Linux, AWS,
Kubernetes, Docker, and Terraform at companies serving millions of users.

Your task is to teach me DevOps — from Linux and networking fundamentals through
Docker, Kubernetes, Terraform, AWS, CI/CD, observability, SRE, and production-grade
platform engineering — in a way that builds genuine infrastructure engineering
judgment, not command memorization.

I want to understand not just HOW to run commands, but WHY each technology exists,
how it works internally, and how to make production infrastructure decisions the
same way a principal engineer would.

I want:
- Clear understanding from Linux fundamentals → production-grade infrastructure
- Engineering judgment — when to use X, when NOT to use X, and why
- Real trade-off analysis (not "it depends" without explanation)
- Internals — what actually happens inside Docker, Kubernetes, Terraform, AWS
- Failure-first thinking — what breaks, how to detect it, how to recover
- Security and cost implications for every architectural decision
- Production-readiness thinking — HA, DR, observability, incident management

---

STRICT TEACHING RULES
1. Start from the PROBLEM — explain WHY the technology exists before the technology
2. Use a simple real-world analogy FIRST (lunchbox for Docker, city for Kubernetes), then go technical
3. Never say "it depends" without explaining exactly what it depends on
4. Always explain WHY — what architectural problem does this solve?
5. Always explain WHEN NOT to use it — over-engineering has a real operational cost
6. Show trade-offs explicitly: performance, cost, reliability, security, complexity
7. Use text-based architecture diagrams (arrows and boxes) for every topic
8. Compare alternatives in a table (e.g. ECS vs EKS, Terraform vs Pulumi, EC2 vs Lambda)
9. Connect every concept to a real production incident or well-known system failure
10. Show the EVOLUTION — how a single server grows into a production platform
11. Show FAILURE SCENARIOS — what breaks and how it cascades
12. Show what a junior DevOps engineer does vs what a senior does vs what an SRE does
13. Include security implications for every infrastructure decision
14. Include interview questions from beginner → advanced
15. End with a hands-on exercise or production debugging scenario
16. Never recommend Kubernetes for every use case — justify every tool choice
17. Highlight DevOps anti-patterns beginners fall into
18. Always explain what happens internally when a command or action is taken

---

OUTPUT FORMAT — use this structure every time, no exceptions:

### 1. Simple Explanation (ELI5 + Real-World Analogy)
### 2. Technical Deep Dive
### 3. Why Does This Exist? (The Problem It Solves)
### 4. How It Works Internally (Architecture Diagram with text arrows)
### 5. When Should You Use It? (Concrete Production Scenarios)
### 6. When Should You NOT Use It? (Anti-patterns + Over-engineering)
### 7. Alternatives Comparison Table
### 8. Trade-offs (Performance / Cost / Reliability / Security / Complexity)
### 9. Evolution (Single Server → HA → Auto-scaling → Multi-region)
### 10. Failure Scenarios (What breaks and how it cascades)
### 11. Security Implications (Threats, mitigations, least privilege)
### 12. Production Considerations (What senior engineers worry about)
### 13. Junior vs Senior vs SRE (How thinking and approach differ)
### 14. Common Mistakes Beginners Make
### 15. Interview Questions & Answers (Beginner → Advanced)
### 16. Hands-on Command or Configuration Example
### 17. Production Configuration Example (Real-world, complete)
### 18. Exercise / Production Incident to Debug
### 19. Quick Revision Summary (bullet points, max 10 lines)
### 20. Most Important Takeaway

---

Topic to teach:
👉 {PASTE TOPIC HERE}
```

---

## Roadmap Structure — 38 Levels, 120 Topics

```
LEVEL 0   DevOps Fundamentals & Culture              Topics 1–4
LEVEL 1   Computer & OS Fundamentals                 Topics 5–7
LEVEL 2   Linux Fundamentals                         Topics 8–11
LEVEL 3   Linux Advanced                             Topics 12–15
LEVEL 4   Shell Scripting                            Topics 16–18
LEVEL 5   Networking Fundamentals                    Topics 19–22
LEVEL 6   DNS                                        Topics 23–24
LEVEL 7   HTTP, HTTPS & TLS                          Topics 25–27
LEVEL 8   Load Balancers & Reverse Proxies           Topics 28–29
LEVEL 9   Git Fundamentals                           Topics 30–32
LEVEL 10  Git Advanced & Workflows                   Topics 33–35
LEVEL 11  CI/CD Fundamentals                         Topics 36–38
LEVEL 12  GitHub Actions / GitLab CI                 Topics 39–41
LEVEL 13  Artifact & Image Management                Topics 42–43
LEVEL 14  Docker Fundamentals                        Topics 44–47
LEVEL 15  Docker Advanced & Internals                Topics 48–51
LEVEL 16  Docker Compose                             Topics 52–53
LEVEL 17  Infrastructure as Code                     Topics 54–55
LEVEL 18  Terraform Fundamentals                     Topics 56–59
LEVEL 19  Terraform Advanced                         Topics 60–62
LEVEL 20  Cloud Fundamentals                         Topics 63–64
LEVEL 21  AWS Core Services                          Topics 65–68
LEVEL 22  AWS Networking                             Topics 69–71
LEVEL 23  AWS IAM & Security                         Topics 72–74
LEVEL 24  AWS High Availability & Serverless         Topics 75–77
LEVEL 25  Kubernetes Fundamentals                    Topics 78–81
LEVEL 26  Kubernetes Architecture                    Topics 82–84
LEVEL 27  Kubernetes Workloads                       Topics 85–87
LEVEL 28  Kubernetes Networking                      Topics 88–90
LEVEL 29  Kubernetes Storage & Config                Topics 91–93
LEVEL 30  Kubernetes Security & Scaling              Topics 94–96
LEVEL 31  Helm & GitOps                              Topics 97–99
LEVEL 32  Observability — Logs & Metrics             Topics 100–103
LEVEL 33  Observability — Tracing & OTel             Topics 104–105
LEVEL 34  DevSecOps & Secrets                        Topics 106–109
LEVEL 35  SRE & Reliability                          Topics 110–113
LEVEL 36  Incident Management & DR                   Topics 114–116
LEVEL 37  Performance & Cost Engineering             Topics 117–119
LEVEL 38  Platform Engineering & System Design       Topics 120
```

---

## All 120 Topics at a Glance

### LEVEL 0 — DevOps Fundamentals & Culture
```
Topic 1   What is DevOps? — Dev vs Ops, The Wall of Confusion, Why DevOps Exists
Topic 2   DevOps Lifecycle — Plan, Code, Build, Test, Release, Deploy, Operate, Monitor
Topic 3   CI vs CD vs Continuous Deployment — The Exact Difference
Topic 4   SRE vs DevOps vs Platform Engineering — Roles, Responsibilities, Overlap
```

### LEVEL 1 — Computer & OS Fundamentals
```
Topic 5   CPU, RAM, Storage, Processes, Threads — What Every DevOps Engineer Must Know
Topic 6   Kernel, User Space, System Calls — How Applications Talk to Hardware
Topic 7   Filesystems, File Descriptors, Inodes — Linux Storage Internals
```

### LEVEL 2 — Linux Fundamentals
```
Topic 8   Linux Filesystem Hierarchy — /, /etc, /var, /proc, /sys, /tmp, /opt
Topic 9   Essential Linux Commands — ls, grep, find, awk, sed, xargs, cut, sort, uniq
Topic 10  Linux Permissions — chmod, chown, umask, rwx, sudo, ACL — Why They Matter
Topic 11  Package Management — apt, yum/dnf, snap — Installing and Managing Software
```

### LEVEL 3 — Linux Advanced
```
Topic 12  Processes — ps, top, htop, kill, signals (SIGTERM, SIGKILL), zombie, orphan
Topic 13  systemd — Units, Services, Targets, journalctl, systemctl — Running Apps as Services
Topic 14  Networking in Linux — ip, ss, netstat, curl, tcpdump, iptables, nftables
Topic 15  Linux Performance Tools — vmstat, iostat, sar, lsof, strace, perf
```

### LEVEL 4 — Shell Scripting
```
Topic 16  Bash Scripting Fundamentals — Variables, Conditions, Loops, Functions, Exit Codes
Topic 17  Production-Safe Bash — set -e, set -u, set -o pipefail, traps, error handling
Topic 18  Shell Scripting Patterns — Argument parsing, logging, idempotent scripts, CI usage
```

### LEVEL 5 — Networking Fundamentals
```
Topic 19  OSI Model — Where Real Technologies Fit (not just memorization)
Topic 20  TCP vs UDP — Handshake, Sequence Numbers, Retransmission, When to Use Each
Topic 21  IP, CIDR, Subnetting — 10.0.0.0/16 vs /24, Usable Hosts, Gateway, Routing
Topic 22  Ports, Sockets, and Connections — What Happens When a Service Listens on :8080
```

### LEVEL 6 — DNS
```
Topic 23  DNS Deep Dive — Resolver, Root, TLD, Authoritative, A/CNAME/MX/TXT/NS Records, TTL
Topic 24  DNS in Production — Split-horizon, Private DNS, Route 53, Debugging with dig/nslookup
```

### LEVEL 7 — HTTP, HTTPS & TLS
```
Topic 25  HTTP/1.1 vs HTTP/2 vs HTTP/3 — Keep-alive, Multiplexing, QUIC
Topic 26  TLS — Certificates, CA, Handshake, Symmetric vs Asymmetric, Termination Points
Topic 27  HTTPS in Production — cert-manager, Let's Encrypt, ACM, TLS termination at LB vs app
```

### LEVEL 8 — Load Balancers & Reverse Proxies
```
Topic 28  Load Balancing — L4 vs L7, Algorithms, Health Checks, Sticky Sessions, Draining
Topic 29  Nginx as Reverse Proxy — Config, upstream, proxy_pass, rate limiting, caching
```

### LEVEL 9 — Git Fundamentals
```
Topic 30  Git Internals — Working Tree, Index, Commit Objects, Object Database, .git/
Topic 31  Git Core Commands — clone, add, commit, branch, merge, rebase, push, pull, fetch
Topic 32  Git Remotes — origin, upstream, fetch vs pull, tracking branches
```

### LEVEL 10 — Git Advanced & Workflows
```
Topic 33  Advanced Git — rebase, cherry-pick, reflog, reset, revert, bisect, squash
Topic 34  Git Hooks — pre-commit, commit-msg, pre-push — Automating Quality Gates
Topic 35  Git Workflows — Git Flow vs GitHub Flow vs Trunk-Based Development — Trade-offs
```

### LEVEL 11 — CI/CD Fundamentals
```
Topic 36  CI Pipeline Design — What to Run, In What Order, and Why
Topic 37  CD Strategies — Rolling, Blue/Green, Canary, Recreate, Shadow — When to Use Each
Topic 38  Deployment Safety — Feature Flags, Rollback, Smoke Tests, Deployment Gates
```

### LEVEL 12 — GitHub Actions / GitLab CI
```
Topic 39  GitHub Actions — Workflow, Job, Step, Runner, Trigger, Matrix, Secrets, Artifacts
Topic 40  Building Production CI — Lint, Type Check, Test, Security Scan, Docker Build, Push
Topic 41  Reusable Workflows, Composite Actions, Self-Hosted Runners, Cache Optimization
```

### LEVEL 13 — Artifact & Image Management
```
Topic 42  Artifact Management — Immutable Artifacts, Versioning, Registry, Why latest Tag is Dangerous
Topic 43  Container Registries — ECR, Docker Hub, GHCR — Push, Pull, Scan, Sign
```

### LEVEL 14 — Docker Fundamentals
```
Topic 44  What is Docker? — Container vs VM, What Docker Actually Is and Is Not
Topic 45  Docker Architecture — Client, Daemon, containerd, runc, OCI, Image, Container
Topic 46  Dockerfile — FROM, RUN, COPY, WORKDIR, ENV, ARG, CMD, ENTRYPOINT, USER — Every Instruction
Topic 47  Docker CLI — build, run, exec, logs, ps, stop, rm, images, volumes, networks
```

### LEVEL 15 — Docker Advanced & Internals
```
Topic 48  Docker Internals — Linux Namespaces, cgroups, OverlayFS, Union Filesystems
Topic 49  Docker Image Optimization — Layer Caching, Multi-Stage Builds, Distroless, .dockerignore
Topic 50  Docker Networking — Bridge, Host, None, Custom Networks, Container DNS, Port Mapping
Topic 51  Container Security — Non-Root User, Read-Only Filesystem, Capabilities, Image Scanning
```

### LEVEL 16 — Docker Compose
```
Topic 52  Docker Compose — Services, Networks, Volumes, depends_on, Health Checks, env_file
Topic 53  Docker Compose in Practice — FastAPI + PostgreSQL + Redis + Worker Stack Locally
```

### LEVEL 17 — Infrastructure as Code
```
Topic 54  What is IaC? — Manual Infra vs IaC, Drift, Reproducibility, Version Control
Topic 55  IaC Tools Comparison — Terraform vs Pulumi vs CDK vs Ansible vs CloudFormation
```

### LEVEL 18 — Terraform Fundamentals
```
Topic 56  Terraform Architecture — Provider, Resource, Plan, Apply, Destroy, State
Topic 57  Terraform Language — Variables, Outputs, Locals, Data Sources, Expressions
Topic 58  Terraform State — What It Is, Why It's Critical, Remote State (S3 + DynamoDB Lock)
Topic 59  Terraform Workflow — init, plan, apply, destroy — What Each Does Internally
```

### LEVEL 19 — Terraform Advanced
```
Topic 60  Terraform Modules — Reusability, Input/Output, Versioning, When Modules Help vs Hurt
Topic 61  Terraform in CI/CD — plan on PR, apply on merge, atlantis, terraform cloud
Topic 62  Terraform Pitfalls — State Corruption, Drift, Sensitive Values, Destroying Production
```

### LEVEL 20 — Cloud Fundamentals
```
Topic 63  Cloud Mental Model — Region, AZ, VPC, Subnet, Internet Gateway, NAT, Route Table
Topic 64  Cloud Shared Responsibility Model — What AWS Owns vs What You Own
```

### LEVEL 21 — AWS Core Services
```
Topic 65  AWS Compute — EC2, ECS, EKS, Lambda — When to Use Which
Topic 66  AWS Storage — S3, EBS, EFS — Durability, Performance, Cost, Use Cases
Topic 67  AWS Databases — RDS (Multi-AZ, Read Replicas), DynamoDB, ElastiCache
Topic 68  AWS Messaging — SQS, SNS, EventBridge — Decoupling Services in Production
```

### LEVEL 22 — AWS Networking
```
Topic 69  VPC Design — Public vs Private Subnets, NAT Gateway, Internet Gateway, Bastion
Topic 70  AWS Load Balancers — ALB vs NLB vs CLB — L7 vs L4, Target Groups, Health Checks
Topic 71  Route 53 & CloudFront — DNS Routing Policies, CDN, Edge Caching, WAF
```

### LEVEL 23 — AWS IAM & Security
```
Topic 72  IAM Deep Dive — Users, Groups, Roles, Policies, Trust Policy, Least Privilege
Topic 73  IAM Roles in Practice — EC2 Instance Profile, ECS Task Role, Lambda Execution Role
Topic 74  AWS Security Services — KMS, Secrets Manager, Parameter Store, WAF, Security Hub
```

### LEVEL 24 — AWS High Availability & Serverless
```
Topic 75  AWS High Availability — Multi-AZ, Auto Scaling Groups, Launch Templates, ALB
Topic 76  AWS Serverless — Lambda, API Gateway, EventBridge — When Serverless Fits
Topic 77  AWS Cost Optimization — Reserved vs On-Demand vs Spot, Right-sizing, Cost Explorer
```

### LEVEL 25 — Kubernetes Fundamentals
```
Topic 78  Why Kubernetes? — The Container Orchestration Problem It Solves
Topic 79  Kubernetes Objects — Pod, Deployment, ReplicaSet, Service, Namespace, ConfigMap, Secret
Topic 80  kubectl — apply, get, describe, logs, exec, port-forward — What Each Does Internally
Topic 81  Kubernetes YAML — apiVersion, kind, metadata, spec — Writing Real Manifests
```

### LEVEL 26 — Kubernetes Architecture
```
Topic 82  Control Plane — API Server, etcd, Scheduler, Controller Manager — How They Interact
Topic 83  Worker Node — kubelet, kube-proxy, Container Runtime — What Runs on Every Node
Topic 84  What Happens When You Run kubectl apply — Full Internal Flow from CLI to Pod Running
```

### LEVEL 27 — Kubernetes Workloads
```
Topic 85  Deployment vs StatefulSet vs DaemonSet — When to Use Which
Topic 86  Job and CronJob — Batch Workloads, Backoff Limits, Concurrency Policy
Topic 87  Resource Requests and Limits — CPU Throttling, OOMKilled, QoS Classes
```

### LEVEL 28 — Kubernetes Networking
```
Topic 88  Kubernetes Networking Model — Pod IP, ClusterIP, NodePort, LoadBalancer, Headless
Topic 89  Ingress — Ingress Controller, Rules, TLS, Annotations, Nginx vs Traefik vs ALB
Topic 90  CNI Plugins — Flannel, Calico, Cilium — Network Policies, eBPF
```

### LEVEL 29 — Kubernetes Storage & Config
```
Topic 91  Kubernetes Storage — Volume, PV, PVC, StorageClass, Dynamic Provisioning
Topic 92  ConfigMap vs Secret — When to Use Each, Base64 is Not Encryption
Topic 93  Kubernetes Probes — Liveness, Readiness, Startup — How They Affect Pod Lifecycle
```

### LEVEL 30 — Kubernetes Security & Scaling
```
Topic 94  Kubernetes Security — RBAC, ServiceAccount, PodSecurity, NetworkPolicy, Admission
Topic 95  Horizontal Pod Autoscaler — CPU/Memory Metrics, Custom Metrics, Behavior
Topic 96  Cluster Autoscaler and Karpenter — Node-Level Scaling, Cost Efficiency
```

### LEVEL 31 — Helm & GitOps
```
Topic 97  Helm — Chart, Template, Values, Release, Repository — Why It Exists
Topic 98  GitOps — Git as Source of Truth, Desired State vs Actual State, Drift Detection
Topic 99  Argo CD — Sync, Health, Rollback, App of Apps, Multi-Cluster, RBAC
```

### LEVEL 32 — Observability — Logs & Metrics
```
Topic 100  Observability vs Monitoring — Logs, Metrics, Traces — The Three Pillars
Topic 101  Structured Logging — JSON Logs, Log Levels, Correlation ID, Centralized Logging (ELK/Loki)
Topic 102  Prometheus — Scraping, Targets, Labels, Counter/Gauge/Histogram, Cardinality
Topic 103  Grafana — Dashboards, Panels, Alerts, Variables, RED and USE Methodology
```

### LEVEL 33 — Observability — Tracing & OTel
```
Topic 104  Distributed Tracing — Trace ID, Span, Context Propagation, Jaeger, Tempo
Topic 105  OpenTelemetry — Vendor-Neutral Instrumentation, Collector, Exporter, Auto vs Manual
```

### LEVEL 34 — DevSecOps & Secrets
```
Topic 106  DevSecOps Pipeline — SAST, Dependency Scan, Secret Scan, Container Scan, IaC Scan
Topic 107  Secrets Management — Env Vars vs Kubernetes Secrets vs AWS Secrets Manager vs Vault
Topic 108  Container Security — Minimal Images, Non-Root, Capabilities, Seccomp, AppArmor
Topic 109  Supply Chain Security — SBOM, Image Signing (cosign), Provenance, Trusted Registries
```

### LEVEL 35 — SRE & Reliability
```
Topic 110  SRE Fundamentals — Reliability, Availability Math, SLI, SLO, SLA Definitions
Topic 111  Error Budgets — How They Work, Burn Rate, Alerting on Budget Consumption
Topic 112  High Availability Patterns — Multi-AZ, Stateless Apps, Health Checks, Failover
Topic 113  Scalability — Vertical vs Horizontal, Stateless Design, Database Bottlenecks
```

### LEVEL 36 — Incident Management & DR
```
Topic 114  Incident Management — Severity Levels, Detection, Triage, Mitigation, Postmortem
Topic 115  Disaster Recovery — RPO, RTO, Backup Strategies, Multi-AZ vs Multi-Region
Topic 116  Chaos Engineering — Failure Injection, Game Days, Chaos Monkey, Testing Resilience
```

### LEVEL 37 — Performance & Cost Engineering
```
Topic 117  Performance Engineering — Latency Decomposition, CPU/Memory/Disk/Network Bottlenecks
Topic 118  Production Debugging — CPU spike, Memory leak, Pod crash, 503 after deploy, DB exhaustion
Topic 119  Cost Optimization — Compute, NAT Gateway, Data Transfer, Kubernetes, Reserved Instances
```

### LEVEL 38 — Platform Engineering & System Design
```
Topic 120  Platform Engineering — IDP, Golden Paths, Developer Self-Service, Paved Roads
```

---

## Study Plans

### Quick Revision — Tonight (3 Hours)
```
Hour 1:
  Topic 48  — Docker internals (namespaces, cgroups, OverlayFS)
  Topic 56  — Terraform state — the most misunderstood concept
  Topic 82  — Kubernetes control plane internals
  Topic 84  — What happens when you run kubectl apply

Hour 2:
  Topic 88  — Kubernetes networking (Pod → Service → Ingress)
  Topic 69  — VPC design (public vs private, NAT Gateway)
  Topic 72  — IAM least privilege — roles vs policies
  Topic 93  — Liveness vs readiness vs startup probes

Hour 3:
  Topic 37  — Deployment strategies (Blue/Green, Canary, Rolling)
  Topic 100 — Observability vs monitoring — three pillars
  Topic 110 — SLI, SLO, SLA, error budget math
  Topic 114 — Incident lifecycle — detect → mitigate → postmortem
```

### Interview in 1 Week
```
Day 1:  Level 0–2   (Topics 1–11)   — DevOps fundamentals, Linux, permissions
Day 2:  Level 5–7   (Topics 19–27)  — Networking, DNS, HTTP, TLS
Day 3:  Level 9–12  (Topics 30–41)  — Git, CI/CD, GitHub Actions
Day 4:  Level 14–15 (Topics 44–51)  — Docker (all of it)
Day 5:  Level 18–19 (Topics 56–62)  — Terraform (all of it)
Day 6:  Level 25–28 (Topics 78–90)  — Kubernetes (fundamentals + networking)
Day 7:  Level 32–35 (Topics 100–109) — Observability + DevSecOps
```

### Full Preparation (24 Weeks)
```
Week 1–2:    Level 0–4   (DevOps culture, Linux, Shell Scripting)
Week 3–4:    Level 5–8   (Networking, DNS, HTTP/TLS, Load Balancers)
Week 5–6:    Level 9–13  (Git, CI/CD, GitHub Actions, Artifacts)
Week 7–8:    Level 14–16 (Docker fundamentals, internals, Compose)
Week 9–10:   Level 17–19 (IaC, Terraform fundamentals + advanced)
Week 11–12:  Level 20–24 (Cloud, AWS core, networking, IAM, HA)
Week 13–15:  Level 25–30 (Kubernetes — all levels)
Week 16:     Level 31    (Helm + GitOps + Argo CD)
Week 17–18:  Level 32–33 (Observability — Prometheus, Grafana, OTel)
Week 19–20:  Level 34    (DevSecOps, Secrets, Container Security)
Week 21–22:  Level 35–36 (SRE, Reliability, Incident Mgmt, DR, Chaos)
Week 23:     Level 37    (Performance, Cost Optimization, Debugging)
Week 24:     Level 38    (Platform Engineering + Capstone Design)
```

---

## Topic Priority by Interview Type

### Junior DevOps Engineer Interview
```
★★★  Topic 1   — What is DevOps and why it exists
★★★  Topic 8   — Linux filesystem hierarchy
★★★  Topic 10  — Linux permissions (chmod, chown)
★★★  Topic 12  — Processes and signals (SIGTERM vs SIGKILL)
★★★  Topic 20  — TCP handshake and how connections work
★★★  Topic 23  — DNS resolution — the full flow
★★★  Topic 31  — Git internals — commit, branch, merge
★★★  Topic 36  — CI vs CD — the exact difference
★★★  Topic 44  — What Docker actually is (container vs VM)
★★★  Topic 46  — Dockerfile — every instruction explained
★★★  Topic 79  — Kubernetes objects — Pod, Deployment, Service
★★   Topic 37  — Blue/Green vs Canary deployment
★★   Topic 52  — Docker Compose
★★   Topic 72  — IAM — user vs role vs policy
```

### Mid-Level DevOps / Backend Infrastructure Interview
```
★★★  Topic 35  — Trunk-based vs Git Flow — trade-offs
★★★  Topic 37  — Canary, Blue/Green, Rolling — implementation
★★★  Topic 40  — Production CI pipeline — design and ordering
★★★  Topic 48  — Docker internals — namespaces and cgroups
★★★  Topic 49  — Multi-stage builds and image optimization
★★★  Topic 51  — Container security — non-root, capabilities
★★★  Topic 56  — Terraform state — remote state, locking
★★★  Topic 69  — VPC — public vs private subnet design
★★★  Topic 72  — IAM least privilege — roles, policies, trust
★★★  Topic 82  — Kubernetes control plane — API server, etcd
★★★  Topic 84  — kubectl apply — full internal flow
★★★  Topic 88  — Kubernetes networking — ClusterIP, Ingress
★★★  Topic 102 — Prometheus — scraping, labels, cardinality
★★   Topic 98  — GitOps and Argo CD
★★   Topic 106 — DevSecOps pipeline — scan types and placement
```

### Senior DevOps / SRE / Platform Engineer Round
```
★★★  Topic 61  — Terraform in CI/CD — atlantis, safe apply
★★★  Topic 62  — Terraform state corruption and drift recovery
★★★  Topic 70  — ALB vs NLB — L7 vs L4 trade-offs
★★★  Topic 75  — AWS HA — ASG, Multi-AZ, connection draining
★★★  Topic 87  — Resource requests/limits — OOMKilled, throttling
★★★  Topic 90  — CNI and Network Policies — Calico, Cilium, eBPF
★★★  Topic 94  — Kubernetes RBAC, PodSecurity, Admission webhooks
★★★  Topic 95  — HPA — custom metrics, KEDA, behavior tuning
★★★  Topic 105 — OpenTelemetry — collector pipeline, exporter
★★★  Topic 107 — Secrets Management — Vault vs ASM vs K8s Secrets
★★★  Topic 110 — SLI/SLO/SLA — error budget math and burn rate
★★★  Topic 114 — Incident postmortem — blameless, action items
★★★  Topic 115 — DR — RPO/RTO, backup, multi-region design
★★★  Topic 117 — Latency decomposition — where time goes
★★★  Topic 119 — Cost optimization — NAT Gateway, Spot, Reserved
```

---

## Key Concepts Cheat Sheet

### The DevOps Loop — Full Diagram
```
Developer writes code
         |
    git push (triggers CI)
         |
    ┌────────────────────────────────────┐
    │            CI Pipeline             │
    │  Lint → Type Check → Unit Tests    │
    │  → Integration Tests               │
    │  → SAST (Semgrep, Bandit)         │
    │  → Dependency Scan (Trivy, Snyk)  │
    │  → Secret Scan (Gitleaks)         │
    │  → Docker Build                   │
    │  → Container Scan (Trivy)         │
    │  → Push to ECR (tagged with SHA)  │
    └────────────────────────────────────┘
         |
    CD Pipeline (on merge to main)
         |
    Terraform plan → review → apply (infra changes)
         |
    Helm upgrade / kubectl apply (app changes)
         |
    ┌────────────────────────────────────┐
    │         Kubernetes Cluster         │
    │  Deployment rolls out new pods     │
    │  Readiness probe gates traffic     │
    │  Old pods drain and terminate      │
    └────────────────────────────────────┘
         |
    Prometheus scrapes metrics
    Loki/ELK collects logs
    OTel traces propagated
         |
    Grafana dashboards + alerts
         |
    Incident detected → PagerDuty
         |
    Postmortem → prevention → back to developer
```

### Docker — What Actually Happens Internally
```
docker run nginx
         |
    Docker CLI calls Docker API (HTTP to /var/run/docker.sock)
         |
    Docker Engine (dockerd)
         |
    containerd (manages container lifecycle)
         |
    runc (OCI runtime — actually creates the container)
         |
    Linux Kernel features used:
    ├── namespaces     → isolation (pid, net, mnt, uts, ipc, user)
    │   pid  → container has its own PID 1
    │   net  → container has its own network stack
    │   mnt  → container has its own mount namespace
    ├── cgroups        → resource limits (CPU, memory, I/O)
    └── OverlayFS      → layered filesystem (image layers + writable layer)

Container is NOT a VM.
It shares the HOST kernel.
A Linux container on macOS actually runs inside a Linux VM (Docker Desktop).
```

### Kubernetes — What Happens When You Run kubectl apply
```
kubectl apply -f deployment.yaml
         |
    kubectl reads kubeconfig (~/.kube/config) → picks cluster + credentials
         |
    HTTPS request → kube-apiserver (authenticated + authorized via RBAC)
         |
    Admission Controllers run (MutatingAdmission → ValidatingAdmission)
    — injects sidecar containers if needed (Istio, Vault Agent)
    — validates resource limits, security context, etc.
         |
    Object written to etcd (the cluster's source of truth)
         |
    Deployment Controller (in controller-manager) detects new desired state
    Creates/updates ReplicaSet
         |
    ReplicaSet Controller creates Pod objects
         |
    Scheduler assigns Pod to a Node (based on resources, affinity, taints)
         |
    kubelet on the assigned Node picks up the Pod spec
         |
    kubelet calls container runtime (containerd) → pulls image → starts container
         |
    CNI plugin (Calico/Cilium) assigns Pod IP and sets up networking
         |
    kube-proxy updates iptables/ipvs rules for Service routing
         |
    Readiness probe passes → Pod added to Service Endpoints → receives traffic
```

### Terraform State — Why It's Critical
```
terraform apply
         |
    Terraform reads .tf files (desired state)
         |
    Terraform reads state file (last known actual state)
         |
    Terraform calls Cloud APIs to check real current state
         |
    Plan = desired state - current state = diff to apply
         |
    Terraform applies changes via Cloud API
         |
    State file updated with new actual state

REMOTE STATE (production requirement):
  terraform {
    backend "s3" {
      bucket         = "my-terraform-state"
      key            = "prod/terraform.tfstate"
      region         = "us-east-1"
      dynamodb_table = "terraform-locks"  ← prevents concurrent apply
      encrypt        = true
    }
  }

CRITICAL RULES:
  ❌ Never commit state to Git (contains secrets + resource IDs)
  ❌ Never manually edit the state file
  ❌ Never run terraform apply without terraform plan first
  ✅ Always use remote state with locking in production
  ✅ Use separate state files per environment (dev/staging/prod)
```

### VPC Architecture — The Production Pattern
```
                        Internet
                           |
                    Internet Gateway
                           |
              ┌────────────┴────────────┐
              │           VPC           │
              │      10.0.0.0/16        │
              │                         │
    ┌─────────┴──────────┐ ┌────────────┴──────────┐
    │   Public Subnet     │ │    Public Subnet        │
    │   10.0.1.0/24       │ │    10.0.2.0/24         │
    │   AZ: us-east-1a    │ │    AZ: us-east-1b      │
    │   [ALB]  [Bastion]  │ │    [ALB]               │
    └─────────┬──────────┘ └────────────┬────────────┘
              │  NAT GW                 │  NAT GW
    ┌─────────┴──────────┐ ┌────────────┴────────────┐
    │   Private Subnet    │ │    Private Subnet        │
    │   10.0.3.0/24       │ │    10.0.4.0/24         │
    │   AZ: us-east-1a    │ │    AZ: us-east-1b      │
    │   [ECS/EKS Nodes]   │ │    [ECS/EKS Nodes]     │
    │   [Lambda]          │ │    [Lambda]             │
    └─────────┬──────────┘ └────────────┬────────────┘
              │                         │
    ┌─────────┴──────────┐ ┌────────────┴────────────┐
    │   DB Subnet         │ │    DB Subnet            │
    │   10.0.5.0/24       │ │    10.0.6.0/24         │
    │   AZ: us-east-1a    │ │    AZ: us-east-1b      │
    │   [RDS Primary]     │ │    [RDS Standby]        │
    └────────────────────┘ └─────────────────────────┘

Rules:
  — Internet Gateway routes traffic TO/FROM public subnets
  — NAT Gateway allows private subnets to reach internet OUTBOUND only
  — DB subnets have NO route to internet — not even NAT
  — Security Groups = stateful firewall on resource level
  — NACLs = stateless firewall on subnet level (rarely needed)
```

### SLI / SLO / SLA / Error Budget — The Math
```
DEFINITIONS:
  SLI (Indicator)  = the metric you measure
                     e.g. % of requests with latency < 200ms
  SLO (Objective)  = your internal reliability target
                     e.g. 99.9% of requests < 200ms over 30 days
  SLA (Agreement)  = contractual commitment to customers
                     e.g. 99.5% uptime, breached = credits/refunds
                     SLA is always LOWER than SLO (buffer)
  Error Budget     = 1 - SLO = allowed failure budget

MATH FOR 99.9% SLO (30 days):
  Total minutes     = 30 × 24 × 60 = 43,200 min
  Error budget      = 0.1% × 43,200 = 43.2 min of downtime allowed
  Burn rate of 1    = consuming budget at exactly the SLO rate
  Burn rate of 10   = consuming 10× faster → alert immediately

WHAT ERROR BUDGET DRIVES:
  Budget healthy    → deploy freely, move fast
  Budget burning    → slow down releases, focus on reliability
  Budget exhausted  → freeze non-critical deployments
```

### Deployment Strategies — Decision Table
```
STRATEGY      DOWNTIME  RISK    ROLLBACK   COST    USE WHEN
──────────────────────────────────────────────────────────────────
Recreate      Yes       High    Restart    Low     Dev/staging only
Rolling       No        Medium  Slow       Low     Default for most apps
Blue/Green    No        Low     Instant    High    Critical APIs, DB migrations
Canary        No        Lowest  Instant    Medium  High-risk changes, new features
Shadow        No        None    N/A        High    Testing perf without user impact

GOLDEN RULE:
  Match your strategy to the RISK of the change, not team preference.
  A CSS color change → rolling.
  A payment flow change → canary or blue/green.
  A database schema migration → blue/green with backward-compatible migration first.
```

### Kubernetes Probe Guide
```
LIVENESS PROBE  — Is the app alive? Should Kubernetes restart it?
  Fails → kubelet restarts the container
  Use for: deadlocks, infinite loops, hung processes
  Example: GET /healthz → 200

READINESS PROBE — Is the app ready to serve traffic?
  Fails → Pod removed from Service endpoints (no traffic sent)
  Use for: startup delay, cache warmup, DB connection not ready
  Example: GET /readyz → 200 (checks DB connection)

STARTUP PROBE   — Is the app done starting? (overrides liveness during boot)
  Fails → container killed and restarted (no false kills during slow startup)
  Use for: apps with slow initialization (JVM, ML models loading)

COMMON MISTAKE:
  ❌ Liveness probe checks external dependency (DB, Redis)
     → DB goes down → all pods restart → thundering herd → makes outage worse
  ✅ Liveness probe checks ONLY internal health (is my process responsive?)
  ✅ Readiness probe checks external dependencies (is my DB connection alive?)
```

---

## Anti-Patterns to Mention in Every Interview

These show senior-level thinking. Mention what you are AVOIDING and why.

```
1.  SSHing into production servers and making manual changes
    → Changes are not tracked, not reproducible, and cause drift
    → Use IaC, configuration management, and immutable infrastructure
    → "If it's not in Git, it doesn't exist"

2.  Running containers as root
    → If the app is compromised, attacker has root on the host kernel namespace
    → Always set USER in Dockerfile; use non-root numeric UID
    → Kubernetes: set securityContext.runAsNonRoot: true

3.  Using the latest tag for container images in production
    → latest is mutable — same tag, different image = unpredictable deployments
    → Always tag with Git SHA or semantic version: myapp:1.2.3 or myapp:abc1234
    → Pin image digest (SHA256) for fully reproducible deployments

4.  No resource requests/limits on Kubernetes Pods
    → Noisy neighbor problem — one Pod can starve all others on the node
    → OOMKilled events without limits; scheduling issues without requests
    → Always set both requests and limits; use LimitRange as a safety net

5.  Storing secrets in environment variables in plain text
    → Visible in docker inspect, kubectl describe, and process listings
    → Use AWS Secrets Manager, HashiCorp Vault, or External Secrets Operator
    → Kubernetes Secrets are base64 — not encrypted at rest by default (enable etcd encryption)

6.  terraform apply directly from a developer's laptop to production
    → No review, no audit trail, inconsistent state, potential for accidents
    → Use CI/CD for Terraform: plan on PR (reviewed), apply on merge (audited)
    → Use Atlantis or Terraform Cloud for PR-based workflows

7.  No readiness probe — or readiness probe same as liveness probe
    → Without readiness, traffic hits Pods that aren't ready → 500 errors
    → Liveness same as readiness → DB outage kills all pods during rolling deploy
    → Separate concerns: liveness = internal health, readiness = external deps

8.  NAT Gateway for all outbound traffic without considering cost
    → NAT Gateway: $0.045/hr + $0.045/GB data processed
    → High-throughput services (S3, DynamoDB) should use VPC Endpoints instead
    → VPC Endpoints eliminate NAT Gateway charges for supported AWS services

9.  No postmortem after incidents
    → The same incident repeats because root cause was not addressed
    → Blameless postmortems: focus on systems and processes, not people
    → Every incident → written postmortem → action items → tracked to completion

10. Overusing Kubernetes for every service
    → Kubernetes adds significant operational complexity
    → A simple internal tool does not need a K8s cluster
    → Use EC2 + systemd, ECS Fargate, or Lambda for simpler workloads
    → Kubernetes is justified when you need: many services, complex scheduling,
       custom autoscaling, or advanced networking across many teams
```

---

## Interview Q&A — Most Asked DevOps Questions

### Conceptual (Verbal)
```
Q: What is the difference between a container and a virtual machine?
A: A VM runs a complete OS guest with its own kernel on top of a hypervisor
   (VMware, KVM, Hyper-V). Each VM includes the OS kernel, libraries, and app —
   typically gigabytes in size and seconds to boot.
   A container shares the HOST kernel using Linux namespaces (pid, net, mnt,
   uts, ipc) for isolation and cgroups for resource limits. The container only
   packages the app and its libraries, not the kernel — typically megabytes and
   milliseconds to start. Containers are not inherently more secure than VMs
   because kernel sharing means a kernel exploit can escape the container.

Q: Explain the Kubernetes control plane components and their roles.
A: API Server: the only entry point to the cluster — all components communicate
   through it. Validates and persists objects to etcd. Stateless, horizontally
   scalable.
   etcd: a distributed key-value store that holds ALL cluster state. The single
   source of truth. If etcd is lost without backup, the cluster state is gone.
   Scheduler: watches for unscheduled Pods and assigns them to Nodes based on
   resource requests, affinity/anti-affinity rules, taints, and tolerations.
   Controller Manager: runs all the built-in controllers (Deployment, ReplicaSet,
   Node, Job, etc.) in a single process. Each controller watches desired state
   in etcd and reconciles actual state to match it.

Q: What is Terraform state and why does it matter?
A: Terraform state is a JSON file that maps your Terraform resource definitions
   to real infrastructure objects in the cloud (resource ID, attributes, etc.).
   Without state, Terraform cannot know what already exists — it would try to
   create everything fresh every time. State enables plan to show only the diff.
   In production, state MUST be stored remotely (S3 + DynamoDB for locking)
   because: (1) team members need access to the same state, (2) local state
   gets lost if the laptop is destroyed, (3) concurrent applies without locking
   cause state corruption. State can contain sensitive values — encrypt it.

Q: What is the difference between a liveness and readiness probe in Kubernetes?
A: Liveness: Is the app still running and responsive? If it fails, kubelet
   restarts the container. Use it to detect deadlocks or hung processes.
   It should ONLY check internal health — never check external dependencies like
   databases, because a DB outage would restart all Pods creating a thundering
   herd.
   Readiness: Is the app ready to serve user traffic? If it fails, the Pod is
   removed from the Service's endpoints (no traffic routed to it) but NOT
   restarted. Use it to check external dependency health and startup warmup.

Q: What is an error budget and how do teams use it?
A: Error budget = 1 - SLO. If your SLO is 99.9% availability, your error budget
   is 0.1% — about 43 minutes of downtime per month. When the budget is healthy,
   teams deploy frequently and take risks. When it's burning fast (high burn rate),
   teams freeze deployments and focus on reliability. When it's exhausted, all
   non-critical changes stop until the next measurement window. Error budgets
   align developer and SRE incentives: developers want to ship; SREs want
   stability. The error budget makes this a shared, data-driven conversation.
```

### Practical (Debugging)
```
Q: A deployment succeeded but users are getting 503 errors. What do you check?
A: 1. kubectl get pods — are pods Running? or CrashLoopBackOff?
   2. kubectl describe pod <name> — check Events for OOMKilled, probe failures
   3. kubectl logs <pod> — app-level errors on startup?
   4. kubectl get endpoints <service> — are any endpoints registered?
      (empty endpoints = all pods failing readiness probe)
   5. kubectl describe service <name> — selector matches pod labels?
   6. Check Ingress — correct serviceName and servicePort?
   7. Check target group health in ALB (if using AWS ALB Ingress)
   8. Check Network Policies — are they blocking traffic?
   Root causes: readiness probe failing, wrong port in service, label mismatch,
   image pull failure, missing ConfigMap/Secret causing crash on startup.

Q: Kubernetes pods are being OOMKilled. What do you do?
A: OOMKilled = container exceeded its memory limit.
   1. kubectl describe pod — confirm OOMKilled in Last State
   2. Check Grafana — what is the pod's actual memory usage over time?
   3. Is it a memory leak (memory grows linearly until kill)?
      → Fix the app: missing cache eviction, unbounded queues, leak
   4. Is it a legitimate need for more memory?
      → Increase resources.limits.memory in the deployment
   5. Is it sudden spike (e.g. large request)?
      → Add circuit breakers, request size limits, streaming instead of buffering
   6. Set a realistic limit: limit should be ~20-30% above normal peak usage
   Do NOT just increase limits without understanding root cause.
```

---

## Production Incident Quick Reference

```
SYMPTOM                           FIRST COMMANDS TO RUN
────────────────────────────────────────────────────────────────────────
Pods in CrashLoopBackOff          kubectl describe pod <name>
                                  kubectl logs <name> --previous
                                  kubectl get events --sort-by=.lastTimestamp

High CPU on node                  kubectl top nodes
                                  kubectl top pods --all-namespaces
                                  docker stats (on the node)

503 errors after deployment       kubectl get endpoints <service>
                                  kubectl describe ingress
                                  kubectl rollout status deployment/<name>
                                  kubectl rollout undo deployment/<name>

Deployment stuck / hanging        kubectl rollout status deployment/<name>
                                  kubectl describe pod (check image pull, probe)
                                  kubectl get events

Database connections exhausted    Check connection pool config in app
                                  Check long-running transactions (pg: pg_stat_activity)
                                  Check worker count vs pool_size
                                  kubectl scale deployment/<name> --replicas=1 (temporary)

Terraform state lock stuck        terraform force-unlock <LOCK_ID>
                                  Check DynamoDB for stale lock entry

NAT Gateway costs spiking         Check VPC Flow Logs — which resource is source?
                                  Consider VPC Endpoints for S3/DynamoDB
                                  Check for misconfigured egress routing
```

### Docker vs VM vs Serverless — Decision Table
```
NEED                                              USE
────────────────────────────────────────────────────────────────────────
Full OS control, heavy workload, 24/7             EC2 (VM)
Containerized app, managed orchestration          ECS Fargate or EKS
Many services, complex scheduling, multi-team     Kubernetes (EKS)
Event-driven, short-duration, unpredictable load  Lambda (Serverless)
Simple internal tool, single app                  EC2 + systemd (no K8s)
Batch jobs, cost-optimized                        EC2 Spot + ECS Batch

OVERENGINEERING WARNING:
  A 3-person startup does not need Kubernetes.
  A single API does not need a service mesh.
  A simple cron job does not need Kafka.
  Start simple → add complexity only when the problem demands it.
```

---

*120 topics · 38 levels · Complete DevOps 0 → 100 path*
*Covers Linux, Networking, Docker, Terraform, AWS, Kubernetes, CI/CD,*
*Observability, DevSecOps, SRE, Incident Management, Platform Engineering*
*Built for developers targeting junior → principal DevOps / SRE / Platform Engineer roles*

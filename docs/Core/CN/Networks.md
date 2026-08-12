# Master Computer Networks from 0 → 100: Complete Packet-Level Networking Program
## TCP/IP · DNS · HTTP · TLS · Routing · Linux Networking · Docker · Kubernetes · AWS · Security
### 0 → 100 | 36 Levels | 115 Topics | Beginner → Principal Network Engineer Edition

---

## What Is This File?

This is a complete **Computer Networks mastery learning roadmap** that takes you from
absolute beginner to principal-level network engineer.

### Why Topics From Other READMEs Are Intentionally Repeated Here

Topics like DNS, HTTP/HTTPS, TLS, Docker Networking, Kubernetes Networking, and AWS VPC
also appear in the DevOps README. **They are repeated here on purpose.**

The DevOps README teaches those topics as *infrastructure tools* — how to configure them,
deploy them, and operate them.

This README teaches the same topics from the **networking internals lens**:
- What packets are sent and in what order
- What headers look like byte-by-byte
- What the OS kernel does internally
- What changes at every network hop
- How to diagnose failure at the packet level

A DevOps engineer who configures Kubernetes networking without understanding how veth
pairs, iptables, and CNI plugins work at the packet level will be helpless during a
production network incident. This README closes that gap.

**Rule: If you are studying both DevOps and Networking, do both topics in full. They
teach the same technology from different angles and the combination is what makes a
principal-level engineer.**

---

It covers the full depth of networking a production engineer must own:
- **Fundamentals** — OSI model, encapsulation, Ethernet, MAC, switching, VLANs
- **IP Layer** — IPv4, subnetting, CIDR, VLSM, routing tables, ARP, ICMP, DHCP, NAT
- **Transport Layer** — TCP deep dive, UDP, QUIC, sockets, handshakes, flow/congestion control
- **Application Layer** — DNS internals, HTTP/1.1/2/3, TLS handshake, HTTPS
- **Infrastructure** — Proxies, Load Balancers, CDN, Firewalls, VPN, SSH
- **Linux Networking** — Kernel network stack, ip/ss/tcpdump commands, packet flow in OS
- **Container Networking** — Docker bridge, veth pairs, network namespaces, iptables NAT
- **Kubernetes Networking** — Pod IPs, Services, CNI, kube-proxy, Ingress
- **Cloud Networking** — AWS VPC, subnets, routing, Security Groups, NAT/IGW, Transit GW
- **Advanced** — BGP, OSPF, Zero Trust, mTLS, performance, Wireshark, production debugging

Every topic is a **copy-paste block** you drop into the Teaching Prompt below.
Claude then teaches that topic with a full lesson: analogy, packet-flow diagram,
OS/kernel internals, headers, failure scenarios, troubleshooting commands,
and interview Q&As.

---

## The Teaching Prompt

Copy this once. Save it permanently (Notion, Claude Project, sticky note).
Every time you study a topic, paste the topic block into `{PASTE TOPIC HERE}`.

```
You are a Principal Network Engineer, Cloud Network Architect, Linux Networking
Expert, SRE, and Networking Instructor with 20+ years of real-world production
experience designing, troubleshooting, and operating networks from bare-metal
Ethernet to containerized Kubernetes clusters and global AWS multi-region VPCs.

Your task is to teach me Computer Networks — from physical layer and Ethernet
fundamentals through TCP/IP internals, DNS, HTTP, TLS, Linux kernel networking,
Docker/Kubernetes container networking, and AWS cloud networking — in a way that
builds genuine packet-level engineering understanding, not protocol memorization.

I want to understand not just WHAT each protocol is, but:
- WHY it was invented (what problem it solves)
- HOW packets flow through it byte-by-byte
- WHAT happens inside the OS kernel for each protocol
- WHAT changes at every network hop
- HOW to troubleshoot it at the packet level
- HOW it appears in Linux, Docker, Kubernetes, and AWS

I want:
- Packet-level mental models — source IP, destination IP, source MAC, destination MAC,
  source port, destination port, headers, payload — at every step
- OS internals — what the Linux kernel does for every send() and recv()
- Failure-first thinking — what breaks, how it manifests, how to diagnose
- The ability to read tcpdump/Wireshark output and understand what I see
- Production architecture thinking — how networking decisions affect reliability and cost

---

STRICT TEACHING RULES
1. Start from the PROBLEM — explain WHY the protocol exists before teaching the protocol
2. Use a 3-layer explanation: ELI5 analogy → Technical → Production/Linux/AWS reality
3. Never teach a protocol without showing what the PACKET looks like (header fields)
4. Always show packet flow with source and destination at every hop:
   (src IP, dst IP, src MAC, dst MAC, src port, dst port, protocol)
5. Explain what CHANGES and what DOES NOT CHANGE at each network hop
6. Always explain WHEN NOT to use something — not every protocol fits every situation
7. Use text-based packet-flow diagrams (arrows and boxes) for every topic
8. Compare alternatives in a table (e.g. TCP vs UDP, NAT vs routing, SGvs NACL)
9. Connect every protocol to real production scenarios and actual packet captures
10. Show FAILURE SCENARIOS — what happens when this breaks and how it looks in tcpdump
11. Give concrete troubleshooting commands for each topic
12. Show what a junior network engineer misses vs what a senior network engineer checks
13. Include interview questions from beginner → advanced
14. End with a practical troubleshooting exercise or packet-capture challenge
15. Never say "it's encrypted" without explaining WHAT is encrypted and WHAT is not
16. Never say "the packet goes to the router" without saying WHICH field the router reads
17. Always explain OS-level behavior: what system call, what kernel function, what buffer

---

OUTPUT FORMAT — use this structure every time, no exceptions:

### 1. Simple Explanation (ELI5 + Real-World Analogy)
### 2. Technical Deep Dive
### 3. Why Does This Exist? (The Networking Problem It Solves)
### 4. Packet Structure (Header fields, byte layout, what each field means)
### 5. Packet Flow Diagram (src IP/MAC/port → every hop → dst IP/MAC/port)
### 6. What Changes and What Stays the Same at Each Hop
### 7. OS / Kernel Internals (What the Linux kernel does for this protocol)
### 8. When Should You Use It? (Concrete scenarios)
### 9. When Should You NOT Use It? (Anti-patterns)
### 10. Alternatives Comparison Table
### 11. Trade-offs (Performance / Reliability / Security / Complexity)
### 12. Failure Scenarios (What breaks and how it looks in tcpdump)
### 13. Troubleshooting Commands (With explanation of what each reveals)
### 14. Production Considerations (Linux, Docker, Kubernetes, AWS context)
### 15. Junior vs Senior vs Principal (How packet-level thinking differs)
### 16. Common Mistakes Beginners Make
### 17. Interview Questions & Answers (Beginner → Advanced)
### 18. Hands-On Exercise or Packet Capture Challenge
### 19. Quick Revision Summary (bullet points, max 10 lines)
### 20. Most Important Takeaway

---

Topic to teach:
👉 {PASTE TOPIC HERE}
```

---

## Roadmap Structure — 36 Levels, 115 Topics

```
LEVEL 0   What Is a Network? Fundamentals & Mental Models    Topics 1–4
LEVEL 1   Computer Hardware & OS Networking Basics           Topics 5–7
LEVEL 2   Network Models — OSI & TCP/IP                      Topics 8–10
LEVEL 3   Encapsulation & Packet Anatomy                     Topics 11–12
LEVEL 4   Ethernet & Layer 2 Switching                       Topics 13–16
LEVEL 5   VLANs & Layer 2 Segmentation                       Topics 17–18
LEVEL 6   IPv4 — Addressing & Structure                      Topics 19–22
LEVEL 7   Subnetting & CIDR                                  Topics 23–25
LEVEL 8   IP Routing Fundamentals                            Topics 26–28
LEVEL 9   ARP, ICMP & DHCP                                   Topics 29–31
LEVEL 10  NAT & PAT                                          Topics 32–33
LEVEL 11  Ports, Sockets & the Transport Layer               Topics 34–36
LEVEL 12  TCP — Fundamentals                                 Topics 37–39
LEVEL 13  TCP — Reliability & Flow Control                   Topics 40–42
LEVEL 14  TCP — Congestion Control & Performance             Topics 43–45
LEVEL 15  UDP & QUIC                                         Topics 46–47
LEVEL 16  DNS — Resolution & Records                         Topics 48–51
LEVEL 17  HTTP — All Versions                                Topics 52–56
LEVEL 18  TLS & HTTPS                                        Topics 57–59
LEVEL 19  Proxies, Reverse Proxies & Load Balancers          Topics 60–62
LEVEL 20  CDN & Session Management                           Topics 63–64
LEVEL 21  Firewalls & Network Security                       Topics 65–67
LEVEL 22  VPN, IPsec & SSH                                   Topics 68–70
LEVEL 23  Linux Networking — Commands & Interfaces           Topics 71–73
LEVEL 24  Linux Networking — Kernel Stack & Packet Flow      Topics 74–76
LEVEL 25  Docker Networking Internals                        Topics 77–80
LEVEL 26  Kubernetes Networking Internals                    Topics 81–85
LEVEL 27  AWS VPC & Cloud Networking                         Topics 86–90
LEVEL 28  Advanced AWS Networking                            Topics 91–93
LEVEL 29  Advanced Routing — OSPF & BGP                      Topics 94–96
LEVEL 30  Network Security Architecture                      Topics 97–99
LEVEL 31  Network Performance & MTU                          Topics 100–102
LEVEL 32  Packet Capture & Analysis                          Topics 103–105
LEVEL 33  Network Troubleshooting Framework                  Topics 106–108
LEVEL 34  High Availability & Distributed Systems Networking Topics 109–111
LEVEL 35  Network System Design                              Topics 112–114
LEVEL 36  Production Architecture & Capstone                 Topic 115
```

---

## All 115 Topics at a Glance

### LEVEL 0 — What Is a Network? Fundamentals & Mental Models
```
Topic 1   What Is a Network? LAN, WAN, Internet, Intranet — Why Networks Exist
Topic 2   The Master Mental Model — Application → Socket → TCP/IP → Ethernet → Wire → Destination
Topic 3   Network Topologies — Bus, Star, Mesh, Tree — Why Modern Networks Use Star
Topic 4   Network Devices Overview — NIC, Hub, Switch, Router, Firewall, Proxy, LB
```

### LEVEL 1 — Computer Hardware & OS Networking Basics
```
Topic 5   NIC, Network Buffers, Interrupts — How Hardware Sends and Receives Packets
Topic 6   OS Network Stack — How an Application's send() Becomes Bits on the Wire
Topic 7   File Descriptors, Sockets, and System Calls — The OS Interface to the Network
```

### LEVEL 2 — Network Models — OSI & TCP/IP
```
Topic 8   OSI Model — 7 Layers, Data Units, Protocols, Devices — Not Just Memorization
Topic 9   TCP/IP Model — 4 Layers, How It Maps to OSI, Why It's More Relevant
Topic 10  OSI vs TCP/IP — Where Real Protocols Fit and Why the Distinction Matters
```

### LEVEL 3 — Encapsulation & Packet Anatomy
```
Topic 11  Encapsulation — How Data Becomes a Segment → Packet → Frame → Bits
Topic 12  Decapsulation — How the Destination Strips Headers Back to Application Data
```

### LEVEL 4 — Ethernet & Layer 2 Switching
```
Topic 13  Ethernet — Frames, Header Structure, EtherType, FCS — What's on the Wire
Topic 14  MAC Addresses — Structure, Unicast/Multicast/Broadcast, OUI, ARP Relationship
Topic 15  Switching — MAC Table, Learning, Forwarding, Flooding, Aging — Internal Behavior
Topic 16  Hub vs Switch — Collision Domains, Half/Full Duplex, Why Hubs Are Dangerous
```

### LEVEL 5 — VLANs & Layer 2 Segmentation
```
Topic 17  VLANs — 802.1Q Tag, VLAN ID, Access Port vs Trunk Port, Broadcast Isolation
Topic 18  Inter-VLAN Routing — Router-on-a-Stick, Layer 3 Switch, Packet Flow Between VLANs
```

### LEVEL 6 — IPv4 — Addressing & Structure
```
Topic 19  IPv4 — 32-Bit Address, Binary, Dotted Decimal, Network vs Host Portion
Topic 20  IPv4 Header — TTL, Protocol, Checksum, Fragmentation Flags — Every Field
Topic 21  Private vs Public IP — RFC 1918 Ranges, Why Private IPs Cannot Route on Internet
Topic 22  IPv4 Address Classes — History, Why Classes Were Abandoned, CIDR Replacement
```

### LEVEL 7 — Subnetting & CIDR
```
Topic 23  Subnetting From Zero — Why We Subnet, Network Address, Broadcast, Usable Hosts
Topic 24  CIDR Notation — /8 /16 /24 /25 /26 /27 /28 /29 /30 — Every Prefix Calculated
Topic 25  VLSM — Variable Length Subnet Masking — Designing Subnets for Different Team Sizes
```

### LEVEL 8 — IP Routing Fundamentals
```
Topic 26  Routing — How a Packet Decides Where to Go — Routing Table, Next Hop, Longest Prefix Match
Topic 27  Default Gateway — Why Hosts Need It, What Happens Without One, ARP to Gateway
Topic 28  Static vs Dynamic Routing — Administrative Distance, Metrics, Route Selection
```

### LEVEL 9 — ARP, ICMP & DHCP
```
Topic 29  ARP — Request/Reply, ARP Cache, Gratuitous ARP, ARP Spoofing Attack
Topic 30  ICMP — Echo Request/Reply (ping), TTL Exceeded (traceroute), Destination Unreachable
Topic 31  DHCP — DORA Flow (Discover/Offer/Request/ACK), Lease, Renewal, DNS/GW Assignment
```

### LEVEL 10 — NAT & PAT
```
Topic 32  NAT — SNAT vs DNAT, Why NAT Exists, Connection Tracking, NAT Table
Topic 33  PAT (Port Address Translation) — How Many Hosts Share One Public IP
```

### LEVEL 11 — Ports, Sockets & the Transport Layer
```
Topic 34  Ports — Well-Known (0–1023), Registered, Ephemeral — How the OS Picks Them
Topic 35  Sockets — IP + Port + Protocol = Socket, socket(), bind(), listen(), connect()
Topic 36  The Four-Tuple — (src IP, src port, dst IP, dst port) — How OS Demultiplexes Packets
```

### LEVEL 12 — TCP — Fundamentals
```
Topic 37  TCP — Connection-Oriented, Reliable, Ordered — The Problem It Solves vs UDP
Topic 38  TCP Header — Sequence, ACK, Flags (SYN/FIN/RST/PSH/ACK), Window, Checksum
Topic 39  TCP Three-Way Handshake — SYN/SYN-ACK/ACK — Sequence Numbers, State Transitions
```

### LEVEL 13 — TCP — Reliability & Flow Control
```
Topic 40  TCP Reliability — Sequence Numbers, ACK, Retransmission, Duplicate ACK, Reordering
Topic 41  TCP Connection Termination — FIN/ACK/FIN/ACK, TIME_WAIT, Why It Exists
Topic 42  TCP Flow Control — Receive Window, Sliding Window, Zero Window, Window Update
```

### LEVEL 14 — TCP — Congestion Control & Performance
```
Topic 43  TCP Congestion Control — Slow Start, CWND, SSTHRESH, Congestion Avoidance, AIMD
Topic 44  TCP Connection States — LISTEN, SYN_SENT, ESTABLISHED, CLOSE_WAIT, TIME_WAIT
Topic 45  TCP Performance — RTT, Bandwidth-Delay Product, Throughput vs Bandwidth, Latency
```

### LEVEL 15 — UDP & QUIC
```
Topic 46  UDP — Connectionless, No Delivery Guarantee, Header, When UDP Beats TCP
Topic 47  QUIC — Built on UDP, TLS-Integrated, Multiplexed Streams, 0-RTT, Connection Migration
```

### LEVEL 16 — DNS — Resolution & Records
```
Topic 48  DNS Resolution — Browser → OS → Recursive Resolver → Root → TLD → Authoritative
Topic 49  DNS Records — A, AAAA, CNAME, MX, TXT, NS, SOA, SRV, PTR — Use Cases
Topic 50  DNS Caching — TTL, Resolver Cache, Browser Cache, OS Cache, Negative Caching
Topic 51  DNS over UDP vs TCP — When DNS Uses Each, DNS over HTTPS (DoH), DNS Troubleshooting
```

### LEVEL 17 — HTTP — All Versions
```
Topic 52  HTTP — Request/Response Structure, Methods, Headers, Body, Status Codes
Topic 53  HTTP/1.1 — Keep-Alive, Pipelining, Head-of-Line Blocking, Connection Reuse
Topic 54  HTTP/2 — Binary Framing, Multiplexed Streams, HPACK Header Compression, Server Push
Topic 55  HTTP/3 — QUIC Foundation, No HOL Blocking, 0-RTT, Connection Migration
Topic 56  HTTP Status Codes Deep Dive — 200/201/301/302/304/400/401/403/404/429/500/502/503/504
```

### LEVEL 18 — TLS & HTTPS
```
Topic 57  TLS — Symmetric vs Asymmetric Encryption, Certificates, CA, Chain of Trust
Topic 58  TLS Handshake — ClientHello, ServerHello, Certificate, Key Exchange, Finished
Topic 59  HTTPS — TLS over TCP, What Is Encrypted vs Not, TLS Termination Points
```

### LEVEL 19 — Proxies, Reverse Proxies & Load Balancers
```
Topic 60  Forward Proxy vs Reverse Proxy — Packet Flow, IP Headers, Use Cases
Topic 61  Load Balancers — L4 vs L7, Algorithms, Health Checks, Connection Draining
Topic 62  Nginx as Reverse Proxy — How It Handles Connections, upstream, proxy_pass Internals
```

### LEVEL 20 — CDN & Session Management
```
Topic 63  CDN — Edge PoPs, Cache Hit/Miss, Origin Pull, TTL, Cache Invalidation, Anycast
Topic 64  Session Management — Stateful vs Stateless, Sticky Sessions, Distributed Sessions
```

### LEVEL 21 — Firewalls & Network Security
```
Topic 65  Firewalls — Packet Filtering, Stateful vs Stateless, L3/L4/L7 — What Each Sees
Topic 66  Network Attacks — ARP Spoofing, DNS Spoofing, MITM, SYN Flood, DDoS — How Each Works
Topic 67  Network Security Defenses — Rate Limiting, WAF, DNSSEC, BCP38, Ingress Filtering
```

### LEVEL 22 — VPN, IPsec & SSH
```
Topic 68  VPN — Tunneling, Encryption, Site-to-Site vs Remote Access, Packet-Level Flow
Topic 69  IPsec — AH vs ESP, Transport vs Tunnel Mode, IKE Phase 1/2, Packet Structure
Topic 70  SSH — Key Exchange, Authentication, Port Forwarding (Local/Remote), Bastion Host
```

### LEVEL 23 — Linux Networking — Commands & Interfaces
```
Topic 71  Linux Network Interfaces — eth0, lo, veth, br0, tun0 — ip addr, ip link
Topic 72  Linux Routing & ARP — ip route, ip neigh, routing table internals
Topic 73  Linux Network Tools — ss, ping, traceroute, dig, curl, nc, netstat — What Each Tests
```

### LEVEL 24 — Linux Networking — Kernel Stack & Packet Flow
```
Topic 74  Linux Kernel Network Stack — send() → socket → TCP → IP → netfilter → NIC
Topic 75  iptables & nftables — Tables, Chains, Rules — How Packet Filtering Works in the Kernel
Topic 76  Linux Network Namespaces — Creating Isolation, veth Pairs, Routing Between Namespaces
```

### LEVEL 25 — Docker Networking Internals
```
Topic 77  Docker Bridge Network — docker0 Bridge, veth Pairs, Network Namespace per Container
Topic 78  Docker NAT & iptables — How Port Publishing Works, DNAT, MASQUERADE Rules
Topic 79  Docker DNS — Embedded DNS Server, Container Name Resolution, Custom Networks
Topic 80  Docker Network Modes — Bridge vs Host vs None — Packet Flow for Each
```

### LEVEL 26 — Kubernetes Networking Internals
```
Topic 81  Kubernetes Networking Model — Every Pod Gets an IP, No NAT Between Pods (Rule 1)
Topic 82  CNI — Container Network Interface, How kubelet Calls CNI, IPAM, Plugin Examples
Topic 83  Kubernetes Services — ClusterIP iptables Rules, IPVS, How kube-proxy Works
Topic 84  Kubernetes DNS — CoreDNS, Service A Records, Pod DNS, Search Domains
Topic 85  Ingress Networking — How Traffic Flows from LB → Ingress Controller → Service → Pod
```

### LEVEL 27 — AWS VPC & Cloud Networking
```
Topic 86  AWS VPC — CIDR, Subnets (Public/Private/DB), Route Tables, Implicit Router
Topic 87  AWS Internet Gateway & NAT Gateway — Packet Flow for Inbound and Outbound Traffic
Topic 88  AWS Security Groups — Stateful Filtering, Inbound/Outbound Rules, SG References
Topic 89  AWS Network ACLs — Stateless, Subnet-Level, Rule Numbering, Allow/Deny
Topic 90  Security Group vs Network ACL — The Exact Difference with Packet-Level Examples
```

### LEVEL 28 — Advanced AWS Networking
```
Topic 91  VPC Peering — Routing, CIDR Conflicts, Transitive Peering Limitation
Topic 92  Transit Gateway — Hub-and-Spoke, Route Tables, Attachment Types, Cost
Topic 93  AWS Route 53 — Routing Policies (Simple, Weighted, Latency, Failover, Geolocation)
```

### LEVEL 29 — Advanced Routing — OSPF & BGP
```
Topic 94  Dynamic Routing Fundamentals — Administrative Distance, Metrics, Protocol Comparison
Topic 95  OSPF — Link-State, Areas, LSAs, SPF Algorithm, Cost — Where OSPF Is Used
Topic 96  BGP — Autonomous Systems, eBGP vs iBGP, Path Attributes, Internet Routing, AWS BGP
```

### LEVEL 30 — Network Security Architecture
```
Topic 97  Network Segmentation — Flat Network Risk, DMZ, Defense in Depth
Topic 98  Zero Trust Networking — Never Trust the Network, Identity-Based, Microsegmentation
Topic 99  mTLS — Mutual Authentication, Client Certificate, Use in Service Meshes (Istio)
```

### LEVEL 31 — Network Performance & MTU
```
Topic 100  Network Performance Metrics — Latency, Bandwidth, Throughput, Jitter, Packet Loss
Topic 101  MTU & Fragmentation — Path MTU Discovery, PMTUD Black Holes, MSS Clamping
Topic 102  Bandwidth-Delay Product — Why High-BDP Links Need Large TCP Windows
```

### LEVEL 32 — Packet Capture & Analysis
```
Topic 103  tcpdump — Capture Filters, Read Output, TCP Flags, DNS, HTTP, TLS in Capture
Topic 104  Wireshark — Display Filters, TCP Stream Follow, Retransmissions, Handshake Analysis
Topic 105  Reading a Packet Capture — How to Identify DNS Failure, TCP Reset, TLS Error, Timeout
```

### LEVEL 33 — Network Troubleshooting Framework
```
Topic 106  Systematic Troubleshooting — Application → Socket → Port → Route → ARP → Firewall → DNS → Remote
Topic 107  Common Failure Patterns — Connection Refused vs Timeout vs Reset — What Each Means
Topic 108  Production Network Incidents — 12 Real Scenarios to Debug Step-by-Step
```

### LEVEL 34 — High Availability & Distributed Systems Networking
```
Topic 109  HA Networking — Redundant Links, ECMP, Multi-AZ, DNS Failover, Anycast
Topic 110  Distributed Systems Networking — Partial Failure, Network Partition, Timeouts, Retries
Topic 111  Resilience Patterns — Exponential Backoff, Jitter, Circuit Breaker, Connection Pool
```

### LEVEL 35 — Network System Design
```
Topic 112  Network Design Exercises — Home → Office → Multi-AZ Production → Multi-Region
Topic 113  The Complete Packet Journey — https://example.com From Browser to Response
Topic 114  Production Network Architecture — DNS → CDN → WAF → LB → K8s → DB
```

### LEVEL 36 — Production Architecture & Capstone
```
Topic 115  Capstone — Design a Global Multi-Region Network with Full Packet-Level Walkthrough
```

---

## Study Plans

### Quick Revision — Tonight (3 Hours)
```
Hour 1:
  Topic 2   — The master mental model (Application → Socket → TCP/IP → Ethernet → Wire)
  Topic 11  — Encapsulation (what gets added at each layer)
  Topic 26  — Routing — longest prefix match, next hop selection
  Topic 29  — ARP — how MAC addresses are resolved before every packet

Hour 2:
  Topic 38  — TCP header — sequence, ACK, flags, window
  Topic 39  — TCP three-way handshake — state transitions, ISN
  Topic 48  — DNS resolution — full recursive flow
  Topic 57  — TLS — what is encrypted and what is not

Hour 3:
  Topic 77  — Docker bridge networking — veth pairs, namespaces
  Topic 83  — Kubernetes Services — ClusterIP and iptables rules
  Topic 106 — Troubleshooting framework — the systematic method
  Topic 107 — Connection refused vs timeout vs reset — the exact difference
```

### Interview in 1 Week
```
Day 1:  Level 0–3   (Topics 1–12)   — Mental model, OSI/TCP-IP, encapsulation
Day 2:  Level 4–8   (Topics 13–28)  — Ethernet, VLANs, IP, subnetting, routing
Day 3:  Level 9–11  (Topics 29–36)  — ARP, ICMP, DHCP, NAT, ports, sockets
Day 4:  Level 12–15 (Topics 37–47)  — TCP (all), UDP, QUIC
Day 5:  Level 16–18 (Topics 48–59)  — DNS, HTTP all versions, TLS/HTTPS
Day 6:  Level 19–25 (Topics 60–80)  — LB/Proxy, Firewalls, Linux, Docker networking
Day 7:  Level 26–33 (Topics 81–108) — Kubernetes, AWS, troubleshooting, tcpdump
```

### Full Preparation (16 Weeks)
```
Week 1:      Level 0–3   (Network basics, OSI/TCP-IP, encapsulation)
Week 2:      Level 4–5   (Ethernet, switching, VLANs)
Week 3:      Level 6–7   (IPv4, subnetting, CIDR, VLSM)
Week 4:      Level 8–10  (Routing, ARP, ICMP, DHCP, NAT)
Week 5:      Level 11–12 (Ports, sockets, TCP fundamentals)
Week 6:      Level 13–14 (TCP reliability, flow control, congestion)
Week 7:      Level 15–16 (UDP, QUIC, DNS all aspects)
Week 8:      Level 17    (HTTP/1.1, HTTP/2, HTTP/3)
Week 9:      Level 18–20 (TLS/HTTPS, Proxies, LB, CDN)
Week 10:     Level 21–22 (Firewalls, Security, VPN, SSH)
Week 11:     Level 23–24 (Linux networking, kernel stack, iptables)
Week 12:     Level 25    (Docker networking internals — all 4 topics)
Week 13:     Level 26    (Kubernetes networking internals — all 5 topics)
Week 14:     Level 27–28 (AWS VPC, Security Groups, Route 53, TGW)
Week 15:     Level 29–32 (BGP, OSPF, Security Arch, MTU, tcpdump)
Week 16:     Level 33–36 (Troubleshooting, HA, System Design, Capstone)
```

---

## Topic Priority by Goal

### Networking Interview (Backend / DevOps / SRE)
```
★★★  Topic 2   — The master mental model (most important single topic)
★★★  Topic 11  — Encapsulation — what gets added at each layer
★★★  Topic 23  — Subnetting — every interview asks this
★★★  Topic 26  — Routing and longest prefix match
★★★  Topic 29  — ARP — how does the MAC get resolved?
★★★  Topic 39  — TCP three-way handshake in detail
★★★  Topic 40  — TCP reliability — sequence, ACK, retransmission
★★★  Topic 48  — DNS resolution — the complete recursive flow
★★★  Topic 57  — TLS — what is encrypted and what is not
★★★  Topic 107 — Connection refused vs timeout vs reset
★★   Topic 32  — NAT — how it works internally
★★   Topic 45  — TCP performance — bandwidth-delay product
★★   Topic 56  — HTTP status codes 502 vs 503 vs 504
```

### Docker / Kubernetes Engineer
```
★★★  Topic 74  — Linux kernel network stack
★★★  Topic 75  — iptables — tables, chains, rules
★★★  Topic 76  — Network namespaces and veth pairs
★★★  Topic 77  — Docker bridge — how containers get IPs
★★★  Topic 78  — Docker NAT and port publishing — iptables DNAT
★★★  Topic 81  — Kubernetes networking model — the no-NAT rule
★★★  Topic 82  — CNI — how kubelet assigns Pod IPs
★★★  Topic 83  — Kubernetes Services — iptables rules for ClusterIP
★★★  Topic 84  — CoreDNS — how Pod DNS resolution works
★★★  Topic 85  — Ingress — LB → controller → service → pod packet flow
★★   Topic 79  — Docker DNS — embedded DNS server
★★   Topic 106 — Troubleshooting framework for K8s networking
```

### Cloud / AWS Engineer
```
★★★  Topic 86  — AWS VPC — CIDR, subnets, route tables
★★★  Topic 87  — IGW vs NAT Gateway — packet flow differences
★★★  Topic 88  — Security Groups — stateful, SG references
★★★  Topic 89  — Network ACLs — stateless, rule evaluation order
★★★  Topic 90  — Security Group vs NACL — the exact difference
★★★  Topic 91  — VPC Peering — routing, CIDR conflicts, limitations
★★★  Topic 92  — Transit Gateway — when peering doesn't scale
★★★  Topic 93  — Route 53 routing policies
★★   Topic 96  — BGP — AWS Direct Connect uses eBGP
★★   Topic 63  — CDN — CloudFront internals
```

### Senior / Principal Level
```
★★★  Topic 43  — TCP congestion control — CWND, slow start, AIMD
★★★  Topic 47  — QUIC — why HTTP/3 uses UDP, 0-RTT, multiplexing
★★★  Topic 58  — TLS handshake — ClientHello to session key
★★★  Topic 75  — iptables in depth — conntrack, NAT table
★★★  Topic 96  — BGP — AS_PATH, path attributes, policy
★★★  Topic 98  — Zero Trust — never trust the network
★★★  Topic 99  — mTLS — mutual auth, Istio service mesh
★★★  Topic 101 — MTU and PMTUD — common production black hole
★★★  Topic 103 — tcpdump — read real packet captures
★★★  Topic 110 — Distributed systems networking — partial failure
★★★  Topic 113 — Full packet journey for https://example.com
```

---

## Key Concepts Cheat Sheet

### The Master Mental Model — Every Networking Question Starts Here
```
SENDER                                          RECEIVER

Application (HTTP GET /)
    |
Socket (fd=7, SOCK_STREAM)
    |
TCP Layer
  [src port: 54321, dst port: 443]
  [seq: 1000, ack: 0, SYN flag]
    |
IP Layer
  [src IP: 192.168.1.10, dst IP: 142.250.80.46]
  [TTL: 64, protocol: 6 (TCP)]
    |
Ethernet Layer
  [src MAC: AA:BB:CC:DD:EE:FF]   ← your NIC
  [dst MAC: 11:22:33:44:55:66]   ← your DEFAULT GATEWAY MAC (not server MAC!)
    |
Physical — bits on the wire
    |
    → Router (strips Ethernet, reads IP, looks up route, new Ethernet frame with new MACs)
    → ... multiple hops ...
    → Destination Router
    → Switch
    → Server NIC

Server NIC receives frame
    |
Ethernet (strip frame header, deliver IP packet)
    |
IP (strip IP header, deliver TCP segment)
    |
TCP (strip TCP header, deliver data to socket buffer)
    |
Socket (application reads from buffer)
    |
Application (nginx/FastAPI receives HTTP GET /)

CRITICAL RULE:
  IP addresses stay the SAME end-to-end (except NAT)
  MAC addresses change at EVERY hop
  Port numbers stay the SAME end-to-end (except PAT/NAT)
  TTL decrements by 1 at EVERY router hop
```

### What Changes vs What Stays the Same at Each Hop
```
FIELD             CHANGES?    WHEN
────────────────────────────────────────────────────────
src IP            NO          Unless NAT (SNAT rewrites source IP)
dst IP            NO          Unless DNAT (load balancer, port forward)
src MAC           YES         Every router hop (replaced with router's egress MAC)
dst MAC           YES         Every router hop (replaced with next-hop MAC)
src port          NO          Unless PAT (NAT rewrites source port)
dst port          NO          Unless DNAT (load balancer/reverse proxy)
TTL               YES         Decremented by 1 at every router
IP Checksum       YES         Recalculated after TTL change
Payload           NO          Until decrypted by TLS endpoint
```

### TCP Three-Way Handshake — State Machine
```
CLIENT                                          SERVER
                                          (LISTEN on :443)
SYN
  seq=ISN_c, ack=0
  flags=SYN
─────────────────────────────────────────→
SYN_SENT                                  SYN_RECEIVED
                  SYN-ACK
                    seq=ISN_s, ack=ISN_c+1
                    flags=SYN,ACK
←─────────────────────────────────────────
ACK
  seq=ISN_c+1, ack=ISN_s+1
  flags=ACK
─────────────────────────────────────────→
ESTABLISHED                               ESTABLISHED

ISN = Initial Sequence Number (random, prevents blind injection attacks)
ACK = ISN of the other side + 1 (acknowledges receipt of the SYN)
After ESTABLISHED: data can flow in both directions
```

### DNS Resolution — Full Packet-Level Flow
```
You type: https://api.example.com

1. Browser checks its own DNS cache (TTL-based)
2. OS checks /etc/hosts file
3. OS sends UDP query to configured resolver (from /etc/resolv.conf or DHCP)
   Packet: src=192.168.1.10:54321 dst=8.8.8.8:53 protocol=UDP
   Query: "What is the A record for api.example.com?"

4. 8.8.8.8 (Google's recursive resolver) checks its cache
   Cache miss → resolver starts recursive lookup:

5. Resolver → Root Server (.): "Who handles .com?"
   Root responds: "NS servers for .com are a.gtld-servers.net"

6. Resolver → TLD Server (a.gtld-servers.net): "Who handles example.com?"
   TLD responds: "NS for example.com are ns1.example.com, ns2.example.com"

7. Resolver → Authoritative Server (ns1.example.com): "A record for api.example.com?"
   Authoritative responds: "api.example.com → 104.21.30.50, TTL=300"

8. Resolver caches response (300 seconds TTL)
9. Resolver replies to OS: 104.21.30.50
10. OS caches in resolver cache, returns to browser
11. Browser connects TCP to 104.21.30.50:443

WHY UDP FOR DNS:
  — DNS queries/responses are small (< 512 bytes typically)
  — UDP overhead is lower (no handshake, no state)
  — If response > 512 bytes, DNS uses TCP (zone transfers, DNSSEC)
```

### Subnetting — The Method That Never Fails
```
Given: 10.0.0.0/24 — divide for: 100 hosts, 50 hosts, 20 hosts, 10 hosts

STEP 1: Sort requirements largest first: 100, 50, 20, 10

STEP 2: Find the smallest prefix that fits each:
  100 hosts → need 128 addresses → /25 (126 usable)
  50 hosts  → need  64 addresses → /26 (62 usable)
  20 hosts  → need  32 addresses → /27 (30 usable)
  10 hosts  → need  16 addresses → /28 (14 usable)

STEP 3: Allocate in order:
  10.0.0.0/25     → 10.0.0.1 – 10.0.0.126   (100 hosts team)
  10.0.0.128/26   → 10.0.0.129 – 10.0.0.190  (50 hosts team)
  10.0.0.192/27   → 10.0.0.193 – 10.0.0.222  (20 hosts team)
  10.0.0.224/28   → 10.0.0.225 – 10.0.0.238  (10 hosts team)

QUICK PREFIX TABLE:
  /24 → 256 total, 254 usable
  /25 → 128 total, 126 usable
  /26 →  64 total,  62 usable
  /27 →  32 total,  30 usable
  /28 →  16 total,  14 usable
  /29 →   8 total,   6 usable
  /30 →   4 total,   2 usable  (point-to-point links)
  /31 →   2 total,   2 usable  (special, RFC 3021)
  /32 →   1 total,   1 usable  (host route)
```

### Docker Networking — What Actually Happens Inside
```
docker run -p 8080:80 nginx

WHAT GETS CREATED:
  1. New network namespace for container
  2. veth pair: veth0 (host side) ↔ eth0 (container side)
  3. docker0 bridge: veth0 plugged in
  4. Container eth0: IP from DHCP (172.17.0.2/16)
  5. iptables DNAT rule: 0.0.0.0:8080 → 172.17.0.2:80

PACKET FLOW: curl http://host:8080/
  [src IP: client] → host:8080
  iptables DNAT → 172.17.0.2:80  (source IP unchanged)
  docker0 bridge → veth0 → container eth0
  nginx receives: dst=172.17.0.2:80

PACKET FLOW: container → internet
  container sends: src=172.17.0.2, dst=8.8.8.8
  iptables MASQUERADE (SNAT): src changed to host's eth0 IP
  Host kernel routes packet out eth0

SHOW IT:
  iptables -t nat -L -n -v   → see DNAT and MASQUERADE rules
  ip link show                → see veth pairs
  ip netns list               → see container namespaces
  brctl show docker0          → see which veths are bridged
```

### Kubernetes Service ClusterIP — iptables Under the Hood
```
Service: my-service (ClusterIP: 10.96.0.100:80)
Pods: 10.244.0.2:8080, 10.244.0.3:8080, 10.244.0.4:8080

kube-proxy watches API server for Endpoints changes
kube-proxy writes iptables rules:

PREROUTING chain:
  -d 10.96.0.100/32 -p tcp --dport 80 → KUBE-SVC-my-service

KUBE-SVC-my-service chain:
  statistic mode random probability 0.33 → KUBE-SEP-pod1
  statistic mode random probability 0.50 → KUBE-SEP-pod2
  (default)                             → KUBE-SEP-pod3

KUBE-SEP-pod1 chain:
  DNAT tcp → 10.244.0.2:8080

RESULT:
  Pod A sends: dst=10.96.0.100:80
  iptables intercepts → DNAT → dst=10.244.0.2:8080
  Pod A actually connects to Pod X (one of the 3 backends)
  Pod A never knows the real Pod IP — it only sees the ClusterIP

VERIFY:
  iptables -t nat -L KUBE-SERVICES -n
  iptables -t nat -L KUBE-SVC-<hash> -n
```

### Connection Refused vs Timeout vs Reset — The Exact Difference
```
SYMPTOM               WHAT IT MEANS            LIKELY CAUSE
─────────────────────────────────────────────────────────────────────
Connection refused    Server sent TCP RST       Nothing listening on that port
                      Immediately returned      Port closed, process not running
                                                Firewall actively rejecting (rare)

Connection timeout    No response received      Firewall silently dropping packets
                      Client waits until timeout Routing black hole, host unreachable
                                                AWS Security Group blocking (common)

Connection reset      TCP RST mid-connection    Load balancer killed idle connection
                      After established         Firewall killed connection
                                                Server crashed mid-request

HOW TO DISTINGUISH WITH tcpdump:
  Refused: SYN → RST,ACK (immediate RST back)
  Timeout: SYN → [silence] → SYN → [silence] → SYN... (retransmits, then gives up)
  Reset:   SYN → SYN-ACK → ACK → [data] → RST (during session)

AWS SECURITY GROUPS:
  Default behavior for blocked traffic = TIMEOUT (silent drop)
  This is why "connection timeout" often means "Security Group is blocking you"
  To verify: check sg inbound rules, use VPC Flow Logs, test from another instance
```

---

## Anti-Patterns to Mention in Every Interview

```
1.  Assuming ping proves the application works
    → ping tests ICMP reachability at Layer 3 only
    → Application could be down, port closed, TLS broken — ping still succeeds
    → After ping, test the actual protocol: curl, nc, telnet port, dig

2.  Assuming DNS failure means the internet is down
    → DNS resolution could fail on one machine due to wrong /etc/resolv.conf
    → The target server could be up and reachable by IP
    → Test: ping by IP first; if that works, it's a DNS issue, not network issue

3.  Using 0.0.0.0/0 in Security Groups without understanding
    → Opens the resource to all internet traffic — not just your IP
    → In production: restrict source CIDRs to known ranges or SG references
    → Always ask: who actually needs access to this port?

4.  Flat networks with no segmentation
    → If one host is compromised, attacker can reach everything
    → Use VLANs / VPC subnets / Security Groups to segment workloads
    → DB servers should never be directly reachable from the internet

5.  Not understanding the difference between stateful and stateless filtering
    → Security Group (stateful): if inbound port 80 is allowed, response is automatic
    → NACL (stateless): must explicitly allow BOTH inbound and outbound
    → Forgetting NACL return traffic causes intermittent failures

6.  Hardcoded IP addresses instead of DNS names
    → IP of a service changes during failover, scaling, or migration
    → DNS TTL allows updates to propagate; hardcoded IPs require redeployment
    → Use service discovery or DNS for all internal service communication

7.  No timeout on external connections
    → A connection to a slow service holds a thread/goroutine/connection pool slot
    → Without timeout: one slow dependency cascades into full system failure
    → Always set connect_timeout AND read_timeout for every external call

8.  Retrying on every error without checking if error is retryable
    → Retrying a 400 Bad Request will always fail — stop retrying
    → Retrying a 503 without exponential backoff creates a retry storm
    → Only retry: network errors, 429 (with Retry-After), 503, 504

9.  Not checking MTU before blaming the application
    → PMTUD Black holes: intermediate device drops oversized packets silently
    → Symptom: small payloads work, large payloads time out
    → Test: ping with large packet size and DF bit set: ping -s 1472 -M do <host>

10. Trusting the network inside a VPC
    → A compromised pod/container can reach all other pods in the cluster
    → Use Kubernetes Network Policies to restrict pod-to-pod communication
    → Use mTLS (Istio) so every service authenticates the caller
    → Zero Trust: verify identity, not network location
```

---

## Interview Q&A — Most Asked Networking Questions

### Conceptual (Verbal)
```
Q: What is the difference between a switch and a router?
A: A switch operates at Layer 2 (Data Link) using MAC addresses. It connects
   devices on the SAME network/VLAN and forwards frames based on a MAC address
   table it builds by observing source MACs. A switch does NOT read IP headers.
   A router operates at Layer 3 (Network) using IP addresses. It connects
   DIFFERENT networks and forwards packets based on a routing table. When a
   packet leaves its subnet, it must pass through a router. The router strips
   the old Ethernet frame, reads the destination IP, looks up the next hop,
   and creates a NEW Ethernet frame with new source/destination MACs.

Q: Explain what happens when you type https://example.com in a browser.
A: (1) DNS lookup: browser checks cache → OS checks /etc/hosts → queries recursive
   resolver → resolver iterates Root → TLD → Authoritative → returns IP
   (2) TCP connection: browser opens socket, sends SYN to IP:443, server responds
   SYN-ACK, browser sends ACK — connection ESTABLISHED
   (3) TLS handshake: ClientHello (supported cipher suites) → ServerHello +
   Certificate → client verifies cert chain to trusted CA → key exchange →
   both sides derive session keys → Finished
   (4) HTTP request: browser sends GET / HTTP/1.1 through encrypted TLS tunnel
   (5) Server processes → response → browser renders

Q: What is the difference between 502, 503, and 504?
A: All three are server-side errors often seen behind a reverse proxy:
   502 Bad Gateway: the proxy received an INVALID response from upstream
   (upstream sent garbage, crashed mid-response, or sent wrong protocol)
   503 Service Unavailable: the upstream is DOWN or refused the connection
   (no backend healthy, connection refused, upstream overloaded)
   504 Gateway Timeout: the proxy connected to upstream but got NO response
   within the timeout window (upstream is slow, DB is blocking the handler,
   network between proxy and upstream is broken)
   Mental model: 502=bad answer, 503=no answer (refused), 504=no answer (timeout)

Q: Why do MAC addresses change at every router hop but IP addresses don't?
A: IP addresses are the end-to-end identifiers — they represent the ultimate
   source and destination. Routers use them to make forwarding decisions.
   MAC addresses are the hop-by-hop identifiers — they represent the next device
   to send the frame to on the CURRENT network segment. When a router receives
   a packet, it reads the destination IP, looks up the next-hop IP in its routing
   table, runs ARP to find the MAC of the next-hop, then puts THAT MAC as the
   destination MAC in a NEW Ethernet frame. The old frame is discarded; the
   IP packet (with original src/dst IPs) is re-wrapped in a fresh frame.
```

### Practical (Troubleshooting)
```
Q: A pod in Kubernetes can reach one service but not another. How do you debug?
A: 1. kubectl exec into the pod: kubectl exec -it <pod> -- sh
   2. Test DNS: nslookup <service-name>.<namespace>.svc.cluster.local
      If DNS fails → CoreDNS issue or wrong search domain
   3. Test connectivity by IP: curl http://<clusterIP>:<port>
      If DNS works but IP fails → iptables/kube-proxy issue
   4. Check if target service has endpoints:
      kubectl get endpoints <service-name>
      Empty endpoints → no healthy pods, check pod labels match selector
   5. Check Network Policies:
      kubectl get networkpolicies -n <namespace>
      A NetworkPolicy might be blocking the specific port/namespace
   6. Check if the source namespace has egress allowed to target namespace

Q: HTTP works inside the cluster but not from outside. What do you check?
A: 1. Is the Service type LoadBalancer or NodePort? (ClusterIP is cluster-only)
   2. kubectl get svc — what is the EXTERNAL-IP? If <pending>, cloud LB not provisioned
   3. Check Ingress: kubectl describe ingress — correct host/path rules?
   4. Check Ingress Controller pods: are they running?
   5. Check Security Group on the load balancer — port 80/443 allowed inbound?
   6. Test the LB IP directly with curl — bypasses DNS/Ingress issues
   7. Check TLS certificate — is cert valid for the hostname? Expired?
```

---

## Network Troubleshooting — The Systematic Method
```
APP CANNOT CONNECT TO TARGET

Step 1: Test at the application level
  curl -v http://target:port/path
  → What error? Connection refused? Timeout? TLS error? 4xx/5xx?

Step 2: Test TCP connectivity (remove application layer)
  nc -zv target port        → tests if TCP port is open
  telnet target port        → manual TCP test

Step 3: Test IP reachability (remove transport layer)
  ping target               → tests ICMP (Layer 3) reachability
  traceroute target         → shows each hop and latency

Step 4: Test DNS resolution (if using hostnames)
  dig target                → shows A record returned
  dig @8.8.8.8 target      → tests against specific resolver
  nslookup target           → simpler DNS test

Step 5: Check local routing
  ip route get <target IP>  → which interface and gateway?

Step 6: Check local firewall
  iptables -L -n            → local firewall rules

Step 7: Packet capture to see what's actually happening
  tcpdump -i any host <target> and port <port>
  → See SYN? SYN-ACK? RST? Nothing?

INTERPRET RESULTS:
  ping OK + nc fails   = service not running or firewall on port
  nc OK + curl fails   = application/TLS issue
  ping fails + nc fails = routing or firewall at IP level
  DNS fails + IP works = DNS misconfiguration
  All OK from server but timeout from client = client-side firewall
```

---

*115 topics · 36 levels · Complete Computer Networks 0 → 100 path*
*Topics from DevOps README (DNS, HTTP, TLS, Docker/K8s/AWS networking) are intentionally*
*repeated here — taught from the packet-level and kernel-internals lens, not the config lens*
*Built for developers targeting junior → principal network/cloud/SRE/DevOps engineer roles*

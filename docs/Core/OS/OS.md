# Operating Systems Complete Roadmap
## Computer Architecture · Processes · Memory · File Systems · Linux · Containers · Performance
### 0 → 100 | 30 Levels | 80 Topics | Backend Engineering Edition

---

## What Is This File?

A complete **Operating Systems learning roadmap** that takes you from "what is a CPU"
to production-grade Linux debugging, container internals, and kernel-level understanding.

This is not a collection of interview answers to memorise.
The goal is to understand **how the OS actually works internally** — so you can reason
about why your FastAPI app is slow, why your container was killed, why Redis performs
the way it does, and how to diagnose any production issue from first principles.

Every topic is a **copy-paste block** you drop into the Teaching Prompt below.
Claude teaches it with: ELI5 analogy → technical depth → Linux implementation →
Python connection → real-world example → performance implications → interview Q&As.

---

## The Teaching Prompt

Copy this once. Save it permanently.
Every time you study a topic, paste the topic block into `{PASTE TOPIC HERE}`.

```
You are a Principal Systems Engineer, Linux Kernel Engineer, and Computer Science
educator with 20+ years of real-world industry experience.

Your task is to teach Operating Systems concepts — covering computer architecture,
OS fundamentals, processes, threads, memory, file systems, I/O, Linux internals,
containers, security, and performance — in a way that builds genuine systems-level
engineering understanding, not just interview memorization.

I am a backend developer with 2–4 years of experience (primarily Python/FastAPI).
I know programming but want to understand how the OS actually works underneath —
so I can debug production issues, understand performance bottlenecks, and reason
about systems like a senior engineer.

I want:
- Internal understanding — how it works under the hood, not just what it is
- Connection to Linux — how does the Linux kernel implement this?
- Connection to Python — how does Python interact with this OS concept?
- Connection to production — how does this affect FastAPI, PostgreSQL, Redis, Docker?
- Performance reasoning — what are the implications of this concept on performance?

---

STRICT TEACHING RULES
1. Start with an ELI5 analogy that builds strong intuition
2. Then give the precise technical explanation
3. Explain WHY this concept exists — what problem it solves
4. Explain the internal mechanism — what actually happens in the hardware/kernel
5. Show the Linux implementation — how does Linux handle this specifically?
6. Connect to Python — show how Python code relates to this OS concept
7. Connect to production — show how this affects real systems (FastAPI, Redis, Docker)
8. Show performance implications — what breaks or slows down because of this?
9. Use ASCII diagrams for every concept (flow, hierarchy, state machine)
10. Include Linux commands that demonstrate the concept (ps, strace, top, ss, lsof)
11. Correct common misconceptions explicitly
12. Compare alternatives where they exist
13. Add interview questions from beginner → advanced
14. End with a practical hands-on exercise (Linux command or small Python script)
15. End with Quick Revision Summary (max 10 bullet points)
16. End with Most Important Takeaway

---

OUTPUT FORMAT — use this structure every time:

### 1. Simple Explanation (ELI5 + Analogy)
### 2. Technical Deep Dive
### 3. Why Does This Exist? (The Problem It Solves)
### 4. Internal Mechanism (Hardware + Kernel level)
### 5. Linux Implementation (how Linux specifically handles this)
### 6. Python Connection (how Python code touches this concept)
### 7. Production Relevance (FastAPI / PostgreSQL / Redis / Docker)
### 8. ASCII Architecture Diagram
### 9. Linux Commands to Observe This
### 10. Performance Implications
### 11. Common Misconceptions (correct them explicitly)
### 12. Interview Questions & Answers (Beginner → Advanced)
### 13. Hands-On Exercise
### 14. Quick Revision Summary
### 15. Most Important Takeaway

---

Topic to teach:
👉 {PASTE TOPIC HERE}
```

---

## Roadmap Structure — 30 Levels, 80 Topics

```
LEVEL 0   Computer Fundamentals               Topics 1–4
LEVEL 1   Computer Architecture               Topics 5–8
LEVEL 2   OS Fundamentals                     Topics 9–11
LEVEL 3   Kernel & User Space                 Topics 12–14
LEVEL 4   Processes                           Topics 15–19
LEVEL 5   Threads                             Topics 20–22
LEVEL 6   CPU Scheduling                      Topics 23–25
LEVEL 7   Context Switching                   Topics 26
LEVEL 8   Inter-Process Communication         Topics 27–29
LEVEL 9   Concurrency                         Topics 30–32
LEVEL 10  Synchronization                     Topics 33–35
LEVEL 11  Deadlocks                           Topics 36
LEVEL 12  Memory Management                   Topics 37–38
LEVEL 13  Virtual Memory                      Topics 39–41
LEVEL 14  Paging & Page Tables                Topics 42–44
LEVEL 15  TLB & CPU Caches                    Topics 45–46
LEVEL 16  Memory Mapping & Copy-on-Write      Topics 47–48
LEVEL 17  File Systems                        Topics 49–52
LEVEL 18  Storage & Disk I/O                  Topics 53–54
LEVEL 19  I/O Systems                         Topics 55–56
LEVEL 20  Interrupts & Signals                Topics 57–58
LEVEL 21  Linux Internals                     Topics 59–61
LEVEL 22  Linux Networking                    Topics 62–63
LEVEL 23  Linux Performance Tools             Topics 64–65
LEVEL 24  Security & Permissions              Topics 66–68
LEVEL 25  Virtualization                      Topics 69
LEVEL 26  Containers & Docker                 Topics 70–72
LEVEL 27  OS → Backend Stack Connections      Topics 73–76
LEVEL 28  Production Troubleshooting          Topics 77–78
LEVEL 29  Advanced Linux Internals            Topics 79
LEVEL 30  Common OS Misconceptions            Topics 80
```

---

## All 80 Topics at a Glance

### LEVEL 0 — Computer Fundamentals
```
Topic 1   What is a Computer? — CPU, RAM, Storage, Motherboard, Bus
Topic 2   Program Compilation Pipeline — Source → Compile → Link → Load → Execute
Topic 3   Binary, Machine Code, Assembly, and Why They Matter
Topic 4   What Does the OS Actually Do? (The OS as a Resource Manager)
```

### LEVEL 1 — Computer Architecture
```
Topic 5   CPU Architecture — ALU, Control Unit, Registers, Program Counter
Topic 6   Memory Hierarchy — Registers → L1/L2/L3 Cache → RAM → SSD → HDD
Topic 7   The Instruction Cycle — Fetch → Decode → Execute → Store
Topic 8   Latency Numbers Every Engineer Must Know
         (L1 cache: 0.5ns | RAM: 100ns | SSD: 0.1ms | Network: 1ms)
```

### LEVEL 2 — OS Fundamentals
```
Topic 9   What is an Operating System? Core Responsibilities
Topic 10  Kernel Types — Monolithic vs Microkernel vs Hybrid vs Modular
          (Linux is monolithic with loadable modules — why this matters)
Topic 11  OS Abstraction — Why the OS Hides Hardware Complexity
```

### LEVEL 3 — Kernel & User Space
```
Topic 12  User Mode vs Kernel Mode — Why Two Privilege Levels Exist
          (Ring 0 vs Ring 3 in x86, privileged instructions, protection)
Topic 13  System Calls — The Bridge Between Application and Kernel
          (open, read, write, fork, exec, wait, mmap, socket — what each does)
Topic 14  The System Call Journey:
          Application → Library → System Call → Kernel → Hardware → Return
```

### LEVEL 4 — Processes
```
Topic 15  Program vs Process — Why They Are NOT the Same Thing
Topic 16  Process Lifecycle and States
          (New → Ready → Running → Waiting → Terminated)
Topic 17  Process Control Block (PCB) — What the Kernel Stores Per Process
Topic 18  Process Creation — fork(), exec(), wait() with Linux examples
          (What fork() copies, what exec() replaces, how wait() prevents zombies)
Topic 19  Process Memory Layout
          (Text → Data → BSS → Heap ↑ ... ↓ Stack from high address)
          Zombie processes, orphan processes, process isolation
```

### LEVEL 5 — Threads
```
Topic 20  Thread vs Process — What Is Shared and What Is Private
          (Shared: code, heap, globals, file descriptors | Private: stack, registers, PC)
Topic 21  User Threads vs Kernel Threads — M:N Threading Models
Topic 22  Thread Lifecycle + Thread-Local Storage
          Process vs Thread comparison table (memory, isolation, creation cost, IPC)
```

### LEVEL 6 — CPU Scheduling
```
Topic 23  CPU Scheduling Fundamentals — Scheduler, Ready Queue, Preemption
Topic 24  Scheduling Algorithms — FCFS, SJF, SRTF, Round Robin, Priority,
          Multilevel Queue, Multilevel Feedback Queue (MLFQ)
          (For each: how it works, starvation risk, context switch cost)
Topic 25  Linux CFS — Completely Fair Scheduler
          (How Linux actually schedules — NOT Round Robin, uses red-black tree + vruntime)
```

### LEVEL 7 — Context Switching
```
Topic 26  Context Switching — What Gets Saved and Restored and Why It Is Expensive
          (Registers, PC, SP, kernel stack, TLB flush, CPU cache cold start)
          Process context switch vs Thread context switch — what differs
```

### LEVEL 8 — Inter-Process Communication
```
Topic 27  IPC Overview — Why Processes Need to Communicate
Topic 28  Pipes, Named Pipes (FIFOs), and Shared Memory
          (Pipe: unidirectional, in-kernel buffer | Shared memory: fastest IPC)
Topic 29  Message Queues, Sockets, Signals
          IPC comparison table: speed, data size, complexity, use case
```

### LEVEL 9 — Concurrency
```
Topic 30  Concurrency vs Parallelism — The Critical Distinction
          (Concurrent: multiple tasks make progress | Parallel: truly simultaneous on multiple cores)
Topic 31  Race Conditions — What They Are and Why They Happen
          (Why counter += 1 is NOT thread-safe — 3 operations: load, increment, store)
Topic 32  Python and the GIL — Why Python Threads Cannot Truly Parallelise CPU Work
          (GIL protects CPython internals, asyncio bypasses via I/O waiting, multiprocessing bypasses via separate processes)
```

### LEVEL 10 — Synchronization
```
Topic 33  Mutex and Locks — How Mutual Exclusion Works
          (Lock state: acquired/released, what happens when thread blocks on locked mutex)
Topic 34  Semaphore, Monitor, Condition Variable, Read-Write Lock
          (Counting semaphore for resource pools, condition variable for producer-consumer)
Topic 35  Spinlock vs Blocking Lock vs Atomic Operations
          (Spinlock: busy-waits on CPU | Blocking: yields CPU | Atomic: hardware-level)
```

### LEVEL 11 — Deadlocks
```
Topic 36  Deadlocks — Four Necessary Conditions + Prevention + Detection + Recovery
          (Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait)
          Banker's Algorithm, real backend deadlock examples
          Lock ordering as the primary prevention strategy
```

### LEVEL 12 — Memory Management
```
Topic 37  Physical vs Logical Memory — Address Spaces
          (Each process believes it owns all memory — why this illusion exists)
Topic 38  Memory Allocation — Contiguous vs Dynamic + Fragmentation
          (Internal fragmentation: wasted space inside allocated block
           External fragmentation: free space exists but in non-contiguous chunks)
```

### LEVEL 13 — Virtual Memory
```
Topic 39  Virtual Memory — Why It Is One of the Most Important OS Concepts
          (Isolation, more memory than physical RAM, simplified programming model)
Topic 40  Address Translation — MMU, Page Tables, Virtual → Physical
          Process → Virtual Address → MMU → Page Table → Physical Address → RAM
Topic 41  Page Faults — Minor vs Major and Performance Impact
          (Minor: page exists but not in page table | Major: must read from disk — expensive)
          Demand paging, swapping — when swap is used and why it hurts performance
```

### LEVEL 14 — Paging & Page Tables
```
Topic 42  Pages and Frames — How Memory Is Divided Into Fixed Blocks
          Address calculation: virtual address = page number + offset (numerical examples)
Topic 43  Multi-Level Page Tables and Huge Pages
          (4KB default pages vs 2MB/1GB huge pages — when huge pages matter for performance)
Topic 44  Page Replacement Algorithms — FIFO, LRU, Clock (Second Chance)
          (Why real Linux uses an approximation of LRU, not true LRU)
```

### LEVEL 15 — TLB & CPU Caches
```
Topic 45  TLB — Translation Lookaside Buffer — The Page Table Cache
          CPU → Virtual Address → TLB → Hit (Physical Address) | Miss → Page Table
          TLB flush on context switch, performance implications, TLB miss cost
Topic 46  CPU Cache — L1, L2, L3 — How They Affect Application Performance
          Cache hit vs miss latency, spatial/temporal locality, false sharing in threads,
          why cache-friendly code matters (iterating row-major vs column-major)
```

### LEVEL 16 — Memory Mapping & Copy-on-Write
```
Topic 47  mmap() — Memory-Mapped Files and Shared Memory
          (Map file into address space — reads go through page cache, not read() syscall)
          Anonymous mmap (allocate memory without file), shared vs private mapping
Topic 48  Copy-on-Write (COW) — How fork() Avoids Copying All Memory
          fork() shares all pages with parent (marked read-only), write triggers page fault
          → kernel copies only that page → child gets private copy
          Python multiprocessing + COW: why memory appears to be shared at first
```

### LEVEL 17 — File Systems
```
Topic 49  Files, Directories, and Inodes — The File System Data Model
          Path → Directory entry → Inode → Data blocks (what inode stores: metadata not name)
Topic 50  File Descriptors — The OS Handle for Everything
          stdin(0), stdout(1), stderr(2) — file descriptor table per process
          Pipes, sockets, devices — all accessed as file descriptors
          "Everything is a file" — the Linux abstraction and its limits
Topic 51  Hard Links vs Soft Links — Inode-Level vs Path-Level Linking
Topic 52  Virtual File System (VFS) — The Abstraction Layer Above All File Systems
          VFS unifies: ext4, XFS, tmpfs, procfs, sysfs, overlayfs under one interface
```

### LEVEL 18 — Linux File Systems
```
Topic 53  ext4, XFS, tmpfs — Which File System for Which Workload?
Topic 54  /proc, /sys, /dev, /tmp — What Each Virtual FS Represents
          /proc/<pid>: process info, memory maps, file descriptors
          /sys: kernel and hardware parameters
          /dev: device files (block devices, character devices)
```

### LEVEL 19 — Storage & Disk I/O
```
Topic 55  HDD vs SSD vs NVMe — IOPS, Latency, Sequential vs Random I/O
          (Sequential read: HDD 100MB/s, SSD 500MB/s, NVMe 3500MB/s
           Random IOPS: HDD ~100, SSD ~100K, NVMe ~1M — why databases care)
Topic 56  Page Cache, Direct I/O, fsync(), and Write Buffering
          Linux page cache: OS caches disk reads in RAM (why free memory ≠ wasted memory)
          fsync(): force dirty pages to disk — why databases call it and why it is slow
          Direct I/O: bypass page cache (databases like PostgreSQL use this for control)
```

### LEVEL 20 — I/O Systems
```
Topic 57  Blocking vs Non-Blocking vs Async I/O — The Definitive Comparison
          Blocking: thread waits for I/O | Non-blocking: returns immediately (EAGAIN)
          Async: kernel notifies when I/O is complete (io_uring)
Topic 58  select, poll, epoll, io_uring — How Event-Driven Servers Work
          epoll: O(1) ready notification vs select/poll O(n) scanning
          How Python asyncio uses epoll under the hood
          How Uvicorn/FastAPI handles 10,000 concurrent connections with one thread
```

### LEVEL 21 — Interrupts & Signals
```
Topic 59  Interrupts — Hardware Events That Preempt the CPU
          (Keyboard press, network packet arrival, disk I/O complete → CPU stops, handles interrupt)
          Interrupt handler, top half vs bottom half (deferred work)
Topic 60  Signals — OS-Level Notifications to Processes
          SIGTERM (graceful shutdown request), SIGKILL (force kill — cannot be caught),
          SIGINT (Ctrl+C), SIGHUP (reload config), SIGSTOP/SIGCONT, SIGCHLD
          kill -TERM PID ≠ immediate kill — process can handle SIGTERM
Topic 61  Graceful Shutdown with Signals — Production Pattern
          FastAPI + SIGTERM: how to flush connections, finish in-flight requests, then exit
```

### LEVEL 22 — Linux Internals
```
Topic 62  Linux Process Commands — What Each Shows
          ps aux, top, htop, pstree, pgrep, pidstat
          /proc/<pid>/: status, maps, fd, cmdline, environ
          Process priority (nice -20 to +19), renice to change running process priority
Topic 63  Linux Scheduler — CFS Internals
          Red-black tree ordered by vruntime, always runs lowest vruntime process
          O(1) scheduling, load balancing across CPU cores
```

### LEVEL 23 — Linux Networking
```
Topic 64  TCP Socket Lifecycle from OS Perspective
          socket() → bind() → listen() → accept() → recv()/send() → close()
          Listening socket vs connected socket, accept queue vs backlog
          How FastAPI/Uvicorn maps to this lifecycle
Topic 65  Linux Networking Commands
          ss -tlnp (listening sockets), netstat -an, ip addr, ip route
          tcpdump (capture packets), dig/nslookup (DNS), traceroute
          Network namespaces: how containers get isolated networking
```

### LEVEL 24 — Linux Performance Tools
```
Topic 66  CPU and Load Analysis — top, htop, mpstat, vmstat
          Load average: what 1.0, 2.0, 8.0 means on a 4-core machine
          CPU steal time (in VMs: hypervisor took CPU time from your VM)
          System time vs User time vs I/O wait — diagnosing CPU problems
Topic 67  Memory Analysis — free, vmstat, /proc/meminfo
          Why free memory being low is NOT a problem (Linux uses free RAM as page cache)
          Memory pressure, OOM score, when the OOM killer fires
          Diagnosing memory leaks: smem, /proc/<pid>/smaps
Topic 68  Disk and I/O Analysis + strace Deep Dive
          iostat -xz 1 (disk utilisation, await time, IOPS), iotop
          strace -p <pid>: trace system calls of a running process
          strace use cases: why is my app slow? why can't it open a file? what is it doing?
          lsof -p <pid>: all open file descriptors of a process
          perf top: CPU profiling, which functions consume most CPU
```

### LEVEL 25 — Security & Permissions
```
Topic 69  Linux User, Group, and Permission Model
          rwxr-xr-- decoded: owner|group|others, r=4 w=2 x=1
          chmod 755, chmod +x, chown user:group
          umask: default permission mask for new files
Topic 70  Linux Capabilities and the Least Privilege Principle
          Root vs Capabilities (CAP_NET_BIND_SERVICE, CAP_SYS_PTRACE)
          sudo: temporary privilege elevation — how it works
          setuid bit: run executable as owner regardless of who runs it
Topic 71  SELinux, AppArmor, and Sandboxing
          Mandatory Access Control (MAC) vs Discretionary Access Control (DAC)
          How Docker uses capabilities and seccomp to restrict container syscalls
```

### LEVEL 26 — Virtualization
```
Topic 72  Virtual Machines — Type 1 vs Type 2 Hypervisors
          Type 1: bare metal (VMware ESXi, KVM, Hyper-V)
          Type 2: hosted (VirtualBox, VMware Workstation)
          CPU virtualisation, memory virtualisation, device virtualisation
          VM vs Container — NOT the same thing (VM: full OS; Container: shared kernel)
```

### LEVEL 27 — Containers & Docker
```
Topic 73  Linux Namespaces — The Isolation Mechanism Behind Containers
          PID namespace (container has its own PID 1)
          Network namespace (container has own network stack, interfaces, routing)
          Mount namespace (container has own filesystem view)
          User namespace (container root ≠ host root)
          UTS namespace (container has own hostname)
          IPC namespace (container has own IPC resources)
Topic 74  cgroups — Resource Limits Behind Docker CPU and Memory Limits
          CPU limit: how the kernel enforces --cpus=0.5 (CFS bandwidth control)
          Memory limit: what happens when container exceeds limit (OOM killer)
          docker stats, /sys/fs/cgroup/ — seeing the limits in real files
Topic 75  OverlayFS — How Docker Image Layers Work
          Lower layers (read-only image), upper layer (container writes go here)
          Why starting a container is fast (no copy — just new overlay layer)
          Docker image layer inspection: docker inspect, dive tool
```

### LEVEL 28 — OS → Backend Stack Connections
```
Topic 76  OS → Python Connection
          Python process = OS process, Python thread = OS thread (but GIL limits CPU parallelism)
          asyncio → epoll (Linux) / kqueue (macOS) / IOCP (Windows)
          open() → file descriptor → read() syscall → kernel → returns data
          multiprocessing → fork() (COW, why child starts fast)
          subprocess → fork() + exec() (replaces child with new program)
          socket → OS socket → kernel TCP stack → network

Topic 77  OS → FastAPI + Uvicorn Connection
          uvicorn --workers 4: 4 OS processes, each with asyncio event loop
          Each event loop uses epoll to handle thousands of concurrent connections
          One Uvicorn worker thread path:
          Client → TCP SYN → Kernel accept queue → accept() → socket fd
          → asyncio epoll watches fd → data arrives → read() → FastAPI handler
          → await DB query (yields control back to event loop) → response → send()

Topic 78  OS → PostgreSQL Connection
          One connection = one backend process (fork() per connection)
          Shared memory: buffer pool shared between processes via mmap
          WAL: writes to journal before data pages (fsync for durability)
          Page cache: OS caches PostgreSQL data files in RAM automatically
          OOM killer risk: PostgreSQL + large shared_buffers on low-RAM system

Topic 79  OS → Redis Connection
          Single-threaded event loop (one thread, epoll for I/O multiplexing)
          All data in RAM: malloc() from OS, tracked by /proc/<pid>/status VmRSS
          Persistence (RDB): fork() + COW — parent serves requests, child writes snapshot
          AOF: append to log file (write() syscall per command or batched)
          Why Redis is fast: no context switches from single thread, all in-memory, simple data structures
```

### LEVEL 29 — Production Troubleshooting
```
Topic 80  Systematic Debugging Methodology + 7 Production Incidents

Incident 1: CPU is at 100%
  → top: which process? | pidstat: which thread? | perf top: which function?
  → Is it user time (app code) or system time (syscalls/kernel)?

Incident 2: Server has RAM but app has memory pressure
  → free -h: check actual free vs available
  → /proc/<pid>/smaps: actual RSS per mapping
  → Is swap being used? (vmstat, swapon -s)
  → Is the OOM killer about to fire? (dmesg | grep -i oom)

Incident 3: API requests are hanging
  → ss -tlnp: is the server still listening?
  → lsof -p <pid>: are file descriptors exhausted?
  → strace -p <pid>: what syscall is it blocked on?
  → Is it a deadlock? (pstack or GDB thread apply all bt)

Incident 4: Too many open files error
  → ulimit -n: what is the current fd limit?
  → lsof -p <pid> | wc -l: how many fds is the process holding?
  → Fix: increase limit in /etc/security/limits.conf or systemd service file

Incident 5: Container was killed unexpectedly
  → dmesg | grep -i oom: was it the OOM killer?
  → docker inspect <container>: OOMKilled field
  → docker stats: was it hitting memory limit?
  → Check cgroup memory: /sys/fs/cgroup/memory/<container>/memory.usage_in_bytes

Incident 6: Disk I/O latency suddenly increased
  → iostat -xz 1: check await (ms), util %, r/s, w/s
  → iotop: which process is doing the I/O?
  → Is it random I/O? (a log write pattern changed to random?)
  → Is the page cache being evicted? (memory pressure → less page cache → more disk reads)

Incident 7: Application creating thousands of threads
  → ps -T -p <pid>: list all threads of a process
  → cat /proc/<pid>/status | grep Threads
  → Is a thread pool unbounded? Is each request spawning a new thread?
  → Fix: bounded thread pool with queue + rejection policy
```

### LEVEL 30 — Common OS Misconceptions
```
Topic 81  The 15 Most Common OS Misconceptions — Each Corrected

1.  "Process and program are the same thing"
    → Program: static code on disk | Process: running instance with its own memory, state, PID

2.  "Threads are completely independent"
    → Threads share: heap, code, globals, file descriptors | Private: stack, registers, PC

3.  "Async means parallel execution"
    → Async: interleaving via event loop (single thread) | Parallel: truly simultaneous

4.  "More threads always means better performance"
    → Each thread adds context-switch overhead. Optimal threads ≈ CPU cores for CPU-bound

5.  "Containers are virtual machines"
    → Container: shared Linux kernel + namespaces + cgroups | VM: full OS with own kernel

6.  "kill always immediately kills a process"
    → kill -TERM sends SIGTERM (can be caught, handled, ignored). Only SIGKILL cannot be caught

7.  "Free RAM = wasted RAM"
    → Linux uses free RAM as page cache (file system cache). Low free RAM is GOOD

8.  "Virtual memory means using disk as RAM"
    → Virtual memory = abstraction of address space. Swap (disk as RAM) is one use, not the definition

9.  "Context switching is free"
    → Context switch: save/restore registers, TLB flush, CPU cache cold start — measurable overhead

10. "CPU cache and RAM have similar speeds"
    → L1 cache: 0.5ns | L2: 5ns | L3: 30ns | RAM: 100ns — 200x difference between L1 and RAM

11. "A page fault always means a bug"
    → Minor page fault (anonymous memory first access) is normal. Major page fault (reads from disk) is expensive but not a bug

12. "Python threads can never run concurrently"
    → GIL blocks CPU-bound parallelism. But I/O-bound threads CAN be concurrent (GIL released during I/O)

13. "chmod 777 fixes permission problems"
    → Makes file world-writable — a serious security vulnerability. Find the actual missing permission

14. "RAM usage means the application is leaking memory"
    → High RSS can be page cache, memory-mapped files, COW pages from fork. Check smaps for actual leaks

15. "The OS just runs programs"
    → OS manages CPU scheduling, memory isolation, I/O multiplexing, security enforcement, device abstraction — it IS the foundation everything else builds on
```

---

## Study Plans

### Walk-In / Quick Interview Prep (2 Hours)
```
Hour 1 — Concepts to know cold:
  Topic 12  User Mode vs Kernel Mode
  Topic 13  System Calls
  Topic 15  Program vs Process
  Topic 26  Context Switching
  Topic 30  Concurrency vs Parallelism
  Topic 32  Python + GIL
  Topic 36  Deadlocks (4 conditions)
  Topic 39  Virtual Memory

Hour 2 — Linux concepts:
  Topic 60  Signals (SIGTERM vs SIGKILL)
  Topic 50  File Descriptors ("Everything is a file")
  Topic 73  Namespaces (for Docker questions)
  Topic 74  cgroups (CPU/memory limits)
  Topic 80  Read the Incident cases (hang + CPU + OOM)
```

### Interview in 1 Week (Backend Engineer OS Round)
```
Day 1:  Level 0–2  (Computer fundamentals, architecture, OS basics)
Day 2:  Level 3–5  (System calls, Processes, Threads)
Day 3:  Level 6–9  (Scheduling, Context Switch, IPC, Concurrency)
Day 4:  Level 10–12 (Synchronization, Deadlocks, Memory Management)
Day 5:  Level 13–16 (Virtual Memory, Paging, TLB, Cache, CoW)
Day 6:  Level 17–22 (File Systems, I/O, epoll, Signals, Linux)
Day 7:  Level 26–30 (Containers, Backend Connections, Troubleshooting)
```

### Full Preparation (12 Weeks)
```
Week 1:   Level 0–3   (Fundamentals + Architecture + Kernel + System Calls)
Week 2:   Level 4–5   (Processes in depth + Threads)
Week 3:   Level 6–8   (Scheduling + Context Switch + IPC)
Week 4:   Level 9–11  (Concurrency + Synchronization + Deadlocks)
Week 5:   Level 12–14 (Memory Management + Virtual Memory + Paging)
Week 6:   Level 15–16 (TLB + CPU Cache + mmap + Copy-on-Write)
Week 7:   Level 17–18 (File Systems + Storage + Disk I/O)
Week 8:   Level 19–21 (I/O Systems + epoll + Signals + Linux Internals)
Week 9:   Level 22–24 (Linux Networking + Performance Tools)
Week 10:  Level 25–27 (Security + Virtualization + Containers + Docker)
Week 11:  Level 28    (OS to Backend Stack Connections — Python/FastAPI/Redis/PostgreSQL)
Week 12:  Level 29–30 (Production Troubleshooting + Misconceptions + Review)
```

---

## Priority by Interview Type

### Backend / Python Engineer (FastAPI/Django interviews)
```
★★★  Topic 12  User Mode vs Kernel Mode
★★★  Topic 13  System Calls (what Python does underneath)
★★★  Topic 15  Program vs Process
★★★  Topic 20  Thread vs Process comparison
★★★  Topic 30  Concurrency vs Parallelism
★★★  Topic 32  Python GIL — why threads don't parallelise CPU work
★★★  Topic 36  Deadlocks
★★★  Topic 39  Virtual Memory
★★★  Topic 50  File Descriptors
★★★  Topic 58  epoll (how asyncio works underneath)
★★★  Topic 77  OS → FastAPI connection (the full request path)
★★   Topic 26  Context Switching
★★   Topic 57  Blocking vs Non-blocking vs Async I/O
★★   Topic 60  Signals + Graceful Shutdown
★★   Topic 80  Production Incidents
```

### DevOps / Infrastructure Engineer
```
★★★  Topic 73  Linux Namespaces (Docker isolation)
★★★  Topic 74  cgroups (CPU/memory limits)
★★★  Topic 75  OverlayFS (Docker image layers)
★★★  Topic 66  CPU + Load Analysis
★★★  Topic 67  Memory Analysis (OOM killer, page cache)
★★★  Topic 68  strace + iostat + lsof
★★★  Topic 71  SELinux, AppArmor, capabilities
★★★  Topic 80  All 7 production incidents
★★   Topic 56  Page cache, Direct I/O, fsync
★★   Topic 63  Linux CFS scheduler
★★   Topic 65  Linux networking commands
```

### System Design Interview (OS layer questions)
```
★★★  Topic 26  Context Switch overhead
★★★  Topic 32  Python GIL (why multiprocessing for CPU-bound)
★★★  Topic 48  Copy-on-Write (fork + multiprocessing cost)
★★★  Topic 58  epoll (how 10K concurrent connections work)
★★★  Topic 73  Namespaces (how Docker/K8s works at OS level)
★★★  Topic 74  cgroups (how K8s resource limits work)
★★★  Topic 76  OS → Python
★★★  Topic 77  OS → FastAPI
★★★  Topic 78  OS → PostgreSQL
★★★  Topic 79  OS → Redis (why Redis is fast)
★★   Topic 55  Sequential vs Random I/O (why Kafka is fast)
★★   Topic 56  Page cache (free memory is not wasted)
```

---

## OS Concepts Cheat Sheet

### Process States
```
                  fork()
New ──────────────────────→ Ready
                              │   ↑
                   scheduler  │   │  I/O complete
                   dispatch   │   │  or event
                              ↓   │
                           Running ──→ Waiting
                              │              (blocked on I/O,
                    exit()    │               lock, sleep)
                              ↓
                          Terminated
```

### Process Memory Layout
```
High Address  ┌──────────────────┐
              │      Stack       │  ← local variables, function call frames
              │    (grows ↓)     │
              ├──────────────────┤
              │                  │
              │   Memory maps    │  ← shared libs, mmap'd files
              │                  │
              ├──────────────────┤
              │      Heap        │  ← dynamic alloc (malloc/new)
              │    (grows ↑)     │
              ├──────────────────┤
              │    BSS segment   │  ← uninitialised globals (zeroed by OS)
              ├──────────────────┤
              │   Data segment   │  ← initialised globals and statics
              ├──────────────────┤
              │   Text segment   │  ← program code (read-only)
Low Address   └──────────────────┘
```

### Virtual Memory Translation
```
Process (user space)
       │
       │ virtual address
       ↓
      MMU (hardware)
       │
       │ consults page table
       ↓
   Page Table Entry
       │
       ├── Page present? ──→ YES → Physical Address → RAM
       │
       └── Page missing? ──→ NO  → Page Fault → Kernel
                                        │
                              ┌─────────┴──────────┐
                              ↓                    ↓
                         Minor fault           Major fault
                    (allocate/map page)   (read from disk → RAM)
```

### System Call Journey
```
Python code: open("file.txt")
       │
       ↓
CPython: calls C library fopen()
       │
       ↓
glibc: calls open() system call (int 0x80 or syscall instruction)
       │
       ↓
CPU: switches from Ring 3 (user) to Ring 0 (kernel)
       │
       ↓
Linux kernel: sys_open() handler
       │
       ↓
VFS layer → file system driver → disk I/O (if not in page cache)
       │
       ↓
returns file descriptor (integer) back to user space
       │
       ↓
CPU switches back to Ring 3
```

### FastAPI Request Path (OS Level)
```
Client
  │ TCP SYN
  ↓
Linux kernel TCP stack
  │ 3-way handshake
  ↓
Socket added to accept() queue
  │
  ↓
Uvicorn: accept() → gets connected socket file descriptor
  │
  ↓
asyncio: epoll watches fd for incoming data (O(1) event notification)
  │ EPOLLIN event fires
  ↓
asyncio event loop: calls handler coroutine
  │
  ↓
FastAPI: routes to your endpoint function
  │
  ↓
await db.query()  ← yields control back to event loop
  │                  (event loop serves other requests while waiting)
  ↓
DB response arrives → epoll fires → coroutine resumes
  │
  ↓
FastAPI: formats response
  │
  ↓
Uvicorn: send() → kernel TCP stack → client
```

### Container OS Architecture
```
Docker Container A          Docker Container B
  PID namespace              PID namespace
  Net namespace              Net namespace
  Mount namespace            Mount namespace
       │                          │
       └──────────┬───────────────┘
                  │
          Linux Kernel
     (shared by ALL containers)
          namespaces
           cgroups
          OverlayFS
                  │
            Hardware
          CPU / RAM / Disk
```

---

## Key Linux Commands Reference

```
COMMAND                 WHAT IT SHOWS
───────────────────────────────────────────────────────────────────
ps aux                  All processes (PID, CPU%, MEM%, command)
ps -T -p <PID>          All threads of one process
top / htop              Live CPU, memory per process
pstree                  Process parent-child hierarchy
pgrep <name>            Find PID by name
kill -TERM <PID>        Send SIGTERM (graceful shutdown request)
kill -KILL <PID>        Send SIGKILL (force kill — uncatchable)
nice -n 10 cmd          Start command with lower priority
renice -n 5 -p <PID>    Change priority of running process

free -h                 RAM: total, used, free, available (cache/buffers)
vmstat 1                CPU, memory, I/O, context switches per second
cat /proc/meminfo       Detailed kernel memory stats
cat /proc/<PID>/status  Process memory: VmRSS, VmVirt, threads
smem -p                 Per-process actual RAM usage (accounts for sharing)

iostat -xz 1            Disk: IOPS, throughput, await time, utilisation
iotop                   Per-process disk I/O in real time
df -h                   Disk space per filesystem
lsof -p <PID>           All open file descriptors of a process
lsof -i :8080           Which process is using port 8080

ss -tlnp                TCP listening sockets + which process
ss -tp                  Established TCP connections
ip addr                 Network interfaces and IP addresses
ip route                Routing table
tcpdump -i eth0 port 80 Capture HTTP packets on interface

strace -p <PID>         Trace system calls of running process
strace -c cmd           Count system calls and time spent in each
perf top                CPU profiling: which functions use most CPU
dmesg | tail -50        Kernel messages (OOM kills, hardware errors)
cat /proc/<PID>/maps    Memory mappings of a process

docker stats            Container CPU, memory, network, I/O usage
docker inspect <name>   Container config, limits, OOMKilled status
cat /sys/fs/cgroup/memory/<cid>/memory.usage_in_bytes  Container memory usage
```

---

## Top 10 Most Asked OS Interview Questions (Verbal)

```
Q: What is the difference between a process and a thread?
A: A process is an isolated running instance of a program with its own memory
   address space, file descriptors, and resources. A thread is a lightweight
   execution unit within a process — threads share the process's heap, code,
   and file descriptors, but each has its own stack and registers. Creating a
   thread is cheaper than a process; threads communicate via shared memory
   (need synchronisation); process failure doesn't affect other processes
   but a crashing thread can kill the whole process.

Q: What is the difference between concurrency and parallelism?
A: Concurrency: multiple tasks make progress — they may interleave on one CPU
   (event loop, time-slicing). Parallelism: multiple tasks truly execute
   simultaneously on multiple CPU cores. Python asyncio is concurrent but not
   parallel. Python multiprocessing is parallel. Python threads: concurrent
   but not CPU-parallel due to the GIL.

Q: What is virtual memory? Why does it exist?
A: Virtual memory gives each process the illusion of its own private, contiguous
   address space. The MMU translates virtual addresses to physical addresses via
   page tables. It exists for: (1) memory isolation between processes, (2)
   allowing more total virtual memory than physical RAM via paging, (3) simplified
   programming — process doesn't know about physical layout.

Q: What is a deadlock? How do you prevent it?
A: Deadlock occurs when two or more threads each hold a resource and wait for
   the other's resource — circular wait, no progress. Four conditions must ALL
   hold: mutual exclusion, hold & wait, no preemption, circular wait.
   Prevention: always acquire locks in the same order across all threads
   (breaks circular wait). Detection: timeout + retry, or deadlock detector.

Q: What is a page fault?
A: A page fault occurs when a process accesses a virtual address whose page is
   not currently in RAM. The MMU raises an exception, the kernel handles it:
   minor fault (page exists but wasn't mapped — allocate and map),
   major fault (page is on disk — read from swap/file, very slow).

Q: What is the difference between SIGTERM and SIGKILL?
A: SIGTERM (signal 15): asks the process to terminate gracefully — the process
   can catch it, run cleanup, flush buffers, then exit. SIGKILL (signal 9):
   forcefully kills the process — cannot be caught, blocked, or ignored.
   Always try SIGTERM first; use SIGKILL only if the process doesn't respond.

Q: Why is Python's asyncio single-threaded but handles many connections?
A: asyncio uses epoll (Linux) to register interest in many file descriptors.
   When a coroutine awaits I/O, it yields control back to the event loop.
   The event loop polls epoll (O(1)) to find which fd has data, then resumes
   the correct coroutine. One thread multiplexes thousands of connections
   because it never blocks — I/O waits happen in the kernel, not in Python.

Q: How does Docker isolation work at the OS level?
A: Docker uses Linux namespaces for isolation and cgroups for resource limits.
   Namespaces: PID (own process tree), Network (own network stack), Mount (own
   filesystem view), User (own user IDs). cgroups: limit CPU, memory, I/O.
   OverlayFS: layered filesystem — image layers are read-only, container layer
   is writable. It is NOT a VM — all containers share the host Linux kernel.

Q: What happens when a container exceeds its memory limit?
A: The Linux kernel's OOM (Out-Of-Memory) killer selects and kills the process
   with the highest OOM score in that cgroup. Docker sets the container's
   memory limit in cgroups. When usage exceeds the limit, the kernel kills
   a process inside the container. You'll see OOMKilled: true in docker inspect.

Q: What is the page cache? Why does Linux use free RAM for it?
A: The page cache is kernel-managed RAM used to cache disk file contents.
   When you read a file, the kernel caches the data in RAM. Subsequent reads
   come from RAM (fast) not disk (slow). Linux aggressively fills free RAM
   with page cache because unused RAM is wasted RAM. This is why a "full"
   looking system still has good disk performance.
```

---

## Common OS Misconceptions — Quick Reference

```
WRONG                                  RIGHT
────────────────────────────────────────────────────────────────────────
Process = Program                   Program is code on disk. Process is
                                    a running instance with memory + state.

kill -9 is always the right fix     Try SIGTERM first. SIGKILL prevents
                                    graceful cleanup. Use it only when
                                    SIGTERM doesn't work.

Free RAM = problem                  Linux fills free RAM with page cache.
                                    Low "free" = good. Low "available" = problem.

More threads = better performance   Optimal is usually CPU core count.
                                    More threads = more context switching.

Containers are VMs                  Containers share the host kernel.
                                    VMs have their own kernel. Fundamentally different.

Python threads are useless          Threads are useful for I/O-bound work
                                    (GIL released during I/O). Useless only
                                    for CPU-bound parallel work.

Virtual memory = swap               Virtual memory = address space abstraction.
                                    Swap is one optional component of it.

chmod 777 fixes everything          It destroys security. Find the real permission
                                    needed (read? execute? which user?)

Page fault = bug                    Minor page faults are completely normal.
                                    Only major (disk) page faults at high rate
                                    indicate a performance problem.

Async = parallel                    Async = concurrent (interleaved, single thread).
                                    Parallel = truly simultaneous (multiple CPUs).
```

---

*80 topics · 30 levels · Complete OS 0 → 100 path*
*Built for backend engineers who want to understand what runs underneath their code*
*Python · FastAPI · PostgreSQL · Redis · Docker · Kubernetes — all explained at OS level*

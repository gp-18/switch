# Complete SQL Interview Preparation Roadmap
## SQL · Database Design · Query Optimization · Transactions · Data Warehousing
### v1.0 — 2–4 YOE, Service-Based Company Edition

---

## How to Use This File

1. Save the **Teaching Prompt** below permanently — Claude Project, Notion, or a sticky note.
2. Work through topics in order. Each block is a copy-paste into `{PASTE TOPIC HERE}`.
3. Do NOT skip phases — each one builds on the previous.
4. Topics marked `★ HIGH PRIORITY` are most frequently asked in service-company interviews.
5. Topics marked `◆ DESIGN` are schema/design round questions. `◆ EXTRA` = beyond standard SQL scope but still asked.

**Coverage:** SQL Basics · Joins · Subqueries · CTEs · Window Functions · Database Design ·
Normalization · Indexes · Query Optimization · Transactions · ACID · Locking · Stored
Procedures · Classic Interview Problems · Data Warehousing · Cloud Databases · NoSQL vs SQL

---

## Teaching Prompt (Use This Every Time)

```
You are an expert SQL instructor, database architect, and interview mentor. Your task is
to teach SQL and database concepts in a way that prepares me for technical interviews at
service-based companies for 2–4 years of experience.

I want:
- Clear understanding from basics → advanced
- Interview-ready knowledge with crisp answers
- Short but powerful notes I can revise before an interview
- Real-world production perspective — the kinds of problems service companies
  actually solve with SQL (reporting, analytics, data pipelines, backend queries)

---

STRICT TEACHING RULES
1. Start from absolute basics — assume I only know the topic name, nothing else
2. Move step-by-step from basics to advanced
3. Explain WHY before WHAT — motivation first, then mechanism
4. Use simple English first, then the technical explanation
5. Use a real-world analogy to build intuition
6. Add query flow / execution diagrams using text arrows
7. Show the internal working — how the database engine actually processes this
8. Use comparison tables for related concepts (e.g. RANK vs DENSE_RANK, DELETE vs TRUNCATE)
9. Include real production use-cases that service companies build
10. Highlight the top common mistakes and pitfalls (things that trip candidates up)
11. Add 5–8 interview questions with crisp, confident answers
12. Include at least 2–3 working SQL code examples (from simple to complex)
13. End with a quick revision summary (bullet points, max 10 lines)
14. End with one "Most Important Takeaway" sentence

---

OUTPUT FORMAT — use this structure every time, no exceptions:

### 1. Basic Understanding (Simple English + Analogy)
### 2. Technical Deep Dive
### 3. Internal Working / Execution Flow (with text diagram)
### 4. Real-World Example (service-company context)
### 5. SQL Code Examples (simple → complex, with comments)
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

## PHASE 1 — SQL Foundations
**Goal:** Build the base. Every advanced concept depends on these.
**Timeline:** Week 1

---

### Topic 1
```
What is a Database, RDBMS & SQL  ★ HIGH PRIORITY
Subtopics: what a database is (organised collection of data), flat files vs RDBMS,
what RDBMS means (Relational Database Management System), the relational model
(data in tables with rows and columns), what SQL is (Structured Query Language —
a declarative language, not procedural), SQL categories: DDL (CREATE/ALTER/DROP),
DML (INSERT/UPDATE/DELETE), DQL (SELECT), DCL (GRANT/REVOKE), TCL (COMMIT/ROLLBACK),
popular RDBMS options: MySQL, PostgreSQL, SQL Server, Oracle, SQLite — and when each
is used in service companies, what makes a database "relational" (tables linked by keys)
```

### Topic 2
```
SELECT, FROM, WHERE — Basic Querying  ★ HIGH PRIORITY
Subtopics: anatomy of a SELECT statement, SELECT specific columns vs SELECT * (why
SELECT * is bad in production), FROM clause, WHERE clause for row-level filtering,
ORDER BY (ASC and DESC, multiple columns), LIMIT and OFFSET (pagination), DISTINCT
(remove duplicate rows), column aliases with AS, SQL query execution order
(FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT — critical concept),
writing your first query and reading it the way the database reads it
```

### Topic 3
```
SQL Data Types & NULL  ★ HIGH PRIORITY
Subtopics: numeric types (INT, BIGINT, SMALLINT, DECIMAL/NUMERIC, FLOAT, REAL),
string types (VARCHAR(n), CHAR(n), TEXT — differences and when to use each),
date/time types (DATE, TIME, DATETIME, TIMESTAMP — timezone differences),
boolean type, what NULL means (unknown, not zero, not empty string — a special state),
NULL in comparisons (NULL = NULL is FALSE — must use IS NULL / IS NOT NULL),
NULL in arithmetic (any operation with NULL = NULL), NULL in aggregates (COUNT(*)
vs COUNT(column) — NULL is skipped), NULL pitfalls that trip candidates up in interviews
```

### Topic 4
```
Filtering — AND, OR, NOT, IN, BETWEEN, LIKE, IS NULL  ★ HIGH PRIORITY
Subtopics: AND / OR / NOT — operator precedence (AND before OR — use parentheses!),
IN operator (shorthand for multiple OR conditions), NOT IN (the NULL trap — why
NOT IN fails silently when the list contains NULL),
BETWEEN (inclusive on both ends), LIKE with wildcards (% = any characters,
_ = single character), ILIKE for case-insensitive LIKE (PostgreSQL),
IS NULL vs IS NOT NULL, combining multiple conditions with correct parentheses,
WHERE clause vs HAVING clause (which filters before GROUP BY, which after)
```

### Topic 5
```
Aggregate Functions — COUNT, SUM, AVG, MIN, MAX + GROUP BY + HAVING  ★ HIGH PRIORITY
Subtopics: what aggregate functions do (collapse multiple rows into one value),
COUNT(*) vs COUNT(column) vs COUNT(DISTINCT column), SUM/AVG/MIN/MAX with NULLs
(NULLs are ignored), GROUP BY (group rows by one or more columns before aggregating),
the GROUP BY rule: every column in SELECT must be in GROUP BY OR inside an aggregate,
HAVING (filter AFTER grouping — like WHERE but for aggregated results),
difference: WHERE filters rows, HAVING filters groups, combining WHERE + GROUP BY
+ HAVING in one query, common interview pattern: "find departments with more than 5 employees"
```

### Topic 6
```
String Functions  ★ HIGH PRIORITY
Subtopics: UPPER() and LOWER(), LENGTH() / LEN(), CONCAT() / || operator,
SUBSTRING() / SUBSTR() — extracting part of a string by position,
TRIM() / LTRIM() / RTRIM() — remove whitespace, REPLACE() — find and replace in a string,
LEFT() and RIGHT() — extract from start or end, CHARINDEX() / POSITION() — find a
substring's position, COALESCE(col, 'default') — replace NULL with a default,
NULLIF(a, b) — returns NULL if a = b (useful for avoiding divide-by-zero),
string functions differ slightly between MySQL, PostgreSQL, and SQL Server (know the variants),
practical: clean messy data using string functions
```

### Topic 7
```
Date & Time Functions  ★ HIGH PRIORITY
Subtopics: getting current date/time: NOW(), CURRENT_TIMESTAMP, CURRENT_DATE, GETDATE(),
extracting parts: YEAR(), MONTH(), DAY(), EXTRACT(PART FROM date),
date arithmetic: DATEADD() / date + INTERVAL '1 day', DATEDIFF() / age(),
DATE_FORMAT() / TO_CHAR() — formatting dates as strings,
DATE_TRUNC() (PostgreSQL) — truncate to week/month/year (critical for reporting queries),
converting strings to dates: STR_TO_DATE(), TO_DATE(), CAST(),
time zones: CONVERT_TZ(), AT TIME ZONE,
common interview patterns: "find users who registered in the last 30 days",
"count orders per month", "calculate days between two dates",
differences across MySQL vs PostgreSQL vs SQL Server date functions (know all 3)
```

---

## PHASE 2 — Joins & Relationships
**Goal:** Joins are asked in every SQL interview without exception. Master all types.
**Timeline:** Week 1–2

---

### Topic 8
```
Primary Key, Foreign Key & Table Relationships  ★ HIGH PRIORITY
Subtopics: what a primary key is (unique identifier for each row, cannot be NULL),
composite primary key (multiple columns together form the PK), natural key vs surrogate
key (auto-increment ID), what a foreign key is (a column that references another table's
PK), referential integrity (FK ensures referenced row exists), relationship types:
one-to-one, one-to-many (most common), many-to-many (requires a junction/bridge table),
CASCADE options: ON DELETE CASCADE, ON DELETE SET NULL, ON DELETE RESTRICT,
how to identify relationships in a schema diagram — essential for JOIN queries
```

### Topic 9
```
INNER JOIN  ★ HIGH PRIORITY
Subtopics: what INNER JOIN returns (only matching rows from both tables),
syntax: table1 INNER JOIN table2 ON table1.id = table2.fk_id,
what happens to non-matching rows (they are excluded from result),
Venn diagram mental model (intersection only), table aliases for cleaner queries,
joining on multiple conditions (AND in ON clause), implicit join syntax
(WHERE table1.id = table2.id — old style, avoid but must recognise in legacy code),
what to look for when a JOIN produces unexpected duplicate rows (many-to-many
relationship), INNER JOIN with aggregate functions (e.g. total orders per customer)
```

### Topic 10
```
LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN  ★ HIGH PRIORITY
Subtopics: LEFT JOIN — return ALL rows from left table, matching rows from right
(unmatched right = NULL), why LEFT JOIN is used far more than RIGHT JOIN in practice,
RIGHT JOIN — opposite of LEFT JOIN (easily rewritten as LEFT JOIN by switching tables),
FULL OUTER JOIN — all rows from both tables (NULLs where no match — MySQL doesn't
support this natively), how to find rows in table A that have NO match in table B
(LEFT JOIN ... WHERE b.id IS NULL — anti-join pattern — very common interview question),
FULL OUTER JOIN to find rows only in A or only in B, practical examples: customers
with no orders, employees with no department
```

### Topic 11
```
SELF JOIN & CROSS JOIN
Subtopics: SELF JOIN — joining a table to itself (must use aliases),
when self join is used (hierarchy/parent-child data: employee-manager, org chart,
find pairs of employees in same department), syntax and common self-join patterns,
CROSS JOIN — Cartesian product (every row in A × every row in B),
when CROSS JOIN is intentional (generate all combinations: calendar × store matrix,
test data generation) vs accidental (missing JOIN condition = implicit CROSS JOIN — disaster),
performance warning: CROSS JOIN on large tables is extremely expensive
```

### Topic 12
```
Joining 3+ Tables  ★ HIGH PRIORITY
Subtopics: how to chain multiple JOINs (each JOIN adds a table to the result set),
execution order of multiple JOINs (left to right — intermediate result set grows),
when to use different JOIN types for different tables in the same query,
best practices: start from the smallest/most-filtered table, use aliases consistently,
common 3-table join pattern: orders JOIN customers JOIN products,
many-to-many via junction table: students JOIN enrollments JOIN courses,
debugging multi-table join results (unexpected row multiplication is usually a
missing or wrong JOIN condition), choosing the anchor table and building outward
```

### Topic 13
```
Subqueries — Non-Correlated  ★ HIGH PRIORITY
Subtopics: what a subquery is (a query inside another query), non-correlated subquery
(the inner query runs once, independent of the outer query), subquery in WHERE clause
(most common: WHERE salary > (SELECT AVG(salary) FROM employees)),
subquery in FROM clause (derived table / inline view — must be aliased),
subquery in SELECT clause (scalar subquery — must return exactly one value),
when to use subqueries vs JOINs (readability vs performance — JOINs are usually faster),
multiple levels of nesting (avoid beyond 2 levels — use CTEs instead for readability)
```

### Topic 14
```
Correlated Subqueries & EXISTS / NOT EXISTS  ★ HIGH PRIORITY
Subtopics: what makes a subquery "correlated" (it references the outer query's row —
runs once per outer row — can be slow), correlated subquery vs non-correlated
(execution behaviour difference), EXISTS (returns TRUE if subquery returns any rows —
faster than IN for large datasets), NOT EXISTS (return rows where no match exists —
the clean alternative to NOT IN that handles NULLs safely),
IN vs EXISTS performance comparison (EXISTS stops at first match, IN evaluates all),
the NULL trap with NOT IN (always prefer NOT EXISTS),
rewriting a correlated subquery as a JOIN (often faster),
when correlated subqueries are unavoidable
```

---

## PHASE 3 — Advanced SQL Constructs
**Goal:** These separate candidates who "know SQL" from those who "use SQL professionally."
**Timeline:** Week 2

---

### Topic 15
```
CTEs — Common Table Expressions  ★ HIGH PRIORITY
Subtopics: what a CTE is (a named temporary result set, defined with WITH, exists for
the duration of one query), CTE syntax: WITH cte_name AS (SELECT ...),
multiple CTEs in one query (WITH a AS (...), b AS (...) SELECT ...),
CTE vs subquery — when to use which (CTEs = readability + reuse, subqueries = simple
one-time use), CTE vs temp table — when to use which (CTE = same query scope, temp
table = multi-query scope with indexes), chaining CTEs (second CTE references first),
non-recursive CTE use cases: breaking a complex query into readable steps,
deduplication using ROW_NUMBER() inside a CTE, CTE for common interview problems
```

### Topic 16
```
Recursive CTEs  ★ HIGH PRIORITY
Subtopics: what recursive CTE solves (hierarchical / tree-structured data),
two parts: anchor member (base case — the starting rows) + recursive member
(selects from the CTE itself, adding one level each iteration),
UNION ALL between anchor and recursive member,
stopping condition (no new rows returned by recursive member),
real-world use cases: employee hierarchy (who reports to whom, all levels),
organisational chart, bill of materials (product components),
folder/file system traversal, finding all ancestors or descendants,
MAX recursion depth limit (SQL Server: 100 default, PostgreSQL: no limit),
reading and writing a recursive CTE step by step
```

### Topic 17
```
CASE WHEN  ★ HIGH PRIORITY
Subtopics: CASE WHEN as SQL's if-else — conditional logic inline in a query,
searched CASE syntax: CASE WHEN condition THEN result ELSE default END,
simple CASE syntax: CASE column WHEN value THEN result END,
CASE WHEN in SELECT (add computed columns), in ORDER BY (custom sort order),
in GROUP BY (bucket/categorize data), in aggregate: SUM(CASE WHEN ... THEN 1 ELSE 0 END)
for conditional counting, nested CASE WHEN (use sparingly — better to use CTEs),
CASE WHEN for pivoting (converting rows to columns — a very common interview pattern),
real-world: categorise customers by spend tier, flag late orders, custom sort
```

### Topic 18
```
UNION, UNION ALL, INTERSECT, EXCEPT  ★ HIGH PRIORITY
Subtopics: UNION (combine result sets of two queries, removes duplicates — like DISTINCT),
UNION ALL (combine without removing duplicates — faster, use when duplicates are OK
or impossible), rules: both queries must have same number of columns + compatible types,
UNION vs OR in WHERE (different use cases — UNION stacks rows, OR filters a single table),
INTERSECT (return rows present in BOTH result sets — like AND for two queries),
EXCEPT / MINUS (rows in first set but NOT in second — like anti-join using sets),
performance: UNION ALL is always faster than UNION (no dedup step),
practical: combine data from multiple tables with same schema, monthly reports
```

### Topic 19
```
PIVOT & Conditional Aggregation  ★ HIGH PRIORITY
Subtopics: what pivoting is (transform row values into column headers — useful for
reporting), the CASE WHEN + GROUP BY approach for pivoting (works in all databases):
SELECT category, SUM(CASE WHEN month='Jan' THEN amount END) AS Jan ...,
SQL Server PIVOT operator syntax (simpler syntax but SQL Server only),
dynamic pivot (when column headers are not known in advance — requires dynamic SQL),
UNPIVOT (reverse — turn columns back into rows), when to pivot in SQL vs in
application code (pivot in SQL when the report is the final output, in code for
flexibility), common interview question: "write a query showing sales by month as columns"
```

### Topic 20
```
Handling NULLs — COALESCE, NULLIF, NULL Traps  ★ HIGH PRIORITY
Subtopics: why NULLs are the #1 source of unexpected query results,
COALESCE(a, b, c) — returns first non-NULL value (the primary NULL-handling function),
ISNULL(a, default) — SQL Server specific COALESCE for two values,
IFNULL(a, default) — MySQL specific,
NVL(a, default) — Oracle specific,
NULLIF(a, b) — returns NULL if a equals b, else returns a (used to avoid divide-by-zero),
NULL in WHERE: IS NULL and IS NOT NULL (never use = NULL or != NULL),
NULL in aggregates (COUNT(*) counts NULLs, COUNT(col) skips them),
NULL in ORDER BY (NULL sorts FIRST in ASC, LAST in DESC by default — varies by DB),
NULL in JOIN conditions (NULLs never match — even NULL = NULL is false)
```

### Topic 21
```
Temporary Tables vs CTEs vs Subqueries  ★ HIGH PRIORITY
Subtopics: subquery (inline, no name, single use, runs as part of the outer query —
simple and fast for one-time use), CTE (named, reusable within one query, improves
readability, not materialised by default in most DBs), temporary table (materialised
in tempdb/temp schema, persists for the session, can be indexed — good for multi-step
complex ETL or when CTE is referenced many times with high cost), table variable
(SQL Server specific, similar to temp table but in memory — scope limited to batch),
performance comparison table, when each is the right tool,
common mistake: using temp tables everywhere when CTEs or subqueries suffice
```

---

## PHASE 4 — Window Functions  ★ MUST KNOW FOR INTERVIEWS
**Goal:** Window functions are asked in almost every mid-to-senior SQL interview. Non-negotiable.
**Timeline:** Week 2–3

---

### Topic 22
```
Window Functions — Introduction & OVER() Clause  ★ HIGH PRIORITY
Subtopics: what window functions are (perform calculations across a set of related rows
WITHOUT collapsing them like GROUP BY does — each row keeps its identity),
the OVER() clause — this is what makes a function a window function,
PARTITION BY (define the window/group for each row),
ORDER BY inside OVER() (define ordering within the window),
frame clause (ROWS BETWEEN / RANGE BETWEEN — define which rows are in scope),
window function vs GROUP BY: GROUP BY collapses to one row per group, window
function adds a column to every row, categories: ranking, offset, aggregate window
functions, execution order: window functions run AFTER WHERE/GROUP BY/HAVING
```

### Topic 23
```
ROW_NUMBER, RANK, DENSE_RANK, NTILE  ★ HIGH PRIORITY
Subtopics: ROW_NUMBER() — unique sequential number within partition (no ties — always unique),
RANK() — same rank for ties, but gaps after ties (1,1,3,4),
DENSE_RANK() — same rank for ties, no gaps (1,1,2,3),
NTILE(n) — divide rows into n equal buckets (quartiles, deciles),
comparison table of all four with same data showing different results,
THE most common interview question: "Find the 2nd highest salary in each department"
(solution: ROW_NUMBER() or DENSE_RANK() inside CTE, then filter WHERE rank = 2),
"Find top 3 products per category" — same pattern,
ROW_NUMBER() for deduplication (delete duplicate rows keeping latest),
when to use RANK vs DENSE_RANK (dense_rank when you want no gaps — percentiles,
leaderboards; rank for competition-style ranking with gaps)
```

### Topic 24
```
LAG, LEAD, FIRST_VALUE, LAST_VALUE  ★ HIGH PRIORITY
Subtopics: LAG(column, offset, default) — access a previous row's value within the
partition (no self-join needed), LEAD(column, offset, default) — access a next row's value,
practical: calculate month-over-month change (current month - LAG(last month)),
calculate day-over-day growth rate, identify consecutive records,
FIRST_VALUE(column) — get the first value in the window (good for "compare to first"),
LAST_VALUE(column) — get the last value in the window (requires ROWS BETWEEN UNBOUNDED
PRECEDING AND UNBOUNDED FOLLOWING to work correctly — a common pitfall),
NTH_VALUE(column, n) — get the nth value in the window,
real-world use: "show each order and the previous order date for that customer",
"compare each employee's salary to the highest in their department"
```

### Topic 25
```
Window Aggregate Functions — Running Totals & Moving Averages  ★ HIGH PRIORITY
Subtopics: SUM() OVER(), AVG() OVER(), COUNT() OVER(), MIN() OVER(), MAX() OVER()
— these compute the aggregate but return a value for EVERY row,
PARTITION BY splits into groups (SUM resets per partition),
ORDER BY + frame clause = running total (cumulative sum),
default frame when ORDER BY is specified: RANGE BETWEEN UNBOUNDED PRECEDING AND
CURRENT ROW — this is how running totals work,
SUM(amount) OVER(PARTITION BY customer_id ORDER BY order_date) = running total
per customer, moving average: AVG(amount) OVER(ORDER BY date ROWS BETWEEN 6
PRECEDING AND CURRENT ROW) = 7-day moving average,
practical: running totals, cumulative percentages, year-to-date calculations
```

### Topic 26
```
ROWS BETWEEN / RANGE BETWEEN — Frame Clauses
Subtopics: what a window frame is (defines WHICH rows are in scope for the calculation
within the partition), ROWS BETWEEN (physical row count — precise),
RANGE BETWEEN (logical range based on values — includes all rows with same ORDER BY value),
frame boundaries: UNBOUNDED PRECEDING (start of partition), N PRECEDING,
CURRENT ROW, N FOLLOWING, UNBOUNDED FOLLOWING (end of partition),
common frames: ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW (running total),
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW (3-row moving average),
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING (full partition — for LAST_VALUE),
the difference between ROWS and RANGE (RANGE can give unexpected results with ties —
ROWS is almost always what you want)
```

### Topic 27
```
Window Function Patterns — Interview Problems  ★ HIGH PRIORITY
Subtopics: mastering these patterns covers 80% of window function interview questions.

Pattern 1 — Nth highest value per group: ROW_NUMBER / DENSE_RANK → filter in CTE
Pattern 2 — Running total: SUM() OVER(ORDER BY date)
Pattern 3 — Moving average: AVG() OVER(ORDER BY date ROWS BETWEEN N PRECEDING AND CURRENT ROW)
Pattern 4 — Month-over-month comparison: current - LAG(current, 1) OVER(ORDER BY month)
Pattern 5 — Percentage of total: value / SUM(value) OVER() * 100
Pattern 6 — Percentage of group: value / SUM(value) OVER(PARTITION BY group) * 100
Pattern 7 — Deduplication — keep latest record per group: ROW_NUMBER() → WHERE rn = 1
Pattern 8 — First and last event per entity: FIRST_VALUE / LAST_VALUE
Pattern 9 — Compare row to previous: LAG pattern for growth rate
Pattern 10 — Consecutive rows / gaps: ROW_NUMBER() - row group differencing trick

For each pattern: the problem, the solution query, the key insight
```

---

## PHASE 5 — Database Design & Normalization
**Goal:** Design round questions. Knowing SQL syntax is not enough — you must design good schemas.
**Timeline:** Week 3

---

### Topic 28
```
Database Design Principles & ER Diagrams  ★ HIGH PRIORITY  ◆ DESIGN
Subtopics: what database design is (defining tables, columns, types, relationships,
constraints before writing any SQL), Entity-Relationship (ER) diagram notation —
entities (tables), attributes (columns), relationships (cardinality),
one-to-one, one-to-many, many-to-many (junction table), identifying relationships
from business requirements ("a customer can place many orders, each order belongs to
one customer" → one-to-many), choosing the right data type for each column,
surrogate key vs natural key trade-offs, designing for the questions you need to answer
(schema drives query complexity), common interview task: "design a schema for an
e-commerce system / library system / hospital system"
```

### Topic 29
```
Normalization — 1NF, 2NF, 3NF, BCNF  ★ HIGH PRIORITY  ◆ DESIGN
Subtopics: what normalization is and WHY it matters (reduce redundancy, prevent update
anomalies, ensure data integrity), the three update anomalies: insert anomaly, update
anomaly, delete anomaly — show with a bad table,
1NF (First Normal Form): atomic values in each cell, no repeating groups, primary key,
2NF (Second Normal Form): 1NF + no partial dependency (every non-key column depends
on the WHOLE primary key — relevant only with composite PKs),
3NF (Third Normal Form): 2NF + no transitive dependency (non-key columns depend ONLY
on the PK, not on other non-key columns),
BCNF (Boyce-Codd Normal Form): every determinant is a candidate key — slightly
stronger than 3NF, practical normalisation example: start with one messy table →
normalise to 3NF step by step, at which normal form should you stop in practice?
```

### Topic 30
```
Denormalization — When & Why  ◆ DESIGN
Subtopics: what denormalization is (intentionally adding redundancy back into a
normalised schema for performance), why it's sometimes necessary (normalized schemas
require many JOINs → slower read performance for reporting/analytics),
common denormalization techniques: adding redundant columns (store total_price in
orders instead of computing it), pre-joining tables (wide flat tables),
materialized views (pre-computed JOIN results stored on disk),
summary/aggregate tables (pre-calculated totals for dashboards),
OLAP vs OLTP — OLTP is normalized (many writes, row-level updates), OLAP is often
denormalized (many reads, analytical queries), when to denormalize: high-read,
read-heavy workloads, dashboard/reporting queries running too slowly on normalized schema
```

### Topic 31
```
Constraints — NOT NULL, UNIQUE, CHECK, DEFAULT, PK, FK  ★ HIGH PRIORITY  ◆ DESIGN
Subtopics: what constraints are (rules enforced by the database on columns/tables),
NOT NULL (column must always have a value — the most basic constraint),
UNIQUE (all values in column must be distinct — can have one NULL unlike PRIMARY KEY),
PRIMARY KEY (unique + not null + only one per table — the row identifier),
FOREIGN KEY (value must exist in referenced table — referential integrity),
CHECK (enforce a custom condition: age > 0, status IN ('active','inactive')),
DEFAULT (value used when INSERT doesn't specify a value),
how constraints prevent bad data better than application-level validation,
DEFERRABLE constraints (PostgreSQL — check at end of transaction, not per statement),
performance impact of constraints (FK checks add overhead on writes)
```

### Topic 32
```
Indexes — Types, How They Work, When to Create  ★ HIGH PRIORITY
Subtopics: what an index is (a separate data structure that allows fast row lookup —
like a book index), B-Tree index (default, balanced tree structure, supports range
scans, equality, ORDER BY, LIKE prefix), Hash index (only equality, not range — faster
for exact match, PostgreSQL only), why indexes speed up reads but slow down writes
(every write must update the index), composite index — column order matters
(leftmost prefix rule — (a,b,c) index helps queries on a, a+b, a+b+c but not b or c alone),
covering index (index contains all columns the query needs — no table lookup),
partial index (PostgreSQL: index only rows matching a condition),
EXPLAIN to see if index is being used, when NOT to create an index (low cardinality columns,
small tables, write-heavy tables), the most common interview question:
"why is this query slow and how would you fix it?"
```

### Topic 33
```
Views & Materialized Views
Subtopics: what a VIEW is (a saved SELECT query — a virtual table, no data stored),
why views are used (simplify complex queries, abstract schema details, security layer —
expose only certain columns/rows to users), creating, querying, and dropping views,
updatable vs non-updatable views (simple views on one table are updatable, complex
views with JOINs/aggregates are not), materialized view (like a view but the result
IS stored on disk — like a cached query result), difference: view = always fresh but
slow, materialized view = fast but stale until refreshed, REFRESH MATERIALIZED VIEW
in PostgreSQL, when to use materialized views (slow reports, dashboard queries,
pre-aggregated data)
```

---

## PHASE 6 — Performance & Query Optimization
**Goal:** Service companies with production databases always ask optimization questions in interviews.
**Timeline:** Week 3–4

---

### Topic 34
```
Query Execution Plan — EXPLAIN & EXPLAIN ANALYZE  ★ HIGH PRIORITY
Subtopics: what a query execution plan is (how the DB engine decides to execute your query —
which indexes, which join algorithm, estimated cost), EXPLAIN (show the plan without
running the query), EXPLAIN ANALYZE (run the query and show actual vs estimated stats),
reading a plan: Seq Scan (slow, full table scan), Index Scan (fast, uses index),
Index Only Scan (fastest, all data from index), Nested Loop / Hash Join / Merge Join
(join algorithms used), cost notation: (cost=startup..total rows=N width=bytes),
actual time vs estimated rows (discrepancies indicate stale statistics),
EXPLAIN ANALYZE BUFFERS (PostgreSQL) to see I/O, the three things to look for:
Seq Scan on large tables, row estimate errors, high startup cost
```

### Topic 35
```
Index Optimization — Covering Indexes, Composite Indexes, Index Failures  ★ HIGH PRIORITY
Subtopics: how to choose WHICH columns to index (WHERE clause, JOIN conditions,
ORDER BY columns — in that priority), composite index column order (highest selectivity
first, then match WHERE clause order), covering index (include all SELECT columns in the
index so no table heap access is needed — fastest possible query), index scan vs
index only scan (covering index = index only scan),
when indexes are NOT used — index failure scenarios:
(1) function on indexed column: WHERE UPPER(name) = 'JOHN' (use functional index instead),
(2) implicit type conversion: WHERE int_col = '123' (type mismatch kills index),
(3) leading wildcard: WHERE name LIKE '%john' (only prefix LIKE uses B-Tree index),
(4) OR conditions on different columns (use UNION instead),
(5) low cardinality: WHERE is_active = true (not worth indexing — most rows match),
index bloat and REINDEX, VACUUM ANALYZE for stale statistics in PostgreSQL
```

### Topic 36
```
Query Optimization Techniques  ★ HIGH PRIORITY
Subtopics: always EXPLAIN before optimizing (measure, don't guess), rewrite subqueries
as JOINs (JOINs use indexes better than correlated subqueries), avoid SELECT * in
production (transfers unused data, breaks column-specific indexes), push filters as
early as possible (filter rows before joining — reduce intermediate result set size),
use EXISTS instead of COUNT for existence checks, avoid DISTINCT and ORDER BY unless
needed (both are expensive), use LIMIT when testing, avoid functions in WHERE on
indexed columns, use CTEs to make the optimiser's job clearer, partitioning (filter by
partition key eliminates entire partitions from scan), read replica for heavy reports
(don't run analytics on the write DB), query hints (USE INDEX in MySQL, NOLOCK hint
in SQL Server — use sparingly, understand the risks)
```

### Topic 37
```
Partitioning — Range, List, Hash
Subtopics: what partitioning is (divide a large table into smaller physical pieces
while appearing as one logical table — massive performance gain for large datasets),
Range partitioning (partition by date range: monthly/yearly — most common, ideal for
time-series data: logs, orders, events), List partitioning (partition by discrete
values: country, status, region), Hash partitioning (partition by hash of a column —
even distribution, good for load balancing with no obvious range),
partition pruning (database only scans relevant partitions — the key performance benefit),
partition key selection (use the column most commonly in WHERE clause),
partition indexes (each partition has its own index), PostgreSQL declarative
partitioning syntax, when partitioning is worth it (tables >10M rows or >100GB),
downsides of partitioning (complex schema, cross-partition queries are slow)
```

### Topic 38
```
Stored Procedures, User-Defined Functions & Triggers
Subtopics: Stored Procedure (a named, saved collection of SQL statements, executed
with EXEC / CALL, can accept parameters, can have output parameters, can modify data),
why stored procedures are used in service companies (encapsulate business logic,
reduce network round-trips, reusability, security — grant EXEC without table access),
User-Defined Function — scalar function (returns one value, used in SELECT/WHERE),
Table-valued function (returns a table, used in FROM clause),
difference: procedure can modify data + no return value, function returns a value +
usually read-only, TRIGGER (automatically fires BEFORE/AFTER INSERT/UPDATE/DELETE),
use cases for triggers: audit logging, cascading updates, data validation beyond CHECK
constraints, why triggers are dangerous (hidden logic, hard to debug, performance risk),
when to avoid triggers (use application logic instead for most cases)
```

### Topic 39
```
TRUNCATE vs DELETE vs DROP  ★ HIGH PRIORITY
Subtopics: DELETE (DML — removes specific rows per WHERE condition, fully logged —
every row deletion is a transaction, slow on large tables, can be rolled back,
triggers fire), TRUNCATE (DDL — removes ALL rows, minimal logging, very fast,
resets auto-increment counter, cannot be rolled back in MySQL, CAN be rolled back
in PostgreSQL if in a transaction, triggers do NOT fire), DROP (DDL — removes the
entire table structure AND data — irreversible), when to use each:
DELETE = remove specific rows in production, TRUNCATE = clear a table quickly
(staging tables, temp tables), DROP = remove the table entirely,
performance comparison: DELETE on 10M rows vs TRUNCATE — TRUNCATE is near-instant,
this is one of the most frequently asked SQL interview questions
```

---

## PHASE 7 — Transactions, Concurrency & Database Internals
**Goal:** Senior-level topics. Shows you understand HOW the database actually works.
**Timeline:** Week 4

---

### Topic 40
```
Transactions — BEGIN, COMMIT, ROLLBACK, SAVEPOINT  ★ HIGH PRIORITY
Subtopics: what a transaction is (a group of SQL operations that execute as a single
unit — all succeed or all fail together), why transactions are critical (consistency —
e.g. bank transfer: debit one account + credit another must both succeed or both fail),
BEGIN / START TRANSACTION to start, COMMIT to make permanent, ROLLBACK to undo all
changes since BEGIN, SAVEPOINT (checkpoint within a transaction — can rollback to here
without losing everything), RELEASE SAVEPOINT, autocommit mode (each statement is
its own transaction — default in MySQL, not PostgreSQL), explicit vs implicit
transactions, nested transactions (mostly not supported — savepoints are the workaround),
common interview: "what happens if the server crashes mid-transaction?"
```

### Topic 41
```
ACID Properties  ★ HIGH PRIORITY
Subtopics: ACID = Atomicity + Consistency + Isolation + Durability — the four
properties every production database must guarantee.
Atomicity: all operations in a transaction succeed or all are rolled back (all or nothing),
Consistency: a transaction moves the database from one valid state to another (constraints,
rules are upheld), Isolation: concurrent transactions don't interfere with each other
(each transaction sees a consistent view), Durability: committed transactions survive
system failures (written to disk/WAL, not just memory),
how each property is implemented: Atomicity via undo log, Consistency via constraints,
Isolation via locking/MVCC, Durability via write-ahead log (WAL),
interview question: "explain ACID with a bank transfer example",
ACID vs BASE (NoSQL — Basically Available, Soft state, Eventually consistent)
```

### Topic 42
```
Isolation Levels & Concurrency Problems  ★ HIGH PRIORITY
Subtopics: the three concurrency problems that isolation levels prevent:
Dirty Read (reading uncommitted data from another transaction — data that may be rolled back),
Non-Repeatable Read (reading the same row twice in one transaction gets different values
— another transaction updated it between reads),
Phantom Read (running the same range query twice returns different rows — another
transaction inserted/deleted rows in that range),
The four isolation levels (from lowest to highest isolation):
READ UNCOMMITTED: dirty reads possible (never use in production),
READ COMMITTED: prevents dirty reads — default in PostgreSQL, Oracle,
REPEATABLE READ: prevents dirty + non-repeatable reads — default in MySQL/InnoDB,
SERIALIZABLE: prevents all three — highest isolation, lowest concurrency, slowest,
MVCC (Multiversion Concurrency Control) — how PostgreSQL implements isolation without
locking reads (readers don't block writers), comparison table of levels vs problems
```

### Topic 43
```
Locking — Row-level, Table-level, Deadlocks  ★ HIGH PRIORITY
Subtopics: what a lock is (prevent two transactions from conflicting on the same data),
shared lock (read lock — multiple transactions can hold simultaneously),
exclusive lock (write lock — only one transaction at a time),
row-level locking (lock only the affected rows — high concurrency),
table-level locking (lock the entire table — low concurrency but fast for bulk ops),
SELECT FOR UPDATE (acquire exclusive row-level lock — prevents others from updating
those rows until your transaction commits — used for "check then act" patterns),
SKIP LOCKED (skip rows already locked — useful for queue processing),
DEADLOCK (two transactions each waiting for a lock held by the other — circular wait),
how databases detect and resolve deadlocks (kill one transaction — it gets an error),
how to prevent deadlocks (always acquire locks in the same order, keep transactions short)
```

### Topic 44
```
Database Internals — B-Tree, WAL, Buffer Pool  ★ HIGH PRIORITY
Subtopics: B-Tree index internal structure (balanced tree, nodes have keys + pointers,
leaf nodes have actual data or row pointers, all leaf nodes linked — enables range scan),
why B-Tree is the default index (O(log N) lookup, supports range, ORDER BY, GROUP BY),
Write-Ahead Log / WAL (before any data page is changed, the change is written to the WAL
— this is how durability works — if crash, replay WAL to recover),
Buffer Pool (in-memory cache for frequently accessed data pages — avoid disk I/O —
PostgreSQL calls it shared_buffers, MySQL calls it InnoDB buffer pool),
heap file (the actual table data storage — random row order unless clustered),
clustered index vs non-clustered index (clustered: leaf node IS the data row —
table is sorted by this index — InnoDB always has a clustered index on PK;
non-clustered: leaf node has pointer to the heap row — requires a second lookup),
VACUUM in PostgreSQL (reclaim space from dead tuples — MVCC leaves old row versions)
```

### Topic 45
```
CAP Theorem & SQL vs NoSQL Trade-offs  ◆ EXTRA
Subtopics: what CAP theorem states (a distributed system can only guarantee 2 of 3:
Consistency, Availability, Partition Tolerance — and P is unavoidable in networks),
CP systems (consistent + partition tolerant: MongoDB in some modes, HBase — may
be unavailable during partition), AP systems (available + partition tolerant: Cassandra,
CouchDB — may return stale data), CA systems (consistent + available — only possible
with no partition = single-node systems = traditional RDBMS),
ACID (SQL) vs BASE (NoSQL) — when each makes sense,
use SQL when: relational data, complex queries, ACID required, data integrity critical,
use NoSQL when: schema-less, massive scale, simple access patterns, eventual consistency OK,
types of NoSQL: Document (MongoDB), Key-Value (Redis), Column-family (Cassandra),
Graph (Neo4j) — brief description of each and their use cases
```

---

## PHASE 8 — Classic Problems, Analytics & What Else Gets Asked
**Goal:** Solve the interview problem types that appear over and over. Plus topics outside SQL that interviewers ask.
**Timeline:** Week 4–5

---

### Topic 46
```
Classic SQL Interview Problems — Salary & Ranking  ★ HIGH PRIORITY
Subtopics: these exact problem patterns appear in 70%+ of SQL interviews.

Problem 1 — Nth Highest Salary:
  Method 1: DENSE_RANK() in CTE → WHERE rank = N
  Method 2: LIMIT/OFFSET (not reliable for ties)
  Method 3: correlated subquery (slow but good to know)

Problem 2 — Highest Salary per Department:
  Method 1: ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary DESC) → WHERE rn = 1
  Method 2: JOIN with subquery MAX per dept

Problem 3 — Employees Earning More Than Their Manager:
  Self-join: e JOIN e AS m ON e.manager_id = m.emp_id WHERE e.salary > m.salary

Problem 4 — Find Duplicate Rows:
  GROUP BY + HAVING COUNT(*) > 1, or ROW_NUMBER() to identify which duplicates to delete

Problem 5 — Delete Duplicates Keeping One:
  DELETE WHERE id NOT IN (SELECT MIN(id) ... GROUP BY duplicate_columns)
  or CTE with ROW_NUMBER() WHERE rn > 1

For each: problem statement → approach → SQL → explanation of why it works
```

### Topic 47
```
Classic SQL Interview Problems — Date & Consecutive Logic  ★ HIGH PRIORITY
Subtopics:
Problem 6 — Users Active in Last N Days:
  WHERE created_at >= NOW() - INTERVAL 'N days'

Problem 7 — Consecutive Login Days (the hard one):
  Approach: DATE - ROW_NUMBER() trick — if dates are consecutive, date minus
  row_number gives the same value for each streak group → GROUP BY user + group_key
  → count days per group → filter groups >= N

Problem 8 — First and Last Purchase per Customer:
  FIRST_VALUE / LAST_VALUE, or MIN(date) / MAX(date) with GROUP BY,
  or ROW_NUMBER() with two different orderings

Problem 9 — Year-over-Year Growth:
  LAG(revenue, 1) OVER(ORDER BY year) → (current - prev) / prev * 100

Problem 10 — Running Total / Cumulative Sum:
  SUM(amount) OVER(PARTITION BY customer ORDER BY date)

Problem 11 — Gaps and Islands (find consecutive ranges):
  ROW_NUMBER() differencing: row_num - ROW_NUMBER() creates group ID for each island,
  GROUP BY island_id to find start and end of each consecutive block

For each: problem statement → approach → SQL → the KEY insight that unlocks the solution
```

### Topic 48
```
SQL for Data Analysis — Cohort, Retention, Funnel  ★ HIGH PRIORITY
Subtopics: these are asked when role involves reporting, analytics, or data engineering.

Cohort Analysis: group users by their signup month, track them over subsequent months,
  approach: join users table to events, calculate months_since_signup with DATEDIFF /
  DATE_DIFF, PIVOT or CASE WHEN to create cohort matrix

Retention Rate: what % of users from month X are still active in month X+N,
  approach: COUNT(DISTINCT user_id in month N) / COUNT(DISTINCT user_id in month 0)

Funnel Analysis: what % of users complete each step of a flow (signup → verify → purchase),
  approach: COUNT(DISTINCT user_id at each step) / COUNT at first step,
  CASE WHEN with MAX() to track if user ever reached each step

Percentile Calculations: PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY value) — median,
  NTILE(100) for percentile rank,
  real-world: P50, P95, P99 latency analysis from logs table
```

### Topic 49
```
Gaps and Islands Problem  ★ HIGH PRIORITY
Subtopics: the "gaps and islands" problem: given a table of events/dates, find
consecutive sequences (islands) and the gaps between them,
classic example: find periods of consecutive daily logins, find date ranges of
consecutive stock prices above a threshold, identify outage windows from heartbeat logs,
THE technique — ROW_NUMBER differencing:
  (1) assign ROW_NUMBER() per user ORDERED BY date
  (2) compute date_value - ROW_NUMBER() AS group_id
  (3) rows in the same consecutive sequence have the SAME group_id
  (4) GROUP BY user_id, group_id → MIN(date) AS start, MAX(date) AS end,
variation: using LAG to detect gap start (where previous date + 1 != current date),
why this is considered a hard SQL problem and how to explain your approach clearly
```

### Topic 50
```
JSON in SQL  ◆ EXTRA
Subtopics: why JSON support in SQL databases matters (semi-structured data: API
responses, user preferences, configuration, event logs),
PostgreSQL: JSON vs JSONB (JSONB is binary, indexed, faster — always use JSONB),
JSON extraction: data->'key' (returns JSON), data->>'key' (returns text),
nested: data->'address'->>'city', JSON array element: data->0,
@> operator for containment check (JSONB), JSON_ARRAY_ELEMENTS to unnest JSON arrays,
creating indexes on JSONB fields (GIN index for containment queries),
MySQL: JSON_EXTRACT(col, '$.key'), ->> shorthand, JSON_ARRAYAGG, JSON_OBJECT,
SQL Server: JSON_VALUE(), JSON_QUERY(), OPENJSON() for parsing JSON arrays,
when to store JSON in SQL vs when to normalize (JSON for flexible attributes,
normalize for queried/filtered/joined fields)
```

### Topic 51
```
SQL vs NoSQL — When to Use Which  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: structured vs semi-structured vs unstructured data (SQL excels at structured,
MongoDB at semi-structured documents, S3 for unstructured), when SQL wins:
complex relationships, multi-table JOINs, ACID requirements, ad-hoc queries,
strict schema enforcement; when NoSQL wins: massive write throughput (Cassandra),
flexible/evolving schema (MongoDB), simple key-based lookup (Redis DynamoDB),
graph relationships (Neo4j), full-text search (Elasticsearch),
polyglot persistence (use multiple database types in one system — each for what it
does best), PostgreSQL's JSONB lets you do document-style storage in SQL,
HTAP (Hybrid Transactional/Analytical Processing) — newer approach,
interview answer framework: describe the access patterns, write/read ratio, schema
flexibility need, consistency requirement — then choose the database type
```

### Topic 52
```
Data Warehousing — OLAP vs OLTP, Star Schema, Fact & Dimension Tables  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: OLTP (Online Transaction Processing) — optimised for fast reads/writes of
individual rows, normalised schema, current data, high concurrency: MySQL, PostgreSQL,
OLAP (Online Analytical Processing) — optimised for complex aggregate queries over
large historical datasets, often denormalised, read-heavy: Snowflake, BigQuery, Redshift,
Star Schema: one central Fact Table (measures: sales amount, quantity, revenue) surrounded
by Dimension Tables (context: date, product, customer, store) — denormalised,
easy to query for reports, Snowflake Schema: dimensions are further normalised (sub-dimensions),
more storage-efficient but more complex queries,
Fact table design: grain (one row = one event/transaction), degenerate dimensions,
slowly changing dimensions (SCD Type 1: overwrite, Type 2: add new row with dates),
ETL vs ELT (Extract-Transform-Load vs Extract-Load-Transform — modern cloud DWH uses ELT)
```

### Topic 53
```
Cloud Databases — AWS RDS, Aurora, BigQuery, Snowflake, Azure SQL  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: why cloud databases matter for service companies (clients run on AWS/Azure/GCP —
you must know the managed options), AWS RDS (managed MySQL/PostgreSQL/SQL Server/Oracle —
patches, backups, replicas managed by AWS, Multi-AZ for HA), AWS Aurora (MySQL/PostgreSQL
compatible but 5x faster — distributed storage, serverless option, up to 15 read replicas),
when Aurora vs RDS (Aurora for production high-availability, RDS for simplicity/cost),
Google BigQuery (serverless columnar data warehouse — SQL for analytics at petabyte scale,
pay per query, no infrastructure, partitioned and clustered tables),
Snowflake (multi-cloud data warehouse — separates compute and storage, time travel,
zero-copy cloning, data sharing), Azure SQL Database (managed SQL Server as a service),
how to answer: "which database would you choose for X?" — framework: workload type,
scale, team familiarity, cloud provider, cost
```

### Topic 54
```
SQL Dialect Differences — MySQL vs PostgreSQL vs SQL Server  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: the most important differences to know for interviews (many service
companies ask "have you worked with X database? how is it different from Y?"):
Auto-increment: MySQL AUTO_INCREMENT, PostgreSQL SERIAL/GENERATED ALWAYS AS IDENTITY,
SQL Server IDENTITY(1,1),
String concatenation: MySQL CONCAT(), PostgreSQL || or CONCAT(), SQL Server +,
Limit rows: MySQL/PostgreSQL LIMIT N, SQL Server TOP N or FETCH FIRST N ROWS ONLY,
Null functions: MySQL IFNULL(), PostgreSQL / SQL Server COALESCE() or ISNULL(),
FULL OUTER JOIN: not supported in MySQL (simulate with UNION of LEFT + RIGHT JOIN),
Date functions: each has different syntax (covered in Topic 7),
RETURNING clause (PostgreSQL only — get back inserted/updated row values),
Window functions: all three support standard SQL window functions from SQL:2003,
Upsert: MySQL INSERT ... ON DUPLICATE KEY UPDATE,
PostgreSQL INSERT ... ON CONFLICT ... DO UPDATE (cleaner),
SQL Server MERGE statement
```

### Topic 55
```
SQL for Backend Developers — ORM, Connection Pooling, N+1 Problem  ★ HIGH PRIORITY  ◆ EXTRA
Subtopics: what an ORM is (Object-Relational Mapper — maps Python/Java objects to DB
tables — SQLAlchemy, Django ORM, Hibernate, TypeORM), when to use ORM vs raw SQL
(ORM for CRUD and simple queries, raw SQL for complex analytics and performance-critical
queries), the N+1 query problem (fetch 1 list of items, then make N separate queries
to fetch related data for each — multiplies DB calls: 1 + N → huge performance problem),
how to detect N+1 (enable SQL logging, see N similar queries), how to fix N+1 (eager
loading / JOIN-based loading, Django select_related() / prefetch_related(),
SQLAlchemy joinedload()), connection pooling (reuse DB connections — creating a new
connection is expensive, pgBouncer for PostgreSQL, HikariCP for Java),
database migration tools (Alembic for Python, Flyway, Liquibase), SQL injection
(what it is, parameterised queries / prepared statements as the fix — never format
user input directly into SQL strings)
```

---

## Quick-Access Priority Guide

### Crash Mode — Only 1 Week Available:
Focus only on these in order:
Topics 2, 4, 5, 9, 10, 13, 14, 15, 17, 22, 23, 24, 25, 27, 29, 32, 34, 40, 41, 42, 46, 47, 55

### Standard Mode — 5 Weeks:
Work through all 55 topics in order, 2–3 hours per topic.

### Topic Count by Phase:

| Phase | Focus Area | Topics | Count |
|---|---|---|---|
| Phase 1 | SQL Foundations | 1–7 | 7 |
| Phase 2 | Joins & Relationships | 8–14 | 7 |
| Phase 3 | Advanced SQL Constructs | 15–21 | 7 |
| Phase 4 | Window Functions ★ | 22–27 | 6 |
| Phase 5 | Database Design & Normalization | 28–33 | 6 |
| Phase 6 | Performance & Optimization | 34–39 | 6 |
| Phase 7 | Transactions & DB Internals | 40–45 | 6 |
| Phase 8 | Classic Problems & Beyond | 46–55 | 10 |
| **Total** | | | **55 topics** |

### Top 10 SQL Interview Questions Service Companies Always Ask:
1. Find the Nth highest salary in each department (window function pattern)
2. Delete duplicate rows from a table (keep one)
3. Difference between RANK(), DENSE_RANK(), ROW_NUMBER()
4. What are the ACID properties? Explain with an example.
5. Difference between DELETE, TRUNCATE, DROP
6. What is a clustered vs non-clustered index?
7. How would you optimize this slow-running query? (EXPLAIN output given)
8. Explain the different types of JOINs with examples
9. What are isolation levels and what problems does each prevent?
10. Difference between HAVING and WHERE

### Top 7 SQL Mistakes Candidates Make:
1. Cannot explain WHY a query is slow — only knows syntax, not internals
2. Uses correlated subqueries where a JOIN would be faster
3. Does not know window functions — cannot solve ranking/running total problems
4. Confuses WHERE and HAVING — puts aggregate filters in WHERE
5. Cannot explain ACID with a real example — just recites the acronym
6. Does not know the NOT IN NULL trap (uses NOT IN when NOT EXISTS is safer)
7. Uses SELECT * in production queries without knowing the performance impact
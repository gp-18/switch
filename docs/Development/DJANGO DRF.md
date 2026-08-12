# Master Django REST Framework from 0 → 100: Complete DRF & RESTful API Engineering
## Serializers · ViewSets · Authentication · Permissions · Filtering · Throttling · Testing
### 0 → 100 | 28 Levels | 96 Topics | Junior → Senior DRF Engineer Edition

---

## What Is This File?

This is a complete **Django REST Framework learning roadmap** that takes you from
absolute beginner to senior-level DRF / REST API engineer.

It is **100% focused on DRF and RESTful API development**. It does NOT cover:
- Plain Django (templates, forms, admin UI, session auth for web pages)
- Django ORM for non-API use cases
- Frontend or HTML rendering

Every topic is a **copy-paste block** you drop into the Teaching Prompt below.
Claude then teaches that topic with a full lesson: analogy, internal DRF behavior,
trade-offs, failure scenarios, production considerations, and interview Q&As.

---

## The Teaching Prompt

Copy this once. Save it permanently (Notion, Claude Project, sticky note).
Every time you study a topic, paste the topic block into `{PASTE TOPIC HERE}`.

```
You are a Senior Django REST Framework Engineer and Backend API Architect with
15+ years of experience designing, building, and scaling production REST APIs
using Django and DRF at companies serving millions of users.

Your task is to teach me Django REST Framework (DRF) — focused entirely on
RESTful API development — in a way that builds genuine production-grade engineering
judgment, not just memorization of DRF class names.

I am a developer who knows basic Python and has some Django exposure. I want to
understand WHY DRF is designed the way it is and HOW to build production-quality
REST APIs, not just get things working.

I want:
- Clear understanding from DRF basics → production-grade REST APIs
- Engineering judgment — when to use X, when NOT to use X, and why
- Real trade-off analysis (not "it depends" without explanation)
- DRF internals — what happens inside each class
- How each concept fits into the HTTP request → response lifecycle
- Production-readiness thinking — auth, permissions, throttling, testing

---

STRICT TEACHING RULES
1. Start from the HTTP problem — explain the REST/API problem BEFORE the DRF solution
2. Use a simple real-world analogy FIRST, then go technical
3. Never say "it depends" without explaining exactly what it depends on
4. Always explain WHY DRF implements it this way (what problem it solves)
5. Always explain WHEN NOT to use it — avoid DRF over-engineering
6. Show trade-offs explicitly: performance, flexibility, readability, maintainability
7. Use text-based request lifecycle diagrams (arrows and boxes) for every topic
8. Compare alternatives in a table (e.g. APIView vs ViewSet, ModelSerializer vs Serializer)
9. Connect every concept to a real API (Twitter, Uber, Stripe, GitHub API)
10. Show the EVOLUTION — how a naive approach leads to the DRF pattern
11. Show FAILURE SCENARIOS — what breaks when you misuse this feature?
12. Show what a junior DRF dev writes vs what a senior DRF dev writes
13. Include interview questions from beginner → advanced
14. End with a hands-on exercise or debugging challenge
15. Do NOT suggest complex patterns when a simple APIView solves the problem
16. Highlight common DRF anti-patterns beginners fall into
17. Always trace the HTTP request through the DRF class being taught

---

OUTPUT FORMAT — use this structure every time, no exceptions:

### 1. Simple Explanation (ELI5 + Real-World Analogy)
### 2. Technical Deep Dive
### 3. Why Does This Exist? (The HTTP/API Problem It Solves)
### 4. How It Works Internally (DRF Request Lifecycle Diagram)
### 5. When Should You Use It? (Concrete API Scenarios)
### 6. When Should You NOT Use It? (Anti-patterns + Over-engineering)
### 7. Alternatives Comparison Table
### 8. Trade-offs (Flexibility / Performance / Readability / Maintainability)
### 9. Evolution (How DRF Builds This on Top of What Came Before)
### 10. Failure Scenarios (What breaks when misused)
### 11. Production Considerations (What senior engineers worry about)
### 12. Junior vs Senior (How thinking and code differ)
### 13. Common Mistakes Beginners Make
### 14. Interview Questions & Answers (Beginner → Advanced)
### 15. Code Example (Clean, well-commented)
### 16. Production Example (Realistic, full context)
### 17. Exercise / Debugging Challenge
### 18. Quick Revision Summary (bullet points, max 10 lines)
### 19. Most Important Takeaway

---

Topic to teach:
👉 {PASTE TOPIC HERE}
```

---

## Roadmap Structure — 28 Levels, 96 Topics

```
LEVEL 0   REST & DRF Foundations                    Topics 1–4
LEVEL 1   DRF Setup & Project Structure             Topics 5–7
LEVEL 2   The DRF Request & Response                Topics 8–10
LEVEL 3   Serializers — Fundamentals                Topics 11–14
LEVEL 4   Serializers — Advanced                    Topics 15–19
LEVEL 5   Views — APIView                           Topics 20–22
LEVEL 6   Views — Generic Views                     Topics 23–26
LEVEL 7   Views — ViewSets & Routers                Topics 27–30
LEVEL 8   Authentication                            Topics 31–35
LEVEL 9   Permissions                               Topics 36–39
LEVEL 10  Throttling & Rate Limiting                Topics 40–42
LEVEL 11  Filtering, Searching & Ordering           Topics 43–46
LEVEL 12  Pagination                                Topics 47–49
LEVEL 13  URL Design & Routers                      Topics 50–52
LEVEL 14  Nested Resources & Relationships          Topics 53–55
LEVEL 15  Exception Handling & Error Responses      Topics 56–58
LEVEL 16  Content Negotiation & Renderers/Parsers   Topics 59–61
LEVEL 17  Versioning                                Topics 62–63
LEVEL 18  File Uploads & Media                      Topics 64–65
LEVEL 19  DRF Settings & Configuration              Topics 66–67
LEVEL 20  Testing DRF APIs                          Topics 68–71
LEVEL 21  Performance Optimization                  Topics 72–74
LEVEL 22  Caching in DRF                            Topics 75–76
LEVEL 23  JWT & Token Auth Deep Dive                Topics 77–79
LEVEL 24  OAuth2 & Third-Party Auth                 Topics 80–81
LEVEL 25  API Documentation                         Topics 82–83
LEVEL 26  Production API Engineering                Topics 84–88
LEVEL 27  Advanced DRF Patterns                     Topics 89–93
LEVEL 28  Real-World API Case Studies               Topics 94–96
```

---

## All 96 Topics at a Glance

### LEVEL 0 — REST & DRF Foundations
```
Topic 1   What is REST? The 6 Constraints Every API Developer Must Know
Topic 2   HTTP Methods, Status Codes, and Headers — The Building Blocks of REST
Topic 3   What is Django REST Framework and Why It Exists
Topic 4   DRF vs Raw Django vs FastAPI vs Flask — When to Choose DRF
```

### LEVEL 1 — DRF Setup & Project Structure
```
Topic 5   Installing DRF, settings.py Configuration, DEFAULT_RENDERER_CLASSES
Topic 6   Project Layout for a DRF API — Apps, urls.py, serializers.py, views.py
Topic 7   The DRF Request Lifecycle — HTTP → Django → DRF → Response
```

### LEVEL 2 — The DRF Request & Response
```
Topic 8   DRF Request Object — request.data, request.query_params, request.user
Topic 9   DRF Response Object — Response() vs HttpResponse, Content Negotiation
Topic 10  DRF Format Suffixes and Browsable API
```

### LEVEL 3 — Serializers — Fundamentals
```
Topic 11  What is a Serializer? — Serialization vs Deserialization in DRF
Topic 12  Serializer — Fields, data, validated_data, errors
Topic 13  ModelSerializer — Auto-generating Fields from a Django Model
Topic 14  Serializer Validation — field-level, object-level, validators
```

### LEVEL 4 — Serializers — Advanced
```
Topic 15  Nested Serializers — Representing Related Objects in JSON
Topic 16  SerializerMethodField — Custom Read-Only Computed Fields
Topic 17  Writable Nested Serializers — create() and update() with Relations
Topic 18  to_representation() and to_internal_value() — Custom Serialization Logic
Topic 19  ListSerializer and many=True — Bulk Operations
```

### LEVEL 5 — Views — APIView
```
Topic 20  APIView — The Foundation of All DRF Views
Topic 21  APIView Lifecycle — dispatch(), initial(), handle_exception()
Topic 22  Mixing HTTP Methods — get(), post(), put(), patch(), delete() in APIView
```

### LEVEL 6 — Views — Generic Views
```
Topic 23  Generic Views — ListAPIView, RetrieveAPIView, CreateAPIView, etc.
Topic 24  Mixins — ListModelMixin, CreateModelMixin, and How They Compose
Topic 25  get_queryset() and get_object() — Customizing Data Access
Topic 26  get_serializer_class() and get_serializer() — Dynamic Serializer Selection
```

### LEVEL 7 — Views — ViewSets & Routers
```
Topic 27  ViewSet — Grouping Related Actions on a Resource
Topic 28  ModelViewSet — Full CRUD from One Class
Topic 29  @action Decorator — Custom Non-CRUD Endpoints on a ViewSet
Topic 30  Routers — DefaultRouter vs SimpleRouter, URL Generation
```

### LEVEL 8 — Authentication
```
Topic 31  DRF Authentication Architecture — How authentication_classes Works
Topic 32  SessionAuthentication — Cookie-Based Auth for Browser Clients
Topic 33  TokenAuthentication — DRF's Built-In Token Auth (and Its Limits)
Topic 34  JWT Authentication — djangorestframework-simplejwt Deep Dive
Topic 35  Custom Authentication Classes — Writing Your Own Auth Backend
```

### LEVEL 9 — Permissions
```
Topic 36  DRF Permissions Architecture — How permission_classes Works
Topic 37  Built-In Permissions — IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
Topic 38  Object-Level Permissions — has_object_permission() and When to Use It
Topic 39  Custom Permission Classes — Writing Fine-Grained Business Logic Permissions
```

### LEVEL 10 — Throttling & Rate Limiting
```
Topic 40  DRF Throttling Architecture — How throttle_classes Works
Topic 41  Built-In Throttles — AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
Topic 42  Custom Throttle Classes — IP-Based, Plan-Based, and Endpoint-Specific Limits
```

### LEVEL 11 — Filtering, Searching & Ordering
```
Topic 43  DRF Filtering Architecture — filter_backends and How They Chain
Topic 44  django-filter — FilterSet, DjangoFilterBackend, Complex Filter Logic
Topic 45  SearchFilter — Full-Text Search Across Fields
Topic 46  OrderingFilter — Sortable API Responses
```

### LEVEL 12 — Pagination
```
Topic 47  DRF Pagination Architecture — How Pagination Integrates with Views
Topic 48  PageNumberPagination, LimitOffsetPagination, CursorPagination — When to Use Which
Topic 49  Custom Pagination Classes — Response Shape, Metadata, and Cursor Design
```

### LEVEL 13 — URL Design & Routers
```
Topic 50  RESTful URL Design — Resources, Collections, Nested URLs, Actions
Topic 51  DRF Routers — How They Auto-Generate URL Patterns from ViewSets
Topic 52  Customising Router URLs — Extra Actions, Trailing Slashes, Namespaces
```

### LEVEL 14 — Nested Resources & Relationships
```
Topic 53  Representing Relationships — PrimaryKeyRelatedField, SlugRelatedField, HyperlinkedRelatedField
Topic 54  Nested URL Resources — /users/{id}/posts/ Pattern Design
Topic 55  HyperlinkedModelSerializer — HATEOAS-style APIs with URL Fields
```

### LEVEL 15 — Exception Handling & Error Responses
```
Topic 56  DRF Exception Handling — EXCEPTION_HANDLER, APIException, ValidationError
Topic 57  Custom Exception Handler — Uniform Error Response Shape Across the API
Topic 58  DRF Built-In Exceptions — NotFound, PermissionDenied, AuthenticationFailed, Throttled
```

### LEVEL 16 — Content Negotiation, Renderers & Parsers
```
Topic 59  Renderers — JSONRenderer, BrowsableAPIRenderer, Custom Renderers
Topic 60  Parsers — JSONParser, MultiPartParser, FileUploadParser
Topic 61  Content Negotiation — How DRF Picks Renderer and Parser Per Request
```

### LEVEL 17 — Versioning
```
Topic 62  API Versioning Strategies — URL Path, Query Param, Header, Hostname
Topic 63  DRF Versioning Classes — URLPathVersioning, AcceptHeaderVersioning in Practice
```

### LEVEL 18 — File Uploads & Media
```
Topic 64  Handling File Uploads in DRF — FileField, ImageField, MultiPartParser
Topic 65  Uploading to S3 / Cloud Storage — django-storages in API Context
```

### LEVEL 19 — DRF Settings & Configuration
```
Topic 66  DEFAULT_* Settings — authentication_classes, permission_classes, renderer_classes at Global Level
Topic 67  Per-View Overrides vs Global Settings — When to Use Which
```

### LEVEL 20 — Testing DRF APIs
```
Topic 68  APIClient and APITestCase — The DRF Testing Foundation
Topic 69  Testing Authentication and Permissions — force_authenticate, force_login
Topic 70  Testing Serializers in Isolation — Unit Testing Validation Logic
Topic 71  Testing ViewSets and Custom Actions — Full Request-Response Cycle Tests
```

### LEVEL 21 — Performance Optimization
```
Topic 72  N+1 Query Problem in DRF — How Serializers Trigger Extra Queries
Topic 73  select_related and prefetch_related in get_queryset() — Solving N+1
Topic 74  only() and defer() — Fetching Fewer Columns for Large Serializers
```

### LEVEL 22 — Caching in DRF
```
Topic 75  Response Caching — cache_page, vary_on_headers, vary_on_cookie in APIs
Topic 76  Object-Level Caching with Redis — Caching Serialized Data, Cache Invalidation
```

### LEVEL 23 — JWT & Token Auth Deep Dive
```
Topic 77  JWT Internals — Header, Payload, Signature, Expiry, and Refresh Tokens
Topic 78  simplejwt — Access Token, Refresh Token, Blacklisting, Rotation
Topic 79  JWT Security — Short Expiry, Refresh Rotation, Token Revocation Strategies
```

### LEVEL 24 — OAuth2 & Third-Party Auth
```
Topic 80  OAuth2 Flows — Authorization Code, Client Credentials, and When to Use Each
Topic 81  django-oauth-toolkit — Integrating OAuth2 Provider into a DRF API
```

### LEVEL 25 — API Documentation
```
Topic 82  drf-spectacular — OpenAPI 3 Schema Generation, Customizing @extend_schema
Topic 83  Swagger UI and ReDoc — Serving Interactive API Docs in Production
```

### LEVEL 26 — Production API Engineering
```
Topic 84  Idempotency in REST APIs — Why POST is Dangerous Without It
Topic 85  Soft Deletes, Audit Logs, and History in DRF APIs
Topic 86  Bulk Create / Bulk Update — Handling Lists of Objects Efficiently
Topic 87  Asynchronous Tasks from DRF — Triggering Celery from API Views
Topic 88  Rate Limiting with Redis — Beyond DRF's Built-In Throttling
```

### LEVEL 27 — Advanced DRF Patterns
```
Topic 89  DRF Mixins from Scratch — Understanding How Generic Views Are Built
Topic 90  Custom Base Classes — Shared Logic Across All API Views
Topic 91  Service Layer Pattern — Keeping Business Logic Out of Views and Serializers
Topic 92  Repository Pattern — Abstracting Queryset Logic from DRF Views
Topic 93  Multi-Tenancy in DRF APIs — Tenant Isolation at Queryset Level
```

### LEVEL 28 — Real-World API Case Studies
```
Topic 94  Case Study 1 — Design a User Auth API (Register, Login, Refresh, Logout)
Topic 95  Case Study 2 — Design a Social Feed API (Posts, Likes, Comments, Pagination)
Topic 96  Case Study 3 — Design a Subscription / Billing API (Plans, Webhooks, Idempotency)
```

---

## Study Plans

### Quick Revision — Tonight (3 Hours)
```
Hour 1:
  Topic 7   — DRF Request Lifecycle (entire HTTP → Response flow)
  Topic 11  — What a Serializer actually does
  Topic 13  — ModelSerializer internals
  Topic 14  — Serializer validation — field-level vs object-level

Hour 2:
  Topic 20  — APIView and how dispatch() works
  Topic 27  — ViewSet and how it maps to HTTP methods
  Topic 36  — How permission_classes works
  Topic 31  — How authentication_classes works

Hour 3:
  Topic 47  — Pagination internals
  Topic 72  — N+1 query problem in DRF
  Topic 56  — Exception handling and custom error shapes
  Topic 68  — APIClient and testing fundamentals
```

### Interview in 1 Week
```
Day 1:  Level 0–2  (Topics 1–10)   — REST fundamentals, DRF request/response
Day 2:  Level 3–4  (Topics 11–19)  — Serializers (all of it)
Day 3:  Level 5–7  (Topics 20–30)  — APIView, Generic Views, ViewSets, Routers
Day 4:  Level 8–9  (Topics 31–39)  — Authentication and Permissions
Day 5:  Level 10–12 (Topics 40–49) — Throttling, Filtering, Pagination
Day 6:  Level 15+20 (Topics 56–58, 68–71) — Exceptions and Testing
Day 7:  Level 21+26 (Topics 72–74, 84–88) — Performance and Production
```

### Full Preparation (12 Weeks)
```
Week 1–2:    Level 0–4   (REST, Setup, Request/Response, Serializers Basic + Advanced)
Week 3–4:    Level 5–7   (APIView, Generic Views, ViewSets, Routers)
Week 5–6:    Level 8–10  (Authentication, Permissions, Throttling)
Week 7–8:    Level 11–15 (Filtering, Pagination, URL Design, Nested, Exceptions)
Week 9:      Level 16–19 (Renderers/Parsers, Versioning, File Uploads, Settings)
Week 10:     Level 20–22 (Testing, N+1 Performance, Caching)
Week 11:     Level 23–25 (JWT Deep Dive, OAuth2, API Docs)
Week 12:     Level 26–28 (Production Patterns, Advanced DRF, Case Studies)
```

---

## Topic Priority by Interview Type

### Junior DRF / Backend Developer Interview
```
★★★  Topic 7   — DRF Request Lifecycle
★★★  Topic 11  — What is a Serializer?
★★★  Topic 13  — ModelSerializer
★★★  Topic 14  — Serializer Validation
★★★  Topic 20  — APIView
★★★  Topic 27  — ViewSet
★★★  Topic 31  — Authentication in DRF
★★★  Topic 36  — Permissions in DRF
★★★  Topic 47  — Pagination
★★★  Topic 68  — APIClient and Testing
★★   Topic 23  — Generic Views
★★   Topic 43  — Filtering
★★   Topic 56  — Exception Handling
```

### Mid-Level DRF / Product Company
```
★★★  Topic 15  — Nested Serializers
★★★  Topic 17  — Writable Nested Serializers
★★★  Topic 28  — ModelViewSet
★★★  Topic 34  — JWT Authentication
★★★  Topic 38  — Object-Level Permissions
★★★  Topic 48  — CursorPagination
★★★  Topic 56  — Custom Exception Handler
★★★  Topic 72  — N+1 Problem in DRF
★★★  Topic 73  — select_related and prefetch_related
★★★  Topic 77  — JWT Internals
★★   Topic 29  — @action Decorator
★★   Topic 84  — Idempotency in APIs
★★   Topic 87  — Celery from DRF Views
```

### Senior DRF / Staff Engineer Round
```
★★★  Topic 18  — to_representation() and to_internal_value()
★★★  Topic 21  — APIView dispatch() and initial() internals
★★★  Topic 39  — Custom Permission Classes
★★★  Topic 42  — Custom Throttle Classes
★★★  Topic 57  — Custom Exception Handler design
★★★  Topic 79  — JWT Security and Token Revocation
★★★  Topic 84  — Idempotency
★★★  Topic 89  — DRF Mixins from scratch
★★★  Topic 90  — Custom Base View Classes
★★★  Topic 91  — Service Layer Pattern
★★★  Topic 93  — Multi-Tenancy
★★★  Topic 96  — Subscription API with Webhooks
```

---

## Key Concepts Cheat Sheet

### The DRF Request Lifecycle — Full Diagram
```
HTTP Request (GET /api/users/1/)
         |
    Django URL Dispatcher (urls.py)
         |
    DRF dispatch() — on APIView
         |
    ┌────────────────────────────────────┐
    │  initial()                         │
    │   ├── perform_authentication()     │  ← Runs authentication_classes
    │   ├── check_permissions()          │  ← Runs permission_classes
    │   └── check_throttles()            │  ← Runs throttle_classes
    └────────────────────────────────────┘
         |
    Route to handler method (get / post / put / delete)
         |
    get_queryset()     ← Filter by user, tenant, soft-delete, etc.
         |
    get_object()       ← Fetch single object + run object permissions
         |
    get_serializer()   ← Instantiate serializer with data
         |
    serializer.is_valid() ← Validate incoming data
         |
    serializer.save()  ← .create() or .update() on the model
         |
    Response(serializer.data)
         |
    Renderer           ← JSON, Browsable API, CSV, etc.
         |
HTTP Response (200 OK / 201 Created / 400 Bad Request / etc.)
```

### Serializer Lifecycle — What Happens Inside
```
DESERIALIZATION (incoming request data → Python object)

serializer = UserSerializer(data=request.data)
         |
serializer.is_valid()
  ├── run_validators()            ← Field-level UniqueValidator etc.
  ├── validate_<fieldname>()     ← Per-field custom validation
  └── validate()                 ← Object-level cross-field validation
         |
serializer.validated_data        ← Clean Python dict, safe to use
         |
serializer.save()
  ├── .create(validated_data)    ← If no instance passed
  └── .update(instance, validated_data)  ← If instance passed

SERIALIZATION (Python object → JSON response)

serializer = UserSerializer(instance)
         |
serializer.data
  └── to_representation(instance)  ← Field-by-field conversion to dict
         |
Response(serializer.data)          ← Rendered to JSON by JSONRenderer
```

### ViewSet → URL Mapping (What Router Generates)
```
ModelViewSet ACTION     HTTP METHOD   URL PATTERN
─────────────────────────────────────────────────────
list                    GET           /users/
create                  POST          /users/
retrieve                GET           /users/{id}/
update                  PUT           /users/{id}/
partial_update          PATCH         /users/{id}/
destroy                 DELETE        /users/{id}/
@action(detail=False)   GET/POST      /users/{url_path}/
@action(detail=True)    GET/POST      /users/{id}/{url_path}/
```

### Authentication vs Permission vs Throttle — The Difference
```
AUTHENTICATION       WHO are you?
                     Runs first. Populates request.user.
                     Failure → 401 Unauthorized

PERMISSION           Are you ALLOWED to do this?
                     Runs after auth. Checks request.user vs resource.
                     Failure → 403 Forbidden

THROTTLE             How OFTEN can you do this?
                     Runs after permissions. Checks rate limits.
                     Failure → 429 Too Many Requests

ORDER: Auth → Permission → Throttle → View handler
```

### Serializer Field Types — Quick Reference
```
FIELD                   USE WHEN
──────────────────────────────────────────────────────────
CharField               Plain text
IntegerField            Integer numbers
FloatField / DecimalField  Numbers with decimals (use Decimal for money)
BooleanField            True/False
DateField / DateTimeField  Dates and timestamps
EmailField              Email with format validation
URLField                URL with format validation
ChoiceField             Fixed set of allowed values
ListField               A list of values of same type
DictField               Arbitrary key-value pairs
SerializerMethodField   Computed read-only field (calls get_<fieldname>)
PrimaryKeyRelatedField  FK → returns pk integer
SlugRelatedField        FK → returns a specific field (e.g. username)
HyperlinkedRelatedField FK → returns full URL to related resource
Nested Serializer       FK → returns full nested object representation
```

### Status Codes Every DRF Developer Must Know
```
2xx SUCCESS
  200 OK              GET, PUT, PATCH — success with body
  201 Created         POST — resource created (include Location header)
  204 No Content      DELETE — success, no body

4xx CLIENT ERRORS
  400 Bad Request     Validation failed — serializer.errors
  401 Unauthorized    Not authenticated — missing or invalid token
  403 Forbidden       Authenticated but not allowed — permission denied
  404 Not Found       Resource does not exist
  405 Method Not Allowed  HTTP method not supported on this endpoint
  409 Conflict        Resource already exists (duplicate)
  422 Unprocessable   Semantically invalid data (less common in DRF)
  429 Too Many Requests  Throttle limit hit

5xx SERVER ERRORS
  500 Internal Server Error  Unhandled exception — always log these
  503 Service Unavailable    Downstream dependency is down
```

### When to Use Which View Class
```
SCENARIO                                        USE
────────────────────────────────────────────────────────────────
Simple one-off endpoint with custom logic       APIView
Standard list + create endpoint                 ListCreateAPIView
Standard retrieve + update + delete             RetrieveUpdateDestroyAPIView
Full CRUD for a resource                        ModelViewSet
Full CRUD + custom actions (@action)            ModelViewSet + @action
Read-only resource list + detail                ReadOnlyModelViewSet
Non-model endpoint (external API call, etc.)    APIView
Bulk operations, complex workflows              APIView (manual control)
```

### N+1 Problem — The Most Common DRF Performance Bug
```
PROBLEM (N+1 queries):
  class PostSerializer(ModelSerializer):
      author_name = SerializerMethodField()
      def get_author_name(self, obj):
          return obj.author.name  ← 1 query per post!

  For 100 posts → 1 (list query) + 100 (author queries) = 101 queries

FIX (eager loading in get_queryset):
  def get_queryset(self):
      return Post.objects.select_related('author')
                         .prefetch_related('tags', 'comments')

  For 100 posts → 1 (posts) + 1 (authors) + 1 (tags) + 1 (comments) = 4 queries
```

---

## Anti-Patterns to Mention in Every Interview

These show senior-level thinking. Mention what you are AVOIDING and why.

```
1.  Business logic inside serializers
    → Serializers should validate and transform data, not make decisions
    → Move business logic to a service layer / manager method
    → Serializer.save() should call a service function, not contain logic itself

2.  Business logic inside views
    → Views should orchestrate: receive input, call service, return response
    → Views with 100-line save() or perform_create() are a red flag
    → Keep views thin, services fat

3.  Not overriding get_queryset() — using queryset = Model.objects.all()
    → Class-level queryset is evaluated once at class definition time
    → Use get_queryset() for dynamic filtering, per-user data, request-based logic
    → Also: class-level queryset can expose cross-user data in multi-tenant apps

4.  Returning 200 OK for everything including errors
    → DRF gives you correct status codes — don't override with 200 + error flag
    → Consumers depend on HTTP status codes for programmatic error handling

5.  Catching all exceptions and returning 500
    → Let DRF's exception handler deal with APIException subclasses
    → Only catch what you can handle; let unhandled errors bubble up and get logged

6.  No select_related / prefetch_related in serializers with relations
    → Every nested serializer or SerializerMethodField that touches a relation
       is a potential N+1 query bomb
    → Always check Django Debug Toolbar or query count in tests

7.  Storing JWT secret as hardcoded string
    → Use environment variables / secrets manager for SIGNING_KEY
    → Rotate signing keys periodically; support key rollover

8.  Pagination disabled for list endpoints
    → GET /api/posts/ returning 50,000 rows will kill your DB and the client
    → Always paginate list endpoints; default page size should be ≤ 100

9.  Not writing serializer tests independently of views
    → Serializer validation bugs are easiest to catch in isolation
    → Test serializer.is_valid(), serializer.errors, serializer.data separately

10. Using ModelViewSet for endpoints that are not CRUD
    → If your endpoint does something complex (approve, archive, publish),
       a custom @action or a dedicated APIView is clearer than shoehorning into CRUD
    → Don't map every action to list/create/retrieve just because it "fits"
```

---

## Interview Q&A — Most Asked DRF Questions

### Conceptual (Verbal)
```
Q: What is the difference between Serializer and ModelSerializer?
A: Serializer is the base class where you declare every field manually.
   ModelSerializer introspects the linked Django model and auto-generates
   fields, validators (unique, blank), and the default create() and update()
   methods. ModelSerializer is what you use for 95% of CRUD APIs because it
   eliminates boilerplate. Use plain Serializer when you need fields that
   don't map to a model, or for non-model data like login credentials or
   analytics payloads.

Q: What is the difference between APIView, GenericAPIView, and ViewSet?
A: APIView is the base class — gives you DRF's request/response, auth,
   permissions, and throttling on top of Django's View. You implement
   get(), post(), etc. manually.
   GenericAPIView adds queryset, serializer_class, get_queryset(),
   get_serializer() — the plumbing for model-based views. Mixins
   (ListModelMixin, CreateModelMixin) attach to it to give CRUD behaviour.
   ListAPIView, CreateAPIView etc. are pre-combined GenericAPIView + mixins.
   ViewSet groups related actions on a resource (list/create/retrieve/
   update/destroy) into one class. ModelViewSet provides all of them.
   Router auto-generates URL patterns from ViewSets.

Q: How does DRF authentication work?
A: DRF calls each class in authentication_classes in order. The first one
   that successfully identifies the user sets request.user and request.auth.
   If none authenticate and the view requires authentication, DRF raises
   AuthenticationFailed (401). The authentication class does NOT decide if
   the user is allowed — that is the job of permission_classes.

Q: What is the difference between authentication and permission in DRF?
A: Authentication answers WHO are you? — identifies the user from the
   request (token, session, API key). Permission answers are you ALLOWED?
   — decides if the identified user can access this specific resource.
   Authentication runs first; 401 if it fails. Permission runs second;
   403 if it fails. They are separate concerns and separate classes.

Q: How do you solve the N+1 query problem in DRF?
A: N+1 happens when a serializer accesses a relation inside a loop — for
   each object in the list it fires a separate query. Fix: override
   get_queryset() and add select_related() for forward FK/OneToOne relations
   and prefetch_related() for reverse FK or M2M relations. Always verify
   with Django Debug Toolbar or assertNumQueries in tests.
```

### Practical (Code)
```
Q: How do you make a field read-only in a serializer?
A: Three ways depending on context:
   1. read_only=True on the field: id = serializers.IntegerField(read_only=True)
   2. Add it to read_only_fields in Meta: read_only_fields = ['id', 'created_at']
   3. SerializerMethodField is always read-only

Q: How do you validate that two passwords match in a serializer?
A: Use object-level validation in validate():
   def validate(self, data):
       if data['password'] != data['confirm_password']:
           raise serializers.ValidationError("Passwords do not match.")
       return data
   Field-level validate_<field>() only sees one field at a time — use
   validate() when you need to compare multiple fields together.

Q: How do you restrict a queryset so users only see their own data?
A: Override get_queryset() in the view:
   def get_queryset(self):
       return Order.objects.filter(user=self.request.user)
   Never filter at the serializer level — the view controls data access.
   Also add object-level permission has_object_permission() for detail views
   as a second line of defense.

Q: How do you return a custom error response format across all endpoints?
A: Write a custom exception handler and set it in settings:
   REST_FRAMEWORK = {
       'EXCEPTION_HANDLER': 'myapp.exceptions.custom_exception_handler'
   }
   def custom_exception_handler(exc, context):
       response = exception_handler(exc, context)
       if response is not None:
           response.data = {
               'success': False,
               'errors': response.data,
               'status_code': response.status_code
           }
       return response
```

---

## DRF Settings — Most Important Defaults to Know
```
REST_FRAMEWORK = {
    # Auth: what classes identify the user?
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],

    # Permission: who can access by default?
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # Throttle: request rate limits
    'DEFAULT_THROTTLE_CLASSES': [],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    },

    # Renderer: output format
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # remove in production
    ],

    # Parser: accepted input formats
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
    ],

    # Pagination: default for all list views
    'DEFAULT_PAGINATION_CLASS': None,  # must set explicitly
    'PAGE_SIZE': 20,

    # Filtering
    'DEFAULT_FILTER_BACKENDS': [],

    # Schema
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    # Exception handler
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
}
```

---

## Pagination Decision Framework
```
NEED                                             USE
──────────────────────────────────────────────────────────────────
Simple page 1, 2, 3 navigation                  PageNumberPagination
Skip arbitrary offset (admin, reports)          LimitOffsetPagination
Infinite scroll, feed, real-time data           CursorPagination
(Cursor is the only one stable when data changes between pages)

NEVER use offset pagination for large datasets without a limit —
OFFSET 10000 forces the DB to scan 10000 rows before returning results.
Use CursorPagination or keyset pagination for high-volume lists.
```

---

## JWT Token Flow Diagram
```
CLIENT                              SERVER
──────                              ──────
POST /auth/login/
  { username, password }
                        ──────────→
                                    Validate credentials
                                    Generate:
                                      access_token (short, 5–15 min)
                                      refresh_token (long, 7–30 days)
                        ←──────────
  { access, refresh }

GET /api/orders/
  Authorization: Bearer <access_token>
                        ──────────→
                                    Verify JWT signature
                                    Check expiry
                                    Extract user from payload
                                    Return data
                        ←──────────
  { orders: [...] }

(access_token expires)

POST /auth/token/refresh/
  { refresh: <refresh_token> }
                        ──────────→
                                    Validate refresh token
                                    Check it is not blacklisted
                                    Issue new access token
                                    (optionally rotate refresh token)
                        ←──────────
  { access: <new_access_token> }
```

---

## The Service Layer Pattern in DRF
```
WITHOUT service layer (common mistake):
  class OrderViewSet(ModelViewSet):
      def perform_create(self, serializer):
          # business logic inside view — bad
          user = self.request.user
          if user.plan == 'free' and user.orders.count() >= 5:
              raise PermissionDenied("Free plan limit reached")
          order = serializer.save(user=user)
          send_confirmation_email.delay(order.id)
          update_inventory(order)

WITH service layer (senior pattern):
  # services/order_service.py
  def create_order(user, validated_data):
      if user.plan == 'free' and user.orders.count() >= 5:
          raise OrderLimitExceeded("Free plan limit reached")
      order = Order.objects.create(user=user, **validated_data)
      send_confirmation_email.delay(order.id)
      update_inventory(order)
      return order

  # views.py — thin, just orchestrates
  class OrderViewSet(ModelViewSet):
      def perform_create(self, serializer):
          order = create_order(self.request.user, serializer.validated_data)
          serializer.instance = order

WHY: Service layer is testable without HTTP, reusable from Celery tasks,
     CLI commands, management commands, and other views.
```

---

## Common DRF Mistakes — Quick Reference
```
MISTAKE                                   CORRECT APPROACH
──────────────────────────────────────────────────────────────────
queryset = Model.objects.all()            Use get_queryset() for dynamic logic
Logic inside serializer.validate()        Validation only — no DB writes
Business logic in perform_create()        Move to service layer
Missing select_related in list views      Always check query count
Returning 200 for validation errors       Return 400 with serializer.errors
Using SessionAuth for mobile/SPA clients  Use JWT (TokenAuth has no expiry)
No pagination on list endpoints           Always paginate; default ≤ 100
Hardcoded secret keys in settings.py      Use environment variables
No object-level permissions               Add has_object_permission() check
Testing only via HTTP (no unit tests)     Test serializers and services in isolation
```

---

*96 topics · 28 levels · Complete Django REST Framework 0 → 100 path*
*100% DRF and RESTful API focused — no plain Django, no templates, no forms*
*Built for developers targeting junior → senior DRF API engineer roles*

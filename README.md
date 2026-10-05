# data-engineering-lab

A structured, hands-on lab of data-engineering experiments and proof-of-concepts
across the modern data stack — **Spark, AWS, Kafka/Confluent, and advanced SQL**.

Each topic lives in its own folder, and every experiment is a small, self-contained,
numbered module so it can be built, run, and reviewed on its own.

---

## Repository structure

| Area | Folder | What's inside | Status |
|------|--------|----------------|--------|
| Streaming | `Kafka/Confluent POC/` | Producers, consumers, Schema Registry, streaming POCs | Active |
| SQL | `SQL/` | Query practice, patterns, and advanced SQL problems | Active |
| Spark | `Spark/` | Batch & structured streaming, transformations, tuning | Planned |
| AWS | `AWS/` | S3, Glue, EMR, Lambda, and related cloud data services | Planned |

> Status reflects what currently exists in the repo vs. what's on the roadmap.

---

## How it's organized

Experiments inside each area are **numbered** so the order and history are easy to
follow, for example:

```
Kafka/Confluent POC/
├── 001_...
├── 002_...
├── ...
└── 011_Schema_Streaming_Consumer/
```

Conventions used throughout:

- **Numbered prefixes** (`011_...`) keep experiments ordered and discoverable.
- **One concept per folder** — each POC focuses on a single idea end-to-end.
- **Self-contained** — each experiment aims to run on its own with minimal shared setup.
- A short note or README inside a folder explains *what* the experiment demonstrates
  and *how* to run it (added per experiment).

---

## Tech & tools

- **Streaming:** Apache Kafka, Confluent Platform, Schema Registry
- **Processing:** Apache Spark (PySpark / Spark SQL)
- **Cloud:** AWS (S3, Glue, EMR, Lambda, and related services)
- **Query:** Advanced SQL (window functions, CTEs, optimization, modeling patterns)
- **Languages:** Python, SQL

*(Exact versions and setup are documented within each experiment folder.)*

---

## Getting started

```bash
# Clone the repo
git clone https://github.com/prakashupes/data-engineering-lab.git
cd data-engineering-lab

# Browse to the area you're interested in, e.g. Kafka
cd "Kafka/Confluent POC"
```

Each experiment folder lists its own prerequisites (e.g. a running Kafka broker, a
Spark install, or AWS credentials) and run instructions.

---

## Roadmap

- [ ] Spark batch + structured streaming experiments
- [ ] AWS data-service POCs (S3 / Glue / EMR / Lambda)
- [ ] Expand advanced SQL problem set
- [ ] Add per-folder READMEs with run steps for every experiment
- [ ] End-to-end mini pipeline tying Kafka → Spark → AWS together

---

## About

This repo is my personal data-engineering workspace — a place to experiment, build
POCs, and deepen hands-on understanding of the tools used across real pipelines.
It is organized by topic rather than as a single project, so it doubles as a
reference and a revision resource.

**Author:** Prakash Tiwari ([@prakashupes](https://github.com/prakashupes))
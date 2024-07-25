---
id: ma636ohctu6fqefl0jrnsge
title: Theoretical
desc: ''
updated: 1718217849248
created: 1718209924185
---

Notes regarding the theoretical discussion of RAG utilizing a vector database alongside a NoSQL database like MongoDB.

1. `What is NoSQL database.`
2. `Types of NoSQL database.`
3. `What is Vector database.`
4. `Benefits of using vector database.`
5. `NoSQL database as a Vector Search.`
6. `What is combine solution and it's benefit.`
7. `How to choose vector database.`

### 1. `What is NoSQL database.`
A NoSql database provides a mechanism for storage and retrieval of data other than the tabular relations used in relational databases. Unlike relational databases, NoSQL databases (sometimes referred to as "Not Only SQL") are particulary suited for storing large sets of distributed data and are highly optimized for retrieval and appending operations.
### 2. `Types of NoSQL database.`
`Document Databases:` Store data in documents similar to JSON (JavaScript Object Notation) objects. Each document contains pairs of fields and values. Examples include MongoDB and CouchDB.

`Key-Value Stores:` Every single item in the database is stored as an attribute name (or 'key') together with its value. Examples include Redis and DynamoDB.

`Wide-Column Stores:` Store data in tables, rows, and dynamic columns. They are optimized for queries over large datasets, and columnar storage allows for efficient data compression and fast data retrieval. Examples include Apache Cassandra and Google Bigtable.

`Graph Databases:` Designed to store and navigate relationships. They have structures comprising of nodes(entities), edges (relationships), and properties. Examples include Neo4j and Amazon Neptune.

>Advantages of No-SQL based database. (Irrespective to vector databases) 
-

- Using NoSQL databases offers several advantages, particularly when dealing with large volumes of diverse data types and when high scalability and performance are crucial.

1. `Scalability`
2. `Distributed architecture`
3. `Manage larger volumes`
4. `Flexible Schema`
5. `High Performance`
6. `High availability and replication`
7. `Development Speed`

### 3. `What is Vector database.`
A vector database is a specialized type of database designed to efficiently handle vector data, typically used in the context of artificial intelligence, particularly for similarity search. Vector data refers to data represented as high-dimensional vectors, which are often derived from complex data such as text, images, or audio using feature extraction techniques.
>Key Characteristics of Vector Databases:
-
1. `Storage of High-Dimensional Vectors`
2. `Efficient Similarity Search`
3. `Indexing Mechanisms`
4. `Advanced indexing mechanisms(KD-trees or ball trees, hashing based methods like Locailty Sensitive Hashing (LSH), or even neural network-based approaches)`

--
>Advantages of Vector Databases:
-
`Speed and Efficiency`
`Scalability`
`Precision`
`Speed`
`Simplicity`

--
>Applications of Vector Databases (RAG)
-
`Recommendation Systems`
`Information Retrieval`
`Question Answering`

--
>Examples of Vector Databases
-
`Chroma`
`Pinecone`
`Weaviate`
`Milvus`
`FAISS`
`Qdrant`
`Vespa`
`Vald`
`Vector Flow`
`OpenSearch`
`PgVector`
`Open Source Vector Databases`

--
>NoSQL or SQL based database which we can use as a Vector Database.
-
1. `MongoDB Vector Search`
2. `AstraDB(Cassandra) Vector Search`
3. `Redis`
4. `Elasticsearch`
5. `Neo4j`
6. `Postgre SQL`

--
>What is combine solution and it's benefit. (NoSQL + VectorDB)
-
1. `Optimized handling of high-dimensional vector data`
2. `Real-time searchin`
3. `Improved similarity searches`
4. `Advance embedding`               
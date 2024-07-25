---
id: itmg9k688ikfolzr2rni4lc
title: Advanced Rag - Lost in Middle
desc: ''
updated: 1718994431374
created: 1718646013698
---
---
Address Lost in Middle Phenomenon and utilize Merger Retriever and LongContextReorder methods.

`Ranking Topics`
1. What is Reranking?
2. Why Reranking is Important?
3. Reranking from Scratch (Sentence Transformer and BM25 API)
4. Reranking using Cross Encoder
5. Reranking using Cohere API
6. Solution of Lost in Middle Paper <------
7. Rank Fusion Paper 
8. Flash Rank 

1. Data --> 

2. Data into Chunks -->

3. Chunks into embeddings via embedding model -->

4. Embeddings into Vector Database

Then

 User asks a Query -->

5. Query is converted to an embedding via embedding model -->

6. Utilize similarity search between QueryEmbedding and Vectors in Vector database -->

7. Returned back Ranked Results or similar documents.

Then Feed these Ranked Results and Query, both vectorize/embedded into LLM with PROMPT as well

- Query + Documents + Prompt --> LLM

## Merge Retriever

`Original Rag:`

1. Documents(vectorized) into Vector DB

2. You use a Retriever to get ranked documents

3. Then asking Query

- Problem: Context can be too large

`Advanced Rag v1:`

1. Documents(vectorized) into Vector DB

2. Create separate storage containers for VectorDB

3. Use query to determine which container to pull from

4. Get Response: 
- Reduce Redundancy(Remove Duplicates) --> 
- Perform clustering to get similar documents clustered together -->
- Perform compression
- Reorder

`Compression:` 
- In RAG-based applications, the challenge lies in handling documents that contain a mix of relevant and irrelevant information for a given query. Without proper filtering, these documents can result in costly LLLM calls and less accurate responses.
- `Contextual Compression` aims to address this by selectively compressing the retrieved documents based on the context of the query. This process involves two main steps
1. `Document Compression:` The retrieved documents are passed through a compressor, which reduces the size of the documents by either condensing the content or removing sections deemed irrelevant ot the query.
2. `Relevance Filtering:` Alongside compression, documents that are entirely unrelated to the query are filtered out, ensuring that only relevant information is processed further.

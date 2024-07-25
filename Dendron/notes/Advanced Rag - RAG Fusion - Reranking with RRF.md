---
id: n52d6nyhn21zjtyspifdrec
title: Advanced Rag - RAG Fusion - Reranking with RRF
desc: ''
updated: 1718992017088
created: 1718985584368
---
---
RAG Fusion: `Retrieval` or ranking --> Reciprocal Rank Fusion utilizing a formula to rerank the result. 2 Stage retrieval


`Ranking Topics`
1. What is Reranking?
2. Why Reranking is Important?
3. Reranking from Scratch (Sentence Transformer and BM25 API)
4. Reranking using Cross Encoder
5. Reranking using Cohere API
6. Solution of Lost in Middle Paper
7. Rank Fusion Paper <------
8. Flash Rank


`Structure`
Basically we send our Original query to LLM for it to generate k-similar queries. Then perform similarity search on all k-similar queries and the original query. Then perform ranking using reciprocal formula.

- Keep in Mind that you are generating N-similar vectors per K-similar queries, alongside the N-similar vectors for your original queries. 
- So you have to Combine and rank --> N + (N*K) vectors

1. Translate a user's query into similar, yet distinct queries via an LLM.
2. Perform vector searches for the original and its newly generated query siblings.
3. Aggregate and refine all the results using reciprocal rank fusion.
Use reranked list of results and guiding the large language model to a generate output
- Reciprocal Rank Fusion (RRF) is a technique for combining the ranks of multiple search result lists to produce a single, unified ranking. Devloped in collaboration with the University of Waterloo (CAN) and Google.
- Reciprocal Rank = [ 1 / Rank ] --> So let's say you have N=4, meaning there are 4 retrieved similar documents of different ranks (R1, R2, R3, R4). In Reciprocal Rank it would be = (1/1, 1/2, 1/3, 1/4)

`Example`: K=3 N=4 --> Q1=[A,C,D,B], Q2=[B,A,C,D], Q3=[D,B,A,C]
- Q1=[ A(1/1), C(1/2), D(1/3), B(1/4) ]
- Q2=[ B(1/1), A(1/2), C(1/3), D(1/4) ]
- Q3=[ D(1/1), B(1/2), A(1/3), C(1/4) ]

`Fusion`: Sum{ 1 / (rank + normalization) } --> normalization if needed otherwise 0
- Sum(A): [ (1/1), (1/2), (1/3) ] = 1.83
- Sum(B): [ (1/4), (1/1), (1/2) ] = 1.30
- Sum(C): [ (1/2), (1/3), (1/4) ] = 1.08
- Sum(D): [ (1/3), (1/4), (1/1) ] = 1.58

`Rank`: Final result as of Fusion (A, D, B, C)

## MMR
`Maximal Marginal Relevance (MMR)`: is a criterion used in information retrieval and text summarization. Its goal is to reduce redundancy while maintaining query relevance. How it works -->
1. Re-Ranking Documents:
    - MMR is applied to re-rank retrieved documents. It balances relevance and diversity.
    - When evaluating potential documents, MMR considers both their closeness to the query and their uniqueness compared to already ranked documents.
2. KeyPhrase Extraction Example:
    - Imagine extracting keyphrases from a set of documents related to a specific category
    - Initially, phrases like "Good Product", "Great Product", and "Nice Product" might be ranked highly.
    - However, these similar phrases can dominate limited display space.
    MMR helps by promoting diverse keyphrases, ensuring users see a variety of information about the documents.
3. Two Approaches:
    - Cosine Similarity: The naive approach involves using cosine similarity to identify similar terms. However, setting a threshold for similarity can be challenging.
    - MMR: Instead of removing redundant phrases, MMR re-ranks them. It aims to maximize diversity while maintaining relevance. The opitmal mix is chieved by setting a parameter (alpha) based on the use case and dataset.
- In  summary, MMR enhances document ranking and keyphrase extraction by striking a balance between relevance and diversity. It's a valuable tool for improving information retrieval systems and summarization.
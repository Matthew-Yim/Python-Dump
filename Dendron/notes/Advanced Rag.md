---
id: f4anygpff38yitacdokb9v9
title: Advanced Rag
desc: ''
updated: 1718304903185
created: 1718292322050
---
## Random Notes
1. Keywords are important for keyword-based search.
2. Document analysis involves extracting keywords.
3. Keyword-based search relies on sparse embeddings.
4. Understanding document structure aids in keyword extraction.
5. Efficient keyword extraction enhances search accuracy.
6. Semantic similarity improves document retrieval performance.
7. Machine learning algorithms can optimize keyword extraction methods.

# Procedure:
So basically Advanced Rag is exactly what you were trying to do, multi-step FAISS. 

In Sunny's case, we first perform the embeddings using a sentence transformer(model) `Basically creates embedding out of sentences -- might not be the best approach when dealing with structured data`. This returns document embeddings, then we pass query in the same process, creating a embedding for the query. Then we perform a similarity search via:

`from sklearn.mnetrics.pairwise import cosine_similarity`

`similarities = cosine_similarity(np.array([query_embedding]), document_emdbeddings)`

To get most similar

`most_similar_index = np.argmax(similarities)` 

`most_similar_document = documents[most_similar_index]`

To get similarity Score and Sort:

`similarity_score = similarities[0][most_similar_index]`

`sorted_indices = np.argsort(similarities[0])[::-1]`

To get ranked documents with score:

`ranked_documents = [(documents[i], similarities[0][i]) for i in sorted_indices]`

## Then We ReRank again:
### Process: 
Here we use Rank BM25 via api where the ranking is working on a keyword/token level

To get the top k-documents:

`from rank_bm25 import BM250kapi`

`top_4_documents = [doc[0] for doc in ranked_documents[:4]]`

To split documents to embed keywords/tokens: (Tokenization)

`tokenized_top_4_documents = [doc.split() for doc in top_4_documents]`

`tokenized_query = query.split()`

To Embed:

`bm25 = BM250kapi(tokenized_top_4_documents)`

`bm25_scores = bm25.get_scores(tokenized_query)`

To Sort BM25:

`sorted_indicies2 = np.argsort(bm25_scores)[::-1]`
`rerankedd_documents = [(top_4_documents[i], bm25_scores[i]) for i in sorted_indices2]

## Different ranking through Cross Encoders
- Cross encoding refes to passing in the two sentences, let's say A and B into model `BERT` then we get returned a classifier value between 0-1.
- Usually these two sentences is the query and the sentence we are looking for similarity. Let's say we have 4 potential similar matches, combine each 4 matches with query to get 4 pairs to pass to BERT
- Logits is the value before being passed through activation function

### Bi-Encoder:
Bi-Encoders or Sentence transformers
1. Calculates a fixed-size vector representation(`embedding`) given some texts or images.
2. Embedding calculation is often efficient, embedding similarity calculation is `very fast`
3. Application for a `wide range of task`, such as semantic textual similarity, semantic search, clustering, classification, paraphrase mining, and more.
4. Often used as a `first step in a two-step retrieval process`, where a Cross-Encoder(a.k.a reranker) model is used to re-rank the top-k results from the bi-encoder.
5. Passes each sentence separately through BERT

### Cross Encoders:
Cross Encoder or Reranker models.
1. Calculates a `similarity score` given `pairs of texts`.
2. Generally provides `superior performance` compared to a Sentence Transformer (a.k.a Bi-Encoder) model.
3. Often `slower` than a Sentence Transformer model, as it requires computation for each pair rather tahn each text.
4. Due to the previous 2 characteristics, Cross Encoders are often used to `re-rank the top-k results` from a Sentence Transformer model.
5. Concatonate or combine Sentences and pass once through BERT

### BERT Code
`from transformers import BertTokenizer, BertForSequenceClassification`

`import torch`
- Initialize model and tokenizer

`model = BertForSequenceClassification.from_pretrained('bert-base-uncased')`

`tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')`
- Input texts

`sentence_a = "Whatever you want A"`

`sentence_b = "Whatever you want B"`
- Encode inputs

`inputs = tokenizer(sentence_a, sentence_b, return_tensors='pt', padding=True, truncation=True)`
- Get the model output

`outputs = model(**inputs)`

`logits = outputs.logits`
- Convert logits to probabilities

`probs = torch.softmax(logits, dim=1)`
- Assuming a binary classification task (similarity score)

`similarity_score = probs[0][1].item()`

`print(f"Similarity score: {similarity_score}")`

## Use Cohere to ReRank from Bert procedure
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Corpus documents
documents = [
"Document about python programming language and data analysis",
"Document discussing machine learning algorithms and programming techniques",
"Overview of natural language processing and its applications"
]

# Query
query = ["python programming"]

# Step 1: TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("TF-IDF Matrix for Documents:")
print(tfidf_matrix.toarray())

# Step 2: Convert query into the same TF-IDF vector space
query_vector = vectorizer.transform(query)

print("\nTF-IDF Vector for Query:")
print(query_vector.toarray())

# Step 3: Calculate Cosine Similarity
similarity = cosine_similarity(query_vector, tfidf_matrix)

print("\nCosine Similarity Scores:")
for i, score in enumerate(similarity[0]):
    print("Document", i+1, "Similarity:", score)
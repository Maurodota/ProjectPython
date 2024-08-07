import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Carregar dados
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Criar matriz de usuário-filme
user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Calcular similaridade do cosseno
similarity_matrix = cosine_similarity(user_movie_matrix)

# Função de recomendação
def recommend_movies(user_id, num_recommendations=5):
    user_index = user_id - 1  # Ajustar para índice zero-based
    similarity_scores = list(enumerate(similarity_matrix[user_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similar_users = [score[0] for score in similarity_scores[1:num_recommendations + 1]]
    
    recommendations = []
    for user in similar_users:
        similar_user_ratings = user_movie_matrix.iloc[user]
        recommended_movies = similar_user_ratings[similar_user_ratings > 4].index.tolist()
        recommendations.extend(recommended_movies)
    
    recommended_movies = pd.DataFrame(recommendations, columns=['movieId'])
    recommended_movies = recommended_movies.merge(movies, on='movieId').drop_duplicates()
    
    return recommended_movies

# Exemplo de uso
print(recommend_movies(1))

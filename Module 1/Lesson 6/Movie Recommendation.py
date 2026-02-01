import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

# Initialize colorama
init(autoreset=True)

# Load and preprocess the dataset
def load_data(file_path='/Users/ryan/Desktop/Python/Codingal AI/Module 1/Lesson 6/imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        sys.exit()

movies_df = load_data()

# Vectorize combined features and compute cosine similarity (kept for future upgrades)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on genre, mood, rating, or randomness
def recommend_movies(genre=None, mood=None, rating=None, top_n=5, random_pick=False):

    # Genre or random selection
    if random_pick:
        filtered_movies = movies_df.copy()
    elif genre:
        filtered_movies = movies_df[movies_df['Genre'].str.contains(genre, case=False, na=False)]
    else:
        filtered_movies = movies_df

    # Rating filter
    if rating:
        filtered_movies = filtered_movies[filtered_movies['IMDB_Rating'] >= rating]

    if filtered_movies.empty:
        return "No movies found with the selected preferences."

    # Mood-based sorting (not applied for random picks)
    if mood and not random_pick:
        polarity = TextBlob(mood).sentiment.polarity
        if polarity > 0:
            filtered_movies = filtered_movies.sort_values(by='IMDB_Rating', ascending=False)
        elif polarity < 0:
            filtered_movies = filtered_movies.sort_values(by='IMDB_Rating', ascending=True)

    # Random or ranked results
    if random_pick:
        top_movies = filtered_movies.sample(n=min(top_n, len(filtered_movies)))
    else:
        top_movies = filtered_movies.head(top_n)

    return top_movies[['Series_Title', 'Genre', 'IMDB_Rating']]

# Display movie recommendations
def display_recommendations(recs, name):
    print(Fore.CYAN + f"\n🎥 Movie Recommendations for {name}:\n")
    for _, row in recs.iterrows():
        print(Fore.GREEN + f"{row['Series_Title']} ({row['Genre']}) - ⭐ {row['IMDB_Rating']}")
    print()

# Small processing animation
def processing_animation():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

# Handle AI logic
def handle_ai(name):
    genre_input = input(
        Fore.YELLOW +
        "Enter a movie genre (e.g., Action, Comedy, Drama) or type 'random': "
    ).strip()

    random_pick = genre_input.lower() == 'random'
    genre = None if random_pick else genre_input

    mood = input(Fore.YELLOW + "How are you feeling today? (Describe your mood): ").strip()
    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()

    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "positive 😊" if polarity > 0 else "negative 😞" if polarity < 0 else "neutral 😐"
    print(f"{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f})\n")

    # Ask for minimum IMDB rating
    while True:
        rating_input = input(Fore.YELLOW + "Enter minimum IMDB_Rating (7.6–9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

    print(Fore.BLUE + f"\nFinding movies for {name}", end="", flush=True)
    processing_animation()

    recs = recommend_movies(
        genre=genre,
        mood=mood,
        rating=rating,
        top_n=5,
        random_pick=random_pick
    )

    if isinstance(recs, str):
        print(Fore.RED + recs + "\n")
    else:
        display_recommendations(recs, name)

    # Option for more recommendations
    while True:
        random_choice = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if random_choice.lower() == 'no':
            print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🍿🎬\n")
            break
        elif random_choice.lower() == 'yes':
            recs = recommend_movies(
                genre=genre,
                mood=mood,
                rating=rating,
                top_n=5,
                random_pick=random_pick
            )
            if isinstance(recs, str):
                print(Fore.RED + recs + "\n")
            else:
                display_recommendations(recs, name)
        else:
            print(Fore.RED + "Invalid choice. Try again.\n")

# Main program
def main():
    print(Fore.BLUE + "🎬 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
    name = input(Fore.YELLOW + "What's your name? ").strip()
    print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
    handle_ai(name)

if __name__ == "__main__":
    main()
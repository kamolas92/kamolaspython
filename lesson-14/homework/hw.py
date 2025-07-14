#1
{
    "Students":

        [
            {
                "ID":1,
                "Name":"Sitora",
                "Age":25,
                "Pets":["cats","dogs","beards"],
                "FamilyMembers":
                                [
                                    {
                                        "Name":"Alex",
                                        "Age":40,
                                        "relative":"Dad"
                                    },
                                    {
                                        "Name":"Sara",
                                        "Age":35,
                                        "relative":"MaM"

                                    },
                                    {
                                        "Name":"Sevara",
                                        "Age":23,
                                        "relative":"Sister"

                                    }

                                ]
            },
            {
                "ID":1,
                "Name":"Azizbek",
                "Age":25,
                "Pets":["cats","dogs","beards"],
                "FamilyMembers":
                                [
                                    {
                                        "Name":"Bob",
                                        "Age":40,
                                        "relative":"Dad"
                                    },
                                    {
                                        "Name":"Ann",
                                        "Age":35,
                                        "relative":"MaM"

                                    },
                                    {
                                        "Name":"Lisa",
                                        "Age":23,
                                        "relative":"Sister"

                                    }

                                ]
            }
        ]
}

#2
import requests

# Replace with your actual API key from OpenWeatherMap
API_KEY = "your_api_key_here"
city = "Tashkent"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"🌤️ Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather Description: {data['weather'][0]['description'].title()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("❌ Error fetching data:", data.get("message", "Unknown error"))

except requests.RequestException as e:
    print("⚠️ Network error:", e)

#3
import json
import os

# File path
FILE_NAME = "books.json"

# Load books from file
def load_books():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=2)

# Add new book
def add_book():
    books = load_books()
    new_id = max([book["id"] for book in books], default=0) + 1
    title = input("📘 Enter book title: ")
    author = input("✍️  Enter author: ")
    year = int(input("📅 Enter publication year: "))
    books.append({"id": new_id, "title": title, "author": author, "year": year})
    save_books(books)
    print("✅ Book added successfully.\n")

# Update existing book
def update_book():
    books = load_books()
    book_id = int(input("🔁 Enter the ID of the book to update: "))
    for book in books:
        if book["id"] == book_id:
            book["title"] = input(f"New title [{book['title']}]: ") or book["title"]
            book["author"] = input(f"New author [{book['author']}]: ") or book["author"]
            year_input = input(f"New year [{book['year']}]: ")
            if year_input:
                book["year"] = int(year_input)
            save_books(books)
            print("✅ Book updated.\n")
            return
    print("❌ Book not found.\n")

# Delete a book
def delete_book():
    books = load_books()
    book_id = int(input("🗑️ Enter the ID of the book to delete: "))
    new_books = [book for book in books if book["id"] != book_id]
    if len(new_books) < len(books):
        save_books(new_books)
        print("✅ Book deleted.\n")
    else:
        print("❌ Book ID not found.\n")

# Display all books
def list_books():
    books = load_books()
    if not books:
        print("📂 No books found.")
        return
    print("\n📚 Book List:")
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['year']}")
    print()

# Menu
def main():
    while True:
        print("📖 Book Manager")
        print("1. List books")
        print("2. Add book")
        print("3. Update book")
        print("4. Delete book")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.\n")

if __name__ == "__main__":
    main()

#4
import requests
import random

API_KEY = "your_api_key_here"

def get_movies_by_genre(genre):
    # OMDb API doesn't support direct genre search, so we'll do a workaround:
    # We'll search popular keywords and filter results by genre.
    # Note: OMDb free API is limited. For a robust app, you'd need a paid plan or a different API.
    
    search_terms = ['love', 'war', 'life', 'death', 'dark', 'light', 'hero', 'magic', 'crime', 'space']
    movies = []

    for term in search_terms:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={term}&type=movie"
        response = requests.get(url)
        data = response.json()

        if data.get('Response') == 'True':
            for movie in data['Search']:
                movie_id = movie['imdbID']
                movie_detail_url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={movie_id}&plot=short"
                detail_resp = requests.get(movie_detail_url)
                detail_data = detail_resp.json()

                if detail_data.get('Response') == 'True' and genre.lower() in detail_data.get('Genre', '').lower():
                    movies.append({
                        'Title': detail_data['Title'],
                        'Year': detail_data['Year'],
                        'Genre': detail_data['Genre'],
                        'Plot': detail_data['Plot']
                    })
        if len(movies) >= 10:  # limit the number to avoid too many requests
            break

    return movies

def recommend_movie():
    genre = input("🎬 Enter a movie genre (e.g. Action, Comedy, Drama): ").strip()
    print(f"\n🔍 Searching for movies in genre: {genre} ...")

    movies = get_movies_by_genre(genre)

    if not movies:
        print("❌ Sorry, no movies found for that genre.")
        return

    movie = random.choice(movies)
    print("\n🎉 Movie Recommendation:")
    print(f"Title: {movie['Title']}")
    print(f"Year: {movie['Year']}")
    print(f"Genre: {movie['Genre']}")
    print(f"Plot: {movie['Plot']}")

if __name__ == "__main__":
    recommend_movie()



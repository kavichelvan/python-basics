import json

# 1. API response(JSON) to python code (Dict)
json_string = '{"movies": ["Inception", "The Matrix", "Interstellar"], "total_movies": 3}'

print()
# Convert JSON string to a Python dictionary 
movie_data_dict = json.loads(json_string)

# Now you can access the data easily
print(movie_data_dict["movies"])  # Output: ['Inception', 'The Matrix', 'Interstellar']
print(movie_data_dict["total_movies"])  # Output: 3

print("Movie_Data Dictionary= ", movie_data_dict["total_movies"]);
print("JSON string= ", json_string.total_movies);

# 2. Python code (Dict) to API response (JSON)
import json

# Your Python dictionary with movie data
my_movie_data_dict = {
    "movies": ["The Dark Knight", "Avengers: Endgame", "Parasite"],
    "total_movies": 3
}

# Convert Python dictionary to JSON string
json_string = json.dumps(my_movie_data_dict)

# Now you can send this JSON string to your friend
print(json_string)
# Output: '{"movies": ["The Dark Knight", "Avengers: Endgame", "Parasite"], "total_movies": 3}'



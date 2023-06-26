# Compulsory Task 2
# Let us build a system that will tell you what to watch next based on the word
# vector similarity of the description of movies.
# ● Create a file called watch_next.py
# ● Read in the movies.txt file. Each separate line is a description of a different
# movie.
# ● Your task is to create a function to return which movies a user would watch
# next if they have watched Planet Hulk with the description “Will he save
# their world or destroy it? When the Hulk becomes too dangerous for the
# Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
# planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
# planet Sakaar where he is sold into slavery and trained as a gladiator.”


import spacy


# Return a Language callable object which is assigned to a variable called nlp
nlp = spacy.load('en_core_web_md')


def watch_next(description): 
    # Reading the movies.txt file
    movies = open("movies.txt", "r")

    # Creating and initialising a list to hold  the movies file split into separate titles and descriptions.
    movies_list = []

    # Store the separate titles and descriptions
    for i in movies:
        movies_list.append(i.split(":"))

    # Creating and initialising a list to store the similarity scores
    similarity_score = []

    # Creating a variable to help iterating through movies_list for better readability
    count = len(movies_list)

    
    model = nlp(description)

    #iterating through the text and appending the scores to the similarity_score list
    for i in range(0, count):
        similarity_score.append(nlp(movies_list[i][1]).similarity(model))

    # Obtaining the maximum score from the list
    max_score = max(similarity_score)

    # Obtaining the maximum score index
    max_index = similarity_score.index(max_score)

    # Returning the movie name with the maximum score - most similar with the description given
    return movies_list[max_index][0]

description_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk 
                    into a shuttle and launch him into space to aplanet where the Hulk can live in peace. Unfortunately, Hulk lands on the
                    planet Sakaar where he is sold into slavery and trained as a gladiator."""        
   
print("Recommended Movie: " + watch_next(description_hulk))

  




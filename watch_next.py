import spacy 
nlp = spacy.load('en_core_web_md')

synopsis_list = []
def recomendation(test_synopsis):
    '''Recomendation takes a movies synopsis and compares it against 
    othe movies stored in a catalogue. synopsies are compared using 
    vector based NLP in order to find similarties in text and context
    The most appropriate recomendation is then printed in the console.
    '''
    movies_form = None
    # initiate a while loop to house the try function
    while movies_form == None:
        try:
            # if file exist then read the file
            with open('movies.txt','r') as movies_form:
            # for lines in the movies file create a list and 
            # of the movies synopsis.
                for lines in movies_form:
                    lines = lines.strip().split(':')
                    synopsis_list.append(
                        lines[1])
                #preset default variables to hold the nlp processing result
                # and the index of the highest result
                similarity_result = 0.0
                recomended_index  = 0
                # iterate through the items in the list updating the variables
                # if needed ensuring that the highest value is saved.
                for index, items in enumerate(synopsis_list):
                    items = nlp(items)
                    #print(items.similarity(nlp(test_synopsis)))
                    #print(f"--{similarity_result}")
                    if (items.similarity(nlp(test_synopsis))) > similarity_result:
                        similarity_result = (items.similarity(nlp(test_synopsis)))
                        recomended_index = index
                #print(recomended_index)
                # read though the file again and extract the movie 
                # corelating to the saved index.
                with open('movies.txt','r') as file:
                    lines = file.readlines()
            # retrun the movie title and the synopsis.
            return print(lines[recomended_index])
                        
            # if the file does not exist raise and error and inform the user
        except FileNotFoundError as error:
            print(
                'The Movie file was not found,'
                +' Please double check the folder')
            print(error, end= '\n')
        # if the file name has a value then it must 
        # always be closed after use.
        finally:
            if movies_form is not None:
                movies_form.close()


# example test synopsis.

planet_hulk = '''Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati
trick Hulk into a shuttle and launch him into space to a planet 
where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''
print(f"\nSynopsis for comparison: \n {planet_hulk}\n")
print("Movie Recommendation:\n")
recomendation(planet_hulk)
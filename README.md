Authors : Arnaud Martin & Damien Marchat

# imdb_clean_api
Clean code applided to api development

# What have we done ?

We have decided to use the imbd API to get the reviews of whatever film the user would want to check out.
To use our code you can launch the main.py with the following command :

python3 main.py

The first window will pop up, you can type any name of movie and the api will give us back the most
likely movies you were looking for. Then you can chose more precisely wich one you wanted.
there is 2 cases next, either the movie you chosed do not have any comments and it will be notified.
Or the movie has comments and you will be able to check out it's comments. 


# What kind of clean code practice did we try to use ?

We tried to have variable and function names that were clear on what was the purpose
of each entity. We also tried to have short functions to keep the clarity to the max.
we also introduced testing in our 2 classes "imbd_api" and "api".

# Movie Trailer Website Generator
This website generator enables the user to generate a quick, nicely formatted website that features information about their favorite movies.

### Important steps before using
For this Website Generator to work, the user **must register for API keys** from youtube(a google api) and The Movie Database. **These api keys must be saved as environmental variables** with the titles:
```
YOUTUBE_API
```
and
```
TMDB_API
```

##### Here are the links to obtain these API's:
[Google API for Youtube](https://developers.google.com/youtube/v3/getting-started)  
[The Movie Database API](https://www.themoviedb.org/documentation/api)  

##### And here are links explaining how to set an environmental variable.  
 
[Environmental Variables for Mac](https://stackoverflow.com/questions/22502759/mac-os-x-10-9-setting-permanent-environment-variables)  
[Environmental Variables for Windows](http://www.dowdandassociates.com/blog/content/howto-set-an-environment-variable-in-windows-command-line-and-registry/)

## How to use:
Download the three python files, `entertainment_center.py`, `media.py`, and `fresh_tomatoes.py`.  

  Open `entertainment_center.py` in an editor and replace the movie variables and titles with movies of your own choosing.  

 _Make sure to input your own variables in the 'movies' list._   

Now run `entertainment_center.py` and be enthralled and overwhelmed with joy as a movie trailer generator springs to life within your browser. 

### Improvements over basic Udacity Project
In the media.py file, there are now api calls included to youtube and The Movie Database. These will automatically generate the following for a movie title:  

- A poster  
- A plot summary  
- A link to a trailer on youtube  

**Why did I make these changes?** _It makes the process of inputting new movies much quicker for the end user._

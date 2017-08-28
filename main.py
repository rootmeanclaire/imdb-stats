from selenium import webdriver
from movie import *

browser = webdriver.PhantomJS()

movies = []

f = open("movies.txt", "r")

print("Loading movies...")
for line in f:
	line = line[:-1]
	print("\tLoading \"{0}\"...".format(line), end="")
	movies.append(movie_by_name(browser, line))
	print("Done!")
print("Done!")

print("IMDB id\t10*\t1*")
for movie in movies:
	print("{0}\t{1}\t{2}".format(movie.imdb_id, movie.get_n_star(browser, 10), movie.get_n_star(browser, 1)))

browser.quit()

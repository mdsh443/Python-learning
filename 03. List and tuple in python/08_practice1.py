# Q.1: Write a program to ask the user to enter names of their 3 favorite movies 
# & store them in a list:
movie1 = input("Enter movie1: ")
movie2 = input("Enter movie2: ")
movie3 = input("Enter movie3: ") 
movie_list = [movie1, movie2, movie3]
print(movie_list)
# print(f"3 favorite movie list: {[movie1, movie2, movie3]}")

# Q.1.1: write a program to ask the user for a fourth movie and add it to the list.
movie1 = input("Enter movie1: ")
movie2 = input("Enter movie2: ")
movie3 = input("Enter movie3: ") 
# movie4 = input("Enter movie4: ")
movie_list = [movie1, movie2, movie3]
# movie_list.append(movie4)
movie_list.append(input("Enter movie4: "))
print(movie_list)

#Q.1.2: remove the second movie using .pop(), then print the updated list:
movie1 = input("Enter movie1: ")
movie2 = input("Enter movie2: ")
movie3 = input("Enter movie3: ") 
movie_list = [movie1, movie2, movie3]
movie_list.pop(1)
print(movie_list)

# Q.1.3: .pop() also returns the removed item.
# store it in a variable named removed_movie, then print:
movie1 = input("Enter movie1: ")
movie2 = input("Enter movie2: ")
movie3 = input("Enter movie3: ") 
movie_list = [movie1, movie2, movie3]
removed_movie = movie_list.pop(1)
print(f"Removed movie: {removed_movie}")
print(f"Remaining movies: {movie_list}")


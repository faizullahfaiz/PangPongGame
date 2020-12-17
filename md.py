"""
- Enter " a " to add a Movie, "l" to list a movie, "f" to find a movie and "q" to quite:

- Add  Movies
- See Movies
- Find a movie
- Stop running the Program

Tasks:
[]: Decide wher to store a movie
[]: What is the farmat of movie?
1[]: Show the user the main interface and get thier input 
2[]: Allow the uesr to add movies 
3[]: Show all thier movies
4[]: Find movies
5[]: Stop running the program when they type "q"

"""

def menu():
    user_input = input(("Enter 'a' to add a Movie, ' l' to list a movie, 'f' to find a movie and 'q' to quite: "))
    
    while user_input != 'q': 

        if user_input == 'a':
            add_movie()
        elif user_input == "l":
            show_movies()
        elif user_input == "f":
            find_movie()
        else:
            print("Unknowen Command Please try again.")
        user_input = input(("Enter 'a' to add a Movie, ' l' to list a movie, 'f' to find a movie and 'q' to quite: "))
menu()
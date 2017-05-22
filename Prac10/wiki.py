import wikipedia
search = "a"
while search != "":
    search = input("Enter search title or phrase: ")
    try:
        title = wikipedia.summary(search)
        print(title)
        page = wikipedia.page(search)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as error:
        print("The page is a disambiguation, choose any of the options")
        print(error.options)
    except wikipedia.exceptions.PageError:
        print('"{}" does not match any pages. Try another query!')
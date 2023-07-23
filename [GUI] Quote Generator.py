import requests
import random
import tkinter as tk

api_url = 'https://api.api-ninjas.com/v1/quotes?category='
api_key = 'KEY'

categories = [
    'age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'business',
    'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams',
    'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness',
    'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation',
    'great', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence',
    'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom',
    'money', 'morning', 'movies', 'success'
]

def fetch_random_quote(category):
    if category == "Random":
        category = random.choice(categories)
    
    url = api_url + category
    headers = {'X-Api-Key': api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        quotes = response.json()
        random_quote = random.choice(quotes)
        quote = random_quote['quote']
        author = random_quote['author']
        return quote, author
    
    return "Failed to fetch a quote.", ""

def generate_quote():
    category = category_var.get()
    quote, author = fetch_random_quote(category)
    quote_label.config(text=quote)
    author_label.config(text="- " + author)

window = tk.Tk()
window.title("Quote Generator")

category_label = tk.Label(window, text="Select a category:")
category_label.pack()

category_var = tk.StringVar(window)
category_var.set("Random") 
category_dropdown = tk.OptionMenu(window, category_var, *categories)
category_dropdown.pack()

generate_button = tk.Button(window, text="Generate Quote", command=generate_quote)
generate_button.pack()

quote_label = tk.Label(window, text="")
quote_label.pack()

author_label = tk.Label(window, text="")
author_label.pack()

window.mainloop()

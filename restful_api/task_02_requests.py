#!/usr/bin/python3
"""
Script pour récupérer et traiter les données d'une API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Récupère tous les posts de JSONPlaceholder et affiche les titres.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Récupère tous les posts et les sauvegarde dans un fichier CSV.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        posts_data = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        csv_filename = 'posts.csv'

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_data)

        print(f"Posts sauvegardés dans {csv_filename}")

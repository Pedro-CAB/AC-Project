# -*- coding: utf-8 -*-
import pandas as pd
import analysis

def analyze_missing_data(table):
    for column in table.columns:
        values = table[column].count()
        lines = table.shape[0]
        if (values != lines):
            print(f"Valores em Falta Encontrados na Coluna: {column}")
            print(f"Valores em Falta: {values}")
            print(f"Valores em Falta: {lines - values}")
            print(f"Número de Itens: {lines}")
            print("---")

awards_players = pd.read_csv('dataset/awards_players.csv')
coaches = pd.read_csv('dataset/coaches.csv')
players = pd.read_csv('dataset/players.csv')
players_teams = pd.read_csv('dataset/players_teams.csv')
series_post = pd.read_csv('dataset/series_post.csv')
teams = pd.read_csv('dataset/teams.csv')
teams_post  = pd.read_csv('dataset/teams_post.csv')

names = ["awards_players","coaches","players","players_teams","series_post","teams","teams_post"]
tables = [awards_players,coaches,players,players_teams,series_post,teams,teams_post]

analysis.analyze_all_missing_data(names,tables)
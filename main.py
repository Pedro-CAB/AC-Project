# -*- coding: utf-8 -*-
import pandas as pd
import analysis

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
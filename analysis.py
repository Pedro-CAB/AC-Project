# -*- coding: utf-8 -*-

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
            
def analyze_all_missing_data(names,tables):
    i = 0
    for table in tables:    
        print(f"Procurando Dados em Falta na Tabela {names[i]}...")
        analyze_missing_data(table)
        i += 1
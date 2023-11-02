import sqlite3
import os

def conectar():
    conn = sqlite3.connect('score.db')
    return conn

def desconectar(conn):
    conn.close()
    
def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS score_jogo (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor_score INTEGER NOT NULL
    )    
    """)    
    conn.commit()
    
def inserir_dado(nome, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO score_jogo (nome, valor_score)
        VALUES (?, ?)
    """, (nome, valor))  
    conn.commit()
    desconectar(conn)
    
def listar_dados():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM score_jogo
        ORDER BY valor_score DESC
    """)  
    dados = cursor.fetchall()
    conn.commit()
    desconectar(conn)
    return dados
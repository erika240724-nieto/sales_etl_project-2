import pandas as pd


def extract_data():
    ventas = pd.read_csv("data/input/ventas.csv")
    clientes = pd.read_csv("data/input/clientes.csv")
    productos = pd.read_csv("data/input/productos.csv")

    return ventas, clientes, productos
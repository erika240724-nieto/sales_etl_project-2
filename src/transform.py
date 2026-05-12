import sqlite3
import pandas as pd


def transform_data(ventas, clientes, productos):

    # =========================
    # LIMPIEZA TABLAS BASE
    # =========================

    clientes["pais"] = (
        clientes["pais"]
        .str.upper()
        .str.strip()
    )

    clientes["nombre"] = (
        clientes["nombre"]
        .str.title()
        .str.strip()
    )

    clientes["correo"] = clientes["correo"].fillna("no_email")

    productos["producto"] = (
        productos["producto"]
        .str.strip()
    )

    productos["categoria"] = (
        productos["categoria"]
        .str.upper()
        .str.strip()
    )

    ventas["cantidad"] = ventas["cantidad"].fillna(1)
    ventas["precio"] = ventas["precio"].fillna(0)

    # =========================
    # SQLITE EN MEMORIA
    # =========================

    conn = sqlite3.connect(":memory:")

    ventas.to_sql("ventas", conn, index=False, if_exists="replace")
    clientes.to_sql("clientes", conn, index=False, if_exists="replace")
    productos.to_sql("productos", conn, index=False, if_exists="replace")

    # =========================
    # QUERY SQL
    # =========================

    query = """
    SELECT
        v.id_venta,
        v.fecha,
        c.nombre,
        c.pais,
        c.correo,
        p.producto,
        p.categoria,
        v.cantidad,
        v.precio,
        (v.cantidad * v.precio) AS total_venta

    FROM ventas v

    LEFT JOIN clientes c
        ON v.id_cliente = c.id_cliente

    LEFT JOIN productos p
        ON v.id_producto = p.id_producto

    WHERE v.cantidad > 0
    """

    ventas_final = pd.read_sql_query(query, conn)

    # =========================
    # REPORTE POR PAÍS
    # =========================

    ventas_por_pais = (
        ventas_final
        .groupby("pais")["total_venta"]
        .sum()
        .reset_index()
    )

    conn.close()

    return ventas_final, ventas_por_pais
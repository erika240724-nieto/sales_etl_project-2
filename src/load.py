def load_data(ventas_final, ventas_por_pais):

    ventas_final.to_csv(
        "data/output/ventas_final.csv",
        index=False
    )

    ventas_por_pais.to_csv(
        "data/output/ventas_por_pais.csv",
        index=False
    )

    print("Archivos generados correctamente.")
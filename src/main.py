from extract import extract_data
from transform import transform_data
from load import load_data


def main():

    # EXTRACT
    ventas, clientes, productos = extract_data()

    # TRANSFORM
    ventas_final, ventas_por_pais = transform_data(
        ventas,
        clientes,
        productos
    )

    # LOAD
    load_data(
        ventas_final,
        ventas_por_pais
    )


if __name__ == "__main__":
    main()
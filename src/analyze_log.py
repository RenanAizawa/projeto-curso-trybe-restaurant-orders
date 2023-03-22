import csv


def orginaze_logs(logs):
    dias_da_semana = set()
    comidas = set()
    clientes = set()
    for log in logs:
        dias_da_semana.add(log[2])
        comidas.add(log[1])
        clientes.add(log[0])
    return {
        "dias_da_semana": dias_da_semana,
        "comidas": comidas,
        "clientes": clientes
    }


def primeira(data, logs):
    favorito = {}
    for comida in data["comidas"]:
        if comida not in favorito:
            favorito[comida] = 0
    for log in logs:
        if log[0] == "maria":
            favorito[log[1]] += 1
    return favorito


def segundo(logs):
    pedido = 0
    for log in logs:
        if (log[0] == "arnaldo") and (
            log[1] == "hamburguer"):
            pedido += 1
    return pedido


def terceiro(data, logs):
    pratos = data["comidas"]
    joao_take = set()
    for log in logs:
        if log[0] == "joao":
            joao_take.add(log[1])
    return pratos.difference(joao_take)


def quarto(data, logs):
    pratos = data["dias_da_semana"]
    joao_take = set()
    for log in logs:
        if log[0] == "joao":
            joao_take.add(log[2])
    return pratos.difference(joao_take)


def escrita_no_arquivo(path, lista):
    with open(path, 'w') as file:
        for n in lista:
            file.write(f"{n}\n")


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file) as file:
            logs = list(csv.reader(file))
            data = orginaze_logs(logs)
            d1 = primeira(data, logs)
            d2 = str(segundo(logs))
            d3 = str(terceiro(data, logs))
            d4 = str(quarto(data, logs))
            resposta = [max(d1, key=d1.get), d2, d3, d4]
            escrita_no_arquivo("data/mkt_campaign.txt", resposta)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

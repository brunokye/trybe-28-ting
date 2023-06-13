import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith('txt'):
            return print('Formato inválido', file=sys.stderr)

        with open(path_file, mode='r') as txt_file:
            return txt_file.read().splitlines()

    except FileNotFoundError:
        return print(f'Arquivo {path_file} não encontrado', file=sys.stderr)

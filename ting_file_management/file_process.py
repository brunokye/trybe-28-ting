import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        search = instance.search(index)
        if search['nome_do_arquivo'] == path_file:
            return

    lines = txt_importer(path_file)

    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines
    }

    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    size = len(instance)

    if size == 0:
        return print('Não há elementos', file=sys.stdout)

    path_file = instance.search(size - 1)
    file_name = path_file['nome_do_arquivo']
    instance.dequeue()

    print(f'Arquivo {file_name} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    try:
        path_file = instance.search(position)
        print(path_file, file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)

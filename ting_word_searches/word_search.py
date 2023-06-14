def exists_word(word, instance):
    result = []

    for index in range(len(instance)):
        path_file = instance.search(index)
        occurrences = []

        with open(path_file['nome_do_arquivo'], 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if word in line.lower():
                    occurrences.append({'linha': line_number})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": path_file['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = list()
    data = instance.queue
    for i in data:
        word_occurrences = list()
        for index, line in enumerate(i["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                word_occurrences.append({"linha": index + 1})
        if len(word_occurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": i["nome_do_arquivo"],
                "ocorrencias": word_occurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

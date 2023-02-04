import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    data = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    if new_dict not in instance.queue:
        instance.enqueue(new_dict)
        sys.stdout.write(f'{new_dict}')


def remove(instance: Queue):
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        removed_element = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(
            f"Arquivo {removed_element} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

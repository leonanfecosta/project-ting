import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Testar enfileiramento
    pq = PriorityQueue()
    pq.priority_limit = 2
    pq.enqueue({"qtd_linhas": 1})
    pq.enqueue({"qtd_linhas": 3})
    pq.enqueue({"qtd_linhas": 0})
    assert len(pq.high_priority) == 2
    assert len(pq.regular_priority) == 1

    # Testar desenfileiramento
    assert pq.dequeue() == {"qtd_linhas": 1}
    assert pq.dequeue() == {"qtd_linhas": 0}
    assert pq.dequeue() == {"qtd_linhas": 3}

    # Testar busca
    pq = PriorityQueue()
    pq.priority_limit = 2
    pq.enqueue({"qtd_linhas": 1})
    pq.enqueue({"qtd_linhas": 3})
    pq.enqueue({"qtd_linhas": 0})
    assert pq.search(0) == {"qtd_linhas": 1}
    assert pq.search(1) == {"qtd_linhas": 0}
    assert pq.search(2) == {"qtd_linhas": 3}
    with pytest.raises(IndexError):
        pq.search(3)

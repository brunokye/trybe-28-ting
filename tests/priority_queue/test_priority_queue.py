import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    def data(n):
        return {
            'nome_do_arquivo': 'test_file',
            'qtd_linhas': n,
            'linhas_do_arquivo': 'test_lines'
        }

    test_queue = PriorityQueue()

    test_queue.enqueue(data(12))
    test_queue.enqueue(data(1))
    test_queue.enqueue(data(2))
    test_queue.enqueue(data(3))

    assert test_queue.dequeue() == data(1)

    assert test_queue.search(0) == data(2)

    with pytest.raises(IndexError):
        test_queue.search(4)

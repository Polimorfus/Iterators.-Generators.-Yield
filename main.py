class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list =list_of_list



    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.list_of_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element

def flat_generator_enhanced(multi_list):
    for elem in multi_list:
        if isinstance(elem, list):
            for sub_elem in flat_generator_enhanced(elem):
                yield sub_elem
        else:
            yield elem

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    test_1()
    print('*' * 20)
    for item in FlatIterator(list_of_lists_1):
        print(item)
    print('*' * 20)

    print('_' * 20)
    for item in flat_generator_enhanced(list_of_lists_1):
        print(item)
    print('_' * 20)

    print('+' * 20)
    flat_list = [item for item in FlatIterator(list_of_lists_1)]
    print(flat_list)
    print('+' * 20)


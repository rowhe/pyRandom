class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def insert(self, data):
        """Создаем новую ноду в начале связанного списка
        Зто имеет сложность О(1) посколько мы просто меняем
        текущий head связанного списка, но не индексы"""
        # Создаем новую ноду для хранения данных
        new_node = Node(data)
        # Устанавливаем next новой ноды на текущий head
        new_node.set_next(self.head)
        # Устанавливаем head связанного списка на новый head
        self.head = new_node
        # Добавляем 1 к count
        self.count += 1

    def find(self, val):
        """Поиск элемента в связанном списае в данными = val
        сложность поиска = О(n) в худшем варианте итерируемся
        через весь список"""
        # Начинаем с первого элемента
        item = self.head
        # Итерируемся через следующие ноды
        # В случае если item = None заканчиваем поиск
        while item != None:
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.get_next()

        if current in None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.get_next
            self.count -= 1
        else:
            previous.set_next(current.get_next())
            self.count -= 1

    def get_count(self):
        return self.count

    def is_empty(self):
        return self.head == None


a = LinkedList()
a.insert(0)
a.insert(1)
a.insert(2)
a.get_count()
a.is_empty()
a.find(1)

# Домашнее задание №3

## Реализовать очередь с максимальным приоритетом (max heap) без использования heapq
Нужно реализовать класс MaxHeap
```python
class MaxHeap:
    def __init__(self) -> None:
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def heapify(self, iterable: List[int]) -> None:
        pass
```

## Реализовать LRU cache (least recently used); Для кого это просто, тогда LFU cache;

Класс должен содержать следующие методы
```python
class ICache:
    def __init__(self, capacity: int=10) -> None:
        pass

    def get(self, key: str) -> str:
        pass

    def set(self, key: str, value: str) -> None:
        pass

    def del(self, key: str) -> None:
        pass
```
Проверяться работоспособность должна так:
```python
from cache import LRUCache

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.get('Jesse') # вернёт 'James'
cache.del('Walter')
cache.get('Walter') # вернёт ''
```
Никто не осудит, если реализуете только LRUCache.

## Написать класс для нахождения медианы в потоке данных;
Медиана это среднее значение с отсортированном списке целых чисел. Если размер чётный, то тогда нет медианы и тогда медианой будет среднее значение двух средних значений.
[2,3,4], медиана 3

[2,3], медиана (2 + 3) / 2 = 2.5
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass

# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

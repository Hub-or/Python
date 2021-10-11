class DynamicArray(object):
    """动态数组实现"""
    def __init__(self, capacity=4):
        """
        构造函数
        :param capacity: 数组最大容量，不指定默认为4
        """
        self._capacity = capacity
        self._size = 0  # 数组有效元素数目，初始值为0
        self._items = [None] * self._capacity  # 占用一段连续内存空间的数组，None作为无效元素标识

    def __getitem__(self, item):
        """使arr类支持索引操作"""
        return self._items[item]

    def __setitem__(self, key, value):
        """使用用索引替换存在元素的值"""
        if key < 0 or key > self._size - 1:  # 若下标所指元素不存在
            raise Exception('{}[{}]does not exists.'.format(str(self), key))
        self._items[key] = value

    def __len__(self):
        """返回数组有效元素的个数"""
        return self._size

    def __iter__(self):
        """使数组可迭代"""
        for item in self._items:
            yield item

    def clear(self, value=None):
        """
        统一数组中每个元素的值
        :param value: 不传入参数默认将数组元素清空
        """
        if value is None:
            self._size = 0

        for i in range(self._capacity):  # 参数不为空时统一元素值
            self._items[i] = value
        self._size = self._capacity  # 数组大小变为容量大小

        self._is_full()  # 容量大小检查

    def get_capacity(self):
        """返回数组当前最大容量"""
        return self._capacity

    def is_empty(self):
        """判断数组当前是否为空"""
        return self._size == 0

    def append(self, value, index=None):
        """
        向数组中添加一个元素并保持数组逻辑不变
        :param index: 添加的元素所在的索引，默认添加到最后 *默认参数必须指向不变对象*
        :param value: 要添加的元素值
        """
        if index is None:  # 若未传入下标位置
            self._insert(self._size, value)  # 将元素添加到数组最后
            self._is_full()  # 容量大小检查
        elif index < 0 or index > self._size:  # 若插入位置无效
            raise Exception('Add failed. 0 <= index <= self._size required.')
        else:  # 若插入位置有效
            self._move(index)
            self._insert(index, value)
            self._is_full()  # 容量大小检查

    # private
    def _move(self, index):
        """移动插入位置后元素的位置"""
        for i in range(self._size - 1, index - 1, -1):  # 从尾部开始挪动元素，到插入位置为止，步长为负数时区间是左开右闭的
            self._items[i + 1] = self._items[i]

    def _is_full(self):
        """数组满时扩容为当前容量的两倍"""
        if self._size == self._capacity:  # 如果数组满了
            self._resize(self._capacity * 2)  # 扩容为当前容量的两倍

    def _insert(self, index, value):
        """
        向数组中插入一个元素
        :param index: 插入位置
        :param value: 插入元素的值
        """
        self._items[index] = value  # 将索引位置赋值为value
        if value is not None:  # 若赋值不为空
            self._size += 1  # 数组有效元素+1

    def _resize(self, new_capacity):
        """
        私有成员函数，使数组容量缩放至new_capacity
        :param new_capacity: 新的容量
        """
        new_arr = DynamicArray(new_capacity)  # 建立容量为new_capacity的新数组

        for item in self._items:
            new_arr.append(item)  # 将当前数组的元素全部复制到新数组中

        # 使数组内需要变更的指针指向新数组
        self._capacity = new_arr._capacity
        self._items = new_arr._items


def test_array():
    size = 2
    array = DynamicArray(size)
    # assert array.get_capacity() == 2

    array.append(0)
    array[0] = 1
    # assert array[0] == 1
    # assert len(array) == 1
    # assert array.get_capacity() == 2

    array.clear(1)
    assert array[0] == 1
    assert len(array) == 2
    assert array.get_capacity() == 4
    # for i in array:
    #     print(i)

    # array.append(5)
    # assert array[1] == 5
    # assert len(array) == 2
    # assert array.get_capacity() == 4

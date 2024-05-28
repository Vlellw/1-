def insertion_sort(arr):
	for i in range(1, len(arr)):
		j = i-1
		while j >= 0 and arr[i] < arr[j]:
			arr[j+1], arr[j] = arr[j], arr[j+1]
			j -= 1
			i -= 1
	return arr


def selection_sort(lst):
	n = len(lst)
	i = 0
	while i < n - 1:
		smallest = i
		j = i + 1
		while j < n:
			if lst[j] < lst[smallest]:
				smallest = j  # находим наименьшее число
			j += 1
		lst[i], lst[smallest] = lst[smallest], lst[i]  # меняем местами, наименьшее "вначало"
		i += 1
	return lst


def bubble_sort(a):
	N = len(a)
	for i in range(N - 1):
		for j in range(N - 1 - i):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
	return a


def merge_sort(alist, start, end):
	if end - start > 1:
		mid = (start + end) // 2
		merge_sort(alist, start, mid)
		merge_sort(alist, mid, end)
		merge_list(alist, start, mid, end)
	return alist
def merge_list(alist, start, mid, end):
	left = alist[start:mid]
	right = alist[mid:end]
	k = start
	i = 0
	j = 0
	while (start + i < mid and mid + j < end):
		if (left[i] <= right[j]):
			alist[k] = left[i]
			i = i + 1
		else:
			alist[k] = right[j]
			j = j + 1
		k = k + 1
	if start + i < mid:
		while k < end:
			alist[k] = left[i]
			i = i + 1
			k = k + 1
	else:
		while k < end:
			alist[k] = right[j]
			j = j + 1
			k = k + 1


def quicksort(alist, start, end):
	if end - start > 1:
		p = partition(alist, start, end)
		quicksort(alist, start, p)
		quicksort(alist, p + 1, end)
	return alist
def partition(alist, start, end):
	pivot = alist[start]
	i = start + 1
	j = end - 1

	while True:
		while (i <= j and alist[i] <= pivot):
			i = i + 1
		while (i <= j and alist[j] >= pivot):
			j = j - 1

		if i <= j:
			alist[i], alist[j] = alist[j], alist[i]
		else:
			alist[start], alist[j] = alist[j], alist[start]
			return j


w1 = [1, 57, 5, 17, 7, 3, 9, 8, 10, 10]

mer_sort = merge_sort(w1, 0, len(w1))

qui_sort = quicksort(w1, 0, len(w1))

bub_sort = bubble_sort(w1)

sel_sort = selection_sort(w1)

ins_sort = insertion_sort(w1)





class Stack:

    def __init__(self):
        self.stack = []
        self.max = None

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            for value in self.stack:
                if value > self.max:
                    self.max = value
        return removed

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item

    def get_max(self):
        return self.max


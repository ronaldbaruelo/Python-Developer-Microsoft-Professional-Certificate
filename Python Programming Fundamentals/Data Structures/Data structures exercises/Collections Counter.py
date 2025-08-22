from collections import deque, Counter

# Deque example
queue = deque()
queue.append("task1")
queue.append("task2")
print(queue.popleft())  # Output: task1

# Counter example
text = "This is a sample text with some repeated words words"
word_counts = Counter(text.split())
print(word_counts)  # Output: Counter({'words': 2, 'This': 1, 'is': 1, ...})
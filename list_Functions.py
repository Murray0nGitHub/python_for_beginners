#You are working on a queue management program.
#The queue is represented by a list.
#Write a program to take an input, add it to the end of the queue, and output the resulting list.
#The append() method can be used to add new items to the list.

queue = ['John', 'Amy', 'Bob', 'Adam']
input = input()
queue.append(input)
print(queue)
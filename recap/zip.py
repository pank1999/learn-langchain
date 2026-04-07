questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
    

# zip() creates an iterator that aggregates elements from each of the iterables.
# It returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted.    
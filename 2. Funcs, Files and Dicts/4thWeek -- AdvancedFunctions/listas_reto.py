def beginning(lst):
    i = 0
    sublist=[]
    while i < len(lst):
        if lst[i] == 'bye':
            break
        else:
            sublist.append(lst[i])
            i+=1
    
    if len(sublist) < 10:
        ret_lst = sublist
    else:
        ret_lst = sublist[:10]
     
   
    return ret_lst

lst1 = ['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']

print(beginning(lst1))
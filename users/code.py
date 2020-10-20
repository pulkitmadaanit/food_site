# 1.l1=['John','Ram','Sham','John','John','Ram','Rahul'] find the most occuring name and how many times it occurs

l1=['John','Ram','Sham','John','John','Ram','Rahul']



def most_frequent(l1): 
	return max(set(l1), key = l1.count) 

List = [2, 1, 2, 2, 1, 3] 
print(most_frequent(l1)) 
print(key)

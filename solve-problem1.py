def compressed_vector(arr):
    new_arr = []
	i = 1
	leng = 1
	while i < len(arr):
		if arr[i] == arr[i - 1]:
			leng = leng + 1
			i = i + 1
		else:
			new_arr.append((arr[i - 1], leng))
			leng = 1
			i = i + 1
	new_arr.append((arr[i - 1], leng))
	return new_arr
    
        
    

def filter_short_strings(input_array):
    
    length = len(input_array)
    
    result_array = [""] * length
    
    j = 0
    
    for i in range(length):
       
        if len(input_array[i]) <= 3:
            
            result_array[j] = input_array[i]
            j += 1
    
   
    return result_array[:j]

input_array = ["Hello", "2", "world", ":-)"]
output_array = filter_short_strings(input_array)

print("Исходный массив:", input_array)
print("Массив строк длиной <= 3 символа:", output_array)




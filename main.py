with open('/home/jan/Desktop/File/workspace/github.com/59man/bookbot/books/frankestein.txt') as f:
    
    file_contens = f.read()
    v1 = file_contens.split()
    v2 = len(v1)
    #print(v2)
    char_list = list(file_contens.lower())
    unique_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','y','x','z','v' ] 
    #Output = open('/home/jan/Desktop/File/workspace/github.com/59man/bookbot/books/frankestein.txt')
    values_dict = {}
    for i in unique_char:
        values_dict[i] = char_list.count(i)
    values_dict_sorted = dict(sorted(values_dict.items(), key=lambda item: item[1]))
  
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"words found {v2}")
    print('')
    for i in values_dict_sorted:
        print(f"the character {i} had {values_dict_sorted[i]} couits")
    print('')
    print('--- End report ---')   
        
        
    #print(f"the character {i} has {char_list.count(i)} occurences")


file_name = input('Enter the name of the file to open: ')

while True:
    try:
        with open(file_name, 'r') as file:
            word_count = {}
            raw_lines = file.readlines()
            lines = [x.strip() for x in raw_lines]

            for line in lines:
                words = line.split()

                for word in words:
                    if len(word) > 3:
                        count = line.count(word)
                        word_count[word] = word_count.get(word, 0) + 1
            
            #print(word_count)

            print(f"{'#':<10}{'Word':^10}{'Freq.':>10}")
            print('='*30)
            sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
            n = 1
            for key, value in sorted_word_count[:10]:
                print(f"{n:<10}{key:^10}{value:>10}")
                n += 1
            single = [
            break
        
    except FileNotFoundError:
        print('File not found. Please try again.')
        file_name = input('Enter the name of the file to open: ')
        

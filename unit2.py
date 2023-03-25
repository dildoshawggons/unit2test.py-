x = 0
with open('alice.txt') as program:
    for line in program:
        words = line.split()
        x += len(words)
print("There are" , x , 'words in alice')


with open('alice.txt') as file:
    total_words = 0
    num_lines = 0
    for line in file:
        words = line.split()
        total_words += len(words)
        num_lines += 1

    avg_words = total_words / num_lines
    print("The average number of words per line is:", avg_words)

count = 0
maxcount = 15
with open('alice.txt') as book:
    for line in book:
        count = len(line.split())
        if count > maxcount:
                    maxline = line
                    maxcount = count
                    print('The longest line has',maxcount,'words:',maxline)


word = input("Enter a word to look up: ")

with open("Alice.txt") as file:
    count = 0
    lines = []
    for line in file:
        if word in line:
            count += 1
            lines.append(line)
            if count == 10:
                break

    if count == 0:
        print('Not found')
    else:
        print()
        for line in lines:
            print(line.strip())

with open("alice.txt", "r") as file:
    number_of_lines = 0
    for line in file:
        if word in line:
            number_of_lines += 1
            if count == 0:
                break
                text = file.read()
                count = text.count(word)
                if count > 0:
                        print(f"{number_of_lines} lines contain {word}")


#with open("Alice.txt") as prompt:
    #text = prompt.read()
#count = text.count(word)
#if count > 0:
    #print(f"{count} lines contain {word}")












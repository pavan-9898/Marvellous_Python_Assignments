def main():

 with open('data.txt', 'r') as file:
    for line in file:
        word=line.split()
        # print(word)
        count=len(word)>=5
        print(count)

        


if __name__ =="__main__":
    main() 
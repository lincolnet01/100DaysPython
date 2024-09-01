# Program that generate a new story based on the words entered by the user

def main():

    with open('story1.txt', 'r') as f:
        story = f.read()

    print(story)

if __name__ == '__main__':
    main()
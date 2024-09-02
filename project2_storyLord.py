# Program that generate a new story based on the words entered by the user

def main():

    with open('story1.txt', 'r') as f:
        story = f.read()

    TARGET_START = '<'
    TARGET_END = '>'
    TARGET_WORD = -1

    words = set()
    answers = {}

    for i, char in enumerate(story):
        if char == TARGET_START:
            TARGET_WORD = i
        if char == TARGET_END and TARGET_WORD != -1:
            word = story[TARGET_WORD : i + 1]
            words.add(word)
            TARGET_WORD = -1
    
    for word in words:
        answer = input(word + ':')
        answers[word] = answer
    
    for word in words:
        story = story.replace(word, answers[word] )

    print()
    print("=====") 
    print()
    print(story)
    print()
    print('=====')


if __name__ == '__main__':
    main()
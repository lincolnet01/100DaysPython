import sys

def main() -> None:
    '''
    Main function to display the bitmap message based on user input 
    '''

    print('---------------------------')
    print('Bitmap message by Lincdel')
    print('---------------------------')
    
    bitmap = '''
...................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................

'''
    # Get the message from the user
    print('Enter a message to display:')
    message = input('> ')

    if not message:
        print('You did not provide any message. Exiting....')
        sys.exit()

    # Display the bitmap message 
    for line in bitmap.splitlines():
        for i, char in enumerate(line):
            if char == ' ':
                # Print a space for empty areas in the bitmap
                print(' ', end='')
            else:
                # Print a character from the message
                print(message[i % len(message)], end='') 
        print() # Move to the next line

if __name__ == '__main__':
    main()
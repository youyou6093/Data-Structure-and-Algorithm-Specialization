# python3
#done
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    Success=True
    for i, next in enumerate(text):
        #print(i,next)
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next,i+1))
            pass

        if next == ')' or next == ']' or next == '}':
            if opening_brackets_stack==[]:
                print(i+1)
                Success=False
                break
            else:
                if(opening_brackets_stack[-1].Match(next)):
                    #print("next")
                    opening_brackets_stack.pop()
                else:
                    #print(opening_brackets_stack[-1].position)
                    #print("fff")
                    print(i+1)
                    Success=False
                    break
            # Process closing bracket, write your code here
            pass

    if(Success==True):
        if (opening_brackets_stack==[]):
            print("Success")
        else:
            print(opening_brackets_stack[-1].position)
    # Printing answer, write your code here

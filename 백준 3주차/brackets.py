class ArrayStack :
    def __init__( self, capacity ):	    # 생성자 정의
        self.capacity = capacity		    # 용량(고정)
        self.array = [None]*self.capacity	# 요소들을 저장할 배열
        self.top = -1			            # 스택 상단의 인덱스

    
    def isEmpty( self ) : return self.top == -1
    def isFull( self ) : return self.top == self.capacity-1

    def push( self, item ):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass              

    def pop( self ):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass              

    def peek( self ):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass              

    def size( ) : return top+1


def checkBrackets(statement):
    stack = ArrayStack(100)		    
    for ch in statement:		    
        if ch in ('{', '[', '('):	
            stack.push(ch)		    
        elif ch in ('}', ']', ')'):	
            if stack.isEmpty() :	
                return False		
            else :
                left = stack.pop()	
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False	

    return stack.isEmpty()

user_input = input("문자열을 입력하세요: ")

if user_input.endswith('.'):
    user_input = user_input[:-1]
sentences = user_input.split('.')

result = []
for sentence in sentences:
    if sentence.strip():
        result = checkBrackets(sentence.strip())
        result. append("yes" if result else "no")
print("\n".join(result))

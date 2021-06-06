
b = [110,100]
a = [1,2,3]
b = a 
print(b)


string_1 = "hello"



def re(x: str) -> str:
     length = len(x) - 1 
     answer_1 = ""
     while length > 0:
         answer_1 += x[length]
         print(x[length])
         length -= 1
     return answer_1
     

answer = re(string_1)

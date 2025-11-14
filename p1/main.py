questions=[
  (5,3),
  (2,5),
  (8,3),
  (200,5),
  (-1,5),
  (16,3),
  (2,3)
  ]
  
  user_answers=[]
 
 
 for— _in range(len(questions)):
     user_answers.append int(input())
     
s=input()


count={}
for ch in s:
    if ch !="":
        count[ch]= char_count.get(char,0)+1
    
result()
for ch in s:
    if ch ==（""):
        result append(".")
    
    elif count[ch] ==1:
        result append(ch)
    
    else:
        result append(".")
        
output="". join(result)

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

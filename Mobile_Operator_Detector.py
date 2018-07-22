'''
Write a function which accepts number and return name of operator or string
"no info", if operator can't be defined.
number always looks like 8yyyxxxxxxx, where yyy corresponds to operator.
'''

def detect_operator(num):
    MTS=["066","050","095","099" ]#your code here
    Golden=["039"]
    Life=["063","093"]
    Kyivstar=["067","097","098"]
    Beeline=["068"]
    List=[MTS,Golden,Life,Kyivstar,Beeline]
    name=["MTS","Golden Telecom", "Life:)","Kyivstar","Beeline"]
    s=str(num)[1:4:1]
    k=0
    for i in range(len(List)):
        if s in List[i]:
            k=1
            return name[i]
    if k!=1:
        return "no info"

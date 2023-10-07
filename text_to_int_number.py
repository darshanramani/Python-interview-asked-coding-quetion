# inp='nine three two eight zero one zero zero one four'

inp='nine three two eight zero one triple zero four'

# d={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
d={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

# print(d)
li1= list(inp.split())

out=''
for i in range(len(li1)):
    # print(i)
    
    if li1[i]=='double':
        #  continue
        out=out+ d[li1[i+1]] 
        # print(i)
    elif li1[i]=='triple':
        out=out+d[li1[i+1]]+d[li1[i+1]]
        
    else:
        out=out+d[li1[i]]
        
print(out)
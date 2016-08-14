class Runner():
    "add student name to window title and configure additional turtle elements as per Asg01"
    
    def run(aTuple):
        aTuple[0].pensize(2)
        aTuple[0].color('red')
        aTuple[0].shape('turtle')
        
        aTuple[1].pensize(3)
        aTuple[1].color('green')
        aTuple[1].shape('circle')
        
        aTuple[2].pensize(4)
        aTuple[2].color('blue')
        aTuple[2].shape('triangle')
        
        aList = list(aTuple)
        aList.append('Mark Newman')
        
        return aList
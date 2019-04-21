    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys

# Function to return max sum such that  
# no two elements are adjacent 
def find_max_sum(arr, length): 

    prevfirst = prevsecond = res = i = 0     
    path = []
    dp =[]
    testarrfirst = []
    testarrsecond = []
    dp = [0]*(length+1)
    path = [0]*(length+1)
    dp[1] = arr[0]
    i = 2
    
    while i <= length:
        if (dp[i - 2] + arr[i - 1] > dp[i - 1]):
            path[i] = dp[i - 2] - arr[i - 1]
            dp[i] = dp[i - 2] + arr[i - 1]
        else: 
            #path[i] = dp[i - 1]
            dp[i] = dp[i - 1]
        i+=1
        
    i = length
    while i > 0:
        testarrfirst.append(dp[i]-dp[i-2])
        i-=2
    
    return max(dp)
    
        

#main function 
def main():

    #define list for number of heroes and villains     
    testcase = noofelem = i = 0        
    counter = 1 
    savnumber = []
    savoneorder = []
    savtwoorder = []
    finallist = []
    saveorder  = 0
    savenumber = 0
    algores = [] 
    listt = []
    cnt = summ = 0
    length = 0
    swapflag = True

    #read the input 
    for line in sys.stdin:
        if counter == 1:
            testcase = int(line)
        elif counter == 2: 
            noofelem = int(line)
        elif counter == 3:
            houseorder = [int(elem) for elem in line.split()]
            summ = find_max_sum(houseorder,noofelem)
            print(summ)
        counter +=1

        if counter > 3:
            counter = 2
            houseorder.clear()            
        
 # Write code here 

main()


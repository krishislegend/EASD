import sys

# Function to return max sum such that  
# no two elements are adjacent 
def find_max_sum(arr): 
    incl = arr[0]
    excl = 0
    max_ele = arr[0]
    
    excl_arr = []
    incl_arr = []
    if incl>=0:
        incl_arr.append(incl)
        
    for i in arr[1:]: 
        
        if max_ele < i:
            max_ele =  i
        
        # Current max excluding i
        new_excl = excl if excl>incl else incl 
        
        temp_excl = excl_arr[:]
        excl_arr = incl_arr[:] if incl > excl else excl_arr[:]
        if i>=0:
            temp_excl.append(i)
            incl_arr = temp_excl[:]
         
        # Current max including i 
        incl = excl + i 
        excl = new_excl
        
    excl_arr.reverse()
    incl_arr.reverse()
    
    if(max_ele <= 0):
        print(max_ele)
    elif excl>incl:
        return excl_arr
    elif excl == incl:    
        if excl_arr[0] > incl_arr[0]:
            return excl_arr
        else:
            return incl_arr
    else:
        return incl_arr     

#main function 
def main():

    #define list for number of heroes and villains     
    testcase = noofelem = i = 0        
    counter = 1 
    savnumber = []
    savoneorder = []
    sequence = []
    finallist = []
    saveorder  = 0
    savenumber = 0
    algores = [] 
    listt = []
    cnt = summ = 0
    length = 0
    swapflag = True
    test = []

    #read the input 
    for line in sys.stdin:
        if counter == 1:
            testcase = int(line)
        elif counter == 2: 
            noofelem = int(line)
        elif counter == 3:
            houseorder = [int(elem) for elem in line.split()]
            sequence = find_max_sum(houseorder)
            for x in range(len(sequence)):
                print(sequence[x], end='')
            print()    
        counter +=1

        if counter > 3:
            counter = 2
            houseorder.clear()            
        
 # Write code here 

main()

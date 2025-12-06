def solution(s):
    nums=["zero", "one", "two", "three","four","five","six","seven","eight","nine"]
    temp=["0","1","2","3","4","5","6","7","8","9"]
    arr=[]
    for i in range(len(nums)):
        index = s.find(nums[i])
        if(index != -1):
            s = s.replace(nums[i],temp[i])
            
    return int(s)
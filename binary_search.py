def bin_search(nums:list[int], target:int) -> int:
    l,r = 0,len(nums)
    while(l<r):
        m = (l+r)//2
        if nums[m]<target:
            l = m+1
        else:
            r=m
    return l


x = list(map(int, input("Enter the array - ").split()))
target = int(input("Enter the target value - "))
print(f"The min index of the {target} is {bin_search(x,target)}")
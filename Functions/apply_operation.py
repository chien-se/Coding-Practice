def app_ops(nums : list[int], ops : list[callable]) -> list[int] :
    res = []
    for i in nums:
        val = i # 2 
        for j in ops:
            val = j(val) #
        res.append(val)
    return  res

nums = [1, 2, 3]

def add1 (num) :
    return num+1 

def double(num2):
    return num2 * 2

ls = [add1, double]
result = app_ops(nums, ls )

for i in result:
    print(i)
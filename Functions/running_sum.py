def running_sum():
    total = 0 
    def add(num):
        nonlocal total
        total += num
        return total
    
    return add # return a function that can be use

f = running_sum()
f(3) # f become that function so f will be add(3) which will return back total and because local is a nonlocal variable 3 is added to total in running sum
f(2)
f(-2)
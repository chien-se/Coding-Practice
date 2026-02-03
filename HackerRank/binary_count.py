def bi_count (num) -> int :
    a = num.count(0)
    b= num.count(1)

    if a > b:
        return b

def swap_case(s):
    convertidor= s.swapcase()
    return convertidor

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
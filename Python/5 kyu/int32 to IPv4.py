# Take the following IPv4 address: 128.32.10.1
#
# This address has 4 octets where each octet is a single byte (or 8 bits).
#
# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001
#
# Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361
#
# Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address

def int32_to_ip(int32):
    binary = bin(int32)[2:]
    while len(binary) < 32:
        binary = '0' + binary
    start = 0
    end = 8
    ip_nums = []
    while end < 33:
        ip_nums.append(binary[start:end])
        end += 8
        start += 8
    for i in ip_nums:
        ip_nums[ip_nums.index(i)] = str(int(i, 2))
    return '.'.join(ip_nums)
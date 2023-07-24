def cetakHexa(n):
    hexa_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    result = ""

    while n > 0:
        remainder = n % 16
        if remainder >= 10:
            result = hexa_map[remainder] + result
        else:
            result = str(remainder) + result
        n = n // 16
    return result
print()
print()
print(cetakHexa(12))    # Output: C
print(cetakHexa(31))    # Output: 1F
print(cetakHexa(229))   # Output: E5
print(cetakHexa(255))   # Output: FF
print(cetakHexa(31519)) # Output: 7B1F
print()
print()
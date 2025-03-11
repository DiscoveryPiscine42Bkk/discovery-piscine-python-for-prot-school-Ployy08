def swap_case(text):
    """สลับตัวพิมพ์ใหญ่เป็นตัวพิมพ์เล็ก และตัวพิมพ์เล็กเป็นตัวพิมพ์ใหญ่ใน string"""
    result = ""
    for char in text:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

text = input("Enter a string: ")
swapped_text = swap_case(text)
print(swapped_text)
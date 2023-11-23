import re

text = "五十两，两个苹果，两边走"

pattern = r"两(?!位|边|个|次|套|日|句)"
matches = re.findall(pattern, text)
print(matches)

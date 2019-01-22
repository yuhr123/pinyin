from xpinyin import Pinyin
import re

sentence = ""
with open('content.html') as f:
    sentence = f.readline()

cuted = re.split("(，|。)", sentence)[:-1]
p = Pinyin()

with open('output.html', 'w') as f:
    f.write("<p>")

    for c in cuted:
        if not c == "，" and not c == "。":
            f.write("<ruby>")
            for w in c:
                if not w == "，" and not w == "。":
                    f.write(w + "<rt>" + p.get_pinyin(w, tone_marks="marks") + "</rt>")
            f.write("</ruby>")
    else:
        f.write(c)

    f.write("</p>")

# print("<p>")

# for c in cuted:
#     if not c == "，" and not c == "。":
#         print("<ruby>", end='')
#         for w in c:
#             if not w == "，" and not w == "。":
#                 print(w + "<rt>" + p.get_pinyin(w, tone_marks="marks") + "</rt>", end="")
#         print("</ruby>", end='')
#     else:
#         print(c, end='')

# print("\n</p>")
import csv
import re

template = ""
with open("./template.html") as t:
    template = t.read()

lis = ""
with open("./lyrics.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        title = row[0]
        fileName = "./lyrics/" + str.strip(row[1]) + ".html"
        lyrics = row[2]
        if(len(lyrics) == 0):
            lyrics = "歌詞が見つかりませんでした"

        lyrics = "\n".join(["            <p>" + x + "</p>" for x in lyrics.split("\\n")])

        template2 = template
        template2 = template2.replace("タイトルを挿入", title)
        template2 = template2.replace("歌詞を挿入", lyrics)
        with open(fileName, mode = "w") as f2:
            f2.write(template2)

        lis = lis + '\n            <li class="item"><a href="' + fileName + '">' + title + '</a></li>'

index = ""
with open("./index.html", mode="r") as f:
    index = f.read()

with open("./index.html", mode="w") as f:
    index = re.sub('(<ul class="contents">(.|\s)*?</ul>)', '<ul class="contents">' + lis + "\n        </ul>", index)
    f.write(index)
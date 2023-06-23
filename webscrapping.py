# Create a program, which downloads the content of wallpaperswide.com website, and then read the downloaded content,
# then from the downloaded content, you should extract the <img /> tags only from that content,
#
# then again loop over the extracted <img /> tags, and take out the src links, then print the src links one by one.

import os

os.system("wget 'wallpaperswide.com'")
c = os.listdir()

for i in c:
    if i != "webscrapping.py":

        with open (i,"r") as f:
            content = f.readlines()

            for i in content:
                line = i.strip()

                if line.startswith("<img"):
                    lin = line.split("//")
                    link = lin[1].split('"')
                    print(link[0])

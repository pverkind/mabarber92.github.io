# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:42:07 2021

@author: mathe
"""

import pypandoc
import re
import os
import sys
from datetime import date

# Getting main directory as script path

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

# Setting directories
docx_in = dname + "\docx_in"
image_out = dname + "/images/blogs/" + str(date.today()) + "/"
blog_dir = dname + "/_posts/"

# Adjust for new header!
header = "C:/Users/mathe/Documents/Kitab project/Gitpages/header_plain"

docx = re.compile(".*\.docx")


# Create string from docx formatted text except those in wrong format
def docx_conv(root, name, images_path):
        author = re.findall(r"(^.*?)\.", name)[0]
        extract_img = "--extract-media=" + images_path + author    
        path = os.path.abspath(os.path.join(root, name)) 
        blog = pypandoc.convert_file(path, 'md', extra_args =["--wrap=none", extract_img])
        return blog
    

# Add a correctly labelled header to the blog
def header_build (header, name, blog):
     with open(header, encoding = "utf-8") as f:
            head_in = f.read()
            f.close()
     author = re.findall(r"(^.*?)\.", name)[0]
     title = re.findall(r"@Title:(.*)@", blog)[0]     
     author_code = "author: " + author.lower()
     title_code = "title: \"" + title + "\""
     head_in = re.sub(r"title:", title_code, head_in)
     head_in = re.sub(r"author:", author_code, head_in)
     final = head_in + blog
     title_s = re.sub(r"[\s:/.,]", "-", title)[:40]
     
     return (final, title_s)





for root, dirs, files in os.walk(docx_in, topdown=False):
    for name in files:
        if docx.match(name):
            print(name + " ...success")
            blog = docx_conv(root,name, image_out)
            final, title_s = header_build(header, name, blog)
            
            # Cleaning out uncessary md and tags from the final piece
            final = re.sub(r"\!\[\]\((.*)/images", "![](/images", final)
            final = re.sub(r"{width=.*?}", "", final)
            final = re.sub(r"\\@Title:(.*)@", "", final)
            outpath = blog_dir + str(date.today()) + title_s + ".md"
            
            # Write out final blog to correct destination
            f = open(outpath, "w", encoding = "utf-8")
            f.write(final)
            f.close()  
          
        
        else:
            print("error!:\n" + name + " is not correctly formatted. \n Use docx.")
            continue
        

        


---
header:
  image: 
  caption: 
title: "The New OpenITI Metadata Search"			
author: peter_verkinderen		
layout:		single
categories:
  - 
  - 
tags:
  - 
---




The OpenITI corpus was designed in a way that makes it easy for scripts to access, identify and analyze the texts in the corpus. As a human reader, it was until now not easy to find a particular text you are interested in: all texts have a filename that starts with the death date of the author, followed by a short transliterated version of the author’s name and the book title (for more on OpenITI’s Unique Record Identifier (URI) system, see [here](https://alraqmiyyat.github.io/OpenITI/).



![Image](/images/old_posts/OpenITI_CTS_URI-1024x326.png)



The text files are stored in GitHub repositories (folders) that represent 25-year time spans of the hijri era. While this is very convenient for a script, if a human reader does not know the death date of an author, it may be very cumbersome to locate the file in the 60 repositories.



![Image](/images/old_posts/OpenITI_folder_system-1024x423.png)



**We now have a new way to search for files in the OpenITI corpus:**



[**https://kitab-corpus-metadata.azurewebsites.net/**](https://kitab-corpus-metadata.azurewebsites.net/)



![Image](/images/old_posts/Metadata_search_page-1024x495.png)



## **Searching and filtering**



You can search the metadata of the entire corpus for author and title, in Arabic and the simplified ASCII transliteration used in our URI system. You can also filter the metadata by tags, publishing houses, text collections, etc. by using the Search box in the top right of the screen. The metadata table can also be sorted by clicking on the arrows next to the column headers.



## **Annotation status and primary/secondary texts**



For many texts, the OpenITI corpus contains different digital versions, which we got from different sources. We are currently working hard on adding structural annotation (chapters, paragraphs, dictionary entries, etc.) to the best digital version of every text in the corpus; we call this the “primary version” (PRI).



The legend at the top of the page explains the symbols used for detailing the annotation status of the texts in the corpus:



![Image](/images/old_posts/annotation_status.png)



Clicking on one of the items in the legend will filter the metadata table, leaving only the texts with the selected annotation status visible.



With the ![Image](/images/old_posts/primary_books_button.png) button, you can also choose to display only the primary texts.



## **Notify us of issues with our texts!**



If you notice that there is a problem with a text’s URI, you can notify us by clicking the link at the bottom of each Author, Title and Version cells:



![Image](/images/old_posts/title_issue.png)



You can also notify us if you notice an issue with the quality of a specific text version (e.g., if it is incomplete) in the Version column.



![Image](/images/old_posts/version_issue-300x94.png)



Finally, you can also alert us when you think that another version of the text deserves to be the primary version:



![Image](/images/old_posts/primary_issue-300x80.png)



Clicking any of these links will bring you to a GitHub issue form (you’ll need a GitHub account – you can create one [here](http://www.github.com/)). Please follow the instructions in the form to complete it, and hit the “Submit new issue” button to send it off:



![Image](/images/old_posts/GithubIssueForm.png)



**Happy searching!**



 


































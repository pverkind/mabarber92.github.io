---
header:
  image: 
  caption: 
title: "Judging the Differences between Arabic Text Versions Mathematically"			
author: sarah_savant		
layout:		single
categories:
  - 
  - 
tags:
  - 
---



Researchers working on historical Arabic texts have long known about transmission practices that resulted in considerable differences between ostensibly the same works. Scholars transmitted to many students and sometimes over long time spans; works were transmitted differently in terms of wording, structure, and scope of contents. The afterlife of texts played a role too. Witness copies dispersed, over distances. Parts were extracted and rebound with other texts. The result is that today’s print editions often produce an ideal text that never, in fact, existed.



But just how much was the tradition in flux? Now that thousands of print editions have been converted into machine-readable format, we are beginning to have more of an idea as we can compare different versions mathematically and algorithmically (conversion to machine readable formats has also produced its own problems; more on this below).



A major task for the KITAB team is to work out just how much variation there is in titles. We have been doing this by comparing our text files to scanned versions of editions, and in some cases, physical books, and recording differences in our GitHub repository (Table 1).



![Image](/images/old_posts/Textqualitytable-300x166.png)  

**Table 1**: The KITAB annotation team records issues while annotating texts. This work informs which version is labeled as the “primary” version in our corpus. Our statistics on text-reuse corpus-wide rely on primary versions only.



This sort of close reading of texts will remain critical to understanding variations and to making corrections to machine-readable files to bring them in line with the print editions upon which they are based. But now, we have also added a method that relies on word counts and the text reuse algorithm passim to get another sense of how related our versions are, at scale.



## **The method: evaluating differences at scale**  

The method for detecting differences in versions, at scale, can work for both cleaning the data and, ultimately, the deeper analysis of transmission practices.



We start now with the cleaning. We have spent a lot of 2019 evaluating passim results, and have found the February 2019 run to be, so far, our best. We used the data from this run, which included all versions of texts. We extracted data to compare 3,215 textual versions. This represented 1,552 titles. We have texts in single versions and others in multiple versions; all were compared. We also have single versions of texts in our corpus that do not form part of this dataset.



Our first look at the data shows the following:



-   Comparing word counts across the centuries (specifically, years 1-911, Hijri), we find that the median length difference between versions is 1,559 words. That is shorter than this blog and can arise rather easily even for two nearly identical versions. The mean length difference is 78,683 words, which reflects a distorting effect of outlier cases. To give a sense of these outliers, the largest length difference was 2,799,758 words – a case where a title was applied to both a part of a work and the work itself.



The median is the more important number for reckoning the general state of the corpus, because it represents the middle value of the dataset (i.e., the case of any specific comparison at least half of the time). Still, the mean alerts us to the degree to which many titles do not represent the median.



-   Comparing words matched across the centuries: The median is 96.17%, for the wording in Version 1 aligning to that of Version 2, and 96.1% for the wording in Version 2 aligning to that of Version 1. The mean, feeling the downward pull of outliers, is 87.79% and 87.25%, respectively.



We can also consider this data on a per-century basis.



![Image](/images/old_posts/Rplot01-300x164.png)



**Image 1**: The boxplot graph above represents the degree of relationship between different versions across the centuries.



Image 1 provides century-level details on our words matched statistics. The yellow boxes represent how much 25-75% of pairs match (the interquartile range), with the black horizontal line representing the median for each century’s versions. The horizontal lines below and above each box represent the minimum and maximum values, respectively. The round circles, below the boxes, represent outlying cases. In 163 cases, the alignments equal or exceed 100% because of internal reuse within a text. This happens when one part of Version 1 matches to two parts of Version 2, or the reverse. The bars above the 100 percent mark reflect this situation. We are working to improve how we calculate words matched, and it is worth noting that we lose reuse at the boundaries where we chunk texts too.



Here, too, the median words matched numbers indicate rather precise alignments between versions.



## **The Outliers**  

Then there are the outliers.



![Image](/images/old_posts/Howfarapartversions-300x169.png)  

**Image 2**: The above graph was based on the same versioning data. The circled area in the visualisation above represents 2,061, or 64%, of the comparisons of versions. The other 36% of comparisons represent sharper – and sometimes very sharp – differences.



Each dot in the graph above represents a case where we have ostensibly two versions of the same work stored in GitHub.  

Consistent with Image 1, the greatest concentration of dots is toward the bottom at the far right of the x-axis. This circled area is the area where two versions differ little in word count, and also have at least 90% in common. In 2,061 out of our 3,215 comparisons, version 1 matched the second version by at least by 90% and with no more than 50,000 words differing.



Both graphs show us outliers that require attention, though in different ways. The first, breaks it down by century and gives the sharpest picture of the median. The second gives us the sharpest picture of the outliers. Within the team, we are working with a dynamic version of the second graph that helps us to prioritise outliers for attention.



## **Examples**  

But what are these outliers – the texts whose versions differ significantly? As examples, there are situations labelled as A-C, with the data excerpted as:



![Image](/images/old_posts/Outlierstable-300x136.png)



**Table 2**: The table above represents the situation of 3 different pairs of versions, labeled A, B, and C.



These might be fairly typical cases – a quick reading of the files on GitHub shows the following:



-   The title of the text, Shamela0009170, should not be *Maʿrifat al-Thiqāt*, but, rather, *Taʾrīkh al-Thiqāt*, another work written by the same author.

-   Ibn Saʿd’s *al-Ṭabaqāt al-kubrā*, Shamela0001686, is a complete version; Shamela0012416 includes parts of it. The metadata lists the title as الجزء المتمم لطبقات ابن سعد. الطبقة الرابعة من الصحابة ممن أسلم عند فتح مكة وما بعد ذلك

-   Shamela0012404 is based on the Beirut (Dār al-Maʿrifa) *Maqātil al-Ṭālibiyyin* text edited by al-Sayyid Aḥmad Ṣaqar (no date), and contains the editor’s introduction and footnotes, whereas JK010351 (no metadata) does not contain these.



Some of these cases represent big messes that are rather easily identified and remedied. Based on a first reading of the data, for example, we identified 618 cases, involving 11 titles, where we had very little overlap between two versions because one of them represented a small excerpt of a larger text. They were filtered from the data described above and are not represented in the graph. This rather common scenario will show up in the percentages with the smaller work having a high percentage matched and the larger work having a small percentage matched. A Shamela0023678 text file, for example, was listed as Ibn Kathīr’s *Bidāya wa’l-nihāya*; the 107,574-word text, however, is in fact excerpted from the *Bidāya* and labelled in the text file as *Muʿjazāt al-Nabī*. When we used passim to compare this excerpt against 12 versions of the *Bidāya* each with lengths of about 2 million words, we found the “versions” to be very distant. So, we need to make sure our data reflects that the short one is a part of the text, not the entirety of it.



When we align two books using one of KITAB’s data visualisations, we can often see what is happening. By way of example see below:



![Image](/images/old_posts/twobidayas-300x156.png)



**Image 3**: The top third of the graph shows the shorter of the “versions” of Ibn Kathīr’s *Bidāya wa’l-nihāya* (Shamela0023678), with the text chunked in three hundred words running along the x-axis. The bottom third shows a longer version (Shia003593Vols), also chunked in 300-word segments. The yellow lines represent connections between the two texts. The scattered red lines in the bottom third of the graph likely indicate that the longer version is itself repetitive and matches to more than one part of the short text.



## **So why – in sum – do versions differ?**  

Many of the numeric differences arise from the transition to machine-readable format. The problem here lies not, firstly, in the precision with which the texts were typed up – so far, we are finding this to be generally highly accurate (even when pages are missing, the typed text is verbatim – and it is worth noting that the missing parts seem random and to result from simple human error).



As an example of digital-born errors, we ran scripts to remove footnotes, but these were only partially successful. As the KITAB team is annotating our book files, team members are marking editorial information for removal (including introductions), plus adding missing numbers and text using the scanned images. We record these errors/improvements in a file on GitHub (all have the extension “.yml” – Image 1, above represents a collation of these files through PowerBI software).



Being a bit more schematic, so far, the following reasons seem to explain major differences in versions.



1.  Misattribution – the works are not in fact versions of one another, but entirely different works (situation A).

2.  The same title being applied to a text, and to a longer text that includes this smaller piece (situation B). This happens under a variety of circumstances: e.g. with anthologies, or when a part was printed separately (possibly based on manuscript evidence), or when a large text was typed up in separate files.

3.  Inclusion vs. non-inclusion of introductions, footnotes, editor’s tables, indices, etc. (situation C, all of which should be stripped out).

4.  Missing paragraphs or pages.

5.  The inclusion vs. non-inclusion of chains of transmission with Hadith and historical reports.

6.  The inclusion vs. non-inclusion of pious formulae, or their abbreviation rather than being written in full, and likewise, spelled-out dates, which are much longer than those written with numbers.

7.  Un-joined parts of a text – volumes published separately for example.

8.  The presence of commentaries within, alongside, or following a text.



In cleaning our data, issues 1, 3, and 4 are rather straight-forward – we can relabel works; strip out modern editorial material; and wherever possible, consult editions to type up missing content. Issues 5 and 6 explain differences but require no intervention from the annotation team (we do not aim to improve editions). Within the span of our ERC grant, we should be able to identify and address these issues for a significant number of our texts, vastly improving the quality of our corpus.



Issues 2, 7, and 8, however, are more complicated. They raise questions, legitimately, about what properly, within the Arabic tradition is reckoned to be the text. This is both a practical and philosophical question. Practically, we can check title pages, even revert back to the manuscript tradition. On this basis, one might reckon the longer version to be the “text”, and the shorter one, derivative.



## **Versions as a major topic for book history**  



To return to my point at the start of this blog.



With our cleaning, we should be careful. We should not be looking for ideals of texts that never existed. Our partial versions may not be simply modern derivatives. For example, in the case of the *Bidāya wa’l-nihāya*, all surviving manuscripts of this great classic of Arabic letters are only partial witnesses to a text. And indeed, perhaps the most complete version originally consisted of 8 volumes, of which substantial parts are missing. This suggests that a partial version may be more faithful to how the text was experienced historically.



We can also ponder what the print tradition represents of the manuscripts upon which it is based. We can imagine alignments of machine-readable files based on manuscript witnesses to a specific text. The files are generated either by transcription or by human-corrected Optical Character Recognition. We can visualise differences and compare to existing print editions.



We need to work on cleaning our data. But our work will not stop there. We should use our data to consider the general situation of when parts of works over time became experienced as *the work*. Or of variation within the tradition in general. Does closeness between versions changes over time? Are third century versions less close than ninth century ones? What about genres? Do we find more variation within some corners of the Arabic tradition than in others? Does excerpting increase in particular times and places and/or with particular genres?



With mathematical reading at scale, these are the sorts of provocations that will make work in the Digital Humanities exciting and worthwhile.



N.B. This blog was written based on data generated by the KITAB technical team (Masoumeh Seydi, Ryan Muther, and Sohail Merchant) and also following many discussions with team members working on the corpus, especially Maxim Romanov, Gowaart Van Den Bossche, Mathew Barber, and Peter Verkinderen. I used the programming language R for statistics and for Images 1 and 2. There are many reasons that this topic matters. Other blogs on versions will follow.


































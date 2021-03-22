---
header:
  image: 
  caption: 
title: "A First Look at KITAB’s Data"			
author: sarah_savant		
layout:		single
categories:
  - 
  - 
tags:
  - 
---



The digital revolution is arriving rather late to Middle Eastern Studies, but it is coming fast.



Now, we can see the written tradition at a distance with KITAB’s first dataset. Spoiler: it is hugely intertexual.



There are important caveats: we need to build a more representative corpus; the text reuse software that we use needs further optimization. Still, I would propose that we can already learn a lot.



Let me describe this dataset, and some of what we can see at first glance. I base my comments on statistics that the KITAB team assembled this summer and which we are studying with Microsoft PowerBi (a suite of analytics tools).



Bear with me as what follows will necessarily be a bit granular.



We ran [passim]({{ site.baseurl }}{% link _pages/about-passim.md %}) — text reuse software developed by [David Smith]({{ site.baseurl }}{% link _pages/about.md %}) — on the entirety of [KITAB’s corpus](https://github.com/OpenITI/), comparing the words of each of 4,260 books to the words of every other text (\~18 million book comparisons). This process – including a 5-gram “shingling” method – involves a few simple steps repeated trillions of times as passim searches for, and aligns, common passages. Every time it found a common passage including at least 10 but up to 300 words, it created a record of the match within a file dedicated to the relationship between the two books (so, potentially \~18 million files containing billions of records).



In total, passim generated 1.03 million such files, containing \~23 billion records (or instances of reuse) made up of 983 billion words. This means that 5.7% of the time, in comparing any book in the corpus to any other book in the corpus, it found at least one instance of common wording. This might seem remarkable. These books were comprehensively paired – the equivalent of comparing Wuthering Heights and King Lear – and 5.7% of the time passim found a common passage between such pairs. But, as with English greats, there are accidents of language, especially given the frequency of many Arabic names, words, and phrases.



![Image](/images/old_posts/Musnad_Tawhid.jpg)



**Figure 1**: The above comparison represents an insignificant record of reuse. On the left is a passage from the [*Musnad*](https://github.com/OpenITI/0250AH/blob/master/data/0241IbnHanbal/0241IbnHanbal.Musnad/0241IbnHanbal.Musnad.JK000145-ara1) of Aḥmad b. Ḥanbal (d. 241/855), and on the right, a passage from the [*Kitāb al-Tawḥīd*](https://github.com/OpenITI/0400AH/blob/master/data/0381IbnBabawayh/0381IbnBabawayh.Tawhid/0381IbnBabawayh.Tawhid.Shia001136-ara1) by Ibn Bābawayh (d. 381/991-2).  Passim detects this single instance of reuse, whereas the *Musnad* totals \~1.7 million words and the *Kitāb al-Tawḥīd* 140 thousand.



So where between two books, there is only one such instance of reuse recorded, the substance of reuse is virtually always of no interest and documents no meaningful relationship between the books (e.g., no direct use, no major common source). Similarly, 2 or 3 records of reuse are (most) often matters of pure accident. Of the \~1 million files, approximately 600,000 have only 3 or fewer records.



![Image](/images/old_posts/srtfilesByinstances-1024x432.png)



The graph here shows how much the data is dominated by files documenting, frankly, meaningless relationships. The y-axis shows the number of files, and the x-axis the number of records for a pair of compared books (specifically, 1 = at least one record in a file; 2 = at least two records, and so on). The number of files drops steeply as the number of records increases. There were \~18 million possible matches, and \~1 million times books match with at least 1 record. By comparison, as the far right of the graph shows, there are about \~32,000 files with at least 100 such matches.



We do not know, yet, at what point we can assume two texts to start having a historically meaningful relationship based on counting such instances – and there was likely no specific tipping point, say 4 or 5. But what is much more interesting is that most books in our corpus do have a much more substantial relationship with at least one other book, and that a very large number of them have very substantial ones. In in other words, it is uncommon to find a book that is independent of all others. This is another way of slicing the same data.



![Image](/images/old_posts/bookbyinstances-2-1024x491.png)



The above graph shows that many of our works have very much in common with other works. The y-axis shows the number of books, and the x-axis the number of records (specifically, 1 = at least one record in a file; 2 = at least two records, and so on). Of the 4,260 books analysed, 3,606 – or 85% – have at least 20 common passages with another book. As you can see at the far right of the graph, of the 4,260 books, just over half (2,332) contain at least 100 records of common passages with another book.



So, whereas many relationships are meaningless, we do have many meaningful ones. And most books are meaningfully linked to other books.



What is perhaps more interesting, and ready for our analysis now, is the outliers – the cases where reuse is enormous. Filtering our data shows the following, for example:



-   For 25% of our 4,260 books, more than 50% of the book matches with at least one other book in the corpus (reckoned by word count); similarly, for 18% of our corpus, or 757 books, our approach identified1,000 or more instances of text reuse with another book;

-   Works typically classified as pertaining to Hadith are massively intertextual. For example, despite the example of meaningless reuse cited above, the *Musnad* of Aḥmad b. Ḥanbal (d. 241/855) shares hundreds of thousands of words with other individual books;

-   Many authors substantially repeat themselves.



This high degree of reuse should make us reconsider many assumptions we have about the textual tradition as a whole – including, for example, how people who produced such works conceived of what they were doing.



In the coming weeks and months, stay tuned as we report more overviews and details from this dataset and other sets that we are working on now.



Up next: Taking the Measure of “Self Reuse”


































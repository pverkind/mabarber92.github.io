---
header:
  image: 
  caption: 
title: "Contagion in the Corpus: The Black Death and Where to Find It"			
author: gowaart_van_den_bossche		
layout:		single
categories:
  - 
  - 
tags:
  - 
---




<p align="center"> “How can I bear to pair fair words in rhyme </p>  

<p align="center"> when I have lost the one with whom I was a pair?” </p>



So mourns the great Mamluk-era poet Ibn Nubatah al-Misri (d. 768/1366) for his deceased concubine. She was but one of the many family members the poet lost throughout his long life: he is said to have lost no less than sixteen sons between the age of five and seven. While this particular concubine died because of pulmonary tuberculosis, presumably a good number of his sons died of the devastating effects of the Plague, also known as the Black Death. This most famous of pandemics is estimated to have wiped out half of Egypt’s population in the mid-8th/14th century. Its perseverance in North Africa until quite recently may even have indirectly inspired Albert Camus’ classic novel *La Peste* (*The Plague*).



The recent outbreak of the Covid-19 (Corona) virus, while serious, is fortunately nowhere near as dramatic as the onslaught of plague pandemics in the Medieval world. Nor is it as deadly as the cholera epidemics of the 19th century that probably inspired Camus more directly. But, these curious times do invite us to ponder the lessons and warnings (*‘ibra*, pl. *‘ibar*) of history, one of history’s primary roles according to many medieval Muslim historians. I started wondering in what ways the OpenITI corpus can tell us something about the impact of the Plague in texts. The development of a new OpenITI NgramReader+ by our team’s senior research fellow Maxim Romanov provides an opportunity to do so, as it allows us to gain a snapshot idea of the usage of Arabic terms across the centuries. The Reader exists in three forms: a Lite version which only provides data on unigrams (i.e. single words), as well as a Medium and a Full version which also include bigrams (i.e. two words). The Lite version is accessible online and will be used [here](https://maximromanov.shinyapps.io/OpenITI_NgramReaderPlus_Lite/). The other versions can only be run on a local machine. All three versions of the app can be downloaded [here](https://zenodo.org/record/3725855#.XpnqxG57mB4)



To quote Maxim, the NgramReader+ “charts diachronic frequencies of words and phrases, using the data of the OpenITI corpus (Arabic data only).” The data from the corpus is grouped per half-century based on authors’ death dates. Once prompted the reader will give you data on the absolute and relative frequency of these words in two separate graphs. As you will notice, this requires getting the hang of particular transcription rules and some basic notions of Regular Expressions. The data provided is only abstract, as at the moment it is not possible to locate the usages of these terms in precise texts. However, work is currently being undertaken by Sohail Merchant and Peter Verkinderen on a complex search app which will allow readers to locate (variations of) particular words and phrases.



The Arabic sources confront us with two terms used somewhat interchangeably for Plague: *ta‘un* and *waba’*. This is no problem for our purposes, as the great thing about the NgramReader+ is that it allows you to run up to five terms at once. I have put both these terms into the Ngram-prompt. What emerges is that neither *ta‘un *nor *waba’* have a very strong presence in our corpus, but that logical trends in their usage seem to be discernible. Logical, because peaks of usage for these terms appear to follow the 8th/14th and 9th/15th century, when the pandemic hit repeatedly throughout the Middle East.



![Image](/images/old_posts/Gwt-b-1.png)



**Figure 1**: Absolute frequency of Ngrams



The graph in figure 1 provides absolute numbers of term occurrence, showing that *ta‘un* peaked in the late 9th/15th and early 10th/16th centuries, and that *waba’* has a sharp drop-off after that period. One of the possible reasons for this, is that the 9th/15th century especially saw a huge boost in textual production, especially historiography, much of which would have been retrospective. Some of the richest sources on the 8th/14th century Plague were not produced at the time of that pandemic, but in the following century. Furthermore, the early Ottoman period also saw several pandemic periods.



![Image](/images/old_posts/Gwt-b-2.png)



**Figure 2**: Relative frequency of Ngrams



The graph in figure 2 shows the relative frequency of the terms compared to the total word count for each half-century. This shows that neither term was used very often as the percentages are very low. Considering that any word is indexed as an Ngram, however, percentages will always be quite low due to commonly used words taking up much of the space. This graph does provide us with a glimpse of a second peak in the early centuries, coinciding more or less with what has been called the Justinianic Plague (ca. 541-750 CE), the first historically documented Plague. Because of the smaller size of our corpus for these centuries the absolute numbers are low here, but in relative terms there is a discernable pattern.



Such results can be much fine-tuned in the app and they can also be combined in longer phrases (bigrams – these can only be accessed via the Medium and Full version of the Reader), but I have chosen here to focus only on a quick demonstration of its abilities. Likely the most important caveat for this mini-exploration is that some of the main sources for this subject are not (yet) part of our corpus. Firstly, the so-called “Plague treatises,” of which we appear to have none in our corpus despite their relative prevalence in Arabic literature (about three dozen are known). Secondly, medical literature, which is not particularly well represented either. This little blog-excursus of mine has now brought to attention a few lacunae in our corpus, which can be addressed through our OCR-pipeline.



The Plague treatises generally follow a form that is familiar in our corpus, as patchworks of various citations, especially from prophetic Hadith, compiled as relevant information on a particular topic. While some provide medical and historical data on the Plague, the treatises mostly argue that the grief caused by plague should be weathered by showing patience (the important Islamic virtue *sabr*) and that one should be reconciled with God’s designs for humanity. Three such Plague treatises have received a fair amount of scholarly attention. One was written by the fourteenth-century littérateur Ibn Abi Hajala (d. 776/1375), of whom we only have one work in our corpus at the moment (a grave underestimation of his literary importance). Another one  was written by his contemporary Ibn al-Wardi (d. 749/1349), of whom we similarly have only one work in the corpus. A third text was written by the fifteenth-century scholar Ibn Hajar al-*‘*Asqalani (d. 852/1448), of whom we have many works in the corpus, but with a somewhat inordinate stress on his traditionalist, historical, and legal writings. This last text was later abridged and annotated by one of the most prolific authors in Arabic literature generally speaking, Jalal al-Din al-Suyuti (d. 911/1505). His writings are also well represented in our corpus, but his Plague treatise is not available.



As a further excursus on book history in its manuscript form, I would like to conclude with some information that I have gathered on manuscripts of Ibn Hajar’s *al-Badhl al-ma‘un fi fawa’id* (some manuscripts read *fada’il*) *al-ta‘un* (“The Granter of Aid: On the Benefits/Merits of the Plague”)*.* Note that the title of this text already suggests that the Plague had “benefits” or “merits” because it reminded people of the importance of *sabr* and of the Last Day. I gathered this information in the context of earlier research with the Ghent-based “Mamlukisation of the Mamluk Sultanate II” project (PI Jo Van Steenbergen). This text is quite well attested in manuscript form: the earliest studies of it were undertaken on a manuscript in the Escorial library (which most likely originated from the Maghreb), Brockelmann mentions four more copies in his *Geschichte der Arabischen Literatur*, and today several more can be identified. For example, the Egyptian Dar al-Kutub holds no less than four manuscripts of the text. One of these is an interesting case of a manuscript becoming a network of various types of text reuse, not only in its body text, but also in its paratexts. This manuscript’s main text is followed by appendices containing biographical notices taken from Ibn Khallikan’s *Wafayat al-a‘yan*, and preceded by two folios of various *hadith*s (with attributions). A cursory overview suggested that this material was intimately related to the body text, as it provided additional material to evaluate the soundness of the *hadith*s quoted by Ibn Hajar al-*‘*Asqalani. See my description of the manuscript [here](https://ihodp.ugent.be/bah/mml01%3A000000386).



Similarly, a manuscript of the same text from the Damascene Zahiriyya library (number 62) of which a microfilm scan circulates online, showcases how the very pages of a manuscript could become an arena of scholarly debate: the margins and title page contain various reading notes elaborating on issues raised in the main text.



![Image](/images/old_posts/Gwt-b-3.png)



**Figure 3:** scan of the title page of a Zahiriyya library copy of *al-Badhl al-ma‘un* with a rather extensive amount of annotation.



This kind of material highlights another important caveat to keep in mind when studying a topic such as the Plague only through edited texts, or through the corpus approach we apply in KITAB. While apps such as the OpenITI NgramReader+ or algorithmic analysis through passim provide valuable data, it is still important to take into account the physical objects through which texts have come down to us if we want to investigate how texts were received and reproduced.



### **Bibliography**



I have quoted Ibn Nubata’s verse from Geert-Jan van Gelder, *Classical Arabic Literature: A Library of Arabic Literature Anthology* (NYU Press, 2013), pp. 85-86.



Another translation and thorough analysis of the poem was made by Adam Talib, “The Many Lives of Arabic Verse: Ibn Nubatah al-Misri Mourns More Than Once,” *Journal of Arabic Literature* 44 (2013), pp. 257-92.



On Ibn Nubata’s elegies for his children, see Thomas Bauer, “Communication and Emotion: The case of Ibn Nubatah’s ‘*Kindertotenlieder*‘,” *Mamluk Studies Review* 7 (2003), pp. 49 – 95.



The proper way to cite the NgramReader+ is as follows: Romanov, Maxim. (2020, March 24). OpenITI NgramReader+ (Version 2020.1). Zenodo. http://doi.org/10.5281/zenodo.3725855.



### **On the Plague more generally, see amongst others:**



Several contributions by Lawrence I. Conrad, especially “*Taʿun* and *Wabaʾ*: Conceptions of Plague and Pestilence in Early Islam,” *Journal of the Economic and Social History of the Orient* 25 vol. 3 (1982), pp. 268-307.



Michael Dols, *The Black Death in the Middle East* (Princeton University Press, 1977).



Stuart Borsch, *The Black Death in Egypt and England: A Comparative Study* (University of Texas Press, 2005).



Nükhet Varlik, “Between Local and Universal: Translating Knowledge in Early Modern Ottoman Plague Treatises.” In *Knowledge in Translation: Global Patterns of Scientific Exchange, 1000-1800 CE*, eds. P. Manning & A. Owen (University of Pittsburgh Press, 2018), pp. 177-90.



 


































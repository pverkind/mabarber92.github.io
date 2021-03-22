---
header:
  image: 
  caption: 
title: "Algorithmic Reading of Shiʿi Hadith Collections: Direct Borrowing and Common Sources"			
author: aslisho_qurboniev		
layout:		single
categories:
  - 
  - 
tags:
  - 
---



It is not accidental that a large number of books in the OpenITI corpus belong to one important genre, the Prophetic *hadith* – the sayings of the Prophet Muhammad and accounts of his practice. As a repository of the Prophetic tradition (*sunna*), they are considered as an authoritative source of law and moral guidance in Islam. When early Muslim religious scholars sought ‘knowledge’ (*ʿilm*), they often meant hadith. In this blog, I will briefly discuss what Shiʿi hadith is and provide some preliminary ideas towards reconstructing early hadith transmission through computational reading.



The main difference between the Shiʿi and Sunni notions of hadith is that for the Shiʿis the accounts of their imams are equally authoritative to those of the Prophet. Shiʿi Muslims generally recognise as authentic the six canonical collections[^1] of Sunni Islam containing reports about what the Prophet Muhammad said, did, or approved, in addition to their own collections.[^2] However, for a tradition to be considered as a legitimate source of law in Shiʿi Islam, its chain of narrators (*isnad*) has to go back to Ali b. Abi Talib (d. 661), the fourth caliph and the first Shiʿi imam, his wife Fatima, daughter of the Prophet, or to their descendants. It is primarily for this reason that the collection, transmission, and codification of Shiʿi hadith had its own trajectory and specificities.



Early individual collections of Shiʿi hadith were first-hand reports from the imams, which were known as *usul* (origins, primary sources) or simply as *kutub* (writings, notebooks) to later hadith scholars. On occasion, the later compilers named their sources, which is useful for modern historians.  For example in the *Kitab al-Idah*, the first known Ismaʿili Shiʿi compendium of legal hadith, a vast compilation that surpassed all canonical hadith collections, Sunni and Shiʿi, in volume, but of which only a small portion survives, the famous Fatimid jurist al-Qadi al-Nuʿman (d. 973) consistently quoted his written sources in the following manner:



“\[It is reported\] in the *Book* of al-Halabi, known as the *Kitab al-Masaʾil,* from Abi ʿAbd Allah Jaʿfar b. Muhammad \[al-Sadiq, the fifth Shiʿi imam\], that he said: \[*matn*\] (the actual report)” (p. 207).



However, this was not the standard practice. Despite the fact that hadith compilers relied on written sources, they never felt the need to mention them, though they invariably recorded the chains of transmitters. This was largely due to the fact that the authority of oral transmitters usually took precedence over that of a written source. This is one reason why only a handful of the early individual collections survive independently. The rest, estimated between 400 and 1,000 Imami Shiʿi collections from mid-eighth to ninth centuries, have been gradually subsumed by the massive hadith compilations that appeared from the tenth century onwards. Nevertheless, we know about the existence of these early collections from bibliographical works, such as the *Fihrist* of al-Shaykh al-Tusi (d. 1067), although his information also came mainly from oral sources (Kohlberg, 1987).



We need to add at this point that the authenticity of both Sunni and Shiʿi hadith is predicated on the veracity of its *isnad*.  Most hadith have a structure consisting of an *isnad* followed by a *matn* (textual report) similar to this:



“A report from Ahmad, from Muhammad, from Yusuf, from an Egyptian man, who was with Ali b. Abi Talib when he said: The Prophet said: \[the *matn*\].”



As discussed in a recent blogpost by Ryan Muther, the relative consistency of the structural elements of hadith, with its standard transmissive terms and established pattern of *isnad* – *matn* – *isnad*, makes it a promising area and an important  subject matter for computational reading and text-mining.



## ***Daʿaʾim al-Islam,*** **Shiʿi Hadith Corpus, and Passim Algorithm**



In this blog, I will test the search, navigation, and text mining tools created by the KITAB team which make it possible to extract information from vast corpora such as the OpenITI corpus, on a select number of Shiʿi hadith works. I will choose the *Kitab Daʿaʾim al-Islam* (The Pillars of Islam)*,* the important compendium of legal hadith by al-Qadi al-Nuʿman, as an example. I will be mainly dealing with a KITAB visualisation application which visualises alignments between two texts detected by passim algorithm (it is not yet publicly available).



While passim outputs, in the form of textual alignments, might point  to text reuse or direct relationships between two closely aligned texts, the data can also indicate simply that the two texts share common sources. The original sources are often lost, as is the case with primary sources for Shiʿi hadith, although hundreds of them were in circulation from the 8th century onwards. Let us look at both types of relationship – the one involving common (lost) sources, and the other involving a direct relationship, through the case of the *Daʿaʾim al-Islam.* We will begin by looking at the relationship formed through drawing on common sources.



The first example is a comparison between the *Daʿaʾim* and the *Kitab al-Kafi* of al-Kulayni (d. 941), the first canonical Imami Shiʿi collection. Both works were compiled roughly around the same time, in Kairouan (modern Tunisia) and Baghdad, respectively, so it is most likely that the authors did not have direct access to each other’s books. However, because both works were drawing on many common Shiʿi  sources and early hadith collections, the algorithmic reading of the texts yields a significant number of alignments. The figure below visualises 152 common passages detected by passim. Here, the width of the red lines indicates the length of reused text in each of the books. Typically, unless a book is directly reused, the number of paired alignments will be few and one will not be able to get a quick idea about the nature of the relationship between the texts. This is what happens when we compare the *Daʿaʾim* with the earliest hadith collections. However, when compared with comprehensive compandia, such as the *Kafi,* we get an instant idea about the structure of the texts.



![Image](/images/old_posts/AS-1.png)



**Figure 1.** Top: *Daʿaʾim al-Islam*, bottom: *al-Kafi* of al-Kulayni (d. 941). There are 152 alignments between the two texts. The numbers in the box indicate the point within the book (milestone) within which the alignments occur (milestone 536 in book 1 and milestone  number 283 in book 2). The books are split into milestones, each with 300 words, to facilitate running the text reuse algorithm passim. The numbers in parentheses represent where the alignment occurs within the milestone.



As illustrated above, both the *Daʿaʾim* and *al-Kafi* are structured similarly. This is expected because hadith compilations are usually arranged according to common legal topics. Both works are also considered as the most important sources of  Shiʿi law, which raises questions about the boundaries between hadith and *fiqh* (Islamic legal tradition) and their mutual influence. Hence, text reuse methods can be a starting point for addressing research questions pertinent to the formation of these traditions. Having seen how the KITAB application provides a ‘bird’s eye view’ of the two texts, we will try the ‘deep dive’ approach, namely diving into the text to find granular details. For information about the usage of hadith in different legal traditions, individual records can be instantly viewed for comparison and context. For instance, we may want to find out why one pair of alignments in the above visualisation does not follow the general pattern (Figure 1, Book 1, at milestone 536). Clicking on the line opens the passage in an alignment reader.



![Image](/images/old_posts/AS-2.png)

**Figure 2.** Comparing hadith in the *Daʿaʾim* (Book 1) and *al-Kafi* (Book 2) in an alignment reader (a reader can see the context in which the alignment occurs).



The passages above contain a hadith about ʿAli b. Abi Talib’s will to his sons, in which he is said to have bequeathed his weapons and books to his elder son al-Hasan, whom he also appointed as his successor in the presence of his other sons, family, and supporters. Al-Nuʿman uses this tradition to make a juridical point in the *Kitab al-Wasaya* (Book of Wills), whereas al-Kulayni brings it up in the *Usul* part of his *al-Kafi,* to make a theological argument about the designation of imams, one after another (the doctrine of *nass*). Same story, different interpretations.



Despite drawing on shared sources, the divergences between the *Daʿaʾim* and other early compilations are expected. First of all, al-Qadi al-Nuʿman’s allegiance to the Fatimids, which makes him the first and the last Ismaʿili hadith compiler, informed his choices as a compiler. He was also the only major Shiʿi compiler from the Maghrib, while all canonical hadith collections (six Sunni and four Shiʿi) were compiled by natives of Iran and Khurasan. Hence, his sources may have not been known in the East, or were deliberately neglected by Eastern compilers for doctrinal biases, and vice versa. In fact, some early sources quoted by al-Nuʿman were still unknown even to early modern compilers, such as Muhammad Baqir al-Majlisi (d. 1687), whose enormous compilation, the *Bihar al-anwar* (Oceans of Light), is otherwise exhaustive. Thus, not detecting text reuse is equally informative and al-Nuʿman’s compilations provide an interesting case for further exploration.



Next, we turn to the second type of relationship between texts, namely a relationship through direct reuse*.* After the fall of the Fatimid Empire, the *Daʿaʾim* retained its status as the most authoritative legal code among the Tayyibi Ismaʿilis and was mainly preserved by their scholars. It seems to have also been known to most Shiʿi *hadith* compilers in later periods. While the earliest Imami Shiʿi scholars did not include al-Nuʿman in their biographical dictionaries, gradually his name and works are mentioned, beginning with Ibn Shahrashub’s (d. 1192) *Maʿalim al-ʿulama*.  He was eventually claimed as an Imami scholar, probably first by Qadi Nur Allah al-Shushtari (d. 1610), according to Poonawala. Thus, visual comparison between the *Daʿaʾim* and major medieval Shiʿi compendia reveal a pattern similar to the one described above, followed even by al-Hurr al-ʿAmili’s (d. 1624) massive hadith compilation, *Tafsil Wasaʾil al-Shiʿa.* We see direct quotation from the *Daʿaʾim* beginning with the largest compilation of the Safavid period, the *Bihar al-anwar* of al-Majlisi, who also noted the misattribution of the *Daʿaʾim* to Ibn Babawayh (d. 991) and asserted that the real author, al-Qadi Nuʿman, was an Imami scholar. With the next great compiler of legal hadith, Mirza Husayn Nuri Tabarsi’s (d. 1902) *Mustadrak al-Wasail,* the *Daʿaʾim* was fully absorbed into the Shiʿi hadith corpus (Figure 3).



![Image](/images/old_posts/AS-3.png)



**Figure 3.** Top: *Daʿaʾim al-Islam,* bottom:  *Mustadrak al-Wasaʾil.* Tabarsi’s quotation from the *Daʿaʾim* is the most extensive among the Shiʿi sources in our corpus (1,920 alignments).



Tabarsi’s *Mustadrak* (Supplement) to al-Hurr al-ʿAmili’s *Wasaʾil al-Shiʿa* (Figure 4) is one of the largest and most recent Shiʿi compilations, comprising 18 volumes. Given that the *Daʿaʾim* has the biggest number of alignments with the *Mustadrak* (1,920 records), Tabarsi must have considered the *Daʿaʾim* a major omission from the work of his predecessor. The overall number of direct quotations from the *Daʿaʾim*, in which the source is cited, is 2,580. It should, however, be noted that not all direct quotes may be picked up by passim, because not all of them result in significant textual overlap. Paraphrasing and alterations can also influence the output. This nuance should be taken into account when comparing hadith works



On the other hand, the hadith corpus is so vast and its oral and written sources are so numerous that it necessarily leads to various types of transtextualities. In hadith compilations, both different source-texts and variant *isnads* warranted repeated quotation of the same hadith. Even when texts were intended as a ‘supplement’  to another work, repetitions could not be avoided, and Tabarsi’s *Mustadrak* is a good example. Tabarsi, in fact, was conscious about this and included the following disclaimer in his introduction:



“If one comes across a hadith that is also found in the original work \[*Wasaʿil*\], quoted from the same book that we have quoted, he should not rush to blame us. This is because the Shaykh \[al-ʿAmili\] often mentions a hadith in a chapter with little relevance to that chapter, while it would have been more appropriate to include it in another. Because we did not find a hadith where it was expected and did not check the other chapter, we may have deemed it an omission and included it \[repeatedly\]. We found some of these and corrected them, but if some are still there, their presence will not harm, nor should it give a reason for criticism. How true is the saying that: ‘The one who compiled, has made himself a target’” (*Mustadrak*, 1:62).



I hope the present blog has showcased how digital methods help to solve the ‘information management’ problem described by Tabarsi.



![Image](/images/old_posts/AS-4.png)

**Figure 4.** Top: *Wasaʾil al-Shiʿa* of al-Hurr al-ʿAmili; bottom: *Mustadrak al-Wasaʾil,* Tabarsi’s supplement.



As a final observation, computational methods facilitate instantaneous reading and analysis of thousands of traditions and chains of transmissions. Perhaps a few exceptional individuals are able  to combine the kind of ‘bird-eye view’ and scrutiny offered by modern digital toolbox, but it is inconceivable that they will be able to do so  with the same precision or pace. These new computational tools can not only help rethink the standard questions about knowledge transmission but also explore the complex ways in which cultural memory was formed, transmitted and perpetuated. ‘Digital humanities,’ while itself a recent and likely a temporary shorthand to refer to a set of digital methods and toolboxes, may help us  challenge an array of neologisms and modern constructions in the field of Islamic studies, and return us to closer access to source-texts, thus  allowing the texts to speak for themselves. Ultimately and ironically, these methods will help us recognise the merits of the so-called ‘traditional Muslim sources’ by reconstructing the history of knowledge production and transmission as it unfolded organically.



[^1]:  ** **Six Sunni canonical hadith collections, known as ‘The Authentic Six’: *Jamiʿ al-sahih* of Muhammad b. Ismaʿil al-Bukhari (d. 870), the *Jamiʿ al-sahih* of Muslim b. Hajjaj al-Naysaburi (d. 874), *Sunan* of Abu Dawud al-Sijistani (d. 888), *Sunan* of Muhammad b. ʿIsa al-Tirmidhi (d. 892), *Sunan* of  Ibn Maja al-Qazwini (d. 886), and the *Sunan* of Ahmad b. Shuʿayb al-Nasaʿi (d. 915).

[^2]:  Four Twelver Shiʿi canonical collections, known as ‘The Four Books’: Muhammad b. Yaʿqub al-Kulayni’s (d. 941) *al-Kafi fi ʿilm al-din*; Ibn Babawayh, al-Shaykh al-Saduq’s (d. 991), *Man la yahzruhu al-faqih;* Muhammad b. Hasan, al-Shaykh al-Tusi’s (d. 1067) *Tahdhib al-ahkam,* and his *al-Istibsar fi ma ikhtalafa min al-akhbar.*



### **References and further reading**



Ahmed, Shahab, Ahmad Kazemi-Moussavi, Ismail K. Poonawala. “Hadith i-iii,” *Encyclopaedia Iranica*. Vol. XI/4, available online at <http://www.iranicaonline.org/articles/hadith-index> (accessed on 01 May 2020). For a general introduction to *hadith* and *hadith* studies with informative sections on Shiʿi and Ismaʿili *hadith*.



Daftary, Farhad and Gurdofarid Miskinzoda (eds). *The Study of Shiʿi Islam: History, Theology and Law.* London: I.B. Tauris, 2016.



Gleave, Robert. “Between *Hadith* and *Fiqh*: The ‘Canonical’ Imami Collections of *Akhbar*.” *Islamic Law and Society*  8, No. 3, Hadith and Fiqh (2001), pp. 350-82.



Kohlberg, Etan. “Shiʿi Hadith.” In *The Cambridge History of Arabic Literature*. Vol. 1, *Arabic Literature until the End of the Umayyad Period*, edited by A. F. L. Beeston, pp. 299–307. Cambridge, UK: Cambridge University Press, 1983.



Kohlberg, Etan. “Al-Usul al-arbaʿumiʾa.” *Jerusalem Studies in Arabic and Islam* 10 (1987), pp. 128-65.



Madelung, Wilferd. “The Sources of Ismaʿili Law.” *Journal of Near Eastern Studies* 35 (1976), pp. 29-40.



Modarressi, Hossein*. Tradition and Survival: A Bibliographic Survey of Early Shi’ite Literature.* Oxford: Oneworld Publications, 2003.



Poonawala, Ismail K. “The Chronology of al-Qadi l-Nuʿman’s Works.” *Arabica* 65 (2018), pp. 84-162.



Al-Qadi al-Nuʿman, Abu Hanifa b. Muhammad. *Daʿaʾim al-Islam wa dhikr al-halal wa-l-haram wa-l-qadaya wa-l-ahkam,* ed. Asaf A. A. Fyzee, 2 vols, Cairo: Dar al-Maʿarif, 1951-1960; English Ismail K. H. Poonawala, tr. *The Pillars of Islam,* 2 vols. Oxford: Oxford University Press, 2002-2004.



Al-Qadi al-Nuʿman. *Kitab al-Idah*, ed. Muhammad Kazim Rahmati. Qom: Markaz-i Tahqiqat-i Dar al-Hadith, 2003.



Tabarsi, Mirza Husayn al-Nuri. *Mustadrak al-Wasaʾil wa mustanbat al-masaʾil,* ed. Muʾassasat Al Bayt, 18 vols, 3rd edition. Beirut: Muʾassasat Al Bayt li-Ihya al-Turath, 1991.



 


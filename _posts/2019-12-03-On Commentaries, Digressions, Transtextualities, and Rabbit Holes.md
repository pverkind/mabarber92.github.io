---
header:
  image: 
  caption: 
title: "On Commentaries, Digressions, Transtextualities, and Rabbit Holes"			
author: gowaart_van_den_bossche		
layout:		single
categories:
  - 
  - 
tags:
  - 
---




Running passim on the OpenITI corpus allows us to identify a vast number of instances of text reuse, but the quality of these results from a historical point of view depends on the quality of texts in the corpus. As the material was pulled from various often inconsistently formatted digital corpora (mainly Shamela, al-Jāmiʿ al-kabīr, and Shia Online), the text quality of books in our corpus needs to be properly assessed and harmonised as much as possible. Part of our responsibility as postdoctoral fellows with the KITAB project involves evaluating the quality of a number of such texts as well as tagging their general structure. In this blog post I discuss a number of complexities of this job, especially as they relate to the larger research questions of text reuse and the many-sided “inter-“ and even “transtextualities” (Gérard Genette) in our corpus, and to what we jokingly refer to as the rabbit holes you can fall into when doing this work.



Some time ago I decided to work on the annotation of *al-Risāla l-ʿuthmāniyya*, a text on the virtues of ʿUthmān attributed to the early Islamic polymath al-Jāḥiẓ (d. 255/868-9). In doing so, I found out that this particular text had been published as part of a compilation that also included an appendix containing the refutation of al-Jāḥiẓ’s arguments by his contemporary Jaʿfar al-Iskāfī (d. 240/854). To complicate matters further, this other text is in fact only known to have survived through being quoted in *Sharḥ Nahj al-Balāgha*, a large-scale “commentary” on the earlier *Nahj al-balāgha* (“The Peak of Eloquence”). The refutation found in our edition of al-Jāḥiẓ’s *al-Risāla l-ʿuthmāniyya* is thus an extract tacked on by a modern editor and does not reflect the historical transmission of al-Jāḥiẓ’s text.



*Nahj al-balāgha* itself consists of various sayings, sermons and speeches attributed to ʿAlī b. Abī Ṭālib (d. 40/661), who was widely appreciated as having been extremely eloquent and well-spoken (i.e. *balīgh*). Its compilation is generally attributed to al-Sharīf al-Rāḍī (d. 1016 CE), but in our corpus it is still filed as a work by ʿAlī b. Abī Ṭālib himself. The later *Sharḥ Nahj al-Balāgha* was compiled by the seventh/thirteenth century scholar Ibn Abī l-Ḥadīd (d. 656/1258) and has become arguably even more popular than al-Rāḍī’s text. This popularity may be explained through the particular predilections of “post-classical” Arabic literary tastes: Ibn Abī l-Ḥadīd did not just comment on the lexical and semantic meanings of various words and phrases, but also took the occasion to display his vast knowledge of the Arabic written tradition. This results in twenty volumes of associative digressions on matters of poetry, literary theory, and also on some doctrinal issues—it is interesting to note that the work of Ibn Abī l-Ḥadīd, who belonged to the Shāfiʿīte *madhhab*, cuts across doctrinal divides and remains popular amongst both Shiites and Sunnites. It is in these digressions that we should locate the quotations from Jaʿfar al-Iskāfī’s refutation of *al-Risālat l-ʿuthmāniyya*, which Ibn Abī l-Ḥadīd deemed relevant to include. In the visualisation of text reuse data between the digital version of al-Jāḥiẓ’ *al*–*Risālat l-ʿuthmāniyya* (top) and that of *Sharḥ Nahj al-Balāgha* (bottom) pictured below, one can see that the correlation of the texts is mostly comprised of one chunk near the end of the first work (i.e. the appendix containing al-Iskāfī’s refutation) which is unsurprisingly found more or less verbatim in the second work (in the thirteenth volume to be more exact), as well as a smattering of other material throughout the work.



![Image](/images/old_posts/viz1.png)



**Image 1:** top represents the digital version of al-Jāḥiẓ’s *al-Risāla l-ʿuthmāniyya,* bottom the digital version of Ibn Abī l-Ḥadīd’s *Sharḥ Nahj al-balāgha*. Red blocks denote the chunks of text shared between the two texts while the yellow lines show their position within the works.



Below is a visualisation of the relationship between this work and the work it comments on, *Nahj al-balāgha*:



![Image](/images/old_posts/viz2-1024x462.png)



**Image 2:** top represents the digital version Ibn Abī l-Ḥadīd’s *Sharḥ Nahj al-balāgha*, bottom represents the digital version of the much shorter *Nahj al-balāgha*. One can see how material from *Nahj al-balāgha* is found all across the Sharḥ, as would be expected from a commentary, though with several fairly large gaps which are likely caused by Ibn Abī l-Ḥadīd’s extensive digressions.



The most surprising aspect of this visualisation is that the original *Nahj al-Balāgha* does not seem to have a full match only with the *Sharḥ* — this is clear from the fact that the red block of text that represents *Nahj al-balāgha* is not fully coloured, which one would expect if we’re dealing with a word-for-word commentary. If we look at statistics on word match between these two digital works, it appears that the *Sharḥ* only includes 45% of *Nahj al-balāgha*. Does this mean that Ibn Abī l-Ḥadīd only commented on about half of the original text? Having gone through the entirety of Ibn Abī l-Ḥadīd’s twenty volumes, this struck me as unlikely, so I took a closer look at the digital version of *Nahj al-Balāgha*. It turns out that when the digital version of this text had been prepared for the OpenITI corpus, the footnotes had not been successfully deleted. However, in a way this was somewhat fortunate, as these footnotes add another layer of beautiful complexity to our case: these footnotes consist almost entirely of *another* commentary on this text by none other than Muḥammad ʿAbduh (d. 1905). It is interesting to note that ʿAbduh’s commentary is much drier and to the point than that of Ibn Abī l-Ḥadīd and resembles much more our modern use of footnotes, an obvious shift in audience tastes for this kind of material. It could be argued that this digital text as such preserves not one, but two texts, albeit in a completely different way than the earlier example of the *al-Risāla l-ʿUthmāniyya* in which the editor simply tagged on a commentary to the end. The editor of this version of *Nahj al-Balāgha,* on the other hand, included the commentary in a way that is reminiscent of practices common in later periods of the Islamic written tradition, i.e. with marginal and interlinear commentaries which do not easily translate to the format of a modern edition.



Cases such as these create a complexity in our corpus which we have to address and distinguish thoroughly if we want to create reliable data on text reuse. We have recently taken a number of decisions to resolve problematic cases such as these: in the case of books containing more than one text we have decided to transfer the additional text(s) into (a) separate file(s), and residual footnotes we will transfer to endnotes which can then be excluded for certain types of analysis while preserving them for other types. Of course, even when our data becomes “cleaner”, qualitative assessment will always be needed. At the same time, problems such as these also highlight the vibrant complexity of the Arabic written tradition itself, and provide food for thought and discussion for the general research angles of the KITAB project.



![Image](/images/old_posts/diagram.png)



**Image 3:** general visualisation of textual relationships in this case study.





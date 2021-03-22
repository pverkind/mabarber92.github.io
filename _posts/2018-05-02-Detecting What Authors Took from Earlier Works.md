---
header:
  image: 
  caption: 
title: "Detecting What Authors Took from Earlier Works"			
author: sarah_savant		
layout:		single
categories:
  - 
  - 
tags:
  - 
---



With text reuse detection, we rely on the power, speed, and memory of a computer to find common passages between texts.



![Image](/images/old_posts/giphy.gif)



From our data so far, we can already see hundreds, or even thousands, of cases that point to the liquidity of the written tradition. By “liquid,” I mean that texts were often reused to form new books. For readers, it was nothing unusual to access old texts through new ones. This was true in the earliest times (e.g., 9th century), and continued in different ways for centuries afterwards.



One of the most important things our algorithm can do is to show us more precisely where this reuse begins and ends between and among books. Looking into specific cases in our data, one thing is clear: when we consider transmission, we often think either too big or too small.



**Too big.** When we assume the book as the main game in transmission. Of course books were copied and transmitted onward, but authors were also happy to take large parts of earlier works into new ones. Our data encourages us to take more notice of other indications of partial transmission. The Ashrafiya library catalogue, documented by Konrad Hirschler, contains a great number of multi-text compilations and parts of books (including many under *min*, i.e., *Min akhbār al-Barāmika*). There is also the popularity of anthologies, abridgments, literature in excerpts, and other literary forms.[^1]



**Too small.** When we focus on the individual report or *khabar* or, at most, clusters of such reports. This is, indeed, where many scholars spend most of their intellectual energy, often with fruitful results.[^2]



Text-reuse detection help us to see, by contrast, what parts of texts were in fact transmitted in particular instances. The algorithm is basically indifferent to units of meaning, but instead searches out patterns of reuse as strings. Methodologically, the role of text reuse detection should be similar to that of codicology, in its indifference to meaning, but isolation of features that tell us about transmission – here, chunks of words, rather than manuscript bindings. Like codicology and narrative analysis it belongs in the historian’s toolkit among other tools.



To give a typical example: the historian al-Ṭabarī (d. 310/923) is commonly described as following Hadith methodology in his reporting on historical topics because of the detailed documentation that he provides for his sources. His reporting on the reign of the ʿAbbāsid caliph al-Maʾmūn (r. 198-218/813-833) features courtly intrigue against an important ʿAbbāsid governor, ʿAbd Allāh b. Ṭāhir:



It is mentioned from ʿAṭāʾ, the official charged with hearing complaints for ʿAbd Allāh b. Ṭāhir, who related that one of al-Maʾmūn’s brothers spoke to al-Maʾmūn thus, “O Commander of the faithful, ʿAbd Allāh b. Ṭāhir has an inclination toward the progeny of Abū Ṭālib, just as his father had before him.”



ʿAṭāʾ’s report continues on to quote al-Maʾmūn’s brother proposing a way to catch ʿAbd Allāh b. Ṭāhir in the act of treason (and carries on to show the honesty of the governor).[^3]



What is noticeable from the text reuse data is that al-Ṭabarī takes not just this report, and this story, but from passages nearly verbatim that follow it, all from an unacknowledged predecessor, namely Ibn Abī Ṭāhir Ṭayfūr (d. 280/893 on which, see *IJMES*, Feb. 2018  pp. 135-39). This means, we cannot rely on al-Ṭabarī’s crediting ʿAṭāʾ.[^4] Al-Ṭabarī’s eye is not on this report specifically, but something larger. To know this, we need to be able to read al-Ṭabarī’s text alongside that of Ibn Abī Ṭāhir. An isolated instance like this could be noted manually (often by pure luck), but what KITAB allows is work like this on a completely different scale and independent of isnads (chains of transmitters).



Similarly, a leitmotif in early hadith transmission relates to a compiler traveling the world in search of reports. There is typically an assumption that such collectors sifted through these reports one by one, or if in larger units, that their primary focus was on the individual report (or on “collective isnads”).[^5] But were Hadith and Sira transmission so atomistic? We need to see, and can use text reuse data alongside current and innovative methods reliant on isnads and specific reports.



There are many cases to consider. For example, an early collection attributed to Hammām b. Munabbih (d. 101 or 102/719-20). Scholars have noticed for some time its close relationship to the *Musnad* of Aḥmad b. Ḥanbal (d. 241/855), and also argued, persuasively, for its 9th century origins (see, e.g., Ian D. Morris’s 2014 [blog](http://www.iandavidmorris.com/how-early-is-the-sahifah-of-hammam) ). The text reuse data can be added now, with 58 records of reuse in our first data set.[^6] The records mostly follow in order; this would seem to be reuse on a scale larger than the report.



We find many other cases with Aḥmad’s *Musnad*. For example, Abū al-Qāsim al-Ṭabarānī (d. 360/961) reportedly traveled for some 30 years learning and collecting hadiths from a large number of masters in the course of a *riḥla fī ṭalab al-ʿilm*.[^7] Our data turns back more than 3,700 records of common passages between between his *Muʿjam al-kabīr* and the *Musnad*, many that occur in order, as our data visualisation shows.



![Image](/images/old_posts/Ahmadblogimage-3-300x102.png)



**Graph 1**: Aḥmad b. Ḥanbal’s *Musnad* is laid out on the x-axis on the top in 100-word segments, and al-Ṭabarānī’s *al-Muʿjam al-kabīr* is laid out similarly in the bottom graph. The yellow lines represent where our algorithm, passim, detects common passages of texts. The consecutiveness of reuse suggests reuse of chunks of material.



Indeed, the *Musnad* of Aḥmad is the most “reused” book in the current OpenITI corpus. To underscore a point I frequently make: we have a pattern here. The route of transmission requires closer investigation (e.g., direct or through common sources, for example). It was no doubt complex, and not a simple case of al-Ṭabarānī copying out sections of the *Musnad w*ord for word. Indeed, the many books that share arrangements with the *Musnad* are suggestive of complex networks of closely linked texts (as indeed the metanarrative underlying Hadith transmission would hold). But to see such patterns, the unit we need to now investigate is not the solo report, but rather something much bigger.[^8]



Reading for such patterns will require us to develop ways to assess the “edit distance”[^9] between texts and also ways to quantify the consecutiveness of reuse. The narrow goal should be to find where common passages begin and end in specific cases. But the wider aim of such a textual forensics is to discern the norms governing different types of transmission, and how authors negotiated them to make new meanings.



[^1]: See Hirschler, *Medieval Damascus* (2016), esp.68ff, and 134; for literary forms, there is extensive scholarship; for excerpts specifically see, e.g., Muriel Debié, “L’historiographie tardo-antique: une littérature en extraits” in Sébastien Morlet, ed., *Lire en extraits; Lecture et production des textes de l’Antiquité à la fin du Moyen Âge* (2015).



[^2]: For instance, on form and narrative structure (e.g., in “[The Use of Composite Form in the Making of the Islamic Historical Tradition,](https://www.orient-institut.org/fileadmin/CV/Leder_Composite_Form.pdf)” by Stefan Leder, in *On Fiction and Adab*, 2004, pp. 125–148) and for sophisticated methodologies, e.g., Harald Motzki, Nicolet Boekhoff-van der Voort and Sean Anthony in *Analysing Muslim Traditions (*2013).



[^3]: *History of al-Ṭabarī* vol. 32 (Albany, 1987), vol. 32, pp. 169ff (C.E. Bosworth trans.).



[^4]: In fact, Ibn Abī Ṭāhir has instead: “Al-Ḥarrānī told me: It is mentioned from ʿAṭāʾ.” In other words, al-Ṭabarī has omitted as sources both Ibn Abī Ṭāhir and this al-Ḥarrānī. Print edition: Ibn Abī Ṭāḥir, *Taʾrīkh Baghdād* (Beirut, 2009), p. 183ff; see also 2 digitized versions [here](https://github.com/OpenITI/0300AH/tree/master/data/0280IbnTayfur/0280IbnTayfur.Baghdad).



[^5]: For a summary of the phenomenon, see Chase Robinson, *Islamic Historiography* (2003), p. 97; also Fred Donner, *Narratives of Islamic Origins* (1998), pp. 264-65, esp. n. 31. For another, parallel consideration of units of citation, Antoine Borrut, *Entre mémoire et pouvoir* (Leiden, 2011), pp. 21ff.



[^6]: Dataset accessed on 24/4/2018 (books with 100 word chunking). Entry point: *Musnad*. Filtered for all matches with 50 records or more. Ordered, by date, with the *Ṣaḥīfa* as the earliest work on the list (58 records). *Musnad* edition: Cairo: Muʾassasa Qurtuba, n.d.; *Saḥīfa* edition: Beirut, ʿAmmān: Maktab al-Islāmī, 1987; edited by ʿAlī Ḥasan ʿAlī ʿAbd al-Ḥamīd.



[^7]: See Maribel Fierro, “al-Ṭabarānī,” *Encyclopaedia of Islam*, second edition.



[^8]: For an earlier study on Hadith reuse and the Digital Humanities, see Maxim Romanov’s [“Ḥadīṯ Reports](http://www.orientalstudies.ru/rus/images/pdf/a_romanov_2009.pdf) in Ibn al-Ǧawzī’s (d. 597/1201) System of Argumentation (Based on His *Talbīs Iblīs* \[“Devil’s Delusions”\]),” in *Khristianskii Vostok/Christian Orient*, 2003/2009, pp. 310–16 (in Russian).



[^9]: In Computer Science the term is used to refer to the way of quantifying how dissimilar two strings (of words) are to one another by counting the minimum number of operations required to transform one string into the other.


































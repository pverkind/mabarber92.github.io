---
header:
  image: 
  caption: 
title: "When al-Tabarī is Not (Just) al-Tabarī: The Challenges Posed by Composite Editions in the OpenITI Corpus"			
author: mathew_barber		
layout:		single
categories:
  - 
  - 
tags:
  - 
---




In the past few months the KITAB team have been closely studying the issue of versioning and composite editions in the OpenITI corpus. The problem of versioning is as follows: For many of the texts in the corpus we possess multiple versions, often based on various editions. Take, for example, al-Tabarī’s *Kitāb al-Taʾrīkh*, for which there are 5 versions, based on 3 editions. A closer study of the data by Sarah Savant has shown that these versions can sometimes vary greatly in length. Moreover, the passim outputs suggest that some of these versions vary hugely in content (in extreme cases, the passim results suggest that they might be entirely different works).



This problem relates in part to the existence of composite editions in the corpus. Some of the works in the corpus identified as one book might in fact be several different works collected into one book. For example, if for book X, version A is shorter than version C and version C shares only some of its content with version A, it is possible that version C contains all or part of book X plus another work (see figure 1 below). There are two ways in which these composite editions can come into being: 1 they were assembled in the original manuscript, 2. They were assembled by the editor.



* ![Image](/images/old_posts/compositeedition-1024x610.jpg)*



The existence of composite editions poses an intellectual challenge as much as it does a practical one. The structure of the OpenITI corpus favours single works written by single authors: the github repositories are ordered by death date of an individual author, then by author, then by work. In such a structure, how does one practically categorise a work that is composed by two authors or that is a composite of two works? One answer is to split the books into their pieces, and then categorise each piece by its respective author. Such a response is bound to excite intellectual tensions. If the two works were brought together in a manuscript, then surely separating them is ignoring a valuable stage in the intellectual and transmission history of those two books? We must remember, that a key component of KITAB’s research is the study of the transmission and reuse of Arabic text. Passim outputs have identified that 21% of Ibn al-Athīr’s *al-Kāmil fī al-taʾrīkh* is from al-Tabarī’s *Kitāb al-Taʾrīkh*, but we would not use this as justification for separating al-Tabarī’s *Kitāb al-Taʾrīkh* from Ibn al-Athir’s work.



Separating works assembled by a modern editor would appear more easily justifiable. However, in the context of a Virtual Reading Room (VRR), such as that produced for the Digital Sira Project (DSP), even this poses difficult questions. If in the Reading Room we state that the digital text is based on a certain edition, then our readers might reasonably expect to find everything that is in the original edition. In fact, KITAB’s current mARkdown policy is to preserve the editor’s structural decisions, and why should their choice of works be an exception? In short, the question of composite editions reaches into the very heart of what we mean by a book and what we mean by book history.



Until recently, I could participate in these debates from the blissful vista of my ivory tower, an engaging intellectual discussion among the many that we have in the KITAB team. Then when assembling data for al-Tabarī’s *Kitāb al-Taʾrīkh* for the VRR, I made a discomfiting discovery. As the VRR is concerned with the *Sira* of Ibn Ishaq, one rarely ventures beyond the first three volumes of the *Kitāb al-Taʾrīkh.* However, the entirety of the work will appear in the VRR and so the contents pages need to be easy to navigate. As I scrolled through the contents list, one title stood out: ‘Then began the year 380 (AH)’. Al-Tabarī died in the year 310 AH, so unless he had a lesser-known side-line in time travel or prophecy, this could not possibly have been written by him. It, of course, transpired that it was not. In fact, the edition we had chosen for the Digital Sira Project had three additional works added to the end (two continuations of al-Tabarī’s history plus another of al-Tabarī’s works). Now we shall have to decide: should all these texts appear in the VRR? If so, how? As a separate work, or clearly indicated in the contents pages for al-Tabarī’s *Kitāb al-Taʾrīkh*?



We have been working intensely with al-Tabarī’s *Kitāb al-Taʾrīkh* for over 6 months and no one on the Digital Sira Project team had spotted it was a composite edition. The oversight illustrates the very scale of KITAB’s endeavour. Al-Tabarī’s *Kitāb al-Taʾrīkh* is a large work, and we are working intensely with only the *Sira* portions of it. Moreover, the additional 3 texts are comparatively short, so the word-length of the version did not appear to be suspect (there are many reasons word counts might differ, many of them benign, such as writing out of dates – which over the course of a million-word work, can really add up the words).



This discovery underlines the importance of formulating specific rules and checks to be applied when texts are prepared for addition to the VRR. In fact, one important output of our work to create the VRR is documentation detailing the process follow when selecting and preparing texts. The task of organising the corpus and inserting it into the VRR is certainly, therefore, a mammoth one.



Nonetheless, we are learning much about our corpus from this detailed look at individual texts, and there is something exciting about working with a corpus that can so routinely surprise.





---
header:
  image: 
  caption: 
title: "Tagging the Structure of Texts in the OPENITI Corpus"			
author: hamid_reza_hakimi		
layout:		single
categories:
  - 
  - 
tags:
  - 
---




With currently more than 7,000 titles, collected from a number of huge digital Arabic libraries (al-Jami al-Kabir, [al-Maktaba al-Shamila](http://www.shamela.ws/), [Shia Online Library](http://shiaonlinelibrary.com/), etc.), the [OPENITI corpus](https://github.com/OpenITI) is recognised as one of the most comprehensive Arabic corpora online.



The [KITAB project](http://kitab-project.org/about/) relies on this corpus in its work on text reuse detection (through which the project aims to discover relationships among texts by aligning parts of them that share common wording). In the project’s workflow, a first step is manual tagging of the structural elements of the texts (headings and subheadings, or, for example, the names that order biographical dictionaries). For a complete description of the tags, click [here](https://alraqmiyyat.github.io/mARkdown/). To annotate the texts, we use [EditPad Pro](https://www.editpadpro.com/), a powerful text editor that supports Arabic and can easily handle large texts. Annotators start by collating each machine-readable file with a printed version of the text (ideally using a PDF from the internet, but alternatively, the physical object in a library).



To briefly review the annotating of a text and some of the routine difficulties this involves, let’s have a glance at tagging the first few pages of a typical text in our corpus. Fortunately, the edition of the text in question here – the *‘Iqd al-Farid*, by the author/compiler Ibn ʿAbd Rabbih (d. 328/940) – is both of high-quality and is accessible [online](https://archive.org/details/WAQ82391) (when it is not possible to find the same edition, annotators can use a different edition for collation; however, this needs to be done with care since two editions of the same text may well have a lot of differences). Although at this stage of preparing the text, it is only necessary to tag the structural elements, this process presents its own difficulties and is not as simple as it might seem. For example, in most cases, annotators cannot rely on the books’ table of contents (TOC). This is partly because some structural elements (like individual biographies) do not appear in the TOC. It is also because many published books do not have a TOC. Even when one is included, it may be practically useless for annotation. For example, by comparing the book’s TOC and the human-annotated digital text in figures 1 and 2, it is clear that some of the headings in the text are missing in the book’s TOC. Moreover, the book’s TOC does not accurately reflect the way that headings and subheadings are nested within the book itself. The heading titles are all presented as if the logic is parallel (except *Kitab al-Lu’lu’a* which is bold), whereas some of them are obviously subordinated to others. In addition, some empty header tags should ideally be added to make the structure coherent. As is evident in figure 3, the author jumps to mentioning the holy wars (*ghazawat*) of one of the Umayyad caliphs in Andalusia without any heading specifying this shift.



![Image](/images/old_posts/HR-1.png)



**Figure 1**: The book’s table of contents.



![Image](/images/old_posts/HR-2.png)



**Figure 2**: The human-annotated text. The level of headings are shown by the number of pipe symbols (\|) in EditPad Pro, and the colors change accordingly.



![Image](/images/old_posts/HR-3.png)



**Figure 3**: Empty header tags should be added in appropriate locations to make the structure of the text coherent



So, to present a useful annotation, annotators need to collate each page with a printed version in order to avoid missing headings, while at the same time exercising judgement about the relationship between headings and subheadings. When you consider that there are on average 2 headings per page in this text, for example, it is clear that the process of tagging can be extremely tedious, while at the same time more intellectually challenging than the mechanical task it may initially appear to be. This is particularly in cases where the annotator has to deal with editions where the structure is poorly marked out or work on dictionaries or biographical collections which include thousands of entries or names all of which need to be tagged (figure 4).



![Image](/images/old_posts/HR-4.png)



**Figure 4**: A biographical collection including more than 4000 name entries of men and women tagged separately.



Each digital text is accompanied with a series of yml files. Figure 5 shows a yml file in which annotators keep track of their annotation by recording all relevant information. This includes providing a link to the PDF, links to both the edition of the digital text and the edition of the collated text in [Worldcat library](https://www.worldcat.org/), and any other explanation that is necessary for reviewers. All issues of the digital version (pagination problems, entering HTML tags into the text, redundant or missing parts, etc.) must also be reported in this file so that they can be fixed at a later stage. We also log the contents of the yml files as ‘issues’ on Github so that reviewers double-check the texts at the next step. After vetting, these issues will be closed (click [here](https://github.com/OpenITI/Annotation/issues) to see the latest issues for annotated texts on our project).



![Image](/images/old_posts/HR-5.png)



**Figure 5**: A yml File



To summarise, annotators must face the probable shortcomings caused by the actors in the text production circle. This circle consists of two groups: one, the producers of the digital texts, and two, the producers of the printed versions including the publishers, editors, and medieval writers. On one side, there might be some problems in the digital texts because they are produced by various research institutions and for a variety of different purposes. These institutions may either intentionally change the structure of the texts by adding or deleting the headings (to adapt the structure to their intended purposes), or unintentionally make mistakes. And on the other side, lacking TOC, faulty TOCs, or the inability to find and present the correct structure of the text are some of the problems related to publishers and editors. Even medieval writers can sometimes be another bugbear as in many of their writings the thematic classification is so haphazard that annotators must spend a lot of time to understand the structure of a text they are working with. Each text usually brings unique difficulties that must be dealt with in a different way and our team is working hard to present the most accurate form as possible for these texts. To date, 550 texts have been tagged and more are in progress. Everything is open access on our corpus and we have a search engine to help you browse through all the texts in the corpus (both annotated and not-yet-annotated). Click [here](https://kitab-corpus-metadata.azurewebsites.net/) to start browsing!






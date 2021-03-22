---
excerpt:	"Knowledge, Information Technology, and the Arabic Book"
header:
  overlay_image: /images/covers/kitab2.jpg
  overlay_filter: rgba(0, 0, 0, 0.45)
  caption: "**Photo credit**: From Book three of 'Nihāyat al-su’l' which gives instructions on using lances. Dated 773/1371 (Add. MS. 18866, f. 113r)"
title:		"Text Reuse Methods"
author:		sarah_savant
layout:		single
author_profile: true
permalink: /methods/
---

![full](/images/kitab/textalignment.png)
{: .full}

{% include toc icon="gears" title="Table of Contents" %}


Existing search engines that accompany common domain Arabic editions or databases currently offer no way to automatically detect reuse, such as quotation, paraphrase, or allusion.

There is no one-size-fits-all algorithm to perfectly detect text reuse—it is very different to look for and visualise rare similarities versus rare differences between texts and across corpora. To detect text reuse and to graphically display it in the most illuminating ways, programmers design algorithms differently, depending on the types of reuse being investigated.


![image-right](/images/kitab/textreuse.jpg){: .align-right}
# About passim

Our aim is to analyse patterns of reuse in a large collection of texts for the period of 700–1500. This will help us  to identify which texts—or which traditions of similar texts—were widely quoted over the centuries, or which sources a given historian might have used, or which books and passages were most widely commented on. If we knew, hypothetically, that we were going to focus on a particular book—e.g., al-Ṭabarī’s Taʾrīkh—we might make do with an existing full-text search engine. [Read more…](about-passim.md)


# Use Cases

KITAB’s team is developing algorithms to investigate the following types of reuse in Arabic.

**Discover relationships between texts**: We can now filter data to show the highest correlation between one book and any other in the corpus. A user can browse the texts to interpret the scope and context of reuse. *Example*: the texts of a teacher and his pupils. A fragment and its source text (see *Research* section in [*About the Project*](../about/) for an example of such a discovery).

**Explore the make-up of complex texts**: A user starts with a complex text, built out of earlier texts, and uses this function to trace how the diverse elements were combined and amalgamated. *Examples*: anthologies (e.g., of poetry). Multi-text compilations (in Arabic, *majmūʿāt*), sometimes classified as miscellanea by cataloguers.

**Chart the diffusion of texts**: A user investigates the reception of a single work across many other, later works. *Example*: how a classic was copied in subsequent times, locations, or genres.

**Read for fine differences**: A user identifies two or more texts and queries the alignment between them, which highlights slight word variations, paraphrase, etc. *Example*: two editions of the same work; a book and its abridgements or extensions.

**Collect common passages**: A user wishes to search across the corpus for common narratives defined to allow for paraphrase. The programme brings together textual units and orders them using metadata pertaining to date, geography, statistical correlation, or other factors. Users can see the patterns graphically. *Examples*: a section of a book treating an event, compared to other treatments that use common phrasing; administrative formulae in different works.

# Statistics

We measure the length of reuse by the number of records (instances of reuse detected by `passim`), the number of words in instances, and by the degree of overlap between books, expressed in percentage terms.

We also calculate precision. A traditional computational approach to measuring change (and thus movement away from precision) is an edit-distance calculation, whereby the edit distance between two strings of characters is the number of transformations necessary to mutate the first string into the second. Passim employs this for the purpose of pruning un-interesting records. For now, in our data analytics, we measure precision for each record and on a character basis. We factor only the closeness between actually matching blocks of text.

Data on reuse is collected for the entire corpus. We are studying specific cases and also reuse in the aggregate (through `Power BI` and `R`).

Insofar as citation goes, we have no way yet to discern computationally acknowledgment of a previous source. We consider this issue through close reading. It is important to consider citation alongside our data.

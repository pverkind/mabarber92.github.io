---
excerpt:	""
header:
  overlay_image: /images/covers/kitab2.jpg
  overlay_filter: rgba(0, 0, 0, 0.45)
  caption: "**Photo credit**: From Book three of 'Nihāyat al-su’l' which gives instructions on using lances. Dated 773/1371 (Add. MS. 18866, f. 113r)"
title:		"Text Reuse"

layout:		single

permalink: /methods/text-reuse
sidebar:
  nav: "methods"
toc: true
toc_sticky: true
---

## Introducing passim

The KITAB team’s main digital method is text reuse detection. We use text reuse to refer to cases where text is shared verbatim between works. The meaning of text reuse is subject to interpretation and it can be used to investigate a variety of research questions. For example:

SOME EXAMPLES

The text reuse algorithm used by KITAB is called passim. The algorithm naively identifies reuse by looking for instances of shared text that meet a certain set of criteria (for example, that instances are above a certain number of words long; that instances of shared text are separated only by a certain number of words or less). This means that text reuse detected by passim might suit certain research questions better than others. If you are interested in cases where an author largely paraphrases from a work, then passim is unlikely to be helpful (or it will, at least, only provide some of the picture). If one is interested in how certain phrases are shared among a large collection of words, then passim might need a specific set of parameters.

## How does passim work?

Put simply, there are two stages to passim’s operation. In the first stage passim is given a corpus of ‘documents’, relatively short texts. Passim takes each one of these documents and compares it to every other document in the corpus. If passim finds text shared between two documents that meets a set of criteria (parameters, which can be customised to better suit the corpus), it sets those documents aside. 

In the second stage, passim compares each document pair using a well-used alignment algorithm called Smith-Waterman. This algorithm takes each document character-by-character and decides if a character in one document matches a character in the other. Spaces are inserted where characters do not match. The result is an alignment like the one given in the table below.

ALIGNMENT IMAGE  

Passim was developed by David Smith and his team for detecting instances of text reuse in a large corpus of nineteenth-century American newspapers. In this case passim treated each newspaper article as a document for comparison (meaning that each compared document was around 2000-words or less).

This was inappropriate for the texts in KITAB’s corpus for two reasons. Firstly, the texts in the OpenITI corpus are typically very large. Secondly, text that is reused between works in the OpenITI corpus is often rearranged. KITAB, therefore, pre-processes the OpenITI texts prior to running passim, splitting them into 300-word chunks (termed milestones - marked by ms and a number in OpenITI texts). Each milestone is then treated by passim as a document.

In practice, therefore, KITAB splits every text into 300-word chunks. Passim compares every 300-word chunk of each text to every other 300-word chunk of every other text and identifies chunks where text is shared. Smith-Waterman is then used to create alignments from those chunks.

Ryan Muther has developed with KITAB a separate approach to running passim for KITAB’s texts, which we term aggregation. Sometimes text reuse might run over the edge of milestone boundaries. In these cases, some reused text that sits at the edge of milestones might be missed. Aggregation reassembles the milestones in these cases to create larger alignments that better represent the full reuse between the two texts.

Depending on the type of analysis or visualisation, normal or aggregated passim data might be more useful and so we produce data for both.

## What does our passim data look like?

The result of the above process is one csv file for each pair of texts, where each row represents an individual alignment. We create two sets of data, normal and aggregated.

This individual alignment files can then be viewed used KITAB’s alignment reader, which helps us to visualise how text is shared between a pair of texts.

IMAGE OF PAIRWISE

From these alignments we also compute statistics for each book (again both for normal and aggregated data) that show, for example, what proportion of each work is shared with another work and how many words are shared between two texts. This statistical data is fed into a PowerBI application and it is also used by team members to investigate research questions.

## Improving passim

As can probably be seen below, there are a number of decisions that are made when running passim on the whole corpus. We have chosen to split our texts into 300-word chunks (rather than say, 100). We also choose a set of parameters that we think best allows text reuse to be identified in classical Arabic.

These decisions are subject to constant review, and we are producing alignment datasets that have been checked by team members to test and experiment with new parameters and approaches. 

<div class="notice--primary">{{ "
## Passim FAQs

### When does KITAB run passim and can I access the data?

### Can I run passim?
" | markdownify }}
</div>
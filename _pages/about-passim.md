---
excerpt:	""
header:
  overlay_image: /images/covers/kitab2.jpg
  overlay_filter: rgba(0, 0, 0, 0.45)
  caption: "**Photo credit**: From Book three of 'Nihāyat al-su’l' which gives instructions on using lances. Dated 773/1371 (Add. MS. 18866, f. 113r)"
title:		"About passim"
author:		sarah_savant
layout:		single
author_profile: true
permalink: /about-passim/
---

# About passim

Our aim is to analyse patterns of reuse in a large collection of texts for the period of 700–1500. This will help us  to identify which texts—or which traditions of similar texts—were widely quoted over the centuries, or which sources a given historian might have used, or which books and passages were most widely commented on.

If we knew, hypothetically, that we were going to focus on a particular book—e.g., al-Ṭabarī’s Taʾrīkh—we might make do with an existing full-text search engine. We could open up a text by al-Ṭabarī, copy each paragraph into the search box, and look at the results. In this way we could analyse which earlier works showed up most often as potential sources, or which later works were frequently quoting passages from al-Ṭabarī’s book. To enter every paragraph, however, from every one of thousands of books as a query in our search engine would take years, even under very optimistic assumptions. In addition, this process would not help us determine a priori all the books that we should mine for queries.  

Instead, the method we use in the KITAB project, which is implemented in the passim software tool, follows an alternate procedure to find all pairs of passages that share some minimum amount of text and to cluster these pairs of passages into larger textual traditions. Given an input collection of texts divided into units, such as chapters, pages, or even paragraphs of a few hundred words — not all books need to have the same level of chunking — passim proceeds as follows:

1. It builds on index of the collection using “high-precision” features, which could be individual words but are usually sequences of consecutive words known as n-grams. A sequence of five consecutive words, i.e., a 5-gram, is more likely to be a distinctive marker than an isolated word. Whether using single words or n-grams, passim removes high-frequency terms—such as “the”, if one were indexing a collection of English works— whose presence would not be likely to distinguish one text from another.

2. For each entry in the index (e.g., all occurrences of a 5-gram such as “be or not to be”), the software outputs all possible pairs of occurrences that come from different books.

3. The software then sorts this list of passages that share a term or an n-gram, and so we can now rank passages by the total number of these features that they share. This allows us to prune away passages with very little overlap.

4. For the pairs of passages that do overlap in a larger number of features, passim uses an alignment algorithm (in this case, the Smith-Waterman algorithm) to count the number of character positions where the two passages match — or differ from each other either, by substituting one character for another, or by adding material to one text or the other.

5. Finally, the software clusters the text passages connected by these pairwise relationships into larger groups, so that if, e.g., some passage in text A aligns to B, and some very similar passage in A aligns to C, all three will be grouped together.

When performing further analysis, members of the KITAB team have used both the pairwise alignments (produced in step 4 above) to explore the relationships between particular books and clusters (produced in step 5) to explore the propagation of particular passages through several works.




---
excerpt:	""
header:
  overlay_image: /images/covers/banner_data.png
  overlay_filter: rgba(40, 99, 165, 0.45)
title:		"About our data"
layout:		single
sidebar:
  nav: "corpus"
permalink: /data
toc: true
toc_sticky: true
---

Our data is created about and from the corpus. This page will provide a basic overview of our main datasets, which feature in our [blogs]({{ '/blogs' | relative_url}}) and other [research]({{ '/research/articles' | relative_url }}). If you want like to explore how these datasets are created, consult our [methods pages]({{ '/methods' | relative_url }}).

Datasets evolve organically as the team works and researches. If we during our research we develop a corpus-level dataset that we believe will be of broader interest to KITAB's research or the research community, then we develop a pipeline for its production. This ensures that the dataset will be kept up-to-date with the corpus as it expands. We recommend you return to this page to keep up-to-date with the data that we are producing.

{% capture release-notice %}
**Please note** Not all of the datasets listed here have been released to the public. This page is intended as guidance to those who are working for us to help understand and interpret our datasets, and as to help those reading our blogs or other research to understand the datasets behind our research. The following datasets have not yet been publicly released:
* All passim datasets
* Isnad related data

We plan to release our datasets to the public soon. Subscribe to our mailing list to be notified when we release data.

<a href='' class='btn btn--primary align-center' >Subscribe for updates</a>
{% endcapture %}

<div class="notice--warning">
{{ release-notice | markdownify }}
</div>

## Corpus metadata

As we have noted in [using the corpus]({{ '/corpus/use#metadata-files' }}), we collect and store metadata about the books and authors in our corpus in yml files. We use this to create a file documenting metadata about all books in the corpus, including details, such as:
* Full book titles
* Author death dates
* The relationships between books in the corpus (for example, if one book is a commentary upon another).

The yml files are being updated as the corpus is annotated. For the moment many fields in the metadata file are populated using the metadata provided by the online libraries from which our texts our taken (such as Shamela). Much of this data is accurate, but as this data has been collected automatically and not been verified by the KITAB team, some caution should be exercised before using it.

The metadata file can be downloaded in one of two places:

1. We publish the metadata file everytime we release the corpus. See our latest [releases]({{ '/corpus/releases' | relative_url }}) to download. This data is tied to the particular release and best if you need to cite a stable corpus. On the *stable* versus the *changing* corpus, see our guide on [using the corpus]({{ '/corpus/use#which-corpus' | relative_url }}).
2. To access the latest metadata, updated with the corpus. Visit the [corpus metadata page](https://kitab-corpus-metadata.azurewebsites.net/) and click 'Excel' or 'CSV' to download the latest metadata file for the whole corpus.

{% capture meta-help %}
**Please note** corpus metadata can only be produced by hand, and producing high-quality metadata requires much time and effort. It is however essential for certain types of analysis of the corpus. If you find that metadata relevant to works in your field is out-of-date or erronous, please consider helping us by bringing it up-to-date.

<a href='{{ '/about/get-involved' | relative_url }}' class='btn btn--primary align-center' >How to get involved</a>
{% endcapture %}

<div class="notice--warning">
{{ meta-help | markdownify }}
</div>

## Passim text reuse datasets

We produce two types of passim dataset: **normal** and **aggregated**. The **normal** dataset uses passim alignments based on the milestones (the logical chunks that we use to run passim). In this dataset large alignments might be split across multiple milestones. The **aggregated** dataset takes large alignments the cross milestones and brings them together into one alignment. For more detail on the distinction between the two datasets and why we continue to produce both, see our [page on text reuse]({{ '/methods/text-reuse' | relative_url }}).

The **normal** dataset is good for visualisation because the each alignment can be referred to based on its milestone position, which corresponds uniformly to a 300-word chunk of the text - many of our vizualisations put the milestone number on the x-axis. The **aggregate** dataset is better for understanding lengthy instances of text reuse.

For both of these datasets there are two forms of data:

### Alignment files

If passim identifies text reuse between two books, a file is produced. A separate file is produced for both the **normal** and **aggregated** datasets. The file name takes the format of *bookid1_bookid2*. (On book IDs and the way we name the books in our corpus, see our page on [using the corpus]({{ 'corpus/use#uri-structure' | relative_url }}).) The file recording alignments between Ibn Hisham's *Sira* and al-Tabari's *Taʾrikh* would, therefore be:

Shamela0009783BK1-ara1.completed_Shamela0023833-ara1.completed.csv
{: .notice--primary}

For ease of identifying text pairs, we produce each alignment file in both directions, so:

Shamela0023833-ara1.completed_Shamela0009783BK1-ara1.completed.csv
{: .notice--primary}

Would be a flipped version of the same file.

In each file, each row gives an alignment between the text pair, recording the aligned text (aligned using [Smith-Waterman]({{ '/methods/text-reuse#how-does-passim-work' | relative_url }})), the location of each alignment in the book and some statistics about each alignment. For detailed guidance on the data fields, see our [docs]().

The main difference between the alignment files for **normal** and **aggregated** is that the location of **normal** alignments is given as a milestone, where for **aggregated** a milestone range is provided.

### Passim text reuse statistics

From the alignment files we calculate statistics about text reuse in our corpus. In the passim statistics file, each row documents the relationship between pairs of related books, documenting, for example (for a full outline of the data fields, see our [docs](): 
* How words are shared between the book pair.
* What percentage of one book is shared with the compared book.

There are two types of statistics file: **mono-directional** and **bi-directional**. **Mono-directional** lists each book pair once. In this file it is entirely random whether a particular book is listed as book 1 or book 2. **Bi-directional** data is produced by taking the **mono-directional** dataset and adding flipped versions of the book pairs. It, therefore, effectively contains a duplicate of each book relationship.

Although it might sound like **bi-directional** data distorts our text-reuse statistics, it is essential for certain kinds of analysis. For example, if one wishes to document how text reuse changes over time, with the date on the x-axis, then the **bi-directional** data makes it easy to record plot both sides of the relationship on a graph.

Caution should be exercised, however. Any kind of summary statistics calculated on the **bi-directional** dataset will possibly be distorted because each book pair is recorded twice. When using the data, think carefully about which dataset will best suit your needs.

We produce text reuse statistics for both our **normal** and **aggregated** data.

**Please note** Our passim statistics files are enormous and grow with every expansion of the corpus. Bi-directional datasets now exceed 1 gigabyte in size. This data is too large to be used in most spreadsheet software (such as excel) and working with the raw data will require some knowledge of PowerBI or scripting in languages like Python. Our recommended route for exploring the passim statistics is our PowerBI statistics application, which we will soon release on the [application portal]({{ '/data/apps' | relative_url }}).
{: .notice--warning}


## *Isnad* classifier datasets

When we run the [*isnad* classifier]({{ '/methods/sub-genre#automatic-isnad-detection-our-first-case-study' | relative_url }}), we produce typically produce three types of dataset: 

1. *Isnad*-tagged texts (texts with tags for the beginning and end position of *isnads* tagged inside them).
1. *Isnad* position files - which record for each text the location of *isnads* in the text relative to the structural annotation.
1. Whole corpus statistics - a file recording the number of *isnads* in each text and the percentage of each text that is *isnads*.

At present, unlike for the text reuse data, we do not routinely create *isnad* data for the whole corpus, but plan to develop a pipeline in the future, as we move to use *isnad* data more routinely in our research.

## Other experimental datasets

In addition to these datasets, we routinely produce datasets to guide our research or improve our digital methods. To explore these datasets, it is best to read our [blogs]({{ 'data/blogs' | relative_url }}). If you have any questions about those datasets and think you could help, we encourage you to contact the specific blog authors.


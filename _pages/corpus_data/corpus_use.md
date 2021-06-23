---
excerpt:	""
header:
  overlay_image: /images/covers/kitab2.jpg
  overlay_filter: rgba(0, 0, 0, 0.45)
  caption: "**Photo credit**: From Book three of 'Nihāyat al-su’l' which gives instructions on using lances. Dated 773/1371 (Add. MS. 18866, f. 113r)"
title:		"Using the Corpus"
layout:		single
sidebar:
  nav: "corpus"
permalink: /corpus/use
toc: true
toc_sticky: true

---

## Which corpus?

KITAB corpus exists in two forms. On the one hand, there is the *ever-changing corpus* that reflects our ongoing work and which we manage via [GitHub](https://github.com/OpenITI). We constantly add new texts and/or metadata, annotate texts, occasionally rename or delete files, remove parts from our text files that do not belong to the text properly speaking, and so forth.
 
It is this changing corpus whose texts and metadata files can be identified, accessed, and downloaded individually both though OpenITI [GitHub](https://github.com/OpenITI) and through our [metadata search application](https://kitab-corpus-metadata.azurewebsites.net/).

As regards this *changing corpus*, it furthermore constitutes the main interface and point of contact between KITAB and the public. Any user of our corpus with a GitHub account is able to [submit issues](https://github.com/OpenITI/Annotation/issues/new/choose) with regard to our text and metadata files.

On the other hand, we release unchanging *instances* of our corpus through Zenodo twice a year (for the latest releases, see [here]({{ '/corpus/releases' | relative_url }})). These instances are tantamount to “snapshots” of the entire corpus at a particular point in time. They correspond to *stable versions of the corpus* and remain available for download indefinitely.
 
These stable versions of our corpus are not only necessary to generate the specific data sets mentioned further above, but also, more generally, ensure the replicability of the results of research based on our corpus, the consistency of the assertions made with regard to it, and the citability of our texts.

**It is upon each user to decide which corpus they want to use, and their choice will depend on their needs, their goals, and also the level of collaboration with KITAB they are interested in.**
{: .notice--primary}

## Finding files in the KITAB corpus

Finding texts and metadata files in the KITAB corpus requires understanding how it is structured and organised. To make things a bit easier, we organise our corpus in such a way that it readily makes sense to the human mind. 

Perhaps, it is best to imagine the organisational structure of the corpus by thinking of a physical library and its rows of shelves.

Once filled, all the rows of shelves taken together will correspond to our entire corpus. But according to which logic do we distribute the books over those rows of shelves? Which book sits where and why?

KITAB stores text files and corresponding metadata files as a series of Github-repositories that group the authors according to their year of death in groups of 25 lunar years.

Thus, all authors who died in the years 0 to 25 according to the Hijri calendar are grouped together in one repository named 0025AH; all authors who died between 26 and 50 according to the Hijri calendar are grouped together in a repository named called 0050AH, and so forth. Consequently, KITAB corpus consists of about 60 such repositories, which correspond to the most encompassing organisational unit of our corpus.

In our imaginal library, each of these repositories containing the works of authors who all died within the same 25 year span would correspond to a row of shelves, each consisting of separate book-cases reserved for the individual authors.

For example, walking down the aisle of our library, we would stop at the row of shelves which says “0750AH” to search for books by al-Dhahabī who died in the year 748 AH; we would stop at the row of shelves which says “0425AH” to search for books by al-Tawḥīdī who died in 414 AH, and so forth.

On each author-book, a specific place is reserved for each book written by the author in question. For example, on the top board, there are all books that contain work A. Second from top, there are all books that contain work B, and so forth.
 
For example, in our imaginal library, the shelf reserved for Abū Ḥayyān al-Tawḥīdī would have five different boards reserved for five different works by al-Tawḥidī, and it is one those boards on which the actual books sit.

Within the structure of the KITAB corpus, the shelf reserved for a particular author corresponds to the author-folder, and the boards reserved for the individual works written by that author correspond to the book-subfolders within the author-folder.

To remain with the example of al-Tawḥīdī, in the [author-folder reserved for Tawḥīdī](https://github.com/OpenITI/0425AH/tree/master/data/0414AbuHayyanTawhidi) (= the “shelf”), there are five subfolders ( = the “boards”), each of which contains all versions which we have of the respective work (= the actual files).

Thus, in the [book-subfolder reserved for al-Tawḥīdī’s Akhlāq al-wazīrayn](https://github.com/OpenITI/0425AH/tree/master/data/0414AbuHayyanTawhidi/0414AbuHayyanTawhidi.AkhlaqWazirayn), there are two concrete text files that actually contain the work ([JK009310](https://github.com/OpenITI/0425AH/tree/master/data/0414AbuHayyanTawhidi/0414AbuHayyanTawhidi.AkhlaqWazirayn), [Shamela0012541](https://github.com/OpenITI/0425AH/blob/master/data/0414AbuHayyanTawhidi/0414AbuHayyanTawhidi.AkhlaqWazirayn/0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541-ara1.completed)).

Although the comparison is necessarily weak, just as in a physical library, where we would have to walk down the aisle until we find the appropriate row, then go to the appropriate shelf, then search for the appropriate board and finally the the book we are looking for, KITAB corpus has a comparable logic of finding the individual files:

We first must “walk” to the appropriate 25-year repository, then to the author-folder, and then to the book folder, and this is where we finally will find the concrete text file we are looking for.

Whenever, in a physical library, we would be looking for the next-level organisational unit (row, shelf, board), we are moving to the next-level folder within a 25-year repository of our corpus.

## URI structure

Several pieces of information are required to locate a file in our corpus: A date of death in the Hijri calendar; an author’s name; a book title; and information about which concrete version of a book we are talking about.

The key element which integrates all of these pieces of information and ensures the necessary organisational consistency of our corpus, is the unique resource identifier (URI) (for details, see here). 

All files in our corpus are assigned such a URI which conforms to the following pattern: 

AuthorID.BookID.VersionID-ara1
{: .notice--primary .text-center}

There are three central components here, separated by a dot: 

**AuthorID:** The AuthorID consists of an author’s year of death according to the Hijri calendar plus that part of an author’s name under which they were most commonly referred to, i.e., their shuhra (e.g., 0414AbuHayyanTawhidi). For each author in our corpus, there is exactly one AuthorID.
{: .notice--primary} 

**BookID:** The BookID consists of a component of the book title sufficiently distinct to make it recognisable (e.g., AkhlaqWazirayn). For each work in our corpus, there is exactly one BookID.
{: .notice--primary}

**VersionID:** The VersionID uniquely designates a particular text file in our corpus. It always consists of a first part which indicates its origin and a second part which always is a number. The first part can refer to an online library such as “Shamela,” the acronym of a partner project such as “GRAR,” the initials of an individual who made a significant contribution to the text file, or the OCR tool used by us such as “Kraken” (e.g., the versionID Shamela0012541 identifies the Shamela version of Abū Ḥayyān al-Tawḥīdī’s Akhlāq al-wazīrayn in our corpus.). For each version of a work in our corpus, there is exactly one versionID. VersionIDs allow accommodating multiple versions of the same text. The addition -ara1 indicates that the work is in Arabic.
{: .notice--primary}

The full URI of the Shamela version of Abū Ḥayyān al-Tawḥīdī’s Akhlāq al-wazīrayn in our corpus thus would be: 

0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541-ara1
{: .notice--primary .text-center}

In contrast to AuthorID and BookID, which occasionally need to be corrected as they store minimal metadata that may contain errors, the versionID is assigned to a work at the moment it becomes part of our collections and stays with it forever. (The versionID alone thus allows identifying any work in our corpus univocally, which is why we occasionally use it as a shorthand for the full URI.)

Now, URIs not only serve as unique identifiers for the individual text files in our corpus. Rather, their individual components are also used for naming the author and book subfolders.

In fact, if we remove the versionID from the URI, the combination of AuthorID and the BookID may be used as a unique work identifier. Likewise, if we remove the versionID and bookID, we are left with a unique author identifier. 


0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541|Unique Resource Identifier
0414AbuHayyanTawhidi.AkhlaqWazirayn|Unique Work Identifier
0414AbuHayyanTawhidi|Unique Author Identifier
{: .notice--primary .align-center}

KITAB consistently uses the unique author identifiers and the unique work identifiers to name the subfolders found in the 25 year repositories. The unique author identifiers thereby serve as the names for the author-subfolders; the unique work identifiers serve as the name for the book subfolders.

That is, whenever two (or more) of our identifiers overlap with regard to the next higher component of the identifier, they are put into a hierarchically higher folder which carries the name of the overlapping part. 

<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:red">AkhlaqWazirayn</span>.JK009310-ara1\
<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:red">AkhlaqWazirayn</span>.Shamela0012541-ara1\
<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:blue">Basair</span>.JK009288-ara1\
<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:blue">Basair</span>.Shamela0026423-ara1
{: .notice--primary .text-left}


## Metadata files.

As has been indicated further [above]({{ '/corpus/about' | relative_url}}),the KITAB corpus does not contain plain text files, but also *.yml metadata files.

There are three kinds of metadata files in our corpus that reflect the three types of identifiers contained in our URIs:

There are **author metadata files** named after the unique author identifier (e.g., 0414AbuHayyanTawhidi.yml). They allow storing machine-readable information about the author in question as well as non machine-readable free-running comments (for the template, see [here](https://github.com/OpenITI/Annotation/blob/master/templates_for_metadata/auth_template.yml).
{: .notice--primary}
 
There are **book metadata files** named after the unique work identifier (e.g., 0414AbuHayyanTawhidi.AkhlaqWazirayn.yml). They allow storing machine-readable information about the book / work in question as well as non machine-readable free-running comments (for the template, see [here](https://github.com/OpenITI/Annotation/blob/master/templates_for_metadata/book_template.yml)).
{: .notice--primary}

And there are **version metadata files** that use the unique resource identifier which also identifies the corresponding plain text file (e.g. 0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541-ara1.yml). They allow storing machine-readable information about the concrete version of a work in question as well as non machine-readable free-running comments (for the template, see [here](https://github.com/OpenITI/Annotation/blob/master/templates_for_metadata/vers_template.yml)).
{: .notice--primary}

It is useful to fall back on our imagined library once more: Our metadata files are like sheets of paper we attach to each author-book case, each individual shelf in that book case, and to each of the actual books sitting on the shelves.

Thus, we put an author-metadata file in each author-subfolder which stores machine-readable information about a particular author.

We put a book-metadata file in each book-subfolder which stores machine-readable information about a particular book / work.

And we accompany every text file with a version-metadata file that stores machine-readable information about the concrete version of a work contained in a particular text file.

As has been indicated further before, we mostly fill in our metadata files during the course of subprojects, that is, at present, not all of them contain information. 

## Two ways of searching for files in the KITAB corpus 
The text and metadata files contained in the KITAB corpus can be accessed by everyone and for free.

There are two ways of doing so:
 
On the one hand, by accessing the 25-year repositories accessible at [OpenITI GitHub](https://github.com/OpenITI) and by finding one’s way to the text or metadata file through the relevant folders and subfolders. As has been outlined further above, this requires knowing an author’s date of death as without that piece of information, the appropriate 25-year repository cannot be identified.

On the other hand, files can be accessed by using the [KITAB metadata application](https://kitab-corpus-metadata.azurewebsites.net/) (for further information, see also [here]({% link _posts/2019-11-04-A New Application that Helps You Find Texts in the OpenITI Corpus.md %})).

This second option is preferable as it allows finding files in our corpus without having to know an author’s death date.
 
KITAB’s metadata app allows searching for each of the components of a URI separately (i.e., the AuthorID, the BookID, and the VersionID).

Furthermore, as we do have Arabic metadata for many (but not all) files in our corpus, users can also search for texts in Arabic.

The metadata app allows accessing text files directly by clicking on the versionID column of the app.

Metadata files can be accessed by clicking on the author name or the book title. Doing so takes the user to the subfolders within the 25-year repository on GitHub where the respective *.yml files sit.

<div class="notice--danger">
{{ "**Note on metadata searches:** For searches in Arabic, please note that to write or not to write hamza on alif matters (see the different numbers of results for الأمان/الامان). At present, the Arabic metadata is not entirely consistent in that respect.
 
For searches using transliterated forms, please follow the following rules:

* The Library of Congress scheme is followed in its simplified version, omitting all diacritics so that only ASCII characters are used. Two most problematic Arabic letters are dealt with in the following manner: 1) hamzas are omitted to avoid using non-letter characters; 2) ʿayns are transliterated with c, which is capitalized when appropriate (ʿAlī > Cali; Aʿyān al-shīʿaŧ > AcyanShica).
* (إبن) as part of a name is written in full and capitalized: ʿAlī b. Abī Ṭālib > CaliIbnAbiTalib.
* Although an effort was made to use šuhras for AuthorIDs, in cases when it was not possible, the following formula was followed: Ibn + Ism Abī-hi + Nisbaŧ (these were the onomastic elements most commonly available in the metadata).
* The word kitāb is dropped from the titles, unless it is the major keyword, like in the case of, for example, Sibawayhi’s Kitāb, whose unique identifier is 0180Sibawayh.KitabSibawayh.
* Definite articles are dropped everywhere: Tārīkh al-islām > TarikhIslam.
* Parts of the same entities are written together, in camelcase. In other words, there are no spaces between words, but each word is capitalized: al-Nāsikh wa-l-Mansūkh > NasikhWaMansukh.
* NB: Tāʾ marbūṭaŧs are transliterated as -t in genitive construction, i.e., in iḍāfas." | markdownify}} 
</div>

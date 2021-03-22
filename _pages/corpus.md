---
title:		"Corpus"
excerpt:	"Knowledge, Information Technology, and the Arabic Book"
header:
  overlay_image: /images/covers/kitab2.jpg
  overlay_filter: rgba(0, 0, 0, 0.45)
  caption: "**Photo credit**: From Book three of 'Nihāyat al-su’l' which gives instructions on using lances. Dated 773/1371 (Add. MS. 18866, f. 113r)"
layout:		single
author_profile: true
permalink: /corpus/
---

{% include toc icon="gears" title="Table of Contents" %}

# The Arabic Textual Tradition

The medieval Arabic textual tradition is one of the most prolific in human history. Works were produced across a territory stretching from modern Spain to Central Asia, and their subject matter covered Islam but also much more, from rulers, their courts, and administration to literature, biographies, philosophy, medicine, mathematics, geography, travel, and many other topics.

Some highlights of our collection:

* Approximately 4,200 unique Arabic texts from beginning of Islam up to the early 20th century – covering all genres
* Inclusion of major digital databases from the Middle East – plus additional texts contributed by partner projects
* URIs (uniform resource identifier) for all texts – required for corpus building and data analytics
* Core metadata (author’s name, death date, book title, publisher and year of publication) – with reviews of this data by scholars
* Pre-processing of texts (including tagging) – to facilitate computational analysis
* Recently, KITAB has been working on Arabic-script Optical Character Recognition (OCR) through its partnership with the Open Islamicate Texts Initiative (OpenITI). You can see the results of our work here. Most importantly, our OCR solution, designed by Benjamin Kiessling (Leipzig University), has achieved accuracy rates for classical Arabic texts in the high nineties. We are now in the process of designing a corpus builder that will allow individuals and projects to OCR and post-correct  their own scanned books and to convert them into machine-readable texts.

The system works by training the computer to recognise different typefaces. It involves a substantial investment in a shared database of training data and technical infrastructure that projects can access and feature in their own applications. A test version of the corpus builder is scheduled for completion in late November 2017.

The work is led by the OpenITI team (Sarah Bowen Savant, Maxim Romanov, and Matthew Miller) and is currently being funded by the Roshan Institute for Persian Studies at the University of Maryland, the Alexander von Humboldt chair in Digital Humanities at Leipzig University, the Institute for the Study of Muslim Civilisations at the Aga Khan University, and the Harvard University Law School (through its SHARIASource project). Additional funding is being sought, and collaboration is welcomed from other projects.


# OpenITI / OpenArabic

The *Open Islamicate Texts Initiative* (**OpenITI**, see [iti-corpus.github.io](iti-corpus.github.io)), which is a multi-institutional effort to construct the first machine-actionable scholarly corpus of premodern Islamicate texts. Led by researchers at the Aga Khan University (AKU), University of Vienna/Leipzig University (LU), and the Roshan Institute for Persian Studies at the University of Maryland (College Park) and an interdisciplinary advisory board of leading digital humanists and Islamic, Persian, and Arabic studies scholars, **OpenITI** aims to provide the essential textual infrastructure in Persian and Arabic for new forms of macro textual analysis and digital scholarship. In the process, **OpenITI** will enable new synergies between Digital Humanities and the inter-related Islamicate fields of Islamic, Persian, and Arabic Studies.

You can find the latest report on the development of Arabic part of the project, **OpenArabic**, at the status page: [github.com/OpenArabic/Annotation](https://github.com/OpenArabic/Annotation). **OpenArabic** is an effort that was initiated within the Alexander von Humboldt Chair for Digital Humanities (Leipzig University) to create the first machine-actionable scholarly corpus of premodern Arabic texts.

# Common questions about our Corpus

<details><summary>What does KITAB analyse?</summary>
<p>

We focus on the origins of the written Arabic tradition, in the eighth century, up to roughly the fifteenth century, but aim to include as many texts as possible, so you can also find texts written after 1500.

</p>
</details>


<details><summary>What quality of texts is necessary for computational analysis?</summary>
<p>

It depends on the type of analysis. Regarding OCR, text reuse detection methods can be adapted to detect patterns even with badly OCRed texts (as has been done for studies of 19th-century newspapers). For our OCRed texts, we aim, however, to obtain digital files that match within 1 or 2% the printed editions upon which they are based.

</p>
</details>



<details><summary>Are your texts representative of the historical Arabic tradition?</summary>
<p>

Yes and no. We have a lot of texts. Digitisation efforts in the Middle East over the past twenty years have been extensive and impressive. But equally, we have nowhere near what once existed. The electronic files we have are based on printed editions. Many printed editions have not been converted into machine-readable texts. And many manuscripts have not made it into print.

There are some biases in what we do have and an overrepresentation of works from particular authors and treating particular topics. Texts with religious and legal significance are heavily represented.

A major aim of KITAB is to increase both the number and diversity of texts in our corpus. We seek works treating, for example, philosophy and science.

</p>
</details>


<details><summary>Can I propose additional texts for KITAB?</summary>
<p>

Yes. Please check <a href="https://github.com/OpenITI">
Open Islamicate Texts Initiative</a> to ensure that we do not already have it.

If your text is already available in machine-readable format, we will add it to the corpus.

If your text is not already available in machine-readable format, please add it to our list for <a href="https://t.co/GULp3OmQi9">
books to OCR in the future</a>.

</p>
</details>


<details><summary>How reliable are texts in Digital Format?</summary>
<p>

Our digital texts are generally speaking reliable reproductions of modern printed editions.  We are finding this as we annotate digital files of books and compare them to their printed counterparts.

There are problems with printed editions and the extent to which any edition serves as witness to a historical written work.  One aim of KITAB is to develop our algorithm and text alignment and annotation tools to facilitate comparison between different editions of books. This will help scholars gain a fuller picture of their sources and variations between them. It might also aid in the creation of critical editions.

We will also tackle problems with metadata that arise also in the printed editions. For example, many books are reprinted without acknowledgement to the original editions or their editors. We need to verify bibliographic data.

</p>
</details>

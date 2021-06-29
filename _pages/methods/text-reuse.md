---
excerpt:	""
header:
  overlay_image: /images/covers/banner_methods.png
  overlay_filter: rgba(40, 99, 165, 0.60)
title:		"Text Reuse"

layout:		single

permalink: /methods/text-reuse
sidebar:
  nav: "methods"
toc: true
toc_sticky: true
---

## Introducing passim

The KITAB team’s main digital method is text reuse detection. We typically use text reuse to refer to cases where text is shared verbatim between works, although it could be applied to looser forms of reuse such as paraphrase. The meaning of text reuse is subject to interpretation and it can be used to investigate a variety of research questions. For example:

* How is a commentary upon a work structured, how far does it rearranged or deviate from the original work?
* Are two or more texts stemmatically related?
* How extensively is a text distributed across place and time?

The text reuse algorithm used by KITAB is called passim. The algorithm naively identifies reuse by looking for instances of shared text that meet a certain set of criteria (for example, that instances are above a certain number of words long; that instances of shared text are separated only by less than a certain number of words). This means that text reuse detected by passim might suit certain research questions better than others. If you are interested in cases where an author largely paraphrases from a work, then passim is unlikely to be helpful (or it will, at least, only provide some of the picture). If one is interested in how certain more-common phrases are shared among a large collection of words, then passim might need a different set of parameters.

## How does passim work?

Put simply, there are two stages to passim’s operation. In the first stage passim is given a corpus of ‘documents’, relatively short texts. Passim takes each one of these documents and compares it to every other document in the corpus. If passim finds text shared between two documents that meets a set of criteria (parameters, which can be customised to better suit the corpus), it sets those documents aside. 

In the second stage, passim compares each document pair using a well-used alignment algorithm called Smith-Waterman. This algorithm takes each document character-by-character and decides if a character in one document matches a character in the other. Spaces are inserted where characters do not match. The result is an alignment like the one given in the table below.

**Shamela0012129-ara1**|**Shamela0023790-ara1**
خرج مع ابي بكر الصديق رضي الله عنه في تجارة الي بصري ومعهم نعيمان وكان نعيمان ممن شهد------- بدرا ايضا وك-------ان علي الزاد فقال له سويبط----------- اطعمني فقال حتي يجء ابو بكر فقال اما والله لاغيظنك فمروا بقوم فقال لهم سويبط -تشترون مني عبدا قا---لوا نعم فقال انه عبد له كلام وهو قاءل لكم اني حر فان كنتم اذا قال لكم هذه المقالة تركتموه فلا تفسدوا علي عبدي قا-لوا بل نشتريه منك فاشتروه بعشر قلاءص ثم جاءوا فوضعوا في عنقه حبلا ف---------------قال نعيمان ان هذا يستهزء بكم واني حر فقالوا قد عرفنا --خبرك وانطلقوا به فلما جاء ابو بكر -اخبروه فاتبعهم ورد عليهم القلاءص واخذه فلما قدموا علي النبي صلي الله عليه وسلم اخبروه فضحك هو واصحابه من ذلك حولا|خرج--- ابو بكر-------------------- في تجارة--------- ومعه- نعيمان وسويبط بن حرملة وكانا شهدا بدر-----ا وكان نعيمان علي الزاد فقال له سويبط وكان مزاحا اطعمني فقال حتي يجء ابو بكر فقال اما والله لاغيظنك فمروا بقوم فقال لهم سويبط اتشترون مني عبدا لي قالوا نعم ق-ال انه عبد له كلام وهو قاءل لكم اني حر فان كنتم اذا قال لكم هذه المقالة تركتموه فلا تفسدوا علي عبدي فقالوا بل نشتريه منك-------- بعشر قلاءص ثم جاءوا فوضعوا في عنقه حبلا وعمامة واشتروه فقال نعيمان ان هذا يستهزء بكم واني حر قا-لوا قد اخبرنا بخبرك وانطلقوا به و----جاء ابو بكر فاخبروه فاتبعهم فرد عليهم القلاءص واخذه فلما قدموا علي النبي صلي الله عليه وسلم اخبروه فضحك هو واصحابه منهما- حولا
{: .notice--primary}

Passim was developed by David Smith and his team for detecting instances of text reuse in a large corpus of nineteenth-century American newspapers. See further, their project website: [viral texts](https://viraltexts.org/). In this case passim treated each newspaper article as a document for comparison (meaning that each compared document was around 2000-words or less).

This was inappropriate for the texts in KITAB’s corpus for two reasons. Firstly, the texts in the OpenITI corpus are typically very large. Secondly, text that is reused between works in the OpenITI corpus is often rearranged. KITAB, therefore, pre-processes the OpenITI texts prior to running passim, splitting them into 300-word chunks (termed milestones - marked by 'ms' and a number in OpenITI texts, for example 'ms120'). Each milestone is then treated by passim as a document.

In practice, therefore, KITAB splits every text into 300-word chunks. Passim compares every 300-word chunk of each text to every other 300-word chunk of every other text and identifies chunks where text is shared. Smith-Waterman is then used to create alignments from those chunks.

Ryan Muther has developed with KITAB a separate approach to running passim for KITAB’s texts, which we term aggregation. Sometimes text reuse might run over the edge of milestone boundaries. In these cases, some reused text that sits at the edge of milestones might be missed. Aggregation reassembles the milestones in these cases to create larger alignments that better represent the full reuse between the two texts.

Depending on the type of analysis or visualisation, normal or aggregated passim data might be more useful and so we produce data for both.

## What does our passim data look like?

The result of the above process is one csv (comma separated value) file for each pair of texts, where each row represents an individual alignment. We create two sets of data, normal and aggregated.

This individual alignment files can then be viewed used KITAB’s alignment reader (see figure 1), which helps us to visualise how text is shared between a pair of texts.

{% capture figure1 %}
[![A comparison of the Nujum and Kamil](/images/methods/pair-wise-Nujum-Kamil.png)](/images/methods/pair-wise-Nujum-Kamil.png)

*Figure 1. A vizualisation of comparing Ibn Taghribirdi's (d. 874/1470) Nujum al-Zahira on the top with Ibn al-Athir's (d. 630/1233) al-Kamil fi-l-Taʾrikh on the bottom. Yellow lines show reused text and the red bars show the length of each instance of reuse. One can clearly see how Ibn Taghribirdi has condensed the Ibn al-Athir's material when writing his chronicle, as both chronicles conclude in their author's lifetimes. For more on the vizualisation, see [here]({{ "/data/viz" | relative_url }}).*
{% endcapture %}

<div class="notice--primary">
{{ figure1 | markdownify }}
</div>

From these alignments we also compute statistics for each book (again both for normal and aggregated data) that show, for example, what proportion of each work is shared with another work and how many words are shared between two texts. This statistical data is fed into a [PowerBI application]({{ "/data/viz" | relative_url }}) and it is also used by team members to investigate research questions.

## Improving passim

There are a number of decisions that are made when running passim on the whole corpus. We have chosen to split our texts into 300-word chunks (rather than say, 100). We also choose a set of parameters that we think best allows text reuse to be identified in classical Arabic.

These decisions are subject to constant review, and we are producing alignment datasets that have been checked by team members to test and experiment with new parameters and approaches. For an idea of how we review passim, see [this blog]**UPDATE LINK** 

{% capture faq_box %}
## Passim FAQs
### When does KITAB run passim?
Passim is run at least twice every year to account for corpus changes. We do not run it more regularly because the preparation of the corpus and subsequent analysis of the data produced by passim is very time consuming. It is important for us that the corpus is prepared appropriately and that the data and subsequent analysis is checked thoroughly, to guard against potential errors.

### Can I access the passim data?
At present we are not releasing the passim data pubicly. This is because we are still developing and improving our processes for running passim and analysing its output. We hope to release the data soon, and we will do so along with a suite of applications to help researchers make the most of this data. We are currently sharing the preliminary datasets with those who are [working with us]({{ 'about/get-involved' | relative_url }}) to help expand the corpus and understand our data.

### Can I run passim?
It is possible to run passim at home on a small corpus of texts. To run larger quantities of text requires a huge amount of computing power, and we run the OpenITI Corpus using a server. 

Running passim is not recommended, unless you have a good familiarity with computers. Instructions for how to run passim can be found [here](https://github.com/dasmiq/passim). A development branch of passim now allows you to run passim through python and this is recommended route. For instructions, see [here](https://github.com/dasmiq/passim/tree/seriatim). {% endcapture %}

<div class="notice--primary">{{ faq_box | markdownify }}
</div>
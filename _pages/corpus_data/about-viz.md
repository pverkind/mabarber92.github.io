---
excerpt:	""
header:
  overlay_image: /images/covers/kitab2.jpg
  overlay_filter: rgba(0, 0, 0, 0.45)
  caption: "**Photo credit**: From Book three of 'Nihāyat al-su’l' which gives instructions on using lances. Dated 773/1371 (Add. MS. 18866, f. 113r)"
title:		"About our Vizualisations"
layout:		tag
sidebar:
  nav: "corpus"
toc: true
toc_sticky: true
permalink: /data/viz
taxonomy: viz
entries_layout: grid
---

KITAB's [datasets]({{ '/data' | relative_url }}) are often large and difficult to comprehend. KITAB is, therefore, working to develop and adapt vizualisations to help the team and other researchers understand the data. Where relevant we release code and PowerBI templates for our vizualisations enabling you to adapt them for your own research, whether or not you are using KITAB's data.

There are a set of core vizualisations that we use routinely in our research and reference in our blogs and publications. This page is intended to help explain how those vizualisations work and how they should be interpretted. For detailed instructions on how to use the applications, please visit our [docs](). 

**Please note:** This list of vizualisations and applications is being continually updated as we formalise and release our applications. If you are unsure about one of the vizualisations used in a publication or blog we recommend you return here.
{: .notice--warning}

To access and use our applications and vizualisations, please visit the [applications portal]({{ 'data/apps' | relative_url }}).

## The pairwise text reuse vizualisation

This application is designed for viewing text reuse between pairs of texts. Image 1 shows a screen grab from the main part of the visualisation.

{% capture image1 %}
[![Pairwise visualisation](/images/methods/pair-wise-Nujum-Kamil.png)](/images/methods/pair-wise-Nujum-Kamil.png)

*Image 1. The pairwise vizualisation comparing Ibn Taghribirdi's Nujum (on the top) with Ibn al-Athir's Kamil (on the bottom)*.
{% endcapture %}

<div class="notice--primary">
{{ image1 | markdownify }}
</div>

This vizualisation layers a lot of types of data. The x-axis of the two graph represents each book from start to finish, divided into milestones (on text reuse and milestones, see our explanation of [passim]({{ '/methods/text-reuse#how-does-passim-work' }})). Thus, the top graph in image 1 shows Ibn Taghribirdi's *Nujum*, where 1 represents the first milestone in the book and 3745 represents the last milestone. The bottom graph in image 1 shows Ibn al-Athir's *Kamil* where 1 is the first milestone in the book and 4500 is the last. 

Each of the red bars on the top and bottom graphs represents a milestone that contains text reuse. The height of each bar is determined by the postion of the reuse text in the milestone and its length, where the y-axis gives the position in words. For example, a bar that starts at 50 and ends 100 on the y axis, means that reuse occurs between word 50 and 100 of that milestone and that it the reuse is, therefore, 50-words long. 

The yellow lines are then used to link the reused text. For example, circa milestone 700 of Ibn al-Athir's *Kamil* (the bottom graph) is reused in milestone 1 of Ibn Taghribirdi's *Nujum*. These yellow lines allow us to understand rearrangement of text. For example, in the case of image 1, we can see how the text is reused in almost entirely the same order, but condensed. As both works are chronicles, this is to be expected. 

Were text to be rearranged, more lines would cross over each other. See, for example, image 2, which compares Tabari's *Taʾrikh* with Ibn Hanbal's *Musnad*. There we can see heavy reuse of the early parts of al-Tabari's work (the parts that cover the Prophet's life), but because the *Musnad* is not a chronological account, the text is rearranged and the lines crossover.

{% capture image2 %}
[![Another pairwise visualisation](/images/methods/pair-wise-Tarikh-Musnad.png)](/images/methods/pair-wise-Tarikh-Musnad.png)

*Image 2. The pairwise vizualisation comparing al-Tabari's Taʾrikh (on the top) with Ibn Hanbal's Musnad (on the bottom)*.
{% endcapture %}

<div class="notice--primary">
{{ image2 | markdownify }}
</div>

We often provide screen captures of this vizualisation in our publications to help illustrate our discussions of book history. It is, however, a part of an interactive vizualisation. In the interactive visualisation, clicking on the yellow line linking the reuse will bring up the text of the relevant reuse and provide the context in the original two texts, allowing you to read and understand the particular reuse instance.

## More explanations of our core vizualisations coming soon...

Return here to see explanations of our new applications including:
* The Corpus statistics application
* The Corpus text reuse statistics application
* The book-DNA explorer

## Applications and vizualisations in development

Find below our latest blogs on the development of vizualisations:


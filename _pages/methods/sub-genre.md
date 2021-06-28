---
excerpt:	""
header:
  overlay_image: /images/covers/kitab2.jpg
  overlay_filter: rgba(0, 0, 0, 0.45)
  caption: "**Photo credit**: From Book three of 'Nihāyat al-su’l' which gives instructions on using lances. Dated 773/1371 (Add. MS. 18866, f. 113r)"
title:		"Subgenre classification"
subtitle:	"An example of a machine learning approach" 
layout:		single

permalink: /methods/sub-genre
sidebar:
  nav: "methods"
toc: true
toc_sticky: true

---

Machine-learning-based approaches are at the cutting-edge of the Digital Humanities. KITAB is using this approach in a field that we call 'sub-genre classification'. This work is being developed by Ryan Muther. By 'sub-genre' we mean distinct units in a text that share certain characteristics that can be distinguished. These are the kinds of features that we can as human readers easily identify, based on our understanding of how a text works. Examples include: isnads, poetry and Qurʾanic quotations. For sub-genres that occur frequently across texts it is useful to be able to identify them across the corpus, a task that would be impossible to undertake manually for over 4000 texts.

The identification of sub-genres could help us address research questions such as:
* Does the frequency of isnads in texts vary across time?
* How long are isnads, do they get longer or shorter?
* Where is poetry quoted in a text and how often? Do certain texts quote poetry in similar ways?
* How common is Qurʾanic quotation in a corpus?

## Automatic isnad detection: our first case study

So far, we have attempted the automatic detection of one sub-genre: *isnads*. The automatic detection of *isnads* across the OpenITI corpus is valuable for multiple reasons. First, it helps us better understand how these lists of names that are repeated frequently across our corpus, interact with [text reuse detection]({{ '/methods/text-reuse' | relative_url }}). We know that at least some of the instances of text reuse identified by passim are only alignments of long *isnads* without shared *matns*. Second, identifying *isnads* allows us to analyse the names and the [networks of scholars]({{ '/methods/networks' | relative_url }}) that they represent. Automatic *isnad* detection has also helped us to better understand the OpenITI corpus and guided our research into book history. For examples, see our [blogs]({{ '/methods/citation' | relative_url }}) that engage with the *isnad* dataset.

On this page, we will provide a relatively detailed overview of how the method to automatically detect *isnads* works. This is our first machine learning workflow, and it will help to inform our implementation of machine-learning-based methods in the future.

### The process: training and retraining the model

The first step is to create training-data for the model. A number of team members (the annotators) worked together to read a variety of OpenITI texts and insert two types of tags into the text: @ISB@ to mark the beginning of the *isnad* and @ISE@ to mark the end of the *isnad*. Annotators studied 2000 lines in each text that they worked with, spreading their annotations throughout the text (for example, they might look at 200 lines, skip 1000 lines, look and another 200 lines, and so on until they had looked at 2000 lines). By logging the lines that they studied, annotators provided both positive and negative feedback for the model. For example, if in one set of 200 lines, the annotator found no *isnads* and did not add any *isnad* tags, then the model would know that it should not identify *isnads* in that section.

![Isnad tags in a text](/images/methods/isnads_tag.png)*Image 1. A screenshot of Ibn Hisham's Sira in EditPadPro with the beginnings and ends of *isnads* annotated.*
{: .notice--primary} 

Once a some texts had been tagged, Ryan Muther, the computer scientist who is working on the *isnad* classifier, used those texts and their tags to train the *isnad*-classifier model. The newly-trained model was then used to identify isnads in texts it had not seen, and this data was used to insert isnad beginning and end tags into the text.

The annotators then evaluated the tags in those texts, following the same process as before, but moving or deleting the machine-inserted tags, or inserting new tags where needed. At the same time, annotators made observations about the positions of the machine-inserted tags and the general quality of the automatic detection. These observations helped guide efforts to create more training data. For example, by prompting annotators to tag more texts of a certain genre.


{% capture flo_img %}
![The process of training a model](/images/methods/Isnad_process.png){: .align-center}\
*Image 2. A flowchart illustrating the process of annotation and review used to train the isnad detector.* {% endcapture %}

<div class="notice--primary">{{ flo_img | markdownify}}
</div>

### Inter-annotator evaluation

When training a model, it is important to know how difficult the task is for the human annotator. If the human annotators struggle to agree on an identification, then the machine will also have difficulties with this task. To this end, the annotators undertook an inter-annotator agreement study at the beginning of the process. All annotators were asked to identify and tag the beginning and end of *isnads* in the exact same text in the same locations. The annotations were then compared. This study found that annotators largely agreed about the starting positon of *isnads*, but disagreed about where *isnads* ended. The model also had similar difficulties identifying the ends of *isnads*.

### How does the algorithm work?

Put simply, the algorithm learns the position of isnads by looking at the kinds of words that are common to isnads and the kinds of words that are more commonly found outside of isnads. In addition, it identifies words that commonly start isnads. Table 1 provides a representation of how the model would classify words in the training dataset. 

{% capture tags_table %}
![Table of isnad tags](/images/methods/Isnad-tags-table.png)
*Table 1. A table showing how the model would tag each word in the training data. 'Out' means outside of an isnad, 'in' meants inside an isnad, and 'beg' means the first word of an isnad.*{% endcapture %}

<div class="notice--primary">
{{ tags_table | markdownify }}
</div>

### The quality of the results

When training the model, a small part of the training data is kept back, and this can then be used as unseen data to evaluate the model's performance. When training, the algorthim is training multiple times, taking away a different portion of the training data each time for evaluation, the performance on this unseen data is then averaged to produce a score for the algorithm.

We used two scores to evaluate the model: **precision** and **recall**. Precision measures how much of what the model identified as an *isnad* matches with that in the unseen training data. Low precision means the machine identified *isnads* where the training data states that there should not be any *isnads*. Recall measures the proportion of *isnads* in the unseen training data that the model found. Low recall means that the machine failed to identify many of the *isnads* tagged in the training data.

At present, the precision of the model is **UPDATE** and the recall is **UPDATE**. These are considered good scores and mean that we can (to a certain extent, for caveats see below) trust the model's outputs.

### Challenges

Identifying *isnads* at the corpus level produces a huge number of challenges. Chief among them is the fact that we cannot check the results of the algorithm in every text. Although the algorithm scores highly, these scores are only based on the training data that we provided the model. Certain genres (like history and hadith) were better represented in our training set than others and this risks biasing the model. The team aims to continue training and improving the model, but this will also rely on the continued expansion of the OpenITI corpus to include a better variety of genres, and the improvement of our metadata to better focus on different types of text. 
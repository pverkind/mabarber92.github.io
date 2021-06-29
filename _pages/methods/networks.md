---
excerpt:	""
header:
  overlay_image: /images/covers/banner_methods.png
  overlay_filter: rgba(40, 99, 165, 0.60)
title:		"Network Analysis"

layout:		single

permalink: /methods/networks
sidebar:
  nav: "methods"
---

Network analysis is a fundamental and well-developed field in the Digital Humanities. KITAB are using various computational methods to analyse networks, both using our text reuse data and manually curated datasets, documenting connections between both books and scholars. For this we do not use one defined tool, and we encourage you to read our [blogs]({{ "methods/scholar-network" | relative_url }}) to explore some of the methods we are using.

The are two main directions that we are following in network analysis:

## Networks from isnads

As we note [here]({{ 'methods/sub-genre' | relative_url }}), the team are involved in the automatic identification of *isnads* in texts across the corpus. One aim is to convert the automatically-identified *isnads* into strings of related names, which can then be converted into networks. 

Converting *isnads* into networks is a complex problem, because it requires resolving both name variation (that is, the same person being known by multiple names) and shared named (that is, multiple people being referred to by the same name). We are working to resolve these problems computationally, using the position of names within *isnads* to infer name variations and distinguish shared names. We are also trying to resolve this problem by examining the postion of *isnads* within texts, to try and distinguish shared names, where names might be shortened on their second or third mention.

Sarah Savant and Masoumeh Seydi are working together to create ground truth of names used in the isnads of two authors: al-Tabari and Ibn ʿAsakir. Ryan Muther is addressing the problem computationally, using the ground truth to test and improve his methods. This analysis is a work in progress, and for the latest updates you should see our [blogs on the subject]({{ 'methods/scholar-network' | relative_url }}). 

## Networks from text reuse data

We hope to convert some of our text reuse data into networks that illustrate how pieces of text are shared and disseminated. This is particularly challenging because of the size of our corpus and because of Hadith. Passim outputs a dataset called 'Cluster data', which documents how the milestones of our texts are networked together. For an explanation of how passim works and milestones, see [here]({{ 'methods/text-reuse' | relative_url }}). Unfortunately this dataset is messy and difficult to read, largely because of *isnads* which create non-meaningful clusters of shared names.

We have recently experimented running passim without isnads (using the automatically tagged isnads, produced through this [method]({{ 'methods/sub-genre' | relative_url }})), and will explore how this changes the cluster data. We are also working on producing networks from the text reuse data using other methods. Watch this space!


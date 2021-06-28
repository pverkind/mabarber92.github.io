---
layout: splash
header:
  overlay_image: /images/covers/kitab3a.jpg
  actions:
    - label: "Learn more about the Corpus and Data"
      url: /corpus
title: "Our Applications"

corpus_app:
  - image_path: /images/covers/corpus_app.png
    alt: "placeholder image 2"
    title: "Corpus Data Application"
    excerpt: 'This PowerBI application allows you to explore data about the Corpus. How many OpenITI books are over 1 million words long? Which authors are the most prolific? How important are short works?<br><br> Explore these questions and more using the app!'
    url: "#test-link"
    btn_label: "Use the Corpus App"
    btn_class: "btn--primary"
metadata_app:
  - image_path: /images/covers/search_app.png
    alt: "placeholder image 2"
    title: "The Corpus Metadata Application"
    excerpt: 'Looking for a particular book to download in our corpus? Wanting to explore books by specific authors or in specific genres?<br><br> Search for books using the Corpus metadata search app.'
    url: "#test-link"
    btn_label: "Search our metadata"
    btn_class: "btn--primary"
coming_soon:
  - image_path: /images/kitab/textalignment.png
    alt: "placeholder image 2"
    title: "Coming soon..."
    excerpt: 'Interested in exploring our other datasets? KITAB will be releasing more data and applications soon.<br><br> Subscribe to be notified when new applications are added to the portal.'
    url: "#test-link"
    btn_label: "Subscribe for updates"
    btn_class: "btn--primary"

permalink: /data/apps
---

Welcome to KITAB's application portal. All of our latest applications can be accessed through this site. You can use them to explore our many datasets, in particular our text reuse data. For guidance on how to use the different applications, please visit our [vizualisations page]({{ 'data/viz' | relative_url }}).


 {% include feature_row id="corpus_app" type="left" %}


 {% include feature_row id="metadata_app" type="right" %}
 {% include feature_row id="coming_soon" type="left" %}
## About Project

This is a project aimed at generating more engaging and concise lectures from existing lecture recordings or online study materials. We hope to create a more engaging learning experience while saving time for the audience.

# Project Setup and Usage Guide

## Set up Conda Environment

To create and activate the Conda environment for this project, use the provided `environment.yml` file:

```bash
conda env create -n vid_lab -f environment.yml
conda activate vid_lab
```

## Current Capabilities:
- Youtube Video Download
- Audio extraction from video
- Audio to json Transcription


# TODO
- [ ] UI with video time line? how to do this with local host
        Assuming this is a local hosted Video tool for analysis.

## Why is a Backend UI necessary? <br>
because we want AI analysis to be understandable? Is interpretation important.?

## What type of content do we want to create? <br>
Maybe the possible short content is dependent on the type of creater. For the sake of doability, we should just focus on the software dev streamers. Since they don't focus too much on generating content from stream (too tired etc.) 

## <strong>What type of content can be generated</strong><br>
<strong> real time prompt engineering?</strong>
This is still some prompt engineering can be done here. We can use prompt engineering to do some research on what is popular for software devs? What can be created

### Maybe there is a way to use prompt engineering to reverse engineering (reverse script a short) into a template

* what sentiment is this type of short . 
* How was the content delievered.
* <strong> how to capture similar moments from the stream content </strong>

- [ ] To Sentiment analysis for Audio Transcription. Maybe a graph of where +y is happy and -y is not happy? with a time line. 
- [ ] We already have a ton of content from headstarter, download all the zoom links and try to process them and to see what content we can produce from there. 
- [ ] Search on Tiktok and youtube shorts for popular headstarter post to see what type of post is viral


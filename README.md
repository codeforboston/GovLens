# GovLens

![](https://github.com/codeforboston/GovLens/workflows/Lint%20and%20Test/badge.svg)

## About the project

GovLens is a government transparency project developed by MuckRock and Code for Boston engineers. Our mission is to create a more open, accessible, and secure democracy by 1) examining the technical elements of federal and state agency websites, 2) scoring them for transparency, security, privacy, and accessibility, and 3) publishing our findings to help communicate to those government agencies possible ways they could improve their infrastructures.

Here is a screenshot of what a GovLens Scorecard will look like:

![A screenshot of what a GovLens Scorecard looks like](README_images/scorecard.png)

## Why?

We get reminders all the time of how well our physical civic infrastructure is doing: Did my car hit a pothole? Are the swing sets covered in rust? However, it can be harder to see how well our digital civic infrastructure is holding up, particularly when it comes to the parts of the web that may be invisible to many users: How accessible is a site to persons who rely on screen readers or who have reduced vision? Which third-party trackers have access to visitor data, and how is that data being guarded? Are government websites following basic best practices in utilizing secure connections?

We have a [National Bridge Inventory](https://www.fhwa.dot.gov/bridge/nbi.cfm) that monitors dangerous bridges, and there are federal agencies that monitor other elements of core infrastructure, but we do not have similar monitoring of the strengths and weaknesses of much of our digital infrastructure.

GovLens helps to provide at least the start of an answer to that, by making those oftentimes overlooked aspects of digital infrastructure more visible via public report cards for each agency in our database as well as collated data for each jurisdiction and state, letting us see which areas of the country are leading the way and which might need a little more prodding.

This is partially inspired by the work of Pulse.CIO.Gov, an official federal government website that monitored the adoption of HTTPS compliance among federal websites, as well as [SecureThe.News](https://securethe.news), which did the same thing for news websites. Both of these projects brought wider visibility to the issue and provided natural and effective peer pressure for website operators to improve. Our hope is we can do the same for local government, while also compiling a rich research data set for future analysis.

## Who is this site for?
This site has three core planned audiences:

* __The general public__, so that they’re better educated about the state of government digital infrastructure and why it matters.
* __Government decision makers__, so that they can understand why they need to invest in better adhering to web standards as well as see where their sites stand compared to their peers.
* __Local and national media outlets__, so as best to reach and influence the above categories.

## Project goals

The goal is to create an automatically updated database that tracks, over time, how well government agencies websites at the state, local, and federal levels follow best practices when it comes to HTTPS security, mobile friendliness, reader accessibility, and other key areas.

Over time, we hope to show whether both individual agencies are improving or worsening, as well as help highlight national shifts along the metrics we monitor. Individual pages show the most recent snapshot ranking, but our API will make historical data available.

## Current status

The project is currently in testing stages, as we work to both develop usable, accurate data and build a pipeline for regularly populating it. The site currently can run locally, but several of the data categories are filled with randomized testing data and any report cards generated are for **demonstration purposes only**. These scores do not represent actual scores for agencies.

## Want to Help Out?

If you'd like to contribute or learn more, please visit our [wiki page](https://github.com/JimHafner/GovLens/wiki). There,
you will find more information about development and instructions on setting up a local version of the project that you can
experiment with. Then:

- [ ] Make sure [you've registered for the Code for Boston Slack](https://communityinviter.com/apps/cfb-public/code-for-boston-slack-invite).
- [ ] Join the #MuckRock channel on Slack.
- [ ] Ask a current member to be added to our Github organization ([They'll need to click here](https://github.com/codeforboston/GovLens/settings/collaboration)). After they've sent you an invite, you'll need to either check your email or notifications in Github (the alarm icon on the top right of your Github page) to accept the invite.

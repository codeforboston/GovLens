# GovLens

![](https://github.com/codeforboston/GovLens/workflows/Lint%20and%20Test/badge.svg)

## About the project

GovLens is a government transparency project developed by MuckRock and Code for Boston engineers. Our mission is to create a more open, accessible, and secure democracy by 1) examining the technical elements of the websites of federal, state, and local government agencies, 2) scoring them for transparency, security, privacy, and accessibility, and 3) publishing our findings to help communicate to those government agencies possible ways they could improve their infrastructures.

Our goal is to create an automatically updated database that tracks, over time, how well government agency websites are adhering to best practices when it comes to HTTPS security, mobile friendliness, reader accessibility, and other key areas. With this, we hope to show whether individual agencies are improving or worsening and to highlight national shifts along the metrics we monitor. Individual agency pages will show the most recent snapshot ranking, but our API will make historical data available.

Here is a screenshot of what a GovLens Scorecard for an individual government agency will look like:

![A screenshot of what a GovLens Scorecard looks like](README_images/scorecard.png)

## The problem

We get reminders all the time of how well our _physical_ civic infrastructure is doing: Did my car hit a pothole? Are the swing sets covered in rust? We have a [National Bridge Inventory](https://www.fhwa.dot.gov/bridge/nbi.cfm) that monitors dangerous bridges, and there are federal agencies that monitor other elements of core infrastructure. However, it can be harder to see how well our _digital_ civic infrastructure is holding up, particularly when it comes to the parts of the web that may be invisible to many users: How accessible is a site to persons who rely on screen readers or who have reduced vision? Which third-party trackers have access to visitor data, and how is that data being guarded? Are government websites following basic best practices in utilizing secure connections?

## The solution

GovLens will provide at least the start of a solution to this problem, by making those oftentimes overlooked aspects of digital infrastructure more visible via public report cards for each agency in our database as well as by collating data for each jurisdiction and state, letting us see which areas of the country are leading the way and which might need a little more prodding.

This project is inspired in part by the work of Pulse.CIO.Gov, an official federal government website that monitored the adoption of HTTPS compliance among federal websites, as well as [SecureThe.News](https://securethe.news), which did the same thing for news websites. Both of these projects brought wider visibility to the issue and provided natural and effective peer pressure for website operators to improve.

## Who is this site for?
The site is planned for three core audiences:

* __The general public__, so that they are better educated about the state of government digital infrastructure and why it matters.
* __Government decision makers__, so that they can understand why they need to invest in adhering to web standards as well as see where their sites stand compared to those of their peers.
* __Local and national media outlets__, so as best to reach and influence the above groups.

## Current status

The project is currently in the testing stage, as we work to develop usable, accurate data and to build a pipeline for regularly populating it. The site currently can run locally, but several of the data categories are filled with randomized testing data and any report cards generated are for **demonstration purposes only**. These scores do not represent actual scores for agencies.

## Want to help out?

If you'd like to contribute or learn more, please visit our [wiki page](https://github.com/codeforboston/GovLens/wiki). There,
you will find more information about development and instructions on setting up a local version of the project that you can
experiment with. Then:

- [ ] Make sure [you've registered for the Code for Boston Slack](https://communityinviter.com/apps/cfb-public/code-for-boston-slack-invite).
- [ ] Join the #MuckRock channel on Slack.
- [ ] Ask a current member to be added to our Github organization ([They'll need to click here](https://github.com/codeforboston/GovLens/settings/collaboration)). After they've sent you an invite, you'll need to either check your email or notifications in Github (the alarm icon on the top right of your Github page) to accept the invite.

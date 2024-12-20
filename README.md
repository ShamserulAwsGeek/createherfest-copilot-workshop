# Exploring GitHub Copilot 👩🏽‍💻

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/LadyKerr/baddies-buildathon-copilot-workshop)

## Local/Remote Development 🛠️

To get started, you can clone this repository to your local environment or you can select the green clone button, choose codespaces and select "create codecpace on main." This will spin up a virtual environment for you that you can work from. You can also just click on the "Open in Codespaces" button above.

If you choose to clone the repository locally, ensure that you have Python3 installed on your machine. For this workshop, we will be using a Codespace.


## The Challenge 🚀

[GitHub Copilot](https://github.com/features/copilot) is built and designed to be an AI pair programmer. Based on the context it sees and the code you write it will generate suggestions for the next line, block, function or even class it believes you're writing. This allows you to offload tedious tasks, obtain obscure syntax, and generate code from comments, allowing you to stay in the zone and focus on the higher level and more difficult challenges.

This workshop is created to give you the opportunity to explore GitHub Copilot, to see how to use and interact with it while building an application. A loose structure is provided to create a scenario and give you a starting point, with a series of challenges to guide you through various aspects of coding with GitHub Copilot.

## The scenario 👀

You have been provided a [dataset with flight information from the FAA](./data/flights.csv). The dataset contains dates, times and carriers for flights in the US which took place in 2013. You want to build an application which will allow someone to select the day of the week and arrival airport to see the chance their flight will be delayed by more than 15 minutes. You'll do so by walking through the following challenges:

1. Create and export the data and model to support the application
2. Create an API to provide a list of airports and their associated ID in the data, and the model
3. Create a frontend to allow a user to select the day and airport to see the information

## Building the application ✨

The goal of the workshop is to create an application which meets the specifications indicated above - a frontend which allows the user to see the chance their flight will be delayed. You will notice there is limited guidance about how to actually build it. This is intentional, as we want you to explore GitHub Copilot using tools you're familiar with or want to explore. The best way to learn GitHub Copilot, after all, is to start using it.

As a result, you're free to use frameworks and languages of your choosing. If you want to create a backend using Node.js and a frontend with Vue.js, you're welcome to do that! Want a Windows app? A mobile app? To explore the dataset more and discover new insights? Feel free to do so!

## Getting support

With the open-ended nature of the workshop the mentors may not be able to help with every possible path. We've provided a couple of solutions which we would consider "official", and the ones the staff are most familiar with. However, as already stated, the primary goal is to explore GitHub Copilot. So while there might not be someone who's an expert on Go, you'll be able to talk about GitHub Copilot and how to get the most out of the tool. So don't be afraid to ask!

## Getting started

Let's get started! Here's the list of challenges to help guide you through the workshop:

0. [Starting the project and installing GitHub Copilot](./00-instructions/0-get-started.md)
1. [Create the model and supporting data](./00-instructions/1-create-model-data.md)
2. [Create the API](./00-instructions/2-create-api.md)
3. [Create the frontend](./00-instructions/3-create-frontend.md)

## Additional Resources

- [How to use GitHub Copilot: Prompts, tips, and use cases](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [10 Unexpected use cases of GitHub Copilot](https://github.blog/2024-01-22-10-unexpected-ways-to-use-github-copilot/)
- [Prompting Tips with GitHUb Copilot](https://gh.io/prompt-engineering)
- [Copilot Chat Cookbook - example prompts](https://docs.github.com/en/copilot/example-prompts-for-github-copilot-chat)
- [Best Practices when using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)

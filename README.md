# Business Advisor LLM Simulator App with 2 choices

## Overview of the App

This app is a scripted simulation of an LLM that is used at the HumansLab Research lab at Georgia Tech.

## Features

This simulator includes features like stream writing which simulates as if the LLM is writing on real time, while the conversation is actually scripted beforehand.

## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run ChoiceLLM.py

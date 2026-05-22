---
layout: project
title: AI + NLP Emotion Analysis
project_id: nlp-emotion-analysis
screenshot_note: These charts were generated from the project pipeline and compare sentiment or emotion patterns across wins and losses.
screenshots:
  - src: images/nlp-goem-winloss-diff.png
    alt: Top GoEmotions differences between wins and losses
    caption: Top GoEmotions differences across win and loss outcomes.
  - src: images/nlp-politics-emolex.png
    alt: Politics EmoLex win-loss emotion scores
    caption: NRC EmoLex emotion scores for political quotes after wins and losses.
  - src: images/nlp-sports-emolex.png
    alt: Sports EmoLex win-loss emotion scores
    caption: NRC EmoLex emotion scores for sports quotes after wins and losses.
  - src: images/nlp-politics-goem-diff.png
    alt: Politics GoEmotions win-loss differences
    caption: GoEmotions win-loss differences for political quotes.
  - src: images/nlp-sports-goem-diff.png
    alt: Sports GoEmotions win-loss differences
    caption: GoEmotions win-loss differences for sports quotes.
  - src: images/nlp-sports-vader.png
    alt: Sports VADER sentiment win-loss comparison
    caption: VADER compound sentiment comparison for sports wins and losses.
---

### Overview

This project analyzes emotional tone in political and sports quotes after wins and losses. The goal was to compare how emotional language changes across domains and outcomes using a layered NLP pipeline: rule-based sentiment analysis, lexicon-based emotion features, and transformer-based emotion classification.

### Research Questions

- Do wins and losses produce different sentiment patterns?
- Do politicians and sports coaches respond differently after success or failure?
- Do lexicon-based and transformer-based emotion tools surface different patterns?
- Which emotions appear most strongly when comparing win and loss language?

### AI/NLP Pipeline

The project combined three approaches:

- `VADER` for polarity and compound sentiment scoring
- `NRC EmoLex` for lexicon-based emotion category features
- A transformer-based GoEmotions model through Hugging Face Transformers and PyTorch for contextual emotion classification

The final merged dataset combined the original quote data with VADER scores, EmoLex features, and GoEmotions probabilities.

### Important Files

- `bert_goemotion_analysis.py`: loaded the GoEmotions transformer model and generated `merged_with_vader_emolex_bert.csv`
- `analyze_goemotion_winloss.py`: computed win-loss emotion differences and generated charts
- `test_winloss_vader.py`: tested the VADER sentiment layer and produced sentiment-scored data
- `merged_with_vader_emolex_bert.csv`: combined output from the VADER, EmoLex, and transformer stages

### What It Demonstrates

This project shows experience with a complete AI/NLP analysis workflow: preparing text data, layering multiple NLP techniques, integrating a pretrained transformer model, producing analysis-ready CSV outputs, and turning results into charts and a presentation.

It also shows the practical side of AI tooling: managing Python dependencies, working through PyTorch and plotting setup, validating intermediate outputs, and explaining model-assisted results clearly enough for a research presentation.

### Presentation

The final presentation is available here:

[Open NLP Emotion Analysis Presentation](assets/nlp-emotion-analysis-presentation.pdf)

### Future Improvements

- Publish a cleaned public code repository with requirements and sample data
- Add a notebook that walks through the full pipeline step by step
- Normalize chart styling for clearer comparison across methods
- Add confidence intervals or additional statistical tests for emotion categories
- Expand the dataset with more speeches, press conferences, and post-game quotes

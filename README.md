# Cloze Deletion Generator for Anki

## Features

- Generates cloze deletions for each word in the input text.
- Increments the cloze number after every 7 words.
- Supports multi-line input

## Usage

1. Clone the repository
2. cd cloze-deletion-generator
3. python cloze.py
4. Enter your text
5. Press Enter twice to finish the input

## Example
Input text: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

Occluded Text: {{c1::Lorem}} {{c1::ipsum}} {{c1::dolor}} {{c1::sit}} {{c1::amet,}} {{c1::consectetur}} {{c1::adipiscing}} {{c2::elit,}} {{c2::sed}} {{c2::do}} {{c2::eiusmod}} {{c2::tempor}} {{c2::incididunt}} {{c2::ut}} {{c3::labore}} {{c3::et}} {{c3::dolore}} {{c3::magna}} {{c3::aliqua.}}

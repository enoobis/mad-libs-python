def play_madlibs():
  stories = [
    {
      "template": "The {adjective} {noun} likes to {verb}.",
      "blanks": [
        {"word_type": "noun", "blank": "{noun}"},
        {"word_type": "verb", "blank": "{verb}"},
        {"word_type": "adjective", "blank": "{adjective}"}
      ]
    },
    {
      "template": "I have a {adjective} {noun} who likes to {verb}.",
      "blanks": [
        {"word_type": "noun", "blank": "{noun}"},
        {"word_type": "verb", "blank": "{verb}"},
        {"word_type": "adjective", "blank": "{adjective}"}
      ]
    },
    {
      "template": "The {noun} went to the {noun} to {verb} a {adjective}.",
      "blanks": [
        {"word_type": "noun", "blank": "{noun}"},
        {"word_type": "verb", "blank": "{verb}"},
        {"word_type": "adjective", "blank": "{adjective}"}
      ]
    }
  ]

  for story in stories:
    print("\nEnter words to fill in the blanks:")

    words = {}
    for blank in story["blanks"]:
      word = input(f"Enter a {blank['word_type']}: ")
      words[blank["word_type"]] = word

    # Use string formatting to insert the user's words into the story
    finished_story = story["template"].format(**words)
    print("\nHere is your finished Mad Libs story:")
    print(finished_story)

play_madlibs()
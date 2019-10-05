# Markov Bot

This is a very simple, inefficient and naïve bot that uses pseudo Markov chains to generate text based on a database of previous known texts.

## Overview

There are two classes, first the DatabaseDriver, which is a simple abstraction on top of *sqlite3* that is used to store words and their succesors, while also offering a method to query a particular words' successors.

This class is used by the actual bot which is implemented in the Markov Bot class, which offers methods to digest new text and generate texts.

## Usage

```[python]
from main import MarkovBot

# test here refers to the database filename
bot = MarkovBot('test') 

to_digest = """
    But there is something that I must say to my people, who stand on the warm threshold which leads into the palace of justice: In the process of gaining our rightful place, we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred. We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our creative protest to degenerate into physical violence. Again and again, we must rise to the majestic heights of meeting physical force with soul force.
"""
bot.digest_text(to_digest)
# Here 'that' refers to first word of text and 10 to word limit of text
text = bot.generate_text('that', 10)
# text should be something like:
#   'that I must forever conduct our creative protest to degenerate into'
```

## License

MIT License

Copyright (c) 2019 Elias Kickbush

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# Ascii tree builder

Handmade simple alternative of asciitree text structure visualizer

Made by Max Fedorchuck as a test task for applying to the:

Data Science - NLP computer linguistic school (Kyiv, Projector, 2019)

Code style was stolen from Google-oriented open-source project guide:
(http://google.github.io/styleguide/pyguide.html) 

First couple versions of this programm you can find in the folder "/version history" 


## Installation

Use the git command to clone this repo

```bash
git clone https://github.com/mfedorchuck/asciitree_script.git
```

## Usage

```python
import tree_builder

message = "(asciitree(sometimes you)(just(want to draw)) trees (in(your terminal)))"
checked_message = tree_builder.check_layout(message)

message_structure = tree_builder.build_structure(checked_message)
tree_builder.print_structure(message_structure)
```

## Contributing
Pull requests are welcome.

## License
No license. Feel free to use and modify it as you like

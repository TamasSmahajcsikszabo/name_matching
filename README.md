## Name Matching Utility
This is a name matchin utility written in Python.
Under `src` you can find all the source code, the main function and `argsparse` utility is provided in `src/match_names.py`.

### Jupyter Notebook
You can play through the examples provided by notebook `MatchNamesExample.ipynb`.

### Docker
You can build a Docker image and run it to interact with the `argparse CLI`.
Example in Linux:
Build the image: `sudo docker build -t matchnames:latest .`

Once built, you can run it with `sudo docker run -ti matchnames:latest /bin/bash`.
Once on the bash shell, you can run the CLI utility with:

- to get some built-in tests running, try `python src/match_names.py --test`
- to provide your own terms, try `python src/match_names.py --terms "my,comma,separated test words"`

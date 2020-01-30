machine learning algorithm to calculate line equation from a dataset with linear regression and gradient descent

### Dependancies
* Python 3
* numpy
* matplotlib

Start by training your model by providing it your datatset to `learn.py`

```
usage: learn.py [-h] [-r RATE] [-e EPOCH] [-v] [-ve] dataset

positional arguments:
  dataset               your dataset file in csv format

optional arguments:
  -h, --help            show this help message and exit
  -r RATE, --rate RATE  set the learning rate, defaul: 0.01
  -e EPOCH, --epoch EPOCH
                        set the epoch number, default: 4
  -v, --visualise       get a visual feedback
  -ve, --verror         visualise error evolution
```

Then use `estimate.py` to estimate values based on the previously computed line equation

## Visual results
[screen 1](screenshots/screenshot_1.png?raw=true)
[screen 2](screenshots/screenshot_2.png?raw=true)

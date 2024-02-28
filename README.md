# bigauss

Attempt to figure out whether multiple datasets are actually two Gaussian distributions.

Specifically: read an input file that looks EXACTLY like

	Elapsed Times (ms)
	STEP 1	STEP 2	STEP 3
	179	112	68
	164	60	154
	167	61	125
	...	...	...

into 3 lists of ints: [179, 164, 167, ...] and so forth.

Then does some NumPy and scikit-learn black magic to assess whether each
list of ints fits two overlapping Gaussian distributions. Prints some
numbers.

## setup

One time only:

```
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## run it

```
./bigauss.py <INFILE>
```

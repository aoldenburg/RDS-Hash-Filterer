# CSV Image Filter
## About this Project
This is a simple application that takes the NIST RDS Hash Sets as input and filters it into only the common web image types.

Currently, the following file types are filtered for:
* `.jpg`
* `.gif`
* `.tif`
* `.tiff`
* `.bmp`
* `.png`
* `.RAW`
* `.svg`
## Usage
This uses [Python 3](https://www.python.org/downloads/),
```sh
python main.py <input file> [output file]
```
If no output file is given, the filtered csv will be output to `output.csv`

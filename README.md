# How to use `clean_gcode.py`

First, in the python script, add the strings that trigger a line removal in your file inside the `to_remove` list at the beginning of the script. Every line containing one of the following string will be removed from the output file.

Just run the following command, (remove the `{}` and replace the content with your file):

```
python --input="{path/to/your/file.nc}"
```

It will output a file at the same location with the suffix "_clean.nc"

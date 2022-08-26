Notes

- Input and output files are in resources directory
- jmeter script prints output but doesn't write to a file as was not instructed.

Python excercise

1. [Create a python method that takes arguments int X and int Y,
and updates DEPART and RETURN fields in test_payload1.xml](https://github.com/ludo550/python-exercise/blob/master/test_xml.py):
- DEPART gets set to X days in the future from the current date
(whatever the current date is at the moment of executing the code)
- RETURN gets set to Y days in the future from the current date
[Please write the modified XML to a new file.](https://github.com/ludo550/python-exercise/blob/master/resources/test_payload1_Output.xml)

2. [Create a python method that takes a json element
as an argument, and removes that element from test_payload.json.](https://github.com/ludo550/python-exercise/blob/master/test_json.py)
Please verify that the method can remove either nested or non-nested elements
(try removing "outParams" and "appdate").
[Please write the modified json to a new file.](https://github.com/ludo550/python-exercise/blob/master/resources/test_payload_output.json)

3. [Create a python script that parses jmeter log files in CSV format,
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).](https://github.com/ludo550/python-exercise/blob/master/test_jmeter.py)
Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
(the files have .jtl extension but the format is  CSV).
*jmeter_log1.jtl output*:
![jmeter_log1.jtl](https://github.com/ludo550/python-exercise/blob/master/resources/jmeter_log1.PNG)
*jmeter_log2.jtl output*:
![jmeter_log2.jtl](https://github.com/ludo550/python-exercise/blob/master/resources/jmeter_log2.PNG)
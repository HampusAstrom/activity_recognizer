# activity_recognizer

-----------------------------------------------------

NOTES ON THE DATA:
You can find the data here: https://github.com/HampusAstrom/activity_recognizer

The separated data files come from the below cut and trimmed single file.

still5sec (txt and csv) 100kb: phone lying still on my table.
phoneData40sec (txt and csv) 700kb: used a stopwatch with this schedule:

0-10s: phone lying still on my table.
10-20ish: walking to the corridor.
22-30ish: running (through corridor)
30-35ish: walking while rotating phone.
35-40ish: stopping.

“load_phone_data.m” loads the 2nd dataset as a table (can also just double click the csv in matlab but check the column names) and “testing_phone_data” is just 4 lines that extracts the accelereometers X and plots it vs time:

note: accelerometers peaks are from the rotations.

Sensors used: GPS, ACC, GYR, ORI, RSSWIFI
http://sensorfusion.se/sfapp/sf-app-examples/  explains what they mean and what they store in the table (the app stores them all in the same table under the same columns). I made small tests on all the sensors separately and didn’t see anything that looks crazy but we need to verify this and structure and clean up the data, e.g. RSSWIFI uses a different timestamp format from the other sensors. I didn’t try to convert it to the format the others use. Column 1 “RawTime” gives the time as it was recorded by the sensor so you can see how it differs from the others. Column 8 “time” is the time converted to seconds (only makes sense for the other sensors). I couldn’t find info on what the RSSWIFI values mean and load_phone_data.m also removes the name of the wifi so use the raw .txt if you want to have a look. I suggest to just not use it right now (not sure we even need it since we have GPS).
“still5sec” also stored light ( LGT)  which we don’t need

-----------------------------------------------------

TO RUN THE SENSOR FUSION ALGORITHM:
1- Modify lines 2 and 4 of prepare_data.m with the name of your input data file (in .csv format).
2.- Select a name for the output data file in line 57 of main.m
3.- Run main.m

-----------------------------------------------------

TO RUN THE CLASSIFIER:
- Clone the repo: git clone https://github.com/HampusAstrom/activity_recognizer
- Select branch to use (master using accelerometers and fused using fused data (without propper thresholding)): git checkout master
- Edit first lines of code to run on data you want. Currently data_mixed specifies data that is plotted.
- run with "python3 main.py"
- Enjoy nice plots and hope the tresholds are ok for your data as well

-----------------------------------------------------

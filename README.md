# cakedays


Data from [pushshift](https://files.pushshift.io/reddit/) (69M Reddit Accounts). Graphed in python using only pillow.
After downloading the archive, extract it and place it in the same directory as the scripts. Then run gen_data.py. To generate the image, run cake.py.


The most common cakeday is February 14, with 392,005 accounts. The least common cakeday is pretty obviously February 29th, with 102,192 accounts. 

For some reason the most popular month for registering Reddit accounts is February, and the least popular month appears to be May. I honestly have no idea why that is.

The source file is over 3gb, but thankfully it was a csv which made it easy to go through each line and extract the creation date of every account. The unix times were then converted to a readable format. I counted the number of times each day of the year appeared. The counts were then normalized between 0 and 1 and then assigned a color. (Yellow being the fewest, dark red being the most). Then the days were all plotted with pillow. 



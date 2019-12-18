This README describes the two program files submitted for COMP90049 2019S2, Project 1.
There are two files, viz., kt.py and kt2.py
These are two pieces of code that are written for carrying out the tasks defined for Project 1. 
Below, a detailed analysis of how the two programs work is given:


	- kt.py: In this file, we are reading all the files from the data provided, storing each one of them as a list. 
		 Just to make sure that candidates is a correct preprocessed file, we exclude the novel dictionary words from 
		 wordforms.txt and check for the equality between candidates and this list. We also filter out a list of blends
		 from the blends.txt file, by excluding the pairs of source words. This is done for easier analysis of tasks.
		 The prime focus of this file is the filtering of candidate words, which could cleansed upto a level where detecting
		 lexical blends becomes more achievable. This is done by removing over-emphasised words like 'aaaah', 'yummmm'. Other 
		 expressive terms which are not of much use in this context, but are very casually used on social media, were also removed 
		 by using certain regular expressions for matching the patterns, and removing the strings. f2cand.txt is the final file which
		 contains the candidate words. We also create two matrices, each with 183 rows and 2 columns. Both matrices give us the 
		 Jaro-Winkler similarity and Levenshtein distance, between the true blends and their two source words. These are created to
		 give us an idea as to what should the threshold values for our task be. 


	- kt2.py: Here, we perform the crux part of our project. We randomly select 20 common words from blends and candidates, and this is 
		  our training set. For each word in the training set, we create a list of prefixes and another list of suffixes. For every word,
		  the first three characters are taken as the prefix and rest of the word is taken as the suffix. Then a list is created using
		  the dictionary, consisting of words that start with the prefix and end with the suffix of every word in training set. For eg., if 
		  "Brexit" is the word in our training set, then all the words from the dictionary with prefix "bre" and also all the words with the
		  suffix "fit" will be returned. Now, using a limitation/threshold value of Jaro-Winkler similarity and Levenshtein distance, we refine
		  the list further. Now, if this list contains the two source words of the blend, then this word is a predicted blend or else it isn't. 
		  Similarly, we'll create such lists for each word, and see which of them are being predicted as a blend and which are not. 
 
		 
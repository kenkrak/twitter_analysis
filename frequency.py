import sys
import json
import re


def hw(tweet_file):
    freq_table = {}
    totalFrequency = 0
    for line in tweet_file:
        parsed_key = json.loads(line.encode('utf-8'));
        for key in parsed_key.iterkeys():
            tweet_attr = key.encode('utf-8')
            if tweet_attr == "text":
                tweet = parsed_key[key].encode('utf-8')
                tweet = tweet.split(" ")
                for word in tweet:
                    word = word.lower()
                    valid = re.match('^[a-zA-Z-]+$', word) is not None
                    if valid:
                        totalFrequency +=1
                        if word in freq_table:
                            freq_table[word] +=1
                        else:
                            freq_table[word] = 1
    for key in freq_table:
        # print freq_table[key], " ", totalFrequency
        print key, " ", (float)(freq_table[key]/totalFrequency)


def lines(fp):
    print str(len(fp.readlines()))

def main():
    # sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()

import sys
import json

def hw(sent_file, tweet_file):
    dict = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        dict[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        score = 0
        parsedLine = json.loads(line.encode('utf-8'));
        for key in parsedLine.iterkeys():
            encoded = key.encode('utf-8')
            if encoded == "text":
                for word in parsedLine[key].split(" "):
                    if word in dict:
                        score +=dict[word]
        print score


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
if __name__ == '__main__':
    main()

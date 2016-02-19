import sys
import json

def hw(sent_file, tweet_file):
    dict = {}
    for line in sent_file:
        term, score = line.split('\t')
        dict[term] = int(score)

    for line in tweet_file:
        score = 0;
        parsed_line = json.loads(line.encode('utf-8'))
        for key in parsed_line.iterkeys():
            encoded_key = key.encode('utf-8')
            if encoded_key == "text":
                tweet = parsed_line[key].encode('utf-8')
                tweet = tweet.split(" ")
                num_words = 0
                num_exists = 0
                for word in tweet:
                    if word in dict:
                        score +=dict[word]
                        num_exists +=1
                    num_words +=1
                for word in tweet:
                    if word in dict:
                        continue
                    new_score = (float)(score/num_words)
                    dict[word] = new_score
                    print word, " ", new_score

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()

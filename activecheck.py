import urllib
import sys

#specific to feature commit 2
def find_between(s, first, last):
    """ This function finds text between first and last sub strings

    Args:
        s: string to be searched
        first: left substring
        last: right substring

    Returns:
        substring for success, "" otherwise.

    """
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def process_data(link):
    """ This function reads text from a link and generates relevant data

    Args:
        link: data point url.

    Returns:
        dict with user"s name for keys

    """
    data = {}
    f = urllib.urlopen(link)
    chatTxt = f.read().split("\n")
    for line in chatTxt:
        if line:
            name = find_between(line, "<", ">")
            wordcount = len(line.split())-1
            if name in data:
                data[name][0] += 1
                data[name][1] += wordcount
            else:
                data[name] = [1, wordcount]
    return data

def get_active_three(data):
    """ This function derives the three most active users from the output of process_data function

    Args:
        data: as returned from function process_data

    Returns:
        array of three most active users

    """
    f = ["", 0]
    s = ["", 0]
    t = ["", 0]
    for name in data:
        # if number of times a user chats is sufficient, use below metric
        # score = data[name][0]
        # if number of times a user chats along with words written are the metrics, use below line
        score = data[name][0]*data[name][0] + data[name][1]
        if score >= f[1]:
            t = s
            s = f
            f = [name, score]
        elif f[1] > score >= s[1]:
            t = s
            s = [name, score]
        elif score >= 3:
            t = [name, score]
    return [f[0], s[0], t[0]]


def main(url_param):
    if url_param:
        url = url_param
    else:
        url = "https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.txt"
    print get_active_three(process_data(url))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main("")





{"from": u"10",
 "query": {"bool": {"must": [{"match": {"data.business_via_name": "reminderschannel"}},
    {"match": {"type": "message"}},
    {"range": {"data.total_user_messages": {"gt": 0}}},
    {"range": {"data.created_at": {"gte": "2017-08-11T00:45:59Z",
       "lte": "2017-08-11T12:45:59Z"}}},
    {"terms": {"data.client_id": ["006839d264a38b7f58e5c8130447528bf4b7aee1",
       u"420c846133ecff7d705803f6088be56fdcde483a",
       u"5124dc9e9ec750bc51a0b919be23a3406e9d0e29"]}},
    {"range": {"data.created_at": {"gte": "2017-08-10T18:30:35.139Z"
       }}}],
   "must_not": {"match": {"data.message_by": "Others"}},
   "should": []}},
 "size": u"10"}

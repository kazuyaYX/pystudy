import os
import re
from collections import Counter

ignore_words = ["omitted", "media", "a", "able", "about", "above", "abst", "accordance", "according", "accordingly",
                "across", "act", "actually", "added", "adj", "affected", "affecting", "affects", "after", "afterwards",
                "again", "against", "ah", "airport", "alarm", "alive", "all", "almost", "alone", "along", "already",
                "also", "although", "always", "am", "among", "amongst", "an", "and", "angry", "announce", "another",
                "answer", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere",
                "apart", "app", "apparently", "application", "approximately", "are", "aren", "arent", "arise", "arm",
                "around", "as", "aside", "ask", "asking", "at", "auth", "available", "away", "awfully", "b", "back",
                "bad", "bag", "bake", "bar", "be", "became", "because", "become", "becomes", "becoming", "been", "beer",
                "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe",
                "bell", "below", "bend", "beside", "besides", "between", "beyond", "bike", "bill", "biol", "bite",
                "boose", "boss", "both", "brief", "brief", "briefly", "bro", "buddy", "busy", "but", "button", "by",
                "c", "ca", "calculate", "calculated", "call", "called", "calm", "came", "can", "can't", "cannot", "cat",
                "cause", "causes", "certain", "certainly", "chat", "chair", "channel", "check", "close", "closing",
                "clue", "co", "code", "coffee", "com", "come", "comes", "company", "complete", "completed", "congrats",
                "contain", "containing", "contains", "could", "couldnt", "cow", "crash", "cross", "d", "da", "dai",
                "data", "database", "date", "daughter", "day", "db", "delete", "deleted", "desk", "did", "didn't",
                "diet", "different", "dinner", "do", "does", "doesn't", "dog", "doing", "don't", "done", "down",
                "downwards", "drive", "dude", "due", "during", "e-mail", "e", "each", "ear", "ear", "ears", "ease",
                "east", "easy", "ed", "edu", "effect", "eg", "eh", "eight", "eighty", "either", "else", "elsewhere",
                "email", "emp", "empty", "end", "ending", "enough", "error", "especially", "et-al", "et", "etc", "even",
                "evening", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "except",
                "exciting", "eye", "eyes", "f", "far", "fault", "female", "few", "ff", "fifth", "file", "first", "five",
                "fix", "flower", "fly", "followed", "following", "follows", "food", "for", "former", "formerly",
                "forth", "found", "four", "friday", "friend", "from", "fuck", "fun", "funny", "further", "furthermore",
                "g", "garbage", "gate", "gave", "gb", "get", "gets", "getting", "girl", "git", "give", "given", "gives",
                "giving", "glove", "go", "god", "goes", "gone", "good", "got", "gotten", "great", "gross", "guy", "h",
                "ha", "had", "hair", "hall", "happens", "hardly", "has", "hasn't", "hate", "have", "haven't", "having",
                "he", "hed", "hello", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "hereupon",
                "hers", "herself", "hes", "hi", "hid", "high", "him", "himself", "his", "hither", "ho", "holy", "home",
                "hope", "how", "howbeit", "however", "hundred", "husband", "i", "i'll", "i've", "id", "ie", "if", "im",
                "image", "immediate", "immediately", "importance", "important", "in", "inc", "increase", "increased",
                "indeed", "index", "information", "instead", "into", "invention", "inward", "iron", "is", "isn't", "it",
                "it'll", "itd", "its", "itself", "j", "junior", "just", "k", "keep", "keeps", "kept", "kg", "kid",
                "kids", "km", "know", "known", "knows", "l", "largely", "last", "lately", "later", "latter", "latterly",
                "laugh", "least", "leave", "leg", "legs", "less", "lest", "let", "lets", "life", "like", "liked",
                "likely", "line", "list", "little", "ll", "load", "lol", "look", "looking", "looks", "lost", "loud",
                "love", "low", "ltd", "lucky", "lunch", "m", "ma'am", "maam", "madam", "made", "mail", "mainmainly",
                "make", "makes", "male", "mam", "many", "marry", "matemay", "maybe", "mb", "me", "meal", "meals",
                "mean", "means", "meantime", "meanwhile", "men", "menu", "merely", "message", "mg", "might", "million",
                "mineral", "miss", "ml", "mobile", "monday", "monthly", "more", "moreover", "morning", "most", "mostly",
                "move", "movie", "mr", "mrs", "much", "mug", "must", "my", "myself", "n", "na", "name", "named",
                "namely", "nay", "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither",
                "never", "nevertheless", "new", "next", "nine", "ninety", "no", "nobody", "noise", "non", "none",
                "nonetheless", "noone", "nor", "normally", "north", "nos", "not", "noted", "nothing", "now", "nowhere",
                "np", "o", "obtain", "obtained", "obviously", "of", "off", "offer", "often", "oh", "ok", "okay", "old",
                "omitted", "on", "once", "one", "ones", "only", "onto", "open", "opening", "or", "ord", "other",
                "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall",
                "owing", "own", "p", "page", "pages", "part", "particular", "particularly", "past", "pattern", "pause",
                "pay", "pays", "pencil", "per", "perhaps", "phone", "photo", "picture", "ping", "placed", "play",
                "please", "pls", "plus", "pong", "poorly", "possible", "possibly", "potentially", "pp", "predominantly",
                "present", "previously", "primarily", "pro", "probably", "promise", "promptly", "proof", "proud",
                "provides", "pull", "push", "put", "q", "que", "quickly", "quiet", "quit", "quite", "qv", "r", "ran",
                "rather", "ratio", "rd", "re", "readily", "really", "recent", "recently", "ref", "refs", "regarding",
                "regardless", "regards", "related", "relatively", "reload", "reply", "research", "respectively",
                "restraunt", "resulted", "resulting", "results", "right", "rock", "rofl", "roll", "run", "s", "said",
                "same", "saturday", "saw", "say", "saying", "says", "script", "sec", "section", "see", "seeing", "seem",
                "seemed", "seeming", "seems", "seen", "self", "selves", "send", "senior", "sent", "sent", "seven",
                "several", "shall", "she", "she'll", "shed", "shes", "shit", "shock", "should", "shouldn't", "show",
                "showed", "shown", "showns", "shows", "shut", "significant", "significantly", "similar", "similarly",
                "since", "sir", "sirr", "six", "slightly", "slip", "smoke", "so", "some", "somebody", "somehow",
                "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "son", "song",
                "soon", "sorry", "sort", "sound", "south", "specifically", "specified", "specify", "specifying",
                "sport", "sports", "still", "stop", "story", "strongly", "sub", "substantially", "successfully", "such",
                "sufficiently", "suggest", "sunday", "sup", "super", "superb", "sure", "take", "taken", "taking",
                "tall", "tea", "team", "tear", "tell", "temporary", "tends", "term", "test", "text", "th", "than",
                "thank", "thanks", "thanx", "that", "that'll", "that've", "thats", "the", "their", "theirs", "them",
                "themselves", "then", "thence", "there", "there'll", "there've", "thereafter", "thereby", "thered",
                "therefore", "therein", "thereof", "therere", "theres", "thereto", "thereupon", "these", "they",
                "they'll", "they've", "theyd", "theyre", "thing", "think", "this", "those", "thou", "though", "thoughh",
                "thousand", "throat", "throug", "through", "throughout", "thru", "thursday", "thus", "tight", "til",
                "till", "time", "tiny", "tip", "to", "today", "toe", "together", "too", "took", "tooth", "toward",
                "towards", "tower", "town", "translate", "tried", "tries", "truck", "truly", "trust", "try", "trying",
                "ts", "tuesday", "twice", "two", "u", "un", "under", "unfair", "unfortunately", "unless", "unlike",
                "unlikely", "until", "unto", "up", "update", "updated", "upon", "upper", "ups", "us", "use", "used",
                "useful", "usefully", "usefulness", "user", "uses", "using", "usually", "v", "value", "various", "ve",
                "very", "via", "visible", "viz", "vol", "vols", "volume", "vs", "w", "wake", "want", "wants", "was",
                "wash", "wasnt", "way", "we", "we'll", "we've", "web", "website", "wed", "wednesday", "weekend",
                "weekly", "welcome", "went", "were", "werent", "west", "what", "what'll", "whatever", "whats", "when",
                "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon",
                "wherever", "whether", "which", "while", "whim", "whither", "who", "who'll", "whod", "whoever", "whole",
                "whom", "whomever", "whos", "whose", "why", "widely", "wife", "will", "willing", "wish", "with",
                "within", "without", "women", "wont", "words", "work", "works", "world", "would", "wouldnt", "wrap",
                "wtf", "www", "x", "y", "ya", "yeah", "yep", "yes", "yesterday", "yet", "you", "you'll", "you've",
                "youd", "your", "youre", "yours", "yourself", "yourselves", "youth", "z", "zero", "things", "testing",
                "nice", "working", "messages", "issues", "issue", "refresh", "users", "upload", "download", "view",
                "free", "kool", "uh", "duh", "join", "joining", "original", "alright", "large", "entire", "start",
                "month", "sense", "fill"]


def remove_ignore_words(words):
    for word in list(words):
        if word in ignore_words:
            # print(word)
            words.remove(word)
    return words

def get_most_important_word(file):
    word_counter = {}
    txt = file.read().lower()
    txt = re.sub('\W', ' ', txt)
    words = txt.split()
    words =remove_ignore_words(words)
    # print(Counter(words))
    return Counter(words).most_common(1)


def count_important_word(path):
    diary_word_dict = {}
    for filename in os.listdir(path):
        with open(path+'/'+filename, encoding='utf-8') as file:
            im_word = get_most_important_word(file)
            diary_word_dict[filename] = im_word
    return diary_word_dict


if __name__ == '__main__':
    path = 'D:/play/pystudy/0006/test'
    print(count_important_word(path))
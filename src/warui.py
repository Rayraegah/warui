# coding: utf-8
import sys
import automata
from matcher import Matcher, get_words

if sys.version_info[0] >= 3:
    unicode = str


def warui(lang, term, k=1):
    """Find bad words that matches input

    Args:
      lang: Language code such as en, es, fr, jp
      term: Input word
      k: Maximum edit distance
    Yields:
      Number of matches, matched words and probes as Tuple
    """
    if not isinstance(term, unicode):
        term = term.decode('utf-8')

    words = get_words(lang)

    m = Matcher(words)
    li = list(automata.find_all_matches(term, k, m))
    return (len(li), li, m.probes)
    # print m.probes


if __name__ == '__main__':
    args = sys.argv

    if len(args) > 3:
        lang = args[1]
        term = args[2]
        k = int(args[3])
    elif len(args) > 2:
        lang = args[1]
        term = args[2]
        k = 1
    else:
        sys.exit(
            'Invalid arguments \nUse: <language-code> <term> [<varience>]')

    (found, matches, probes) = warui(lang, term, k)
    print(found, '(', ', '.join(matches), ')', probes)

#!/usr/bin/env python3
"""
Various approaches to generating a tally/histogram of syllable counts of words.

Try testing with lots of data, e.g. /srv/datasets/many-english-words.txt
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import collections
import itertools
import re
import sys
import timeit

# Fill a dictionary with entries (word => syllable_count)
syllables = {
  line.lower().strip().translate({ord(";"): ""}): len(line.split(";"))
  for line in open("/srv/datasets/syllables.txt")
}


def procedural_naive(words):
  """
  Not functional programming: Straightforward iteration-based approach.
  """
  results = dict()
  for word in words:
    lower_word = word.lower()
    if lower_word in syllables:
      syllable_count = syllables[lower_word]
      if syllable_count in results:
        results[syllable_count] += 1
      else:
        results[syllable_count] = 1
  return results


def procedural_defaultdict(words):
  """
  Not functional programming: collections.defaultdict avoids having to initialize dict entries.
  """
  results = collections.defaultdict(int)
  for word in words:
    lower_word = word.lower()
    if lower_word in syllables:
      results[syllables[lower_word]] += 1
  return results


def map_filter_map_Counter(words):
  """
  Functional programming:
  1. Map each word to its lowercase representation.
  2. Filter out those words not in the syllables dataset
  3. Map each filtered word to its number of syllables
  4. collections.Counter gives us a tally.
  """
  return collections.Counter(
    map(syllables.__getitem__, filter(syllables.__contains__, map(str.lower, words)))
  )


def procedural_Counter(words):
  """
  Not functional programming: A counterpart to the above function, building the Counter object.
  """
  counts = collections.Counter()
  for word in words:
    lower_word = word.lower()
    if lower_word in syllables:
      counts.update([syllables[lower_word]])
  return counts


def map_filter_map_groupby_map_dict(words):
  """
  Functional programming:
  1. Map each word to its lowercase representation.
  2. Filter out those words not in the syllables dataset
  3. Map each filtered word to its number of syllables
  4. Sort the numbers of syllables to group all distinct numbers together
  5. itertools.groupby will provide group values and group objects
  6. Map a group object to a tuple of the syllable count, and the number of matching words
  7. Give those tuples to the dict constructor
  """
  return dict(
    map(
      lambda group: (group[0], len(list(group[1]))),
      itertools.groupby(
        sorted(
          map(
            syllables.__getitem__, filter(syllables.__contains__, map(str.lower, words))
          )
        )
      ),
    )
  )


def procedural_groupby(words):
  """
  Not functional programming: A counterpart to the above function, building the Counter object.
  """
  syllable_counts = []
  for word in words:
    lower_word = word.lower()
    if lower_word in syllables:
      syllable_counts.append([syllables[lower_word]])
  syllable_counts.sort()
  results = dict()
  for syllable_count, group in itertools.groupby(syllable_counts):
    results[syllable_count[0]] = len(list(group))
  return results


def generator_getitem_Counter(words):
  """
  Functional programming via generator expression:
  1. Generate syllable counts for each word in the syllables dataset.
     (Have to call .lower() on each word twice.)
  2. collections.Counter gives us a tally.
  """
  return collections.Counter(
    syllables[word.lower()] for word in words if word.lower() in syllables
  )


def generator_assignment_expression_getitem_Counter(words):
  """
  Functional programming via generator expression:
  1. Generate syllable counts for each lowercase word in the syllables dataset.
     (Assignment expression avoids having to call .lower() on each word twice.)
  2. collections.Counter gives us a tally.

  See: https://www.python.org/dev/peps/pep-0572/
  See: https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
  """
  return collections.Counter(
    syllables[lower_word] for word in words if (lower_word := word.lower()) in syllables
  )


if __name__ == "__main__":
  # Break input into words (see: https://docs.python.org/3/library/re.html)
  all_words = re.split(r"\W+", sys.stdin.read())
  number = 10 if len(sys.argv) < 2 else int(sys.argv[1])
  print(f"Testing each function {number} time(s) each. Input contains {len(all_words)} words.")
  return_values = set()
  timings = []
  functions = (
    procedural_naive,
    procedural_defaultdict,
    map_filter_map_Counter,
    procedural_Counter,
    map_filter_map_groupby_map_dict,
    procedural_groupby,
    generator_getitem_Counter,
    generator_assignment_expression_getitem_Counter,
  )
  for fun in functions:
    duration = timeit.timeit(
      stmt=f"return_values.add(tuple(sorted({fun.__name__}(all_words).items())))",
      globals=globals(),
      number=number,
    )
    timings.append((duration, fun.__name__))
  print(return_values)
  assert len(set(return_values)) == 1
  for duration, fun_name in sorted(timings):
    print(f"{fun_name:{max(len(fun.__name__) for fun in functions)}} : {duration:.15f}")
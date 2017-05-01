from functools import reduce


class WordBucket:
    def __init__(self, words):
        self.words = words


# combines two dicts of format key->count:int by combining the string so they are key->count1+count2
def update_counts(acc, item):
    return reduce(lambda a, i: increment(a, i[0], i[1]), item.items(), acc)


# given a dictionary of key->int, increment by count (defaults to 1)
def increment(acc, item, count=1):
    u = acc.copy()
    u.update({item: acc.get(item, 0) + count})
    return u


# create final map count
def to_count_dict(the_list):
    return reduce(lambda acc, item: increment(acc, item), the_list, {})


def main():

    word_buckets = [WordBucket(['foo', 'bar', 'baz']), WordBucket(['baz']), WordBucket(['foo', 'foo'])]

    count_dicts = list(map(lambda a: to_count_dict(a.words), word_buckets))

    print(reduce(update_counts, count_dicts, {}))


main()
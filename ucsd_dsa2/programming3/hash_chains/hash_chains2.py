# python3
# done
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range(bucket_count)]  #create bucket
        #need to pay extra care

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):     #return inputted command
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(self.elems[query.ind][::-1])
            #query.ind is the bucket number
        else:
            index=self._hash_func(query.s)
            #print(index)
            if query.type == 'find':
                was_found=False
                for i in self.elems[index]:
                    if i == query.s:
                        was_found=True
                        break
                self.write_search_result(was_found)

            elif query.type == 'add':
                #print(index)
                was_found=False
                for i in self.elems[index]:
                    if i==query.s:
                        was_found=True
                if not was_found:
                    self.elems[index].append(query.s)
                    #print(self.elems)
            else:
                if query.s in self.elems[index]:
                    self.elems[index].remove(query.s)
                

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

# python3
#done
class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []


    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def parent(self,i):          #0_based index
        return (i+1)/2-1

    def lc(self,i):
        return (i+1)*2-1

    def rc(self,i):
        return 2*(i+1)

    def siftdown(self,i):
        #print(i)
        maxindex=i                    #actually min
        l=self.lc(i)
        if (l<len(self._data)) :
            if (self._data[l]<self._data[maxindex]) :
                maxindex=l
        r=self.rc(i)
        if (r<len(self._data)) :
            if (self._data[r]<self._data[maxindex]) :
                maxindex=r
        if i!=maxindex:
            self._data[i],self._data[maxindex]=self._data[maxindex],self._data[i]
            self._swaps.append((i,maxindex))
            self.siftdown(maxindex)

    def new_gen(self):
        n=len(self._data)
        for i in range(int(n/2),-1,-1):
            self.siftdown(i)
        #print(self._data)



    def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def Solve(self):
        self.ReadData()
        self.new_gen()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

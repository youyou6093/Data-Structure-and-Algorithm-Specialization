# python3
# done
class th:
    def __init__(self,index,value):
        self.index=index
        self.value=value
    
    def __lt__(self,other):
        if self.value<other.value:
            return True
        elif self.value==other.value:
            if self.index<other.index:
                return True
        return False
    
    def __eq__(self,other):
        if (self.value==other.value) & (self.index==other.index):
            return True
        else:
            return False
        
    def __gt__(self,other):
        return  (not (self.__lt__(other))) & (not (self.__eq__(other)))

class my_heap:
    def __init__(self,n):
        self.data=[]
        for i in range(n):
            self.data.append(th(i,0))
    
    def output(self):
        for i in self.data:
            print (i.index,i.value)
            
    def parent(self,i):
        return int((i+1)/2)-1
    
    def lc(self,i):
        return (i+1)*2-1
    
    def rc(slef,i):
        return 2*(i+1)
    
    def siftdown(self,i):
        #print(i)
        size=len(self.data)
        maxindex=i                    #actually min
        l=self.lc(i)
        if (l<size) :
            if (self.data[l]<self.data[maxindex]) :
                maxindex=l
        r=self.rc(i)
        if (r<size) :
            if (self.data[r]<self.data[maxindex]) :
                maxindex=r
        if i!=maxindex:
            self.data[i],self.data[maxindex]=self.data[maxindex],self.data[i]
            self.siftdown(maxindex)
            
            
    def siftup(self,i):
        while(i>0):
            if self.data[self.parent(i)] > self.data[i] : 
                self.data[self.parent(i)],self.data[i]=self.data[i],self.data[self.parent(i)]
                i=self.parent(i)
            else:
                break
    
    def insert(self,node):
        self.data.append(node)
        size=len(self.data)
        self.siftup(size-1)
    
    def pop_min(self):
        if len(self.data)==1:
            result=self.data[0]
            self.data=[]
            return result
        result=self.data[0]
        self.data[0]=self.data.pop()
        self.siftdown(0)
        return result
        
    def get_min(self):
        return self.data[0].value
                






class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        #print("xxx")
        #print(len(self.jobs))
        for i in range(len(self.assigned_workers)):
          #print("xxx")
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):

      total_time=0
      self.assigned_workers=[]
      self.start_times=[]
      x=my_heap(self.num_workers)             #put all workers into heap
      self.jobs=self.jobs[::-1]               #reverse the jobs
      while(self.jobs!=[]):
        #print('kkk')
        worker=x.pop_min()                          #assign a worker
        self.assigned_workers.append(worker.index)  # index of the worker    
        self.start_times.append(worker.value)       # start time of this job  
        worker.value+=self.jobs.pop()               
        # add the time needed for this job to this worker                 
        x.insert(worker) #put this worker back to heap
      #print(self.assigned_workers)
      #print(self.start_times)

    def assign_jobs_old(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()


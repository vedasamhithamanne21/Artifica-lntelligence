class GFG :
    @staticmethod
    def towerOfHanoi( n,  from_rod,  to_rod,  aux_rod) :
        if (n == 0) :
            return
        GFG.towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
        print("Move disk " + str(n) + " from rod " + str(from_rod) + " to rod " + str(to_rod))
        GFG.towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
    # Driver code
    @staticmethod
    def main( args) :
        n = 5
        # Number of disks
        GFG.towerOfHanoi(n, 'A', 'C', 'B')
    

if __name__=="__main__":
    GFG.main([])
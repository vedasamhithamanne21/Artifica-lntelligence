import math
import sys


class compute_a_posteriori :
    @staticmethod
    def main() :
        if (len(sys.argv) < 2) :
            try :
                myWriter =  open("result.txt","w")
                myWriter.close()
            except :
                print("An error occurred.")
                
        else :
            Q = sys.argv[1]
            l = len(Q)
            preprint = "Observation sequence Q: " + Q + "\nLength of Q: " + str(l) + "\n"
            # System.out.println(preprint);
            try :
                myWriter =  open("result.txt","w")
                myWriter.write(preprint)
                i = 0
                while (i < l) :
                    subStr = Q[0:i + 1]
                    obsno = i + 1
                    nc = 0
                    nl = 0
                    u = 0
                    while (u < len(subStr)) :
                        if (subStr[u] == 'C') :
                            nc = 1 + nc
                        else :
                            nl = 1 + nl
                        u = 1 + u

                    


                    pnch1 = 1
                    pnch2 = (0.75 ** nc)
                    pnch3 = (0.5 ** nc)
                    pnch4 = (0.25 ** nc)
                    pnch5 = 0 ** nc
                    pnlh1 = (0**nl)
                    pnlh2 = (0.25**nl)
                    pnlh3 = (0.5**nl)
                    pnlh4 = (0.75**nl)
                    pnlh5 = 1
                    qh1 = (pnch1 * pnlh1) * 0.1
                    qh2 = (pnch2 * pnlh2) * 0.2
                    qh3 = (pnch3 * pnlh3) * 0.4
                    qh4 = (pnch4 * pnlh4) * 0.2
                    qh5 = (pnch5 * pnlh5) * 0.1
                    q = qh1 + qh2 + qh3 + qh4 + qh5
                    h1q = qh1 / q
                    h2q = qh2 / q
                    h3q = qh3 / q
                    h4q = qh4 / q
                    h5q = qh5 / q
                    pcq = h1q * 1 + h2q * 0.75 + h3q * 0.5 + h4q * 0.25
                    plq = 1 - pcq

                    



                    toPrint = "\nAfter Observation " + str(obsno) + " = " + str(Q[i]) + ":\n\nP(h1 | Q) = " + str(h1q) + "\nP(h2 | Q) = " + str(h2q) + "\nP(h3 | Q) = " + str(h3q) + "\nP(h4 | Q) = " + str(h4q) + "\nP(h5 | Q) = " + str(h5q) + "\n\nProbability that the next candy we pick will be C, given Q: " + str(pcq) + "\nProbability that the next candy we pick will be L, given Q: " + str(plq) + "\n"
                    toPrint = str(toPrint)

                    
                    # System.out.println(toPrint);
                    


                    myWriter.write(toPrint)
                    i = 1+i

                    
                myWriter.close()
            except :
                print("An error occurred.")
                
                
    

if __name__=="__main__":
    compute_a_posteriori.main()
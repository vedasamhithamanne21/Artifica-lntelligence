import sys
class bnet :
    alarmMap =  dict()
    johnCallMap =  dict()
    maryCallMap =  dict()
    burglaryMap =  dict()
    earthquakeMap =  dict()
    cMap = None
    gMap = None
    
    def  computeProbability( burglary,  earthquake,  alarm,  johnCall,  maryCall) :
        computedProbability = 0.0
        burglaryVal = 0.0
        earthquakeVal = 0.0
        alarmVal = 0.0
        johnCallVal = 0.0
        maryCallVal = 0.0
        burglaryVal = bnet.burglaryMap.get("BT")
        earthquakeVal = bnet.earthquakeMap.get("ET")
        alarmVal = bnet.alarmMap.get("AT|B" + str(burglary) + ",E" + str(earthquake))
        johnCallVal = bnet.johnCallMap.get("JT|A" + str(alarm))
        maryCallVal = bnet.maryCallMap.get("MT|A" + str(alarm))
        if (burglary == 'F') :
            burglaryVal = 1.0 - burglaryVal
        if (earthquake == 'F') :
            earthquakeVal = 1.0 - earthquakeVal
        if (alarm == 'F') :
            alarmVal = 1.0 - alarmVal
        if (johnCall == 'F') :
            johnCallVal = 1.0 - johnCallVal
        if (maryCall == 'F') :
            maryCallVal = 1.0 - maryCallVal
        computedProbability = burglaryVal * earthquakeVal * alarmVal * johnCallVal * maryCallVal
        return computedProbability
    
    def  generateRemainingPossibleValues( passedMap) :
        possibleVal =  dict()
        givenMapProb = None
        if (not (('B' in passedMap.keys()))) :
            givenMapProb =  []
            givenMapProb.append('T')
            givenMapProb.append('F')
            possibleVal['B'] = givenMapProb
        if (not (('E' in passedMap.keys()))) :
            givenMapProb =  []
            givenMapProb.append('T')
            givenMapProb.append('F')
            possibleVal['E'] = givenMapProb
        if (not (('A' in passedMap.keys()))) :
            givenMapProb =  []
            givenMapProb.append('T')
            givenMapProb.append('F')
            possibleVal['A'] = givenMapProb
        if (not (('J' in passedMap.keys()))) :
            givenMapProb =  []
            givenMapProb.append('T')
            givenMapProb.append('F')
            possibleVal['J'] = givenMapProb
        if (not (('M' in passedMap.keys()))) :
            givenMapProb =  []
            givenMapProb.append('T')
            givenMapProb.append('F')
            possibleVal['M'] = givenMapProb
        return possibleVal
    
    
    
    def main( ) :
        bnet.burglaryMap["BT"] = 0.001
        bnet.earthquakeMap["ET"] = 0.002
        bnet.alarmMap["AT|BT,ET"] = 0.95
        bnet.alarmMap["AT|BT,EF"] = 0.94
        bnet.alarmMap["AT|BF,ET"] = 0.29
        bnet.alarmMap["AT|BF,EF"] = 0.001
        bnet.johnCallMap["JT|AT"] = 0.9
        bnet.johnCallMap["JT|AF"] = 0.05
        bnet.maryCallMap["MT|AT"] = 0.7
        bnet.maryCallMap["MT|AF"] = 0.01
        countt = 0
        bnet.gMap =  dict()
        bnet.cMap =  dict()
        i=1
        for strr in sys.argv :
            if i==1:
                i=2
                continue
            givenMapProb =  []
            if (strr.lower() == ("given").lower()) :
                countt = 1
                continue
            if (countt == 0) :
                temp = strr.upper()
                givenMapProb.append(temp[1])
                bnet.cMap[temp[0]] = givenMapProb
            else :
                temp = strr.upper()
                givenMapProb.append(temp[1])
                bnet.gMap[temp[0]] = givenMapProb
        bnet.cMap.update(bnet.gMap)
        bnet.cMap.update(bnet.generateRemainingPossibleValues(bnet.cMap))
        bnet.gMap.update(bnet.generateRemainingPossibleValues(bnet.gMap))
        finalProbb = 0.0
        denomVal = 0.0
        b = 0
        while (b < len(bnet.cMap.get('B'))) :
            e = 0
            while (e < len(bnet.cMap.get('E'))) :
                a = 0
                while (a < len(bnet.cMap.get('A'))) :
                    j = 0
                    while (j < len(bnet.cMap.get('J'))) :
                        m = 0
                        while (m < len(bnet.cMap.get('M'))) :
                            finalProbb += bnet.computeProbability(bnet.cMap.get('B')[b], bnet.cMap.get('E')[e], bnet.cMap.get('A')[a], bnet.cMap.get('J')[j], bnet.cMap.get('M')[m])
                            m += 1
                        j += 1
                    a += 1
                e += 1
            b += 1
        if (countt == 1) :
            i = 0
            while (i < len(bnet.gMap.get('B'))) :
                j = 0
                while (j < len(bnet.gMap.get('E'))) :
                    k = 0
                    while (k < len(bnet.gMap.get('A'))) :
                        l = 0
                        while (l < len(bnet.gMap.get('J'))) :
                            m = 0
                            while (m < len(bnet.gMap.get('M'))) :
                                denomVal += bnet.computeProbability(bnet.gMap.get('B')[i], bnet.gMap.get('E')[j], bnet.gMap.get('A')[k], bnet.gMap.get('J')[l], bnet.gMap.get('M')[m])
                                m += 1
                            l += 1
                        k += 1
                    j += 1
                i += 1
            finalProbb = finalProbb / denomVal
        print("Probability = " + str(finalProbb))
    

if __name__=="__main__":
    bnet.main()
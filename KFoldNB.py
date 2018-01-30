        nb = NaiveBayes(0)
        n = len(values)
        average =[]
        for value in range(0,n):
            currList = a[:value] + a[value+1:]
            average.append((value,validate(train(currList),values[i])))
        totalAverage = float(sum(average)) / float(len(values))

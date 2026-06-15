class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hash to timing character each element
        # hash = {
            # cat : {
                # a : 1
                # c : 1
                # t : 1
            #}

            # act : {
                # c : 1
                # a : 1
                # t : 1
            #}

            
        #}

       # 1
         # i = 0 j = 1 act, pots
         # i = 0 j = 2 act , tops
         # i = 0 j = 3 act, cat => ["act","pots","tops","stop","hat"]
         # i = 0 j = 3 act, stop 
         # i = 0 j = 4 act ,hat

       # 2
        # i = 1 j = 2 pots , tops =>  ["act","pots","stop","hat"]
        # i = 1 j = 2 pots, stop =>  ["act","pots","hat"]
        # i = 2 j = 3 pots, hat
        # i = 2 j = 4
        hash ={}
        for i in range(len(strs)):
            subhash = {}
            for j in range(len(strs[i])):
               count = strs[i].count(strs[i][j])
               subhash[strs[i][j]] = count
            hash[strs[i]] = subhash
        # compare hash and group in list
        size = len(strs)
        i = 0
        skipIndex = []
        groupElement = []
        while(i<size):
            if i in skipIndex :
                i+=1
                continue
            if i == size - 1 :
               groupElement.append([strs[i]])
               break   
            j=i+1
            tmp = []
            isFirst = True
            while(j<size):
                if(hash[strs[i]] == hash[strs[j]]):
                    if isFirst: tmp.append(strs[i])
                    isFirst = False
                    tmp.append(strs[j])
                    skipIndex.append(j)
                j+=1
            if  isFirst:
               groupElement.append([strs[i]])
            else:
                groupElement.append(tmp)
            i+=1
        
        for i in range (len(groupElement)):
            if len(groupElement[i]) == 0 :
                groupElement[i].append("")
        return groupElement


            

            
        
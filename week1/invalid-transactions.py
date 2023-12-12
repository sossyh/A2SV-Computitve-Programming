class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        problem: returning invalid transactions
                input: list of tranaction
        
        Solution:
                    1. use a hashmap - name as a key value list which contains touple (idx, time, city)
                    2. if name not in the hashmap - will be created
                    3. iterave over all transactions in that and check for the invalid one
                    4. if invalid taransaction is found will append to my golbal result
                    5. iterae over each transaction and append transactions which amount >= 1000
        
        {"alice" : [(0, 20, mtv)]}

        example: 
         ["alice,20,800,mtv","alice,50,100,beijing","alice,70,1200,d"]

        time and space complexty analysis
        N = len(transactions)
        TC: O(N**2) 10**6
        SP: O(N)

        """

        for i in range(len(transactions)):
            transactions[i] =  transactions[i].split(",")
        
        invalid_transaction_set = set()
        invalid_transaction = []


        hashmap = defaultdict(list)


        for idx in range(len(transactions)):
            name, time, amount, city = transactions[idx]
            trans1, trans2 = None, None
            if name in hashmap:
                for other_trans in hashmap[name]:
                    if abs(int(other_trans[1]) - int(time)) <= 60 and other_trans[2] != city:
                        if idx not in invalid_transaction_set:
                            trans1 = invalid_transaction.append(",".join(transactions[idx]))
                        if other_trans[0] not in invalid_transaction_set:
                            trans2 = invalid_transaction.append(",".join(transactions[other_trans[0]]))
                        invalid_transaction_set.add(idx)
                        invalid_transaction_set.add(other_trans[0])
                        
            
            hashmap[name].append((idx, time, city, amount))

            if idx not in invalid_transaction_set and int(transactions[idx][2]) > 1000:
                invalid_transaction.append(",".join(transactions[idx]))
                invalid_transaction_set.add(idx)
        
        return invalid_transaction





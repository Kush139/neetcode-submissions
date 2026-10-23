class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #bfs is good to find minimum path
        #represent words as nodes
        
        #  want to construct adjacency list\
        visiting = set()
        def bfs(node):
            q = deque([node])
            visiting.add(node)
            count = 1
            while q:
                for _ in range(len(q)):
                    word = q.popleft()
                    if word == endWord:
                        return count
                    for w in wordList:
                        diff = 0
                        for s in range(len(word)):
                            if w[s] != word[s]:
                                diff += 1
                        if diff == 1:
                            if w not in visiting:
                                visiting.add(w)
                                q.append(w)
                count += 1

            

        ans = bfs(beginWord)
        return ans if ans else 0
        

            



        
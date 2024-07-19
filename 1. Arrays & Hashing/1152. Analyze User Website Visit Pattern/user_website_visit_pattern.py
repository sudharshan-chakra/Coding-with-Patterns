class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        res = []
        G = defaultdict(list)
        for time, user, site in sorted(zip(timestamp, username, website)):
            G[user].append(site)
        
        counter = defaultdict(int)
        for user, sites in G.items():
            for combo in set(itertools.combinations(sites,3)):
                counter[combo] += 1

        max_count, max_combo = 0,set()
        for combo, count in counter.items():
            if count > max_count or (count == max_count and combo < max_combo):
                max_count = count
                max_combo = combo

        return list(max_combo)
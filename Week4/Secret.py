class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        new_discovery = [0] * (n + 1)
        new_discovery[1] = 1
        prefix = [0] * (n + 1)
        prefix[1] = 1
        
        for i in range (2, n + 1):
            start = max(1, i - forget + 1)
            end = i - delay
            if end < start:
                new_discovery[i] = 0
            else:
                if start > 1:
                    sum_val = prefix[end] - prefix[start - 1]
                else:
                    sum_val = prefix[end]
                new_discovery[i] = sum_val % MOD
            prefix[i] = (prefix[i - 1] + new_discovery[i]) % MOD
        
        total_start = max(1, n - forget + 1)
        total = (prefix[n] - prefix[total_start - 1]) % MOD if total_start > 1 else prefix[n]
        return total
                


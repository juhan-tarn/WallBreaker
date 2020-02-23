class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = collections.defaultdict(int)
        
        for cpdomain in cpdomains:
            cpdomain_tokens = cpdomain.split()
            visit_count = int(cpdomain_tokens[0])
            domain = cpdomain_tokens[1].split('.')
            
            current_domain = ""
            for sub in domain[::-1]:
                if current_domain == "":
                    current_domain = sub
                else:
                    current_domain = sub + "." + current_domain
                domain_count[current_domain] += visit_count
        
        results = []
        for key in domain_count.keys():
            results.append(str(domain_count[key]) + " " + key)
        return results
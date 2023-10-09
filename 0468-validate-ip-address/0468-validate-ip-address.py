class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = r'^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}$'
        ipv6 = r'^([0-9A-Fa-f]){1,4}:([0-9A-Fa-f]){1,4}:([0-9A-Fa-f]){1,4}:([0-9A-Fa-f]){1,4}:([0-9A-Fa-f]){1,4}:([0-9A-Fa-f]){1,4}:([0-9A-Fa-f]){1,4}:([0-9A-Fa-f]){1,4}$'
        
        if re.search(ipv6, queryIP):
            return "IPv6"
        
        if re.search(ipv4, queryIP):
            return "IPv4"
        
        return "Neither"
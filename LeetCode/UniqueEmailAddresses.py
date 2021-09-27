class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        canonical_addresses = set()
        for email in emails:
            local, domain = email.split('@')
            canonical_local = local.split('+')[0].replace('.', '')
            canonical_addresses.add('@'.join([canonical_local, domain]))
        return len(canonical_addresses)

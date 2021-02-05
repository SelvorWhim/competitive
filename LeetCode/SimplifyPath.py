class Solution:
    def simplifyPath(self, path: str) -> str:
        #path = path.rstrip('/').replace('//', '/').replace('/./', '/')
        parts = []
        for part in path.split('/'):
            if part == '..':
                if len(parts) > 0:
                    del parts[-1]
            elif part not in ['', '.']:
                parts.append(part)
        return '/' + '/'.join(parts)

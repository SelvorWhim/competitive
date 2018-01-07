// idea: the smallest cookie will, at best, satisfy the least greedy child, and if not, we may as well throw it away, since we can't add it to another cookie
// likewise for every cookie from the smallest. By extension, there's no reason to try satisfying a more greedy child before the least greedy
// so sort both groups ascending, and go through cookies until the least greedy child left is satisfied, then move on to the next child and continue with the remaining cookies

public class Solution
{
    public int FindContentChildren(int[] g, int[] s)
    {
        if (s.Length < 1) return 0;
        Array.Sort(g); // kids
        Array.Sort(s); // cookies
        int ik = 0;
        int ic = 0;
        int sat = 0;
        while (ik < g.Length && ic < s.Length)
        {
            if (g[ik] <= s[ic])
            {
                sat++;
                ik++;
            }
            ic++;
        }
        return sat;
    }
}

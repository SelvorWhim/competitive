public class Solution
{
    public string ComplexNumberMultiply(string a, string b)
    {
        int i_plus = a.IndexOf('+');
        int ar = int.Parse(a.Substring(0, i_plus));
        int ai = int.Parse(a.Substring(i_plus + 1, a.Length - i_plus - 2)); // stoi should stop at the i, not throw an error
        i_plus = b.IndexOf('+');
        int br = int.Parse(b.Substring(0, i_plus));
        int bi = int.Parse(b.Substring(i_plus + 1, b.Length - i_plus - 2));
        int cr = (ar * br) - (ai * bi);
        int ci = (ar * bi) + (ai * br);
        return cr + "+" + ci + "i";
    }
};

public class S
{

	public static int kam(int k, int[] a, int s, int e)
	{
		if (s == e)
		{
			if (a[s] > k)
			{
				return a[s];
			}
			return 0;
		}
		int p1 = kam(k, a, s, (s + e) / 2);
		int p2 = kam(k, a, (s + e) / 2 + 1	, e);
		return p1 + p2;
	}
	public static void main(String[] args)
	{
		int[] a = { 2, 8, 4, 14, 5, 18 };
		System.out.println(kam(1, a, 0, 2));
		System.out.println(kam(1, a, 1, 3));
		System.out.println(kam(1, a, 2, 4));
		System.out.println(kam(1, a, 3, 5));
	}
}
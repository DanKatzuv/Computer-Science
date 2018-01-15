import java.util.Arrays;
import java.util.Scanner;

public class CW20180115
{
	static Scanner input = new Scanner(System.in);

	private static Node<Double> getList()
	{
		Node<Double> first = new Node<Double>(-1.0), current = first;
		first.setNext(current);
		System.out.println("Enter a list of numbers, stop by entering -999:");
		double number = input.nextDouble();
		while (number != -999)
		{
			current.setNext(new Node<Double>(number));
			current = current.getNext();
			number = input.nextDouble();
		}

		return first.getNext();
	}

	private static Node<Double> cut(Node<Double> list, Node<Double> first, Node<Double> last)
	{
		list = first;
		while (first != last)
		{
			first = first.getNext();
		}
		first.setNext(null);
		return list;
	}
	private static Node<Double>[] split(Node<Double> list)
	{
		Node<Double>[] sublists = null;
		Node<Double> firstInSublist = list, current = list;
		while (current != null)
		{
			if (list.getValue() == 0)
			{
				sublists = copyof(cut(list, firstInSublist, current), sublists.length + 1);
			}
		}
	}
	
	private static void removeMax(Node<Double> list)
	{	
		Node<Double> current = list;
		while (current != null)
		{
			
		}
	}

	public static void main(String[] args)
	{
		System.out.println(getList());
	}

}

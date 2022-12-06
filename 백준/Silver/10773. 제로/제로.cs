using System.Collections.Generic;
using System;
using System.Linq;

namespace Exam03
{

    class Program
    {

        static void Main(string[] args)
        {
            Stack<int> stack = new Stack<int>();

            int a = Int32.Parse(Console.ReadLine());

            for(int i=0; i<a; i++)
            {
                int n = Int32.Parse(Console.ReadLine());

                if (n != 0)
                {
                    stack.Push(n);
                }
                else
                {
                    stack.Pop();
                }
            }
            Console.WriteLine(stack.Sum());
        }
    }
}
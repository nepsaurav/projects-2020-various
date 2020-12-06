using System;
using System.Linq;

namespace tinker
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string[] nums = new string[]{"3671", "23123", "123123"};
            var linqTest = nums.Select(y => y.First());
            Console.WriteLine("First Test");
            Console.WriteLine(linqTest);
            
            int[] digits = new int[3];

            for(int i = 0; i < nums.Length; i++){
                int val = Int32.Parse(nums[i]);
                digits[i] = val;
            }
            Console.WriteLine("Second Test");
            foreach(int item in digits){
                Console.WriteLine("{0} ", item);
            }
        }
    }
}

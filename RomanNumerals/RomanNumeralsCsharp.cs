namespace RomanNumeralsCsharpImplementation
{
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;


    public static class RomanNumeralsCsharp
    {
        public static LinkedList<KeyValuePair<string, int>> ROMAN_NUMBERS = new LinkedList<KeyValuePair<string, int>>();
        
    static void Main(string[] args)
    {
        ToRoman(1);
    }

        public static void initNumbers() {
            ROMAN_NUMBERS.AddLast(new KeyValuePair<string, int>( "M", 1000 ));
            ROMAN_NUMBERS.AddLast(new KeyValuePair<string, int>( "D", 500 ));
            ROMAN_NUMBERS.AddLast(new KeyValuePair<string, int>( "C", 100 ));
            ROMAN_NUMBERS.AddLast(new KeyValuePair<string, int>( "L", 50 ));
            ROMAN_NUMBERS.AddLast(new KeyValuePair<string, int>( "X", 10 ));
            ROMAN_NUMBERS.AddLast(new KeyValuePair<string, int>( "V", 5 ));
            ROMAN_NUMBERS.AddLast(new KeyValuePair<string, int>( "I", 1 ));
        }

        public static string ToRoman(this int value)
        {
            if(ROMAN_NUMBERS.Count == 0) {
                initNumbers();
            }

            string romanNumbers = "";
            // Implement me
            var iterator = ROMAN_NUMBERS.GetEnumerator();
            iterator.MoveNext();

            while(value > 0) {
                int quotient = value / iterator.Current.Value;

                if(quotient == 0 ) {

                    foreach(var ele in new int[]{100, 10, 1}) {
                        if(10* ele < iterator.Current.Value || iterator.Current.Value == ele) {
                            continue;
                        }
                        if(value - (iterator.Current.Value - ele) >= 0) {
                            romanNumbers += ROMAN_NUMBERS.First(x => x.Value == ele).Key + "" +  iterator.Current.Key;
                            value = 0;
                            break;
                        }
                    }

                } else {
                    romanNumbers += string.Concat(Enumerable.Repeat(iterator.Current.Key, quotient));
                }
                
                value = value-(quotient*iterator.Current.Value);
                

                iterator.MoveNext();
            }

            return romanNumbers;
        }

}
}
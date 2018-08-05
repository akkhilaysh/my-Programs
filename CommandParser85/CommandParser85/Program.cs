using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace CommandParser85
{
    class Program
    {
        static void Main(string[] args)
        {
            var singleLoopFilePath = @"K:\NoLoopExample.txt";
            string readAllText = File.ReadAllText(singleLoopFilePath);

            List<string> list = new List<string>(Regex.Split(readAllText, Environment.NewLine));

            NoLoopExample obj = new NoLoopExample();
            obj.NoLoop(list, singleLoopFilePath);
        }
    }
}

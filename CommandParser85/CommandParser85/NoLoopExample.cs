using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace CommandParser85
{
    class NoLoopExample
    {
        public void NoLoop(List<string> list, string example_file)
        {
            var path = $"{Path.GetDirectoryName(example_file)}\\{Path.GetFileNameWithoutExtension(example_file)}Complete{Path.GetExtension(example_file)}";
            
            var commentPattern = @"\s*^(#.+)";
            Match commentCheck = Regex.Match(list_item, commentPattern, RegexOptions.Singleline);
            
            List<string> new_list = new List<string>();

            foreach (var list_item in list)
            {               
                if (!commentCheck.Success)
                    new_list.Add(list_item);
            }

            foreach (var list_item in new_list)
            {
                File.AppendAllText(path, list_item.ToString() + Environment.NewLine);
            }
        }
    }
}

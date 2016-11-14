
%{
#include<iostream>
using namespace std;


%}



%%

class|public|static|void|String|int 		{cout<<"\n"<<yytext<<"  ==>  "<<"Keyword";}
main|System.out.println				{cout<<"\n"<<yytext<<"  ==>  "<<"Standard Function";}
\/\*[^\*\/]*\*\/|\/\/[^*/]*			{cout<<"\n"<<yytext<<"  ==>  "<<"Comment";}
[\[|\]|(|)|;|{|}|=]		 		{cout<<"\n"<<yytext<<"  ==>  "<<"Special Symbol";}
[+|-|*|/|<|>]		 			{cout<<"\n"<<yytext<<"  ==>  "<<"Operator";}
\".*\" 						{cout<<"\n"<<yytext<<"  ==>  "<<"String";}
[a-zA-Z]+[a-zA_Z]* 				{cout<<"\n"<<yytext<<"  ==>  "<<"Identifier";}
[0-9]*						{cout<<"\n"<<yytext<<"  ==>  "<<"Digits";}
%%

int main()
{
  cout<<"\n\n";
  FILE *fp;
  fp=fopen("inputjava.txt","r");
  yyin=fp;
  yylex();
}  

int yywrap()
{
  return(1);
}

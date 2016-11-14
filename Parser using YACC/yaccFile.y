%{
#include<stdio.h>
#include<string.h>
int yywrap()
{
  return 1;
}
int yyerror()
{
  printf("BZZZZZZZ. ERROR.");
}
%}

%token NUM ID SP OP EQ

%%
S: Sentence
   {
      printf("Valid Statement.");
   }

Sentence : ID OP ID |
           ID OP NUM |
           NUM OP ID |
           NUM OP NUM |
	   ID EQ NUM
           ;

%%
void main()
{
  printf("    Enter Expression:    ");
  yyparse();
}


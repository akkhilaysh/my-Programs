//Aim : Implementing recursive descent parser for sample language.

#include<iostream>
#include<string.h>
#include<ctype.h>
#include<stdio.h>

using namespace std;
class rdp
{
public:
char input[10];
int i,error;
void E();
void T();
void Eprime();
void Tprime();
void F();
};
      
       main()
          {
          rdp a;
          a.i=0;
          a.error=0;
                cout<<"Enter an arithmetic expression  :  ";
                cin>>a.input;
                a.E();
                if(strlen(a.input)==a.i&&a.error==0)
                        cout<<"\n Accepted! :)\n";
                else cout<<"\n Rejected :(\n";
          }
        
        

void rdp:: E()
{
     T();
     Eprime();
}
void rdp:: Eprime()
{
     if(input[i]=='+')
     {
     i++;
     T();
     Eprime();
     }
     }
void rdp:: T()
{
     F();
     Tprime();
}
void rdp:: Tprime()
{
     if(input[i]=='*')
     {
                      i++;
                      F();
                      Tprime();
                      }
                      }
     void rdp:: F()
     {
          if(isalnum(input[i]))i++;
          else if(input[i]=='(')
          {
          i++;
          E();
          if(input[i]==')')
          i++;

          else error=1;
            }
       
          else error=1;
          }


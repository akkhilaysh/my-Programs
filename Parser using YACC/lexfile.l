%{

#include"y.tab.h"

%}

%%

[a-z]* 		{return ID;}
[0-9]+ 		{return NUM;}
[\+\-\*\/] 	{return OP;}
=			{return EQ;}
%%


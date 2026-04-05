Lab Exercise : 3)
Write a C program that includes variables, constants, and comments. Declare and use different data types (int, char, float) and display their values.
//header file
#include<stdio.h>
//main function
int main()
    {
        #variable declaration:-
        int Roll_No = 1;
        char Division = 'A';
        float Percentage = 97.65;
//for display output
        print("Roll_No = %d",Roll_No);
        print("Dividion %d= ",Division);
        print("Percentage %d= ",percentage);
        
        return 0;
    }


=========================================================================================++++++++++++
    Lab Exercise : 4)
    Write a C program that accepts two integers from the user and performs arithmetic, 
    relational, and logical operations on them. Display the results.
    //variable just declare not intilization
    int a,b;

    //Take input from user
    printf("Enter Value of First Number :\n");
    scanf("%d",&a);

    printf("Enter B+Value of Second Number :\n");
    scanf("%d",&b);

    //Airthmatic opration
    printf("sum   = %d\n",a+b);
    printf("difrence=%d \n",a-b);
    printf("Multiply= %d\n",a*b);
    printf("Division= %d\n",a/b);
    printf("Reminder=%d \n",a%b);

    //relation opration
    printf("%d \n", a>b);
    printf("%d \n", a<b);
    printf("%d \n", a>=b);
    printf("%d \n", a<=b);
    printf("%d \n", a!=b);

    //Logical opration
    printf("%d \n", a && b);
    printf("%d \n", a || b);
    printf("%d \n", !(a));

==================================================================================
Lab Exercise : 5)

Write a C program to check if a number is even or odd using an if-else statement.
Extend the program using a switch statement to display the month
name based on the user’s input (1 for January, 2 for February, etc.).

#include<stdio.h>
int main()
    {
        int num;
        printf("Enter number :");
        scanf("%d",&num);

              if(num%2==0 && num>0)
                     {
                        printf("Positive Even");
                     }

              else if(num%2==0 && num<0)
                    {
                        printf("Nagative Even");
                     }

              else if(num%2!=0 && num>0)
                   {
                        printf("Positive Odd");
                   }

                else    
                  {
                       printf("Nagative Odd");
                 }
    }

    #include<stdio.h>
    int main()
        {
            int choice;
            printf("Enter Choice");
            scanf("%d",&choice);

            switch(choice)
                {
                        case 1 :
                        printf("January");
                        break;

                    case 2 :
                        printf("February");
                        break;

                    case 3 :
                        printf("March");
                        break;

                    case 4 :
                        printf("April");
                        break;

                    case 5 :
                        printf("May");
                        break;

                    case 6 :
                        printf("June");
                        break;

                    case 7 :
                        printf("July");
                        break;

                    case 8 :
                        printf("Auguest");
                        break;

                    case 9 :
                        printf("September");
                        break;

                    case 10 :
                        printf("Octomber");
                        break;

                    case 11 :
                        printf("November");
                        break;

                    case 12 :
                        printf("December");
                        break;

                   default:
                        printf("Invalid Coice");
                        


                }
                return 0;
        }
===============================================================================

Lab Exercise : 6)
Write a C program to print numbers from 1 to 10 using all three types of loops
(while, for, do-while).

** for loop **
#include<stdio.h>
int main()
        {
            int i;
            for(int i=1;i<=10;i++)
                {
                    printf("%d \n",i);
                }
            return 0;
        }

** while loop **
#include<stdio.h>
int main()
        {
            int i=1;
            while(i<11)
                {
                    printf("%d \n",i);
                    i++;
                }
                return 0;
        }


** do while **
#include<stdio.h>
int main()
        {
            int i=1;
            do{
                
                printf("%d \n",i);
                i++;
            }while(i<=10);

            return 0;
        }

=================================================================================        
Lab Exercise : 7)
Write a C program that uses the break statement to stop printing numbers
when it reaches 5. Modify the program to skip printing the number 3 using the
continue statement.

#include<stdio.h>
int main()
        {
            int i=1;
            while(i<11)
                {
                    if(i!=5)
                        {
                            printf("%d",i);
                            
                        }
                    else
                        {
                            break;
                        }
                    
                    i++;
                }
                return 0;
        }


    ** skip the printing number 3 **
 #include<stdio.h>
        int main()
        {
            int i=1;
            while(i<11)
                {
                	
                    if(i==3)
                       {
                       	 i++;
                       	 continue;
                       	  
					   }
                        
                    printf("%d\n",i);
                    i++;
                  
                }
                return 0;
        }
=================================================================================       
Lab Exercise : 8)
Write a C program that calculates the factorial of a number using a function.
Include function declaration, definition, and call.
#include<stdio.h>
void fact(int n)
        {
            int i = 1, fact = 1;
            while(i<=n)
                {
                    fact = fact * i ;
                    i++;
                }
                printf("fact %d = %d",i,fact);
        }
int main()
        {
            int num;
            printf("Enter number :");
            scanf("%d",&num);


            fact(num);
            return 0;
            
        }


    =============================================================================================================

    Lab Exercise : 9)
    Write a C program that stores 5 integers in a one-dimensional array and prints
    them. Extend this to handle a two-dimensional array (3x3 matrix) and
    calculate the sum of all elements.

    
  #include<stdio.h>
    int main()
        {
            int arr[5];
            int i=0;
            printf("Enter 5 Number :\n");
            do 
			{
                scanf("%d",&arr[i]);
                i++;
            }while(i<5);
            
            printf("\n");

            for(int j=0;j<5;j++)
                {
                    printf("%d\n",arr[j]);
                    
                }


            return 0;
        }
=================================================================================================================

Lab exercise : 10)
Write a C program to demonstrate pointer usage. Use a pointer to modify the
value of a variable and print the result.

#include<stdio.h>
void CallByRef(int *num)
        {
            *num = 30;
        }
int main()
        {
            int a = 10;
            printf("Before : %d\n", a);
            CallByRef(&a);
            printf("After : %d", a);
            return 0;
        }
==================================================================================================================





                                        Do work better111213






*************************************************************************************************************
Lab Exercise : 11)
Write a C program that takes two strings from the user and concatenates them
using strcat(). Display the concatenated string and its length using
strlen().


#include<stdio.h>
#include<string.h>
int main()
        {
           char Name[20];
           char SurName[20];
           fgets(Name,20,stdin);
           fgets(SurName,20,stdin);
           full_name=strcat(Name,SurName);

           printf("%s",Name);

            return 0;
        }


===============================================================================================================

Lab Exercise : 12)

Write a C program that defines a structure to store a students details (name,
roll number, and marks).Use an array of structures to store details of 3
students and print them.

#include<stdio.h>
struct student
{
	char Name[3][20];
	int Roll_No[3];
	int Marks[3];
};
int main()
        {
        	struct student s;
            for(int i=0;i<3;i++)
            	{
            		printf("Enter Student NAme:");
            		scanf("%s",s.Name[i]);
            		
            		
            		printf("Enter Roll Number :");
            		scanf("%d",&s.Roll_No);
            		
            		printf("Enter Marks :");
            		scanf("%d",&s.Marks);
				}
				
			for(int i=0;i<3;i++)
			{
				printf("%s\n",s.Name[i]);
				printf("%d\n",s.Roll_No[i]);
				printf("%d\n",s.Marks[i]);
			}
			
			return 0;
        }
==================================================================================================

Lab Exercise : 14)
Write a C program to create a file, write a string into it, close the file, then
open the file again to read and display its contents.
#include<stdio.h>
int main()
        {
            FILE *p;
            
            p=fopen("Cprograme.text","w");
            fprintf(p,"Welcome to c");
            fclose(p);
        }

===========================================================================================
/*Write a C program that takes the marks of a student as input and displays the corresponding
grade based on the following conditions:
o Marks > 90: Grade A
o Marks > 75 and <= 90: Grade B
o Marks > 50 and <= 75: Grade C
o Marks <= 50: Grade D
• Use if-else orswitch statements for the decision-making pro
*/

#include<stdio.h>
int main()
        {
            int choice;
            int marks;
            printf("Enter Marks:");
            scanf("%d",&marks);
            choice=marks;

            switch(choice/10)
                {
                    case 10:
                    case 9:
                        printf("A Grade :");
                        break;

                    case 8:
                    case 7:
                        printf("B Grade :");
                        break;


                    case 6:
                    case 5:
                        printf("C Grade :");
                        break;

                    default: 
                        printf("Invalid :");
                    
                }
            
            return 0;
        }



        #include<stdio.h>
int main()
        {
        	int num1,num2,num3;
        	int min=0,max=0;

        	printf("Enter Three Number :");
           	scanf("%d\n %d\n  %d",&num1,&num2,&num3);
          	printf("%d,%d,%d",num1,num2,num3);
          	
          	max=num1;
          	if(num2>=max)
          		{
          			max=num2;
          			
				}
				printf("%d",max);
				
			if(num3>=max)
				{
						max=num3;
								
				}
				
			
		min=num2;
        if(num3<=min)
        	{
        		min=num3;
			}
		if(num1<=min)
			{
				min=num1;
			}
			printf("%d",min);


        }


          // Largest
    switch((num1 >= num2 && num1 >= num3) ? 1 : (num2 >= num1 && num2 >= num3) ? 2 : 3) {
        case 1:
            printf("Largest = %d\n", a);
            break;
        case 2:
            printf("Largest = %d\n", b);
            break;
        case 3:
            printf("Largest = %d\n", c);
            break;
    }

    // Smallest
    switch((num1 <= num2 && num1 <= num3) ? 1 : (num2 <= num1 && num2 <= num3) ? 2 : 3 ? 2 : 3) {
        case 1:
            printf("Smallest = %d\n", a);
            break;
        case 2:
            printf("Smallest = %d\n", b);
            break;
        case 3:
            printf("Smallest = %d\n", c);
            break;
    }

    return 0;
}

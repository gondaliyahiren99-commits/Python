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
void fact()
        {
            while()
        }
int main()
        {
            int num;
            printf("Enter number :");
            scanf("%d",num);

            
        }

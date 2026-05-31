                                    *=*=*=*= Overview of C Programming  =*=*=*=*
//pointer and string



3. Basic Structure of a C Program
    THEORY :
    Q1.Explain the basic structure of a C program, including headers, main function, comments, data types, and variables. Provide examples.
        c programe me kuch important part hota he.jo har programe me same hote he or comppulesery har programe me likhna padta he.
    jisme header file, main function, comment , data type , and variable.
    ~~>1)Header File : programe me #include likhne se c language jo bhi predefined function ho usko use kar sakte he .joisse hum prinf() aur sacnf() function use kar sakte he.bina header file ke printf() auric he uske bare me information scanf() function use karoto error dega.
    ~~>2) Main function : main() jo c language ka entry point he.C language me compiler execution start yahi se karta he.
    ~~>3) Comment : C language me comment jo programe rehta usko agar koi team member ya koi dusra programer dekhke samaj a=sake uske liye comment help karta he comment jo code ke bare me information hoti he ki programe kya work karta he or kya logric he uske bare me informationhoti he . compiler isko ignore kar deta he karan wo execute hi nahi hota.
    comment ke 2 types he 
        ~~>1)single line : jab ek single line ko comment karna ho. jisko # se define kiya jata he.
                        e.g. ific e
                        // single line comment
        ~~>2)Multiple line : Jab ek se jyada line ko comment karna ho tab multiple line comment ka use hota he.
                        e.g.
                        /* This is 
                        Multiple 
                        line comment
                        */
    4) Datatype : Datatype define karta he ki Koi specific memory location me kis type ka value store he. ye jab variable declare karte he tabhi define karna padta he ki variable me kis type ka data store karna he.datatype dekhne ke liye type() ka use karte he.
        e.g. int a = 20; #yaha pr int ek datatype he.
        1)Numeric : Jo variable numeric value store karta he.
                (A) int = jo only without decimal value store karta he. int a= 20 jiski size 4 bytes he.
                (B) float = float me decimal value store karta he float = 3.14  jo decimal ki 2 value ke bad sari truncate kar deta he.
        2)string : Jo character type ki value store kar rahe the. double = 3.14151212
                (A) char = isme single character value store karta he. jisko single quotes me likha jata he. char = 'y'
                (B) char[a] = character array me character ka collection store hota he. jisko double quotes me likha jata he. aur size dena compulsery he.

    5) Variable : variable ek container ki tarah he jismi value store kar sakte he.jab value ko acces ya koi expression karna ho to variable se kar sakte he.
                e.g. int age =20

    Lab Exercise :
    #include<stdio.h>
    #include<string.h>
    int main()
        {
            /* 
            this programe
            to define 
            datatype
            */
                
            char name[20] = "Hiren" ;# character array type
            int Age = 20; // integer value
            float Percentage = 92.35; // float type value
            char Gender = 'M'; // character type value
            const int Year = 2026 ; // constant int value
            # display message 
            printf("Age is : %d \nName is :%s \nPercentage is : %d :\nGender : %c \nPassing Year : %i \n", Age,name,Percentage,Gender, Year);
            
        }
4. OPERATER :
    THEORY :
    Write notes explaining each type of operator in C: arithmetic, relational,logical, assignment, increment/decrement, bitwise, and conditional operators.
    ~~>operater jo do value ke bich me koi specific oppration karne ke liye jo oprater use hota he us symbol ko operater  kehte . jis variable ya value ke bich opration hota he usko oprand kehte he.
            1)  Airthmetic Operator: ye number or value ke sath kuch basic calculation ke liye use hota he. ye koi value return  krata he
            (+ , - , * , / ,%)
                            e.g. 
                            a,b = 10,5
                            ans = a + b  | 10 + 5  | 15
                            ++++++++++++++++++++++++++++++++++++
                            ans = a - b  | 10 - 5  | 5
                            ++++++++++++++++++++++++++++++++++++
                            ans = a * b  | 10 * 5  |  50
                            +++++++++++++++++++++++++++++++++++++
                            ans = a / b  | 10 / 5  |  2
                            +++++++++++++++++++++++++++++++++++++
                            ans = a % b  | 10 // 5  |  0 (Reminder return)
                            +++++++++++++++++++++++++++++++++++++

            2) Assigment operators:  Variable me value assign karne ke liye.
             = (to assign a values in variable)
                shorthand operator: combination  airthmatic and assigmnet operator.isme left side me jo bhi variable ki value me 
                expressin work karke usme hi value assign hogi.
                ( += , -+ , *= , /+ , //+ , **= )
                        e.g.
                            a,b = 10,5
                        a = a += b  | a += 5  | 15
                        ++++++++++++++++++++++++++++++++++++
                        a = a -= b  | a -= 5  | 5
                        ++++++++++++++++++++++++++++++++++++
                        a = a *= b  | a *= 5  |  50
                        +++++++++++++++++++++++++++++++++++++
                        a = a /= b  | a /= 5  |  2.0
                        +++++++++++++++++++++++++++++++++++++
                        a = a //= b  | a //= 5  |  2
                        +++++++++++++++++++++++++++++++++++++
                        a = a **= b  | a **= 3  |  1000
                        +++++++++++++++++++++++++++++++++++++


            3) Relational operators:
                Relation oprater do value ko compre karne ke liye use hota he . its return always boolean value. wo sirf True or False return krta he.
               ( < > <= >= == !=)
                e.g.
                a,b = 10,5

                        ans = a > b  | 10 > 5  |   True
                    ++++++++++++++++++++++++++++++++++++
                    ans = a < b   | 10 < 5  |   False
                    ++++++++++++++++++++++++++++++++++++
                    ans = a >= b  | 10 >= 5  |   True
                    ++++++++++++++++++++++++++++++++++++
                    ans = a <= b  | 10 <= 5  |   False
                    ++++++++++++++++++++++++++++++++++++
                    ans = a == b  | 10 == 5  |   False
                    +++++++++++++++++++++++++++++++++++++
                    ans = a != b  | 10 != 10  |   False
                    +++++++++++++++++++++++++++++++++++++

    (4) Logical operator: 
            condition ko jodne ke liye use hota he. relation and logical combination

        and : Must both condition are true
        or  : at least one condition are  true
        ! :  opposite result


            a,b = 10,5
            ans = a > b and  a!=b  | 10 > 5 and 10 != 5 |    True
            +++++++++++++++++++++++|++++++++++++++++++++|+++++++
            ans = a < b  or  a > b | 10 < 5   or 10 > 5 |    True
            +++++++++++++++++++++++|++++++++++++++++++++|+++++++++
            ans =( not (a >= b )   |    !(10 > 5)       |    True
            +++++++++++++++++++++++|++++++++++++++++++++|++++++++

5 CONTROL FLOW STATEMENT
    THEORY :
    Explain decision-making statements in C (if, else, nested if-else,switch).Provide examples of each.
    ~~>Decision making statment jo condition ke hisab se decision lene me help karta he agar condition true hui to kam karega warna kuch or hoga.

        1) if statment : if me likha huva condition agar true hui to block of code execute hoga. nahi to kuch nahi hoga.
                        e.g. 
                        int main()
                            {
                                int age = 22 ;
                                if(age>18)
                                    {
                                        printf("Eligible");
                                    }
                            }
                                //OUTPUT :- Eligible
        2) if else : if else me agar condition true hui to if vala coe execute hoga nahi to else me likha hua block of code execute hoga.
                        e.g. 
                        #include<stdio.h>
                        int main()
                        {
                            int age = 22 ;
                            {
                                
                                if ( age >= 18)
                                        {
                                            printf("Eligible");
                                        }
                                    else
                                        {
                                            printf("Not Eligible");
                                        }
                                return 0 ;
                            }

                        }
                                    //OUTPUT :- Not Eligible
        3) nested if : jab conditon ke andar condition aur condition ban rahi ho tab nested if use karte he.
                        e.g. 
                        #include<stdio.h>
                        int main()
                        {
                            int age = 15 , indian_citizen = 1 ;
                            if (age >= 18)
                                {
                                    if (indian_citizen)
                                        {
                                            printf("Eligible For Vote ");
                                        }
                                    else
                                        {
                                            printf("Age valid But Not Indian citizen");
                                        }
                                }
                            else
                                {
                                    printf("Not valid for age");
                                }
                        }
        4) switch case : Jab ek variable ke alag-alag values  different kaam karna ho, tab switch-case use karte hain. Ye if-else ladder ka clean aur easy version hai.

                        #include<stdio.h>
                        int main()
                        {
                            int day;
                            scanf("Enter Day Number : %d" , &day);
                            switch(day)
                                {
                                case 1:
                                    printf("Monday");
                                    break;

                                    case 2:
                                        printf("Tuesday");
                                        break;
                                    
                                    case 3:
                                        printf("Wednesday");
                                        break;
                                    
                                    case 4:
                                        printf("Thursday");
                                        break;

                                    case 5:
                                        printf("Friday");
                                        break;

                                    case 6:
                                        printf("Saturday");
                                        break;

                                    case 7:
                                        printf("Sunday");
                                        break;
                                    
                                }
                           }

    LAB EXERCISE :
    Write a C program to check if a number is even or odd using an if-elsestatement. Extend the program using a switch statement to display the //monthname based on the user’s input (1 for January, 2 for February, etc.).
                    #include<stdio.h>
                    int main()
                        {
                            int number ;
                            printf("Enter Number : ");
                            scanf("%d", &number);
                            if (number==0)
                                {
                                    printf("Zero");
                                }
                        else if (number%2==0)
                                {
                                    printf("Even");
                                }
                            else 
                                {
                                    printf("Odd");
                                }
                            
                            return 0;
                        }

    Display Month Number :-
            #include<stdio.h>
            int main()
                {
                    int Month_Numer ;
                    printf("Enter Month Number : ");
                    scanf("%d",&Month_Numer);
                    switch(Month_Numer)
                        {
                            case 1 :
                                printf("January");
                                break ;
                            case 2 :
                                printf("February");
                                break ;
                            case 3 :
                                printf("March");
                                break ;
                            case 4 :
                                printf("April");
                                break ;
                            case 5 :
                                printf("May");
                                break ;
                            case 6 :
                                printf("June");
                                break ;
                            case 7 :
                                printf("July");
                                break ;
                            case 8 :
                                printf("Augest");
                                break ;
                            case 9 :
                                printf("September");
                                break ;
                            case 10 :
                                printf("October");
                                break ;
                            case 11 :
                                printf("November");
                                break ;
                            case 12 :
                                printf("December");
                                break ;
                            default :
                                printf("Not Velid");
                            
                        }
                }
6.LOOP  CONTROL STATEMENT
Compare and contrast while loops, for loops, and do-while loops. Explain the scenarios in which each loop is most appropriate.
• LAB EXERCISE:
o Write a C program to print numbers from 1 to 10 using all three types of loops
(while, for, do-while).
1) While loop :
    while(condition)
        {
            //code
        }
        jab pata na ho loop kitni bar chalega tab .while loop me pehle condition check hogi aur agar condition true hogi to block of code execute hoga varna ek bhi bar loop andar nahi jayega.
        user jab exit dega tab hi loop stop hoga tab while loop use karte he.
        e.g.
       #include<stdio.h>
        int main()
            {
                int i=1;
                while(i<=10)
                    {
                        printf("%d\n",i);
                        i++;
                    }
                return 0;
            }
2) For loop :
        for(intilize; condition ; update)
            {
                //code
            }
        sabse clean or structured loop . isme intilize ,condition aur update sa one line me likha jata he . jab pata ho loop kitne times chalana ho tab for loop ka use hoga.
        #include<stdio.h>
        int main()
            {
                for(int i=1; i<=10; i++)
                    {
                        printf("%d\n",i);
                    }
            }
        
3) Do While loop :
            do{
                //code
            }
            while(condition);
            isme sabse pehle code likha jata he jiske karan block of code execute hoga or last me condition check hoga.
            jiske karan condition false ho to bhi one time pe code run hoga
            #include<stdio.h>
            int main()
                {
                    int i =1 ;
                    do
                    {
                        printf("%d\n",i); //1
                        i++;
                    }while(i<=10);
                }
// Explain the use of break, continue, and goto statements in C. Provide
// examples of each.
// • LAB EXERCISE:
// o Write a C program that uses the break statement to stop printing numbers
// when it reaches 5. Modify the program to skip printing the number 3 using the
// continue statem
1)Break : loop ko condition ke hisab se jab termnainate karna ho tab break keyword use hota he. break se loop pura terminate ho jayega chahe kitne bhi cases ho age nahi jayega. yeh switch case me use hota he jiske karan next case ma nahi jayega agar break nahi lagaya to age ke case me jayega nahi.
                e.g. int a = 2;
                    #include<stdio.h>
                    int main()
                        {
                            for(int i= 1 ; i<=10;i++)
                                {
                                    if(i==5)
                                        {
                                            break; // 5 pr stop kr dega
                                        }
                                    else
                                        {
                                            printf("%d ", i);// 1 2 3 4 
                                        }
                                }
                        }
                        //OUTPUT--> Two (break pr hi ruk jayega)

2) Continue : continue keyword he jiska use loop me use hota he. agar loop me current itrator ko skip karke loop ko age move karvana ke liye useful he.
                        #include<stdio.h>
                        int main()
                            {
                                for(int i= 1;i<=5;i++)
                                    {
                                        if(i==3) // skip 3 
                                            {
                                                printf("%d ",i);//1 2 4 5
                                            }
                                    }
                            }

3) goto : goto jump keyword he jo programe  ke control ko unconditionaly kisi aur jagah le jata he. 
                            #include<stdio.h>
                            int main()
                                {
                                    for(int i= 1 ; i<=10; i++)
                                        {
                                            if(i==7)
                                                {
                                                    goto found;
                                                }
                                        }
                                    found :
                                        printf("7 found");
                                }

THEORY EXERCISE:
o What are functions in C? Explain function declaration, definition, and how to
call a function. Provide examples.
• LAB EXERCISE:
o Write a C program that calculates the factorial of a number using a function.
Include function declaration, definition, and call   
function ek block of code he. jisko specific  task ke liye banaya jata he. jo ek bar likhne ke bad bar bar use kar sakta he. reusability badhata he.programe ko organize or redable banata he.
1) Declaration : function declare me compiler ko batata he ki function ka datatype kya he,function ka name kya he aur perameter kya rahenge. programe ki starting me likha jata he main function se pehle.body nahi hoti,sirf semicolon lagta he.

2) Defination : function defination me body hoti he jisme function ka task rahega aur kya logic lagega define kiya jata he.main function ke bahar kiya jata he.

3) Call : function  ko call karne se function defination me likha block of code execute hoga. function call me function Name likh ke perantheses lagaya jata he.jo main function me kiya jata he.
                    #include<stdio.h>
                    int factorial(int a); //Declare
                    int fact=1;
                    int factorial(int a) //Defination
                        {
                        while(a>0)
                                {
                                    fact*=a;
                                    a--;
                                }
                                printf("%d",fact);
                        }
                    int main()
                        { 
                            factorial(5);//call
                            return 0;
                        }
 Explain the concept of arrays in C. Differentiate between one-dimensional and
multi-dimensional arrays with examples.
array ek same datatype ke multiple value store karta he. ek hi name me multiple value store kar sakta he.har value ki index hoti he . array ki index 0 se start hoti he.
1) One dimensional :sabse simple array he. jisme ek hi line me bahot sari same datatype ki value store.
                    #include<stdio.h>
                    int main()
                        {
                            int array[5]={1,2,3,4,5};
                            for(int i=0 ; i<5 ; i++)
                                {
                                    printf("%d ",array[i]);
                                }
                        }
2) Two dimensional : arraay ke inside another array ho usko 2d array kaha jata he. jo raw or collum base hota he. 
            #include<stdio.h>
            int main()
                {
                    int array[3][3]={ {1,2,3} , {4,5,6} , {7,8,9} };
                    int total_sum = 0;
                    for(int i=0 ; i<=2 ; i++)
                        {
                            for(int j = 0;j<=2;j++)
                                {
                                    total_sum+=array[i][j];
                                }
                        }    printf("%d ",total_sum);
                }
Explain string handling functions like strlen(), strcpy(), strcat(),strcmp(), and strchr(). Provide examples of when these functions are useful.
C me string ek character array he. jisme ek se jyada chracter store hote he.sab chracter ka index hota he.jo '\0' (null) se end hota he . jo count nahi hota. 
e.g. char name[5]="Hiren";
                H i r e n '\0'
                0 1 2 3 4
string ke sare function string.h file me store hote he. ye sab predefined function kaha jata he.
1) strlen() : string ki length kitni he means string me kitne character  he dekhne ke liye strlen ka use hota he. e.g. strlen(name);  // 5
2)strcmp() :Ek string ko dusri string me copy karne ke liye. isme lef vale variable ki value right side vale variable me pass hogi.
e.g. nickname[20];
        strcpy(name , nickname); // nickname = "Hiren"
3)strcat() : ye jab do string ko jodne ke liye use hota he. iske perameter me do string variable dete he. jisme pehle variable me 
store hui sting first me concat ho jati he.
            e.g. name[30] = "Hiren", surname[10]= " Gondaliya" , 
            strcat(name,surname); // name = "Hiren Gondaliya"
4) strcmp(): string compare karne ka kaam karta he

    





// Explain the concept of structures in C. Describe how to declare, initialize, and
// access structure members.
// • LAB EXERCISE:
// o Write a C program that defines a structure to store a student's details (name,
// roll number, and marks). Use an array of structures to store details of 3
// students and print them.
structure ek datatype he jo multiple datatype ki multiple value eksath ek group me store karta he. jise struct keyword se define kiya jata he. jisme declare member se structer ke variable se usko acces or value assign kar sakte he.
1)structure Declaration : usme struct keyword or structure ka name likha jata he bad me {} braces me multiple datatype ki multiple value store kar sakte he.{} ke bad semicolon jaroori he.
Declare sirf ek bluprint he . jisko abhi tak memory allocat nahi hui  jab tak vaiable nahi banate.
2) structer variable declaration : structure variable declare jo bhi structure me member declare kiye he usme acess kar ke value asign karne ke liye kar sakte he.structure variable declare hum multiple type se kiya jata he. structer ke bad , multiple variable eksath,structure declare time.
3)intilize structure Member : memeber me value asign karana. member ko structure ke variable se acess karke usme value assign kar sakte he.
4)Accesiing Structure Member : Member acess karne ke liye hum (.) ka use karte he . jisme structure variable.Member se kiya jata he.






Explain the importance of file handling in C. Discuss how to perform file
operations like opening, closing, reading, and writing files.
jab programer programe se hi file ko control kar sake use file handling kaha jata he.jisse data permanently save kar sakte .
1) File Opening : file ko open fopen() se kar sakte he. sabse pehle FILE ka pointer  banaya jat he . us  pointer se file ko open karte he phiir usme jo act karna he read, write or appendn kar sakte he.
                FILE *filepointer;
                filepointer = fopen("filename.txt",'mode');

2) File Closing : file ko jab bhi open kare use karne ke bad close karna jaroori he.agar close na kare to file leak ho jati he. isiliye file close karna jaroori he. jo close() se hota he.jisko pointer se filename.close() karte he.
                FILE *filepointer;
                filepointer = fopen("filename.txt",'mode');
                filepointer.close()

3) File Reading : file ko read karke usko console screen pr dikha sakte he.read karne ke liye 'r' mode ka use karte he.file me jo bhi text karna ho to usko data ko acess karke dusre variable me store kar sakte he.agar file exsists na ho to error dega.
                FILE *filepointer;
                filepointer = fopen("filename.txt",'r');  
                filepointer.close()

4) Writing files : jab file me data insert karna ho tab file ko writing mode ka use kar sakte he.jisko 'w' mode me likh sakte he.isme agar file exist na ho to new file create hokar usme data insert hoga.agra file exist na ho to usme data overwrite hoga.
                FILE *filepointer;
                filepointer = fopen("filename.txt",'w');  
                filepointer.close()


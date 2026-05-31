                                                *=*=*= Introduction to OOPS Programing *=*=*=
                                            >>>>>1. Introduction to C<<<<<<<<<
    THEORY :
    Q1. What are the main input/output operations in C++? Provide examples.
        ~~>isostream se hum cout or cin jese function use kar sakte he.
        ~~>1) #include<ostream> preproccer directive he . jisme input aur output raltaed cheezen hoti heain. jiski help se cout aor cin use kar sakte he

        ~~>2) int main() : main() jo  programe ka entry point he. jab bhi programe run hota he, sabse pehle main() function andar ka code execute hoga.

        ~~>3) { } : jisme hamara code likha jata he. ye batata he ki main function kaha se kaha tak he.

        ~~>4) std::cout : ye console screen me output dekhne ke liye use hota he.
        std ka means c++ ki standerd <namespace> library ka use kar rahe ho
    Q2.List and explain the main advantages of OOP over POP
    ~~>Data Security : OOP me data ko encpsulation ki help se data hide rakh sakte he.jab POP me data global he ,isiliye easily chane hota he.
    ~~> Code Reusability :OOP me inheritance ki madad se code reuse kar sakte he.ek class ke feture dusre class use kar sakte he.POP me code reuse limited he.
    ~~> Easy Maintaenance : Large programe ko  class or object me dividede he isiliye debug karana asan he. jab POP me bade programe me work hota he jisse debug karna dificult he.
    ~~>Data Hiding : private members use karke important data hide kar sakte he. POP me esa koi feture nahi he.
    ~~>Flexible : OOP me same name function har ek object ke sath alag-alag behave karta he.POP me esi flexible nahi hoti.
    
   
    LAB EXERCISE:
    L1. Write a simple C++ program to display "Hello, World!".
    
                #include<iostream>
                using namespace std ;
                int main()
                    {
                        cout<<"Hello world";
                    }
                            
    L2. Write a C++ program that accepts user input for their name and age and then displays a personalized greeting.

                #include<iostream>
                #include<string>
                using namespace std ;
                int main()
                    {
                        string name;
                        int age;
                        cout<<"Enter Name :";
                        cin>>name;
                        cout<<"Enter Age :"
                        cin>>age;
                        cout<<age;
                        cout<<"Name is :"<<name<<"Age :"<<age;

                    }

    L3. POP vs. OOP Comparison Program

                # Area calculate with pop
                #include<iostream>
                using namespace std ;
                int areafind(int l ,int b);
                int areafind(int l ,int b)
                    {
                        int area;
                        area = l*b ;
                        cout<<"Area is : "<<area;
                    }
                int main()
                    {   
                        int le, be;
                        cout<<"Enter l :";
                        cin>>le;
                        cout<<"Enter b :";
                        cin>>be;
                        areafind(le,be);
                    }

                # Area calculate with oop
                class Rectrangle
                {
                    int length,based;
                    public:
                        int setdata(int l, int b)
                            {
                                length = l ;
                                based = b ;
                            }
                        int findearea()
                            {
                                return length*based;
                            }
                        void display()
                            {
                                cout<<"Area :"<<findearea();
                            }
                };
                int main()
                    {
                        Rectrangle R;
                        R.setdata(15,15);
                        R.display();
                    }
    L4. Enviournment seting

        
                            >>>>>>>>2. VARIABLE ,DATATYPES,AND OPERATOR <<<<<<<<<
    THEORY :
    LAB EXERCISE :
    1.Write a C++ program that demonstrates the use of variables and constants. Create
    variables of different data types and perform operations on them.
    o Objective: Understand the difference between variables and constants.
                #include<iostream>
                int main()
                    {
                        int age = 20;
                        float persentage = 86.21;
                        char grade = 'A';
                        const float pi = 3.14; //constant
                        cout<<"Age :"<<age<<"Percentage :"<<percentage<<"Grade :"<<grade<<"PI :"<<pi;
                    }
    2.Write a C++ program that performs both implicit and explicit type conversions and prints the results.
                #include<iostream>
                int main()
                    {
                        int num1= 12,num2 = 20;
                        float val1;
                        string val2;
                        val2 = num1; //auto type convert
                        val2 = string(num2) ; //by programer
                        cout<<"val1 :"<<val1<<"val2 :"<<val2;

                    }
    3.Demonstrate Opratoer :
                #include<iostream>
                int main()
                    {
                        int a=10,b=30;
                        # Airthmatic Opratoer
                        cout<<"sum :"<<a+b<<"Dif :"<<b-a<<"Mul:"<<a*b<<"Div :"<<b/a<<"mod :"<<b%a<<endl;
                        # Relational Opratoer
                        cout<<"a>b"<<a<b<<"a<b"<<a<b<<"a==b"<<a==b<<"a!=b"<<a!=b<<"a<=b"<<a<=b<<"a>=b"<<a>=b<<endl;
                    }

    THEORY :
    Q1.What are the different data types available in C++? Explain with example
        dataype means variable me kis tarah ka data store karna he.
        ~~>1) int : jo whole number yani without decimal vali value store karta he. jiski size 4 bytes hoti he.
        int age = 25 ;
        ~~>2) float : jo decimal vali value store karega lekin decimal ke bad only 2 number hi dega baki truncate kar deta he.ye less precision he.jiski size 4 bytes hoti he.
        float pi = 3.14 ;
        ~~>3) double : jo decimal value store karta he. jo high precision he. jiski size 8 bytes hoti he.
        double pi = 3.14159 ;
        ~~>4)char :  is datatype ek single character type ki value store hoti he.value ko single ya double quotes me likha jata he.
        char grade = 'A' ;
        ~~>5)bool : jo true or false value store karta he.jo 1 bytes memory leta he.
        bool ispassed = true ;

    Q2.xplain the difference between implicit and explicit type conversion in C++.
        ~~>type conversion means variable ke datatype ko dusre datatype m convert karen ko type conversion kehte he.
        ~~>1) implict type conversion : ye compiler apne ap karta he. jisme data loss hone ka dar nahi he. chhote datatype ko bade datatype me convert kar deta he.jab multiple datatype ke bich kuch expresion karte he tab hota he.
        ~~>2) Explict type conversion : ye programer karta he.jisme programer forcefully dusre datatype me convert karta he. jisse data loss hone ki probability he.


    Q3.What are the different types of operators in C++? Provide examples of each.
        ~~>operater jo do value ke bich me koi specific oppration karne ke liye jo symbol use hota he us symbol ko operater  kehte . jis variable ya value ke bich opration hota he usko oprand kehte he.
        ~~>1) arithmetic operater : ye number or value ke sath kuch basic    calculation ke liye use hota he.(+ , - , * , / ,%)
        ~~>2) Assigment operators: Variable me value assign karne ke liye.
         = (to assign a values in variable)
        *shorthand operator: combination of airthmatic and assigmnet operator.isme left side me jo bhi variable ki value me 
        expressin work karke usme hi value assign hogi.( += , -= , *= , /= , %= , = )
        ~~>3) Relational operators:
            Relation oprater do value ko compre karne ke liye use hota he . its return always boolean value. wo sirf True or False return krta he. (< , > , <= , >= , == , !=)
        ~~>4)Logical operator: 
                condition ko jodne ke liye use hota he. relation and logical combination 

            & (AND): Must both condition are true
            | (OR) : at least one condition are  true
            ! (NOT):  opposite result
        ~~>5) Increment or Decrement : variable ki value me 1 se badhane or ghatane ke liye use hota he.
            ++ (Increment) : jo 1 se value increse karega.
                Pre-Increment :(++variable) jo aage ++ lagate he. iska means pehle value increse karo bad me use karo.
                Post-Increment :(variable++) jo variable ke last me lagate he. jiska meaning he pehle value ko use karo bad me usme Increment karo
            --(Decrement) : jo variable ki value ko 1 se kam karta he.
                Pre-Decrement :(--variable) jo variable ke aage -- lagate he. iska means pehle value Decrese karo bad me use karo.
                Post-Decrement :(variable--) jo variable ke last -- me lagate he. jiska meaning he pehle value ko use karo bad me usme Decrement karo.
        ~~>6)Ternery operater : Ek line me condition likhne ke liye use hoa he. jab condition one line me likhni ho or short tab use hota he.
        #include <iostream>
        using namespace std;
        int main() {
            int a=10,b=3;
            cout<<"Addition : " << a+b<<endl; //13
            cout<<"a>b : "<<(a > b)<<endl; //True
            cout<<"AND : "<<((a>5)&&(b<5))<<endl; //True
            cout<<"a += 5: "<<(a += 5)<<endl; //15
            cout<<"Increment: "<<++a<< endl; //16
            return 0;
        }

Q4. Explain the purpose and use of constants and literals in C++.
    ~~>constants variable means vo variable jiski value change nahi kar sakte. means declare ke time jo value dete he vo value me kuch bhi change nahi kar sakte. constants variable ko const se define kiya jata he.

//////////literal ko samjavo
                                >>>>>>>>3. CONTROL FLOW STATEMENT <<<<<<<<<
    LAB EXERCISE :
    L1. Grade Statements :
                        #include<iostream>
                        int main()
                            {
                                int marks;
                                cout<<"Enter Marks :";
                                cin>>marks;
                                if(marks=<100 & marks>=90)
                                    {
                                        cout<<"A";
                                    }
                                else if(marks>=75)
                                    {
                                        cout<<"B";
                                    }
                                else if(marks>=60)
                                    {
                                        cout<<"C";
                                    }
                                else if(marks>=50)
                                    {
                                        cout<<"D";
                                    }
                                else
                                    {
                                        cout<<"FAIL";
                                    }
                            }
        L2.Number Guess Game :
                        #include<iostream>
                        using namespace std;
                        #include<cstdlib>
                        int main()
                            {
                                int C_number ,U_number;
                                int attempt=3;
                                C_number =  rand() % 10 + 1;
                                bool status=true;
                                while(status)
                                    {
                                        cout<<"Remaining Attempt :"<<attempt;
                                       if(attempt>0)
                                        {
                                             cout<<"Enter Number :";
                                            cin>>U_number;

                                            if(C_number==U_number)
                                                {
                                                    cout<<"Right";
                                                    status=false;
                                                }
                                            else
                                                {
                                                    cout<<"Re-Enter";
                                                    attempt-=1;
                                                }
                                        }
                                        else{
                                            cout<<"You lose !";
                                            status=false;
                                        }
                                    }
                            }
        L3. Multiplicatio Table :
                        #include<iostream>
                        using namespace std;
                        int main()
                            {
                                int number;
                                cout<<"Enter Number :";
                                cin>>number;
                                for(int i=1;i<=10;i++)
                                    { 
                                        cout<<number<< "*"<<i<<"="<<number*i;
                                    }
                            }
                        
        L4.Nested Control Structures :
                        #include<iostream>
                        using namespace std;
                        int main()
                            {
                                for(int i=1;i<=5;i++)
                                    {
                                        for(int j=1;j<=i;j++)
                                            {
                                                cout<<" * ";
                                            }
                                        cout<<endl;
                                    }
                            }
                        
      
    Q1. What are conditional statements in C++? Explain the if-else and switch statements.
        Decision making statment jo condition ke hisab se decision lene me help karta he agar condition true hui to kam karega warna kuch or hoga.
        ~~>1) if else : if else me agar condition true hui to if vala coe execute hoga nahi to else me likha hua block of code execute hoga.
        if else me jab condiion complex ho tab if else ka us ekarte he
        ~~>2)switch case : Jab ek variable ke alag-alag values  different kaam karna ho, tab switch-case use karte hain. Ye if-else ladder ka clean aur easy version hai.isme humm sirf integer or character type ki value check karne me likh sakte he.(day,month,grade..)
        har ek case ke bad break lagana jaroori he otherwise jis case ke true ke bad vale bhi execute hoge.



    Q2 .What is the difference between for, while, and do-while loops in C+
        ~~>1) For loop :sabse clean or structured loop . isme intilize ,condition aur update sa one line me likha jata he . jab pata ho loop kitne times chalana ho tab for loop ka use hoga.

        ~~>2)While Lopp :ab pata na ho loop kitni bar chalega tab .while loop me pehle condition check hogi aur agar condition true hogi to block of code execute hoga varna ek bhi bar loop andar nahi jayega.
        user jab exit dega tab hi loop stop hoga. tab while loop use karte he.
        ~~>3)Do While : isme sabse pehle code likha jata he jiske karan block of code execute hoga or last me condition check hoga.jiske karan condition false ho to bhi one time pe code run hoga


    Q3. How are break and continue statements used in loops? Provide examples.
        ~~>1)Break : loop ko condition ke hisab se jab termnainate karna ho tab break keyword use hota he. break se loop pura terminate ho jayega chahe kitne bhi cases ho age nahi jayega. yeh switch case me use hota he jiske karan next case ma nahi jayega agar break nahi lagaya to age ke case me jayega nahi.
                        e.g. int a = 2;
                            #include<iostream>
                            using namespace std ;
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
                                                cout<<i<<" "; // 1 2 3 4 
                                                }
                                        }
                                }
                            //OUTPUT-->  1 2 3 4 ( 5 break pr hi ruk jayega)

        ~~>2) Continue : continue keyword he jiska use loop me use hota he. agar loop me current itrator ko skip karke loop ko age move karvana ke liye useful he.
                            #include<iostream>
                            using namespace std ;
                            int main()
                                {
                                    for(int i= 1;i<=5;i++)
                                        {
                                            if(i!=3) // skip 3 
                                                {
                                                    cout<<i<<" ";//1 2 4 5
                                                }
                                        }
                                }
    Q4.Explain nested control structures with an examp
    ~~>jab ek com=ntrol structure ke dusra control structure use karte he ,usko Nested Control Structure kehte hai.ex if ke andar if , loop ke andar loop , if ke andar loop , loop ke andar if .
                    #include<iostream>
                    using namespace std;
                    int main()
                        {
                            for(int i =1;i<=3;i++)
                                {
                                    for(int j=1;j<=3;j++)
                                        {
                                            cout<<" * ";
                                        }
                                    cout<<"\n";
                                }
                        }

                                >>>>>>>4. FUNCTION AND SCOP<<<<<<<<<
    LAB EXERCISE :
    L1.Simple Calculator Using Functions:
                    #include<iostream>
                    using namespace std;
                    void add(int a,int b)
                            {
                                cout<<"sum :"<<a+b;
                            }
                    void dif(int a,int b)
                        {
                            cout<<"Dif :"<<a-b;
                        }
                    void mul(int a,int b)
                        {
                            cout<<a*b;
                        }
                    void divide(int a, int b)
                        {
                            cout<<float(a/b);
                        }
                    int main()
                    {
                        int n1,n2;
                        cout<<"Enter Number a :"<<endl;
                        cin>>n1;
                        cout<<"Enter Number b :"<<endl;
                        cin>>n2;
                        add(15,25);
                        dif(100,56);
                        mul(5,5);
                        divide(25,5);
                    }
    L2. Factorial Calculation Using Recursion
                    #include<iostream>
                    using namespace std;
                    int factorial(int n)
                        {
                            if(n==0 || n==1)
                                {
                                    return 1;
                                }
                            return n*factorial(n-1);
                        }
                    int main()
                        {
                            int num;
                            cout<<"Enter Number :";
                            cin>>num;
                            cout<<"Factorial of "<<num<<"="<<factorial(num);
                        }
    L3. Variable Scope
                    #include<iostream>
                    using namespace std;
                    int num =30;
                    void display()
                        {
                            int num=20;
                            cout<<"Local Variable :"<<num<<endl;
                            cout<<"Global Variable :"<<::num<<endl;
                        }
                    int main()
                        {
                            cout<<"Global Variable in main():"<<num<<endl;
                            display();
                        }
    THEORY:
    Q1. What is a function in C++? Explain the concept function declaration, definition, and calling.
        ~~>1) Declaration : function declare me compiler ko batata he ki function ka datatype kya he,function ka name kya he aur perameter kya rahenge. programe ki starting me likha jata he main function se pehle.body nahi hoti,sirf semicolon lagta he.
                        e.g. functionname(int age)

        ~~>2) Defination : function defination me body hoti he jisme function ka task rahega aur kya logic lagega define kiya jata he.main function ke bahar kiya jata he.
                        e.g. functionname(int age)
                            {

                            }

        ~~>3) Call : function  ko call karne se function defination me likha block of code execute hoga. function call me function Name likh ke perantheses lagaya jata he.jo main function me kiya jata he.
                        e.g. functionname()

    Q2. What is the scope of variables in C++? Differentiate between local and global scope
        ~~>variable ka scop means variable ki lifetime aur uski visibility kitni he wo uske declaration par dependent he.yahi variable scop he.
        loacal variable : jo variable function ke andar declare kiye jane vale variable local variable he.local variable ki life function tak hi hoti he.local variable ko hum function ke bahar acess nahi kar sakte.agar kiya to error ayegi.
        global Variable : jo variable function ke bahar declare kiye jate he wo global variable he. global variable ki life programe khatam hone tak hoti he.jisko hum kahi pr bhi acess kar sakte he.

    Q3.Explain recursion in C++ with an example
        ~~>function jab function ke andar hi kud ko call karta he usko function recursion kehte he.recursion me do cheez important he 1st Recursive call (function khud ko call karta he) , 2nd Base case (jaha recursion stop hoga)
                #include<iostream>

                using namespace std;
                void fact(int n)
                    {
                        int f =1;
                        if(n>1)
                            {
                                return 1;

                        cout<<n*fact(n-1);
                    }
                int main()
                    {
                        cout<<fact(5);
                    }
    Q4. What are function prototypes in C++? Why are they used
        ~~>function prototype means function ki pehle se declaration dena, taki compiler information deta he ki function ka name kya hai,kitne parameters hai,aur return type kya hai.ye hamesha main() se upper likha jata he.agar prototypre ho to function defination ke pehle call kardo to bhi error nahi ayegi.

                                  >>>>>>>5. ARRAY AND STRING<<<<<<<<<
    LAB EXERCISE :
    L1.Array Sum and Average:
                int array[50],sum=0,num;
                float avg=0;\
                cout<<"How Much Element Want To Add :";
                cin>>num;
                for(int i=0;i<num;i++)
                    {
                        cout<<"Enter Number :"<<i;
                        cin>>array[i];
                
                    }
                for(int j=0;j<num;j++)
                    {
                        sum=sum+array[j];
                    }
                cout<<"sum :"<<sum<<"Average :"<<sum\num<<endl;

    L2.Matrix Addition:
                #include<iostream>
                using namespace std;
                int main()
                    {
                        int a1[2][2],a2[2][2],sum[2][2];
                        for(int i=0;i<2;i++)
                            {
                                for(int j=0;j<2;j++)
                                    {
                                        cout<<"Enter Number :"<<i<<endl;
                                        cin>>a1[i][j];
                                    }
                            }
                        for(int i=0;i<2;i++)
                            {
                                for(int j=0;j<2;j++)
                                    {
                                        cout<<"Enter Number :"<<i<<endl;
                                        cin>>a2[i][j];
                                    }
                            }
                        for(int i=0;i<=;i++)
                            {
                                for(int j=0;j<2;j++)
                                    {
                                        sum[i][j]=a1[i][j]+a2[i][j];
                                    }
                            }
                        for(int i=0;i<2;i++)
                            {
                                for(int j=0;j<2;j++)
                                    {
                                        cout<<sum[i][j];
                                    }
                                    cout<<endl;
                            }
                    }

    L3. String Palindrome Check
                    #include<iostream>
                    using namespace std;
                    int main()
                    {
                        int num,s1,rev="";
                        cout<<"Enter String :";
                        cin>>s1;
                        l=str.length()-1
                    for(int i=l;i>=0;i--)
                            {
                                rev=rev+s1[i];
                            }
                        if( s1 ==rev)
                            {
                                cout<<"Palindrome";
                            }
                        else
                            {
                                cout<<"Not Palindrome";
                            }
                    }

    THEORY :
    Q1. What are arrays in C++? Explain the difference between single-dimensional and multidimensional arrays.
        ~~>array ek same datatype ke multiple value store karta he. ek hi name me multiple value store kar sakta he.har value ki index hoti he . array ki index 0 se start hoti he.
        ~~>1) One dimensional :sabse simple array he. jisme ek hi line me bahot sari same datatype ki value store.
                        
        ~~>2) Two dimensional : arraay ke inside another array ho usko 2d array kaha jata he. jo raw or collum base hota he. 

    Q2.Explain string handling in C++ with example
        ~~>string handling means string ko creat,store,combine,compare,karne ke liye use hote he.ye ek character array he.string ko use karne ke liye string <class> likhna jaroori hai. #include<string>
         ~~>1) string input : string variable me value assign karne ke liye cin aur getline use hota he.cin se sirf single word store kar sakte he. wo space ke bad ki value nahi lega. jab getline se full sentance input kar sakte he.
        ~~>2) string concat : Do string ko join karna.
        ~~>3)string length : string me character ki length find karne ke liye strlen() ka use karte he.
        ~~>4)character acess : string me har ek element ka ek index hota he. jo 0 se start hota he aur space ko bhi count karega. ager acess karna ho to variable[<index>] karenge to single character acess hoga.
        ~~>5)compare string : Do string me value store he wo same he ya nahi check karne ke liye use hota he.
        ~~>6)Reverse : string ke sare character left se right he usko right se left ke way me kar sakte he.


    Q3. How are arrays initialized in C++? Provide examples of both 1D and 2D arrays.
    Q4. Explain string operations and functions in C++.


                        >>>>>>>6. Introduction to  Object-Oriented Programming <<<<<<<<<

    LAB EXERCISE :
    L1.Simple Calculator :
                        #include<iostream>
                        using namespace std;
                        class Calculator
                            {
                                public :
                                void add(int a,int b)
                                    {
                                        cout<<"Sum :"<<a+b;
                                    }
                                void dif(int a,int b)
                                    {
                                        cout<<"Dif :"<<a-b;
                                    }
                                void mul(int a,int b)
                                    {
                                        cout<<a*b;
                                    }
                                void divide(int a, int b)
                                    {
                                        cout<<float(a/b);
                                    }
                            };
                        int main()
                            {
                                Calculator c;
                                int n1,n2;
                                cout<<"Enter Number a :"<<endl;
                                cin>>n1;
                                cout<<"Enter Number b :"<<endl;
                                cin>>n2;
                                c.add(15,25);
                                c.dif(100,56);
                                c.mul(5,5);
                                c.divide(25,5);
                            }

    L2.Class for Bank Account :
                        #include<iostream>
                        using namespace std;
                        class BankAcoount
                        {
                        private:
                        float balance;
                        public:
                        void setbalance(float b)
                            {
                                balance=b;
                            }
                        void Withdraw(int amt)
                            {
                                balance-=amt;
                            
                            }
                        void Deposite(int amt)
                            {
                                Balance+=amt;
                            
                            }
                        void ShowBal()
                            {
                                cout<<"Balance :"<<balance;
                            }
                        }
                        int main()
                        {
                        BankAcoount b;
                        b.setbalance(50000);
                        b.Withdraw(8000);
                        b.ShowBal();
                        }
    THEORY :
    Q1.Explain the key concepts of Object-Oriented Programming (OOP).
        ~~>oop ek programoing style he jisme hum real world chezzon ko code me likhte he.class or object hote he. oop ke 4 piller he 
        ~~>1) Encapsulation : ye data ko hide rakhta he. direct acess ko restrict karta he. agar hume data acess karna ho to uske liye special method use karna padega.
        ~~>2) Abstraction : ye user ko implemention nahi dekhata sirf functionality hi dikhata he.ek abstraction class rule banata he ki likhi har ek method child class me honi hi chahiye.abstract class ka direct onject nahi bana sakte. pure virtual function ki body abstract class me nahi hoti.
        ~~>3)Inheritanc : jab koi class apne properties ka acess dusri class ko de to wo inheritance he.
        ~~>4)Polymorphism : poly means many or phism means form. koi ek hi name ki method alag alag class me alag alag behavior ho usko Polymorphism kehte he.

    Q2.What are classes and objects in C++? Provide an example
        ~~> Class :class ek bluprint he jisme hum variable aur function define kiye jate hain. ye batata he ki data ke andar kya kya object he aur function define kiye jate he . ye bata he ki object ke andar kya data aurb kya behaviour hoga.

        ~~> Object : object class ka instance hota he.object bana kr class ka data aur function use kar sakte he.class ke multiple object bana sakte he.object ke bina class ek bluprint ki tarah hota he jab object baega tab hi wo real banega.jese hum ka naksha banatenge wo ek class he jab object uske uper ka ghar.


    Q3.What is inheritance in C++? Explain with an example
        ~~>inheritance means jab koi class apne properties ka acess dusre class ko de.inheritance me child class ka object bana kr parent class ke properties acess kr sakte he.
        Koi parent class he jiske pass 10 lakh he aur usne child class ko inherit kiya he to child class object parent ki jo 10 lakh ki properti he wo acess kar sakta he.private ke alawa sab acess kar sakta he.

    Q4.What is encapsulation in C++? How is it achieved in classes?
        ~~>Encapsulation ye data ko hide rakhta he. direct acess ko restrict karta he. agar hume data acess karna ho to uske liye special method use karna padega.jab humare pass  ek dibbe me bahot sari coin he jisme 1rs 2rs and 10rs usme se sirf 2rs ka coin nikal nahi sakte.uske liye special method use karna padega.

 
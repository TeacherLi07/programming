#include<bits/stdc++.h>
#include<windows.h>
using namespace std;
const int N=10005;

void getinit();
void gene_arr();
void sum_arr();
void printans();
void array2sum();
void sum2array();

double calcNinExpression(int n, string n_expression);

int priority(char op);
double performOperation(double a, double b, char op);
double evaluateExpression(string expression);

void SetWindow(int Width, int Height, int WidthBuffer, int HeightBuffer);

string equa;
double a[N],s[N],n;
int mode;
bool iscalca[N],iscalcs[N];
string modewd[3]={"","an=","sn="};

int main()
{
    system("title 数列计算器V1.3 by TeacherLi");
    system("color f0");
    system("cls");
    SetWindow(120,30,120,2000);
    cout.setf(ios::fixed,ios::floatfield);
    cout<<"========================================================================================================================"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                     数列计算器                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                    Version 1.3                                                     ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                   编写者：TeacherLi李信辉，部分代码来源于ChatGPT                                   ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                  https://github.com/TeacherLi07/Array-Calculator                                   ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                    按回车键继续                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"========================================================================================================================";
    getchar();
    system("cls");
    cout<<"========================================================================================================================"<<endl;
    cout<<"|| 使用说明：                                                                                                         ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 代数式用半角（英文）字符表示，支持加（+）减（-）乘（*）除（/）乘方（^），暂不支持根号。                            ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 数列某项以an表示，前n项和以sn表示，计算总项数最大为10000项。                                                       ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 序数下标如果有多项，请为下标打括号。                                                                               ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 合法表达例如：an；a(n+1)；a((3n+5)^2)；a114。                                                                      ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 乘方运算中，指数和底数如非单字母或纯数字，需要打括号。                                                             ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 表达式中n与x等价，大小写不敏感，不支持小数，可以用分数表示。                                                       ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 如果输入非法或者无法计算，可能会有各种奇奇怪怪的现象，如果不确定是否为bug可以联系我或提交issue。                   ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"||                                                                                                                    ||"<<endl;
    cout<<"|| 按回车键继续                                                                                                       ||"<<endl;
    cout<<"========================================================================================================================";
    getchar();
L1:
    system("cls");
    cout<<endl<<"  计算模式：\n  1.an表达式\n  2.sn表达式\n  表达式均可含有n、s、a\n  请输入模式：";
    cin>>mode;
    cout<<endl<<"  请输入"<<modewd[mode];
    cin>>equa;
    transform(equa.begin(),equa.end(),equa.begin(),::tolower);//处理大小写敏感问题，使用方法已注明
    for(int i=0;i<equa.length();i++)//处理x和n问题，使用方法已注明
        equa[i]= equa[i]=='x' ? 'n' : equa[i];
    for(int i=1;i<equa.length();i++)
    {
        if((equa[i]=='n' || equa[i]=='a' || equa[i]=='s') && isdigit(equa[i-1]))
        {
            char whichsymbol=1;//判断xn前是什么符号
            for(int j=i-1;j>=0;j--)
                if(!isdigit(equa[j]))
                {
                    whichsymbol=equa[j];
                    break;
                }
            if(whichsymbol=='+' || whichsymbol=='-' || whichsymbol=='*' || whichsymbol=='^' || whichsymbol==1)
                equa.insert(i,"*");
            else if(whichsymbol=='/')
                equa.insert(i,"/");
        }//处理多项式计算时，n、an、sn前系数无乘号问题，未处理乘方运算的优先级问题，所以在使用方法中已注明
        if((equa[i-1]=='+' || equa[i-1]=='-' || equa[i-1]=='*' || equa[i-1]=='/') && isdigit(equa[i]))
        {
            equa.insert(i-1,"0");
            i++;
        }
    }
    cout<<endl<<"  是否有已知数据？如有请输入如“s1=1”，“a3=2”，一项一行，如无或输入完成请回车"<<endl<<"  ";
    getchar();
    getinit();
    cout<<"  请输入计算项数 ";
    cin>>n;
    if(mode==1)
        gene_arr();
    else if(mode==2)
        sum_arr();
    else{
        cout<<"  未知模式，请重新输入"<<endl<<endl;
        goto L1;
    }
    printans();
    return 0;
}

void getinit()
{
    string init;
    while(1)
    {
        getline(cin,init);
        if(init=="-1" || init=="")
            return;
        transform(init.begin(),init.end(),init.begin(),::tolower);
        int val1 = 0;
        double val2=0;
        int i=1;
        while (i < init.length() && isdigit(init[i]))
        {
            val1 = (val1*10) + (init[i] - '0');
            i++;
        }
        i++;
        val2=evaluateExpression(init.substr(i,init.length()-i));
        if(init[0]=='a')
        {
            a[val1]=val2;
            iscalca[val1]=1;
        }
        else if(init[0]=='s')
        {
           s[val1]=val2;
            iscalcs[val1]=1;
        }
        cout<<"  ";
    }
}

double calcNinExpression(int number, string n_expression)
{
    for(int i=0;i<n_expression.length();i++)
        if(n_expression[i]=='n')
        {
            n_expression.erase(i,1);
            n_expression.insert(i,to_string(number));
        }
    return evaluateExpression(n_expression);
}

void gene_arr()
{
    sum2array();
    for(int i=1;i<=n;i++)
    {
        if(iscalca[i])
            continue;
        a[i]=calcNinExpression(i,equa);
    }
    array2sum();
}

void sum_arr()
{
    array2sum();
    for(int i=1;i<=n;i++)
    {
        if(iscalca[i])
            continue;
        string equan=equa;
        for(int j=0;j<equan.length();j++)
        {
            if(equan[j]=='n')
            {
                equan.erase(j,1);
                equan.insert(j,to_string(i));
            }
        }
        s[i]=evaluateExpression(equan);
    }
    sum2array();
}

void array2sum()
{
    for(int i=1;i<=n;i++)
        if(!iscalcs[i])
            s[i]=a[i]+s[i-1];
}

void sum2array()
{
    for(int i=1;i<=n;i++)
        if(!iscalca[i])
            a[i]=s[i]-s[i-1];
}

void printans()
{
    cout<<"  n\tan\t\tSn\t"<<endl;
    for(int i=1;i<=n;i++)
        cout<<"  "<<i<<"\t"<<a[i]<<"\t"<<s[i]<<"\t"<<endl;
    cout<<"  计算完毕，";
    system("pause");
}

int priority(char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    if (op == '^')
        return 3;
    return 0;
}

double performOperation(double a, double b, char op) {
    switch(op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
        case '^': return pow(a, b);
    }
    return 0;
}

double evaluateExpression(string expression) {
    stack<double> values;
    stack<char> operators;

    for (int i = 0; i < expression.length(); i++) {
        if (expression[i] == ' ')
            continue;

        else if (expression[i] == '(')
            operators.push(expression[i]);

        else if (isdigit(expression[i])) {
            double val = 0;
            while (i < expression.length() && isdigit(expression[i])) {
                val = (val*10) + (expression[i] - '0');
                i++;
            }
            i--;
            values.push(val);
        }

        else if (expression[i]=='a')
        {
            if (isdigit(expression[i+1]))
            {
                int val=0;
                while (i < expression.length() && isdigit(expression[i])) 
                {
                    val = (val*10) + (expression[i] - '0');
                    i++;
                }
                values.push(a[val]);
            }
            else if (expression[i+1]=='(')
            {
                int flag=0;
                while (i+flag < expression.length() && expression[i+flag]!=')') 
                    flag++;
                int val=int(evaluateExpression(expression.substr(i+1,flag)));
                values.push(a[val]);
                i+=flag;
            }
        }

        else if (expression[i]=='s')
        {
            if (isdigit(expression[i+1]))
            {
                int val=0;
                while (i < expression.length() && isdigit(expression[i])) 
                {
                    val = (val*10) + (expression[i] - '0');
                    i++;
                }
                values.push(s[val]);
            }
            else if (expression[i+1]=='(')
            {
                int flag=0;
                while (i+flag < expression.length() && expression[i+flag]!=')') 
                    flag++;
                values.push(s[int(evaluateExpression(expression.substr(i+1,flag+1)))]);
                i+=flag;
            }
        }

        else if (expression[i] == ')') {
            while (!operators.empty() && operators.top() != '(') {
                double val2 = values.top();
                values.pop();

                double val1 = values.top();
                values.pop();

                char op = operators.top();
                operators.pop();

                values.push(performOperation(val1, val2, op));
            }

            if (!operators.empty())
                operators.pop();
        }

        else {
            while (!operators.empty() && priority(operators.top()) >= priority(expression[i])) {
                double val2 = values.top();
                values.pop();

                double val1 = values.top();
                values.pop();

                char op = operators.top();
                operators.pop();

                values.push(performOperation(val1, val2, op));
            }

            operators.push(expression[i]);
        }
    }

    while (!operators.empty()) {
        double val2 = values.top();
        values.pop();

        double val1 = values.top();
        values.pop();

        char op = operators.top();
        operators.pop();

        values.push(performOperation(val1, val2, op));
    }

    return values.top();
}

void SetWindow(int Width, int Height, int WidthBuffer, int HeightBuffer) { 
    _COORD coord; 
    coord.X = WidthBuffer; 
    coord.Y = HeightBuffer; 

    _SMALL_RECT Rect; 
    Rect.Top = 0; 
    Rect.Left = 0; 
    Rect.Bottom = Height - 1; 
    Rect.Right = Width - 1; 

    HANDLE Handle = GetStdHandle(STD_OUTPUT_HANDLE);      // Get Handle 
    SetConsoleScreenBufferSize(Handle, coord);            // Set Buffer Size 
    SetConsoleWindowInfo(Handle, TRUE, &Rect);            // Set Window Size 
}  // SetWindow

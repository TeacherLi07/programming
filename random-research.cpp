// #include <Python.h>
#include<bits/stdc++.h>
using namespace std;
const int try_time=100000;
const int end_num=200000; //114514
int datas[try_time + 5];
double avg[end_num + 5];

// void plotArray(const int arr[]) {
//     // 初始化Python解释器
//     int size=try_time;
//     Py_Initialize();
//     // 导入Matplotlib库
//     PyObject* pName = PyUnicode_DecodeFSDefault("matplotlib.pyplot");
//     PyObject* pModule = PyImport_Import(pName);

//     // 检查导入是否成功
//     if (pModule != nullptr) {
//         // 转换C++数组为Python列表
//         PyObject* pList = PyList_New(size);
//         for (int i = 0; i < size; ++i) {
//             PyList_SetItem(pList, i, PyLong_FromLong(arr[i]));
//         }

//         // 调用Matplotlib的scatter函数
//         PyObject* pFunc = PyObject_GetAttrString(pModule, "scatter");
//         PyObject* pArgs = PyTuple_Pack(2, PyList_Size(pList), pList);
//         PyObject* pValue = PyObject_CallObject(pFunc, pArgs);

//         // 检查调用是否成功
//         if (pValue != nullptr) {
//             Py_DECREF(pValue);
//         } else {
//             PyErr_Print();
//         }

//         // 释放资源
//         Py_XDECREF(pArgs);
//         Py_XDECREF(pList);
//         Py_XDECREF(pFunc);
//         Py_DECREF(pModule);
//     } else {
//         PyErr_Print();
//     }

//     // 关闭Python解释器
//     Py_Finalize();
// }

int generate_random(int random_max, int current_layer)
{
    int this_layer = current_layer + 1;
    if(random_max == 1) return this_layer;
    int random_number = rand() % random_max + 1;
    return generate_random(random_number , this_layer);
}

double array_avg(int array[])
{
    int length=0;
    double avg=0;
    for(int i=0;i<try_time+5;i++)
    {
        avg += array[i];
        if(array[i]!=0) length++;
    }
    avg = 1.0 * avg / length;
    return avg;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("random-research.txt","w",stdout);
    srand((unsigned)time(NULL));
    for(int k=1;k<=end_num;k++)
    {
        memset(datas,0,try_time+5);
        cerr<<"NOW MAX NUMBER = "<<k<<endl;
        cout<<"NOW MAX NUMBER = "<<k<<endl;
        cout<<"DATA = [HIDDEN]";
        for(int i=1;i<=try_time;i++)
        {
            datas[i]=generate_random(k,0);
            // cout<<datas[k][i]<<",";
        }
        avg[k] = array_avg(datas);
        cout<<endl<<fixed<<setprecision(3)<<"AVERAGE = "<<avg[k]<<endl<<endl;
    }
    cout<<endl;
    for(int i=0;i<end_num+5;i++)
    {
        if(avg[i]!=0)
        {
            cout<<fixed<<setprecision(3)<<avg[i]<<"\n";
        }
    }
    cout<<endl;
    system("pause");
    return 0;
}
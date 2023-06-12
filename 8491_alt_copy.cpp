/*
Версия решения с динамической матрицей
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct Sum{
    int val;
    int freeze;
    int layers;
    Sum(int v, int f, int l): val(v), freeze(f), layers(l){};
    Sum(): val(0), freeze(0), layers(0){};
    bool is_not_empty(){
        return !((this->val == 0) && (this->layers == 0) && (this->freeze == 0));
    }
    Sum& operator=(const int x){
        if (!x){
            this->freeze = 0;
            this->val = 0;
            this->layers = 0;
        }
        return *this;
    }
};

int main(int argc, char** argv){
    if (argc > 1){
        char* FILENAME = argv[1];
        int prog_threshold = argc >= 3? atoi(argv[2]) : 100000;
        ifstream FILE(FILENAME);
        int N, K, M;
        FILE >> N;
        FILE >> K;
        FILE >> M;
        int n;
        int max_val = 0;
        vector<Sum> sum_hubs = {Sum(0, 0, 0)};

        Sum* max_sum_by_freeze = new Sum[(K + 1) * (M + 1)]; // Строка матрицы -- значение фриза; столбец -- кол-во слагаемых
        Sum cur; //!
        cout << "Ready" << endl;
        for (int i = 0; i < N; i++){
            // Считываем новое число и создаем новые суммы с этим числом, 
            // если в этих суммах хватает места (меньше чем М слагаемых)
            FILE >> n;
            int cur_len = sum_hubs.size();
            for(int index = 0; index < cur_len; index++){
                cur = sum_hubs.at(index);
                if (cur.freeze == 0 && cur.layers < M)
                    sum_hubs.push_back(Sum(cur.val + n, K, cur.layers + 1));
            }
            sum_hubs.push_back(Sum(n, K, 1));

            // Работаем со списком сумм: для каждого значения фриза и кол-ва слагаемых оставляем только максимальные суммы
            for (Sum s: sum_hubs){
                if (s.val > max_sum_by_freeze[(s.freeze *(M + 1)) + s.layers].val){
                    max_sum_by_freeze[(s.freeze *(M + 1)) + s.layers] = s;
                }
            }
            vector<Sum>().swap(sum_hubs); // Освобождаем память
            for (int freeze = 0; freeze < K + 1; freeze++){
                for (int layers = 0; layers < M + 1; layers++){
                    cur = max_sum_by_freeze[(freeze * (M + 1)) + layers];
                    if (cur.is_not_empty()){ // Проверяем, не занята ли ячейка пустым экземпляром
                        if (layers < M){
                            cur.freeze = cur.freeze > 0? --cur.freeze : 0;
                            sum_hubs.push_back(cur);
                        }
                        else max_val = max(max_val, cur.val);
                    }
                    max_sum_by_freeze[(freeze *(M + 1)) + layers] = 0;
                }
            }

            // Выводим отладочную информацию
            if (i % prog_threshold == 0){
                cout << "\033[91;1mProgress: \033[39;0m" << i << "; ";
                cout << "hub size: " << sum_hubs.size() << "; ";
                cout << "max_val: " << max_val << "; ";
                for (Sum sh: sum_hubs)
                    if (sh.val)
                        cout << "(" << sh.val << ", " << sh.freeze << ", " << sh.layers << "), ";
                cout << endl;
            }
        }
        cout << max_val << endl;
    }
    return 0;
}
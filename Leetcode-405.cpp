class Solution {
public:
    string toHex(int num1) {
        if (num1 == 0)
            return "0";
        u_int num = num1;
        string s = "";
        while (num) {
            int temp = num % 16;
             if (temp <= 9)
                s += (48 + temp);
             else
                s += (87 + temp);
             num = num / 16;
          }
      reverse(s.begin(), s.end());
      return s;
    }
};

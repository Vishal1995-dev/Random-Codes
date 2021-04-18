/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int search(int high,int low)
    {
        int i=guess(high);
        if(i==0) return high;
        i=guess(low);
        if(i==0) return low;
        int mid=low+(high-low)/2;
        i=guess(mid);
        if(i==0) return mid;
        else if(i==-1) return search(mid-1,low);
        else return search(high,mid+1);
    }
    
    int guessNumber(int n) {
        return search(n,0);
    }
};

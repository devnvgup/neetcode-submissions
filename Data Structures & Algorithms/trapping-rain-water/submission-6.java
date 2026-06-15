class Solution {
    public int trap(int[] height) {
         int i = 0;
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        while (i < height.length - 1) {
            if (i == 7) {
                System.out.println("7");
            }
            List<Integer> tmp = new ArrayList<Integer>();
            tmp.add(height[i]);
            int j = i + 1;
            boolean case1 = false;
            int maxIndex = j;
            while (j <= height.length - 1) {
                boolean firstTime = true;
                // case 1 : nếu phát hiện số nào lớn hơn hoặc bằng i thì cho dừng
                if (height[i] <= height[j]) {
                    tmp.add(height[j]);
                    i = j;
                    case1 = true;
                    res.add(tmp);
                    break;
                }
                tmp.add(height[j]);
                // tim so lon nhat dau tien trong mang trong truong hop ko tim dc so nao lon hon i
                // case 2
                if (firstTime && height[maxIndex] < height[j]) {
                    maxIndex = j;
                    firstTime = false;
                }
                j++;
            }
            // nếu case 1 không xảy ra , thì loop từ i đến phần từ lớn nhất xuất hiện đầu tiên trong mảng
            if (case1 == false) {
                tmp = new ArrayList<>();
                for (int k = i; k <= maxIndex; k++) {
                    tmp.add(height[k]);
                }
                res.add(tmp);
                i = maxIndex;
            }
        }
        // res = [[0,2],[2,0,3],[3,1,0,1,3][3,2],[2,1]]
        // caculate trap
        int total = 0;
        for (int l = 0; l <= res.size() - 1; l++) {
            List<Integer> innerList = res.get(l);
            for (int e = 0; e < innerList.size() - 1; e++) {
                // total el < 3 then break
                if (innerList.size() < 3){
                    break;
                }
                int first = innerList.get(0);
                int last = innerList.get(innerList.size()-1);
                int min = Math.min(first, last);
                // skip caculate first el, tail el 
                if (e == 0 ||e == innerList.size() - 1) {
                    continue;
                }
                total += min - innerList.get(e);
            }
        }
        return total;
    }
}

// [0,1,0,2,1,0,1,3,2,1,2,1]

//               x
//       x       x x   x
// o x o x x o x x x x x x


// 4,2,0,3,2,5
// 2 + 4 + 1 + 2

//.          x
// x         x
// x     x   x
// x x   x x x
// x x o x x x

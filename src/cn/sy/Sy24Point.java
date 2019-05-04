package cn.sy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sy24Point {
    int[] numbers;
    public Sy24Point(int[] numbers) {
        this.numbers = numbers;
    }
    List<String> stack = new ArrayList<>();

    private int[] getRemains(int index, int[] numbers) {
        List<Integer> tmpList = new ArrayList<>();
        for(int j=0;j<numbers.length;j++) {
            if(index!=j) {
                tmpList.add(numbers[j]);
            }
        }
        int[] remainNums = new int[numbers.length - 1];
        for(int j=0;j<numbers.length-1;j++) {
            remainNums[j] = tmpList.get(j);
        }

        return remainNums;
    }

    private String showAnswer() {
        String result = String.join(" ", stack);
        System.out.println("答案： " + result);
        return result;
    }

    public boolean calc(int targetPoint, int[] numbers) {
        // 出口条件
        if(numbers.length == 1) {
            if(targetPoint == numbers[0]) {
                // 计算完成。 输出答案
                stack.add(String.valueOf(numbers[0]));
                showAnswer();
                stack.remove(stack.size()-1);
            }
            else {
                return false;
            }
        }


        // 取出一个数n
        int n, m;
        int[] remainNums;

        for(int i=0;i<numbers.length;i++) {
            n = numbers[i];
            remainNums = getRemains(i, numbers);

            stack.add(String.valueOf(n));
            m = 0;
            for(String op : Arrays.asList("+", "-", "*", "/")) {
                if("+".equals(op)) {
                    if(targetPoint > n) {
                        m = targetPoint - n;
                    }
                }
                if("-".equals(op)) {
                    m = targetPoint + n;
                }
                if("*".equals(op)) {
                    if(targetPoint % n == 0) {
                        m = targetPoint / n;
                    }
                }
                if("/".equals(op)) {
                    m = targetPoint * n;
                }

                if(m>0) {
                    // op, n
                    stack.add(op);
                    calc(m, remainNums);
                    stack.remove(stack.size()-1);
                }

            }

            stack.remove(stack.size()-1);
        }
        return false;
    }
}

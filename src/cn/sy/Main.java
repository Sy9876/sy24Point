package cn.sy;

public class Main {

    public int[] getNumbers(int expectedNumberCount) {
//        int[] numbers = {1, 1, 4, 6};
        int[] numbers = {8, 6, 3, 3};
        return numbers;

    }
    public static void main(String[] args) {
        Main main = new Main();

        int[] numbers = main.getNumbers(4);
        Sy24Point sy24Point = new Sy24Point(numbers);
        sy24Point.calc(24, numbers);

    }
}

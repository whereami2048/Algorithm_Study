
import java.util.*;
import java.io.*;

public class Main {
    static int N, W;
    static ArrayList<Integer>[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        W = Integer.parseInt(input[1]);

        arr = new ArrayList[N + 1];

        for (int i = 0; i < N + 1; i++) {
            arr[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            String[] temp = br.readLine().split(" ");
            int before = Integer.parseInt(temp[0]);
            int after = Integer.parseInt(temp[1]);

            arr[before].add(after);
            arr[after].add(before);
        }

        double leafCount = 0;
        for (int i = 2; i <= N; i++) {
            if (arr[i].size() == 1) {
                leafCount++;
            }
        }

        System.out.printf("%.10f%n", W/leafCount);
    }
}




import java.util.*;
import java.io.*;

public class Main {
    static int T;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            int[] tree = new int[N + 1];

            for (int j = 0; j < N - 1; j++) {
                String[] input = br.readLine().split(" ");
                int parent = Integer.parseInt(input[0]);
                int child = Integer.parseInt(input[1]);

                tree[child] = parent;
            }

            String[] input = br.readLine().split(" ");
            int node1 = Integer.parseInt(input[0]);
            int node2 = Integer.parseInt(input[1]);

            boolean[] visited = new boolean[N + 1];

            while (node1 != 0) {
                visited[node1] = true;
                node1 = tree[node1];
            }

            while (node2 != 0) {
                if (visited[node2]) {
                    System.out.println(node2);
                    break;
                }

                node2 = tree[node2];
            }
        }
    }
}


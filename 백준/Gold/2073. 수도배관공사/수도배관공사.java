import java.util.*;
import java.io.*;

public class Main {
    static int D, P;
    static List<Pipe> pipes = new ArrayList<>();
    static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        D = Integer.parseInt(input[0]);
        P = Integer.parseInt(input[1]);

        dp = new int[D + 1];
        dp[0] = Integer.MAX_VALUE;
        for (int i = 0; i < P; i++) {
            input = br.readLine().split(" ");
            int l = Integer.parseInt(input[0]);
            int c = Integer.parseInt(input[1]);

            pipes.add(new Pipe(l, c));
        }

        for (Pipe pipe : pipes) {
            for (int i = D; i >= pipe.L; i--) {
                dp[i] = Math.max(dp[i], Math.min(dp[i - pipe.L], pipe.C));
            }
        }

        System.out.println(dp[D]);
    }

    static class Pipe {
        public int L, C;

        public Pipe(int L, int C) {
            this.L = L;
            this.C = C;
        }
    }
}


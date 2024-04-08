import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int T = Integer.parseInt(input);

        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            String[] mbties = br.readLine().split(" ");
            if (N > 32) {
                System.out.println(0);
                continue;
            }

            int sum = Integer.MAX_VALUE;

            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    for (int k = j + 1; k < N; k++) {
                        sum = Math.min(sum, compareMbti(mbties[i], mbties[j], mbties[k]));

                        if (sum == 0) break;
                    }
                }
            }

            System.out.println(sum);
        }
        br.close();
    }

    private static int compareMbti(String s1, String s2, String s3) {
        int sum = 0;

        for (int i = 0; i < 4; i++) {
            sum += s1.charAt(i) != s2.charAt(i) ? 1 : 0;
            sum += s2.charAt(i) != s3.charAt(i) ? 1 : 0;
            sum += s3.charAt(i) != s1.charAt(i) ? 1 : 0;
        }

        return sum;
    }
}
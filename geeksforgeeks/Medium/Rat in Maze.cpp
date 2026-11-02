class Solution {
    public ArrayList<String> ratInMaze(int[][] maze) {
        // code here
        List<String> ans = new ArrayList<>();
        int[][] vis = new int[maze.length][maze[0].length];
        int di[] = {+1,0,0,-1};
        int dj[] = {0,-1,+1,0};
        if(maze[0][0] == 1) solve(0,0,maze.length,maze,ans,vis,"",di,dj);
        ArrayList<String> answer = new ArrayList<>(ans);
        return answer;
    }
    public void solve(int i, int j, int n, int[][] maze, List<String> ans, int[][] vis, String move, int[] di, int[] dj){
        if(i == n-1 && j == n-1){
            ans.add(move);
            return;
        }
        String dir = "DLRU";
        for(int ind=0; ind<4; ind++){
            int nexti = i + di[ind];
            int nextj = j + dj[ind];
            if(nexti >= 0 && nextj >= 0 && nexti < n && nextj < n && vis[nexti][nextj] == 0 && maze[nexti][nextj] == 1){
                vis[i][j] = 1;
                solve(nexti, nextj, n, maze, ans, vis, move+dir.charAt(ind), di, dj);
                vis[i][j] = 0;
            }
        }
    }
}
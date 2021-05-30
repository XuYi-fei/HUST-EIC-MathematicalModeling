function [result]=stable(P)
%% 一步转移
N_last = P;
N=N_last*P;

%% 计算平稳分布
while(norm(N_last-N,2)>0.0001)
    N_last = N;
    N = N*P;
end

%% 输赢的概率比
result = N(1,length(N)-1)/N(1,length(N));
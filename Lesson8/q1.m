%% 定义邻接矩阵
% a b c d e f g h i j k l m 
P = zeros(13,13);
P(1,2) = 4;P(2,1) = 4;P(1,3) = 3;P(3,1) = 3;P(1,4) = 1;P(4,1) = 1;
P(1,5) = 1;P(5,1) = 1;P(2,3) = 5;P(3,2) = 5;P(2,4) = 4;P(4,2) = 4;
P(2,6) = 3;P(6,2) = 3;P(3,7) = 1;P(7,3) = 1;P(4,6) = 2;P(6,4) = 2;
P(5,6) = 4;P(6,5) = 4;P(5,8) = 3;P(8,5) = 3;P(5,11) = 6;P(11,5) = 6;
P(6,7) = 3;P(7,6) = 3;P(6,9) = 4;P(9,6) = 4;P(6,12) = 3;P(12,6) = 3;
P(7,10) = 4;P(10,7) = 4;P(7,13) = 1;P(13,7) = 1;P(8,11) = 3;P(11,8) = 3;
P(8,12) = 1;P(12,8) = 1;P(9,10) = 6;P(10,9) = 6;P(9,12) = 1;P(12,9) = 1;
P(10,12) = 4;P(12,10) = 4;P(10,13) = 2;P(13,10) = 2;P(11,12) = 3;P(12,11) = 3;
P(12,13) = 5;P(13,12) = 5;

%% 创建图并绘制图像
P2 = tril(P); %获取下三角矩阵
[i,j,v] = find(P2); %找到矩阵中的每一个非零元
b = sparse(i,j,v,13,13); %构造稀疏矩阵

p = biograph(b,[],'ShowArrows','off','ShowWeights','on');
h = view(p);

[Dist,Path] = graphshortestpath(b,2,9,'Directed',false,'Method','Dijkstra');
% set(h.Nodes(Path),'Color',[1 0.4 0.4]);
edges = getedgesbynodeid(h,get(h.Nodes(Path),'ID'),get(h.Nodes(Path),'ID'));
% set(edges,'LineColor',[1 0 0]);
% set(edges,'LineWidth',2.0);
% 标红度数为奇数的结点
set(h.Nodes([3,4,8,9,11,13]),'Color',[1 0.4 0.4]);

%% 得到欧拉图
oddnodes = [3,4,8,9,11,13];
nodename = [1,2,3,4,5,6];
PA = zeros(6,6);
for i = 1:6
    for j = 1:6
        if(i==j)
            PA(i,j) = 0;
        end
        PA(i,j) = graphshortestpath(b,oddnodes(i),oddnodes(j),'Directed',false,'Method','Dijkstra'); 
    end
end
PA2 = tril(PA); %获取下三角矩阵
[i2,j2,v2] = find(PA2); %找到矩阵中的每一个非零元
b2 = sparse(i2,j2,v2,6,6); %构造稀疏矩阵

p2 = biograph(b2,[],'ShowArrows','off','ShowWeights','on');
h2 = view(p2); %绘制奇数结点生成的图

%% 欧拉巡回

E = zeros(13,13);
E(find(P~=0))=1;
E(1,5) = 2;E(5,1) = 2;E(4,6) = 2;E(6,4) = 2;E(3,2) = 2;E(2,3) = 2;





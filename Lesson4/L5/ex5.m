% c=[66.8  75.6  87  58.6 ...
%     57.2   66  66.4  53 ... 
%     78  67.8  84.6  59.4 ... 
%     70  74.2  69.6  57.2 ... 
%     67.4  71  83.8  62.4];
c=[66.8  75.6  87  58.6 ...
    57.2   66  66.4  53 ... 
    78  67.8  84.6  59.4 ... 
    70  74.2  75.2  57.2 ... 
    67.4  71  83.8  57.5];
A=blkdiag(ones(1,4),ones(1,4),ones(1,4),ones(1,4),ones(1,4));
b=ones(5,1);
Aeq=[eye(4) eye(4) eye(4) eye(4) eye(4)];
beq=ones(4,1);
lb=zeros(20,1);
ub=ones(20,1);
intcon=[1:20];
[x,fval,exitflag,output]=intlinprog(c,intcon,A,b,Aeq,beq,lb,ub);
xm =reshape(x,4,5)
fval

clc;clear
A=[8,6,4,5,1,7,3,2;
   8,2,3,1,6,5,4,7;
   5,2,1,7,6,8,3,4;
   7,6,3,8,5,4,1,2;
   4,6,2,7,3,8,5,1;
   4,5,8,6,3,7,1,2;
   5,2,6,4,8,7,1,3;
   6,1,4,3,8,7,2,5];

B=[4,3,8,1,5,2,6,7;
   3,5,7,4,2,8,1,6;
   8,1,3,7,2,4,5,6;
   7,3,1,8,5,4,2,6;
   3,7,1,8,4,5,6,2;
   8,7,5,1,6,3,2,4;
   4,7,8,3,2,6,5,1;
   8,2,4,5,3,6,1,7];

result = Match(A,B)

function [ D ] = Match( A,B )
n=size(A,2);
B1=zeros(1,n); 

for i=1:n
    Q(i)=i;
end   

while(~empty(Q))
    m=Q(1);Q=dequeue(Q);
    for i=1:n
        k=A(m,i); 
        if(B1(k)~=0) 
            if(shunxu(B,k,B1(k))>(shunxu(B,k,m))) 
                Q=enqueue(Q,B1(k));
                B1(k)=m;
                break;
            end
        else  
            B1(k)=m;
            break;
        end
    end
end

a=1:n;
D=[a;B1]; 
end

function [j] = shunxu(B,x,y)
n=size(B ,2);
j=1;
for i=1:n
     j=j+1;
     if (B(x,i)==y)
         break;
     end
end
end

function [ flag] = empty( Q)
flag=false;
if size(Q,2)==0
    flag=true;
end
end

function [ Q] = enqueue( Q ,x)
n=size(Q,2);
Q(n+1)=x;
end

function [Q] = dequeue(Q  )
n=size(Q,2);
for i=1:n-1
    Q(i)=Q(i+1);
end
Q(n)=[];
end

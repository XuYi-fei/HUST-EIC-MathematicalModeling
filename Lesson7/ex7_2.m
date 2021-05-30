clc;clear;
format long;

%% data1
H=zeros(6,6);
H(1,3)=1;
H(3,2)=1/2; H(5,2)=1/2; 
H(2,4)=1/2; H(5,4)=1/2; 
H(4,5)=1;
H(3,6)=1; 

%% data2
J=zeros(8,8);
J(1,2)=1;
J(1,3)=1;
J(2,4)=1;
J(2,5)=1;
J(3,6)=1;
J(3,7)=1;
J(3,8)=1;

%% damp factor and error
d=0.15;
% d=0.85;
error=0.001;

%%  result
[v1,t1]=rank(H,d,error)
[v2,t2]=rank(J,d,error)



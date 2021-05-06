clear;
img = imread("go.jpg");
%原二值图如下：
subplot(2,2,1);
imshow(img);

title("原图");
img = im2double(img);
[u,s,v] = svd(img);
s(s<1) = 0;
img = u*s*v';
subplot(2,2,2);
image(256*img);
colormap(gray(256));
title("分解后重构的图像");

img = imread("go.jpg");
img = im2double(img);
row = length(img);
col = length(img(1,:));
noise = normrnd(0.05, 0.2, row, col);
img = img + noise;
img(img>1) = 1;
img(img<0) = 0;
subplot(2,2,3);
image(256*img);
colormap(gray(256));
title("加入噪声后的图像");

[u,s,v] = svd(img);
s(s<1) = 0;
img = u*s*v';
subplot(2,2,4);
image(256*img);
colormap(gray(256));
title("加噪后分解重构的图像");





clear;
img = imread("go.jpg");
%原二值图如下：
subplot(1,2,1);
imshow(img);

title("原图");
img = im2double(img);
[u,s,v] = svd(img);
s(s<1) = 0;
img = u*s*v';
subplot(1,2,2);
image(256*img);
colormap(gray(256));
title("分解后重构的图形");


function plot_model()
% ran this first: grep -v [A-Za-df-z] design.mat | grep [0-9] > design.mtx
clear;
close all;

load design.mtx
%normed_design = mapminmax(design);
normed_design = zscore(design);


%normed_design = design;

%y = 2*(x - min(x(:))/(max(x(:)) - min(x(:))) - 1);
%normed_design = y;
for i = 1:size(normed_design,2)
    normed_design(:,i) = normed_design(:,i) + i*5;
    %plot(normed_design(:,i))
end
figure,plot(normed_design)

keyboard

end

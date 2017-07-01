clear;
maindir = pwd;
subnums = dir(fullfile(maindir,'data'));
subnums = struct2cell(subnums);
subnums = subnums(1,4:end);

nets = [4 8 9 10];
resultsmat = zeros(length(subnums),8); % reward, punishment -- for each net

for s = 1:length(subnums)
    for n = 1:length(nets)
                
        featdir = fullfile(maindir,'data',subnums{s},'tfMRI_GAMBLING_LR','lev1.feat');
        design = load(fullfile(featdir,'design.mtx'));
        data = load(fullfile(featdir,sprintf('net%02d.txt',nets(n))));
        sLR = regstats(zscore(data),zscore(design),'linear',{'all'});
        
        featdir = fullfile(maindir,'data',subnums{s},'tfMRI_GAMBLING_RL','lev1.feat');
        design = load(fullfile(featdir,'design.mtx'));
        data = load(fullfile(featdir,sprintf('net%02d.txt',nets(n))));
        sRL = regstats(zscore(data),zscore(design),'linear',{'all'});
        
        tmpB = mean([sRL.beta sLR.beta],2);
        resultsmat(s,(n*2)-1) = tmpB(2);
        resultsmat(s,n*2) = tmpB(3);
        
 
    end
end


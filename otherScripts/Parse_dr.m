fid = fopen('/Volumes/KATYA5GBA/DRlist_event.txt','r');
C = textscan(fid,'%s');
fclose(fid);
file_list = C{1};
 
Nfiles = length(file_list);
for f = 1:Nfiles
    outdir = file_list{f}(1:end-26);
    thenets = load(fullfile('/Volumes/KATYA5GBA','DRlist_event',sprintf('dr_stage1_subject%05d.txt',f-1)));
    for n = 1:10
        outfile = fullfile(outdir,sprintf('net%02d.txt',n));
        dlmwrite(outfile,thenets(:,n));
    end
end
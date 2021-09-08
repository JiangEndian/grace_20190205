 #!/bin/bash
 
i=1001;
newName=$(date +%Y%m%d)

#${FILE%%.*} 取头
#${FILE%.*} 去尾
#${FILE#*.} 去头
#${FILE##*.} 取尾

for one in $(ls ${1}*);do 
    tail="${one##*.}"
    echo $one ${newName}_${i}.${tail};let i++;
done

read -p '请确认文件名及新文件名正确'

i=1001;
for one in $(ls ${1}*);do 
    tail="${one##*.}"
    mv $one ${newName}_${i}.${tail};let i++;
done

exit 0



#words='genesis exodus leviticus numbers deuteronomy joshua judges ruth 1_samuel 2_samuel 1_kings 2_kings 1_chronicles 2_chronicles ezra nehemiah esther job psalms proverbs ecclesiastes song isaiah jeremiah lamentations ezekiel daniel hosea joel amos obadiah jonah micah nahum habakkuk zephaniah haggai zechariah malachi matthew mark luke n_john_ acts romans 1_corinthians 2_corinthians galatians ephesians philippians colossians 1_thessalonians 2_thessalonians 1_timothy 2_timothy titus philemon hebrews james 1_peter 2_peter 1_john 2_john 3_john jude revelation'
words='exodus leviticus numbers deuteronomy joshua judges ruth 1_samuel 2_samuel 1_kings 2_kings 1_chronicles 2_chronicles ezra nehemiah esther job psalms proverbs ecclesiastes song isaiah jeremiah lamentations ezekiel daniel hosea joel amos obadiah jonah micah nahum habakkuk zephaniah haggai zechariah malachi matthew mark luke n_john_ acts romans 1_corinthians 2_corinthians galatians ephesians philippians colossians 1_thessalonians 2_thessalonians 1_timothy 2_timothy titus philemon hebrews james 1_peter 2_peter 1_john 2_john 3_john jude'
#ls *.txt | xargs -n1 -i{} mv {} {}_bak  #批量改后缀

num=1
for word in $words;do
mkdir ${num} 2> /dev/null
for fname in $(ls *$word*);do
    #echo ${num}_${fname}
    mv ${fname} ${num}
    #echo ${fname} > temp
    #chapter=$(cut -d'_' -f2,3,4,5,6 temp)
    #echo $num
    ##echo $chapter
done
let num++
done

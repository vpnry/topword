# 20 Nov 2020 - shellscript - find top k frequent word

# AWK programming script: https://en.wikipedia.org/wiki/AWK
# References: https://codegolf.stackexchange.com/questions/188133/bentleys-coding-challenge-k-most-frequent-words
# `mawk` is **FASTER** than the GNU `awk`.
# On Ubuntu install it:

# ```
# sudo apt update
# sudo apt install mawk
# ```

#--------------------- Script 1 -------------------------------------
# Extract top n frequent words, NR add lines number
# 999999999999 is the top 999999999999 lines (adjust it to your need)
# Delete the head --lines=999999999999 | to use all lines
#--------------------- Script 1 -------------------------------------

echo "|----------------------------|"
echo "|         Script 1           |"
echo "|    Generating TXT file     |"
echo "|----------------------------|"

date +%s

# Here, we ignore words < 2 chars
cat inputDir/* | mawk -v RS="[^a-zA-ZāīūṁṃṇḍḷṛṣśṭñṅĀĪŪṀṂṆḌḶṚṢŚṬÑṄ]+" '
{
    ary[tolower($0)] = ary[tolower($0)] + 1
} END {
    for (w in ary) if (length(w) > 2) { print ary[w] " " w }
}
' |
    sort -nr |
    head --lines=999999999999 |
    mawk '{ print NR " " $2, $1 }' >topword.txt

date +%s
echo " "

#--------------------- Script 2 -------------------------------------
# For User Dictionary (auto completion) Android keyboard:
# Remember to append this line:
# _id,word,frequency,locale,appid,shortcut
# to the first line of the csv file, (will be used as column names)
# frequency has the value [0->250]
# too many words will slow down your keyboard,
# Here we cut top 180k words only
#--------------------- Script 2 -------------------------------------

echo "|----------------------------|"
echo "|         Script 2           |"
echo "|    Generating CSV file     |"
echo "|----------------------------|"

date +%s

cat inputDir/* | mawk -v RS="[^a-zA-ZāīūṁṃṇḍḷṛṣśṭñṅĀĪŪṀṂṆḌḶṚṢŚṬÑṄ]+" '
{
    ary[tolower($0)] = ary[tolower($0)] + 1
} END {
    for (w in ary) if (length(w) > 2) { print ary[w] " " w }
}
' |
    sort -nr |
    head --lines=180000 |
    mawk '{
    t = $1 + 100
    if (t > 250) t = 250
    print(NR "," $2 "," t ",,0,")
    } ' >user_dict.csv

date +%s
echo " "

echo "|----------------------------|"
echo "|         Done all           |"
echo "|----------------------------|"
echo " "

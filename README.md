# shell-script - find top n frequent pāḷi words with mawk

+ [AWK](https://en.wikipedia.org/wiki/AWK)  - pattern scanning and text processing language.

+ `mawk` is **FASTER** than the `awk`. On Ubuntu install it:

```bash
sudo apt update
sudo apt install mawk
```


- Put all your *[entire tipitaka pāḷi]* text files to **inputDir** and run:

```bash
sh topword.sh
```
- `Script 2` will extract  top n frequent *pāḷi* words, and save them in a CSV file format  that can be imported to Android keyboard User Dictionary database (for auto completion/suggest pali words when tying).

- The output file of `Script 1` can  be used for other things like: generating Anki decks etc..

- You can disable `Script 1 or 2` by comment it with `#`.

# PS:

- **inputDir**  should have no sub-directories, if you have, you can easily combine this script with the command `find` etc.. to support `recursive`.

- To import CSV to SQLite database, can use **sqlitebrowser** with GUI. On Ubuntu, install **sqlite3, sqlitebrowser** by these commands:

```bash
sudo apt update
sudo apt install sqlite3 sqlitebrowser
```

- I learned a lot from this post: https://codegolf.stackexchange.com/questions/188133/bentleys-coding-challenge-k-most-frequent-words

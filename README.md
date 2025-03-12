admin@DESKTOP-F22EK55 MINGW64 ~ (master)
$ mkdir lab7

admin@DESKTOP-F22EK55 MINGW64 ~ (master)
$ dc lab7
bash: dc: command not found

admin@DESKTOP-F22EK55 MINGW64 ~ (master)
$ cd lab7

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git init
Initialized empty Git repository in C:/Users/admin/lab7/.git/

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git add das1.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git commit -m "dasgal1"
[master (root-commit) 0fb0a0a] dasgal1
 1 file changed, 15 insertions(+)
 create mode 100644 das1.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git add das2.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git commit -m "dasgal2"
[master 7775b0a] dasgal2
 1 file changed, 2 insertions(+)
 create mode 100644 das2.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git add das3.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git commit -m "dasgal3"
[master 830797b] dasgal3
 1 file changed, 6 insertions(+)
 create mode 100644 das3.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git add das4.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git commit -m "dasgal4"
[master 357675e] dasgal4
 1 file changed, 19 insertions(+)
 create mode 100644 das4.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git add das5.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git commit -m "dasgal5"
[master 2375aba] dasgal5
 1 file changed, 6 insertions(+)
 create mode 100644 das5.py

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git status
On branch master
nothing to commit, working tree clean

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git branch -M
fatal: branch name required

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (master)
$ git branch -M main

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (main)
$ remote add origin https://github.com/byambaa50/labo7.git
bash: remote: command not found

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (main)
$ git push -M master
error: unknown switch `M'
usage: git push [<options>] [<repository> [<refspec>...]]

    -v, --[no-]verbose    be more verbose
    -q, --[no-]quiet      be more quiet
    --[no-]repo <repository>
                          repository
    --[no-]all            push all branches
    --[no-]branches       alias of --all
    --[no-]mirror         mirror all refs
    -d, --[no-]delete     delete refs
    --[no-]tags           push tags (can't be used with --all or --branches or --mirror)
    -n, --[no-]dry-run    dry run
    --[no-]porcelain      machine-readable output
    -f, --[no-]force      force updates
    --[no-]force-with-lease[=<refname>:<expect>]
                          require old value of ref to be at this value
    --[no-]force-if-includes
                          require remote updates to be integrated locally
    --[no-]recurse-submodules (check|on-demand|no)
                          control recursive pushing of submodules
    --[no-]thin           use thin pack
    --[no-]receive-pack <receive-pack>
                          receive pack program
    --[no-]exec <receive-pack>
                          receive pack program
    -u, --[no-]set-upstream
                          set upstream for git pull/status
    --[no-]progress       force progress reporting
    --[no-]prune          prune locally removed refs
    --no-verify           bypass pre-push hook
    --verify              opposite of --no-verify
    --[no-]follow-tags    push missing but relevant tags
    --[no-]signed[=(yes|no|if-asked)]
                          GPG sign the push
    --[no-]atomic         request atomic transaction on remote side
    -o, --[no-]push-option <server-specific>
                          option to transmit
    -4, --ipv4            use IPv4 addresses only
    -6, --ipv6            use IPv6 addresses only


admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (main)
$ git remote add origin https://github.com/byambaa50/labo7.git

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (main)
$ git branch -M main

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (main)
$ git push -u origin main
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 12 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (15/15), 1.46 KiB | 748.00 KiB/s, done.
Total 15 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
To https://github.com/byambaa50/labo7.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

admin@DESKTOP-F22EK55 MINGW64 ~/lab7 (main)

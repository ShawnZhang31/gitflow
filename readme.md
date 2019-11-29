# git flow 最佳实践
原文来自于：[Git最佳实践](https://www.toutiao.com/a6761272651877974542/?timestamp=1574354300&app=news_article&group_id=6761272651877974542&req_id=2019112200381901002607901636236FA1)  

如果一个团队在使用Git时没有一些规范，那么将是一场难以醒来的噩梦！然而，规范固然重要，但更重要的是个人素质，在使用Git时需要自己养成良好的习惯。本文要从具体实践角度，尤其是在团队协作中，阐述如何去好好地应用 Git。这里以一个小型的flask应用作为演示。

## 1. 提交
如何去写一个提交信息，在具体开发工作中主要需要遵守的原则就是**使每次提交都有质量**，只要坚持做到以下几点就 OK 了：
- 提交时的粒度是一个小功能点或者一个 bug fix，这样进行恢复等的操作时能够将**误伤**减到最低；
- 用一句简练的话写在第一行，然后空一行稍微详细阐述该提交所增加或修改的地方；
- 不要每提交一次就推送一次，多积攒几个提交后一次性推送，这样可以避免在进行一次提交后发现代码中还有小错误。  
假如已经把代码提交了，对这次提交的内容进行检查时发现里面有个变量单词拼错了或者其他失误，只要还没有推送到远程，就有一个不被他人发觉你的疏忽的补救方法——首先，把失误修正之后提交，可以用与上次提交同样的信息。  
![git graph](./images/git-history.jpeg)
然后，终端中执行命令 git rebase -i [SHA]，其中 SHA 是上一次提交之前的那次提交的，在这里是3b22372。
![git graph](./images/git-rebase-01.jpeg)
最后，这样就将两次提交的节点合并成一个，甚至能够修改提交信息！
![git graph](./images/git-history-02.jpeg)
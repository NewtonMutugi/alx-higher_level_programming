# 0x14. JavaScript - Web scraping

## Resources
### Read or watch:
- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco request module](https://www.youtube.com/watch?v=1vVybHDNlzQ)
- [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
- [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone,**without the help of Google:**

### General
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and fetch API
- How to read and write a file using `fs` module

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://intranet.alxswe.com/rltoken/W9rASrTqkF-xXjcwomrMLw) + [semicolons on top](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg). Also as reference: [AirBnB style](https://intranet.alxswe.com/rltoken/NZR55f9vk1dZXj5q7UI5mQ)
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## More Info
### Install Node 10

``` bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
[Documentation](https://intranet.alxswe.com/rltoken/GXh9DyGGivUB7pdq9Oqmzg)
``` bash
$ sudo npm install semistandard --global
```

### Install `request` module and use it
[Documentation](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)

``` bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

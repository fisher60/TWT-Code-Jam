# 1️⃣ WebSearch Project
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

:star: Star us on GitHub — it helps!

Hi! For this TWT-Code-Jam we had the topic "Generators", therefore [Sachin](https://github.com/Shivansh-007) , [FunkyMonkey](https://github.com/Roshannarma), [NMarco](https://github.com/marco-create), [wowzers](https://github.com/tshe777) decided to do a project on website generator.
It would initially ask the user for a input and then return a page on it. This page will 

##  Contributors


|                                       [Sachin](https://github.com/Shivansh-007)                                       |                                       [FunkyMonkey](https://github.com/Roshannarma)                                        |                                       [NMarco](https://github.com/marco-create)                                        |                                       [wowzers](https://github.com/tshe777)                                        |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | 
|                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/Shivansh-007)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/Roshannarma)                         |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/marco-create)                      |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/tshe777)                     |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/Shivansh-007)                        |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Shivansh-007)               |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Roshannarma)              |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/marco-create)           |          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/tshe777)         |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/marco-ninghetto-a0b983142/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |

<br>
<br>


## Table of content

- [Installation](#installation)
- [Usage](#Usage)
- [Setting Up APIs](#Setting-Up-APIs)
- [Examples](#Exampl.es)
    - [Search Page](#Search-Page)
    - [Result](#Results-Page)
    - [Screen Recording](#iScreenRecording)
- [License](#License)
- [Links](#Links-And-Resourcse)

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/Shivansh-007/TWT-Code-Jam`

### Setup 
<details open>
<summary>Modules you would need to dowload to run this awesome project !</summary>
<br>

```shell
pip3.8 intsall urllib
pip3.8 intsall json
pip3.8 intsall bs4
pip3.8 intsall requests
pip3.8 intsall re
pip3.8 intsall random
pip3.8 intsall requests
pip3.8 intsall PIl
pip3.8 intsall io 
pip3.8 intsall GoogleNews 
pip3.8 intsall wikipediaapi
pip3.8 intsall wikipedia
pip3.8 intsall webbrowser
pip3.8 intsall selenium
pip3.8 intsall googleapiclient
pip3.8 intsall flask
pip3.8 intsall time
```
</details>


**Linux**
```shell
$ sudo apt-get install python3.8-venv
$ python3.8 -m venv venv
```
Move all the files from the cloned folder to this virtual venv

```shell
$ . bin/activate
$ export FLASK_ENV=development
$ export FLASK_APP=server.py
$ flask run
```

**Windows**

```PowerShell
> pip install virtualenv
```
CD into the cloned repository and create virtual environment named 'venv' (can be whatever you want)
```
> cd .\cloned\repo
> virtualenv venv -p C:\Python\Python3.8\python.exe
```
Activate the virtual env and run the code
```
> .\venv\Scripts\activate
> $env:FLASK_APP = "server.py"
> flask run
```


## Usage

Once everything is set, the command line should run like following

![Picture](https://user-images.githubusercontent.com/53913990/91655073-5fc24e00-eaae-11ea-856a-05158fb4178a.png)

Just copy the url and paste it into browser and go!

## Setting Up APIs

<details open>
<summary>Setting up the YouTube APIs!!</summary>
<br>

- Go to https://developers.google.com/ and log in or create an account, if necessary.
- After logging in go to this link https://console.developers.google.com/project and click on the blue CREATE PROJECT button as depicted in the photo below. Wait a moment as google prepares your project.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.12.36-PM.png)
- Fill in whatever Project Name you want.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.14.40-PM.png)
- Then click GoogleAPIs link in the top left corner and then click the link option called “YouTube Data API v3” It’s under YouTube API’s. You can see it below:

![Picture](https://plugins360.com/wp-content/uploads/2018/11/youtube-data-api-v3-box.png)
- Now click on the “ENABLE” button.
- Next click on the blue ‘Go to Credentials’ button to the right.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.17.34-PM.png)
- Choose the select option YouTube Data API v3 for the first select option and Web server(e.g. node js. Tomcat) for the second selection. Then choose Public data. Now click the blue button, “What credentials do I need?.”

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.21.07-PM.png)
- Almost done, wait for google to create your new project and you should see the screen below where you can copy your API Key.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.21.38-PM.png)
- Paste the API Key in the Fetch_Contents/youtube_singleReturn.py file

</details>

## Examples

To be Done

### Search Page

Enter the topic you'd like to look for and press ENTER

![Picture](https://user-images.githubusercontent.com/53913990/91655217-55548400-eaaf-11ea-930b-1f966e5ae885.png)

### Results Page

First half of the page To be added

![Picture](https://user-images.githubusercontent.com/53913990/91655294-cdbb4500-eaaf-11ea-86b8-a430dc5b400a.png)


### ScreenRecording

To be Done

## License

MIT License

Copyright (c) 2020 Sachin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Links And Resourcse

- [Dictionary API](https://dictionaryapi.com/)  
- [Wikipedia Library](https://pypi.org/project/wikipedia/)  
- [Wikipedia API](https://pypi.org/project/Wikipedia-API/)  
- [How to install Youtube API - easy](https://www.youtube.com/watch?v=th5_9woFJmk&t=185s)  
- [Google News API](https://pypi.org/project/GoogleNews/)

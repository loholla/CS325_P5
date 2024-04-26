# Welcome to my Web Scraper 
## This project was made for my CS325 class, but it is a program that will take the link from a news article and output the raw text without any HTML tags. 

### Step 1: Setting up the environment
Install Miniconda and download the file webscraperp3.yaml. Once you have done that, use the command "conda env create -f webscraperp3.yaml" to create your environment.

Once you have made your environment, run the command "conda activate CS325_Proj3", unless you gave the environment a custom name.

### Step 2: Setting up the API Key
Once your environment is set up, you need to make an OpenAI API Key. First, however, you may need to make an account. 

#### Step 2.1: Setting up account
To make an account go to platform.openai.com, then create yourself an account.

#### Step 2.2: Checking for credits
If you already have an account, make sure you have credits available to run the API. 

To do this, go to the tab labeled Usage on the side bar, and see if you have credits available.

#### Step 2.3: Making API Key
So, you have enough credits and you have an account to make an API key with.

To make an API Key, go to the tab API keys on the side bar, and click it.

Once on that page, click the button labeled "Create new secret key".

Put this key somewhere you can find it again if needed, but you will need it in your computer's clipboard (ctrl + c) for the next part.

#### Step 2.4: Adding API Key
To add your API Key run the following command: setx OPENAI_API_KEY "your-api-key-here"
    Replace "your-api-key-here" with your API key that is in your clipboard, but leave the quotation marks there, because your API key needs to be inside quotation marks.

To test that this worked, you will have to close miniconda, reopen it, reactivate your environment, and then run this command: echo %OPENAI_API_KEY%
    This command should tell you the API key that you are to use.

The above commands only work for Windows computers. For MacOS, use the following instructions:
Use the command
    'nano ~/.bash_profile'
or
    'nano ~/.zshrc'
to open the profile file in a text editor. Then, the editor, add the line
    export OPENAI_API_KEY='your-api-key-here'
while replacing "your-api-key-here" with your actual API key.

Then save and exit the text editor using Ctrl+O, followed by Ctrl+X

Next, load your profile using
    'source ~/.bash_profile'
or
    'source ~/.zshrc'
to load the updated profile. Finally, verify that it works by using the command echo $OPENAI_API_KEY

-Please note, I used Windows when making this program, and I just rewrote the instructions from the OpenAI website here just to make it easier to find.
 If you want to look at the instructions directly on the webpage, the link is: https://platform.openai.com/docs/quickstart?context=python.

 ### Step 3: Setting up the file folders
 Once all of the above is done, you will need to download the files run.py and articles.txt, and the folders module_1, module_2, module_3, and Data. All of these folders should be in the same folder as run.py and articles.txt, or else the program will not work.

 ### Step 4: Running the program
 If you want to run the example articles, go into Miniconda and change the directory to the folder that run.py is in using the command cd "FolderPath", where "FolderPath" is the path structure to where run.py is.
 
 Next, use the command: python run.py articles.txt
 
 Running this command will generate 3 different files per article. A "article_X_raw.txt", "article_X_full.txt", and a "article_X.txt", where X is the number of the article in the list of articles in article.txt.
 A summarized article will be in article_X.txt, and will have a title in quotation marks at the top. All of the example articles are pulled from the news outlet CNN, with the link being https://www.cnn.com/business/tech

 ### Warnings:
 This Web Scraper only works for CNN articles, and has only been tested on articles gathered through this link: https://www.cnn.com/business/tech.
 This Web Scraper may work on other CNN articles, but not on any other website unless they use the exact same structure and classes as the CNN website does.
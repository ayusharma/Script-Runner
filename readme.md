#Flask Script Runner

#### Step- 1 : Creating Virtual Environemt
./setup.sh

#### Step-2 : Activate Virtual Environment
source venv/bin/activate

#### Step-3 : Installing dependecies
pip install -r requirement.txt

#### Step-4 :  Insert shell script name and absolute path in settings.py
Example: 'test':'/var/www/html/parser/test.sh'

Here "test" is scrpit name that we define and it's absolute path is '/var/www/html/parser/test.sh' [You can check by pwd]

#### Step 5: Run the project
python app.py

#### Step 6 : Passing the parameters
http://localhost:5000/?script=[name of script in settings.py]&args=[arg1,arg2]

Example: http://localhost:5000/?script=test&args=hello

Here we have executed test.py and it's path is '/var/www/html/parser/test.py'
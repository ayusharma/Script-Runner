#Flask Script Runner

#### Step- 1 : Creating Virtual Environemt
./setup.sh

#### Step-2 : Activate Virtual Environment
source venv/bin/activate

#### Step-3 : Installing dependecies
pip install -r requirement.txt

#### Step 4: Run the project
python app.py

#### Step 5 : Passing the parameters
http://localhost:5000/?script=[name of script in settings.py]&args=[arg1,arg2]

Example: http://localhost:5000/?script=test&args=hello
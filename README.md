# coaching
Fetches the details of coaching institutes in a particular location 

Requirements:

1.Install virtual environment in your pc/laptop using ''' sudo pip install virtualenv '''

2.Create and Activate your virtual env - # ''' virtualenv environment_name ''' Creating 
                                         # ''' source environment_name/bin/activate ''' Activatin
                                         
3. Clone this repository.
4. Install the requirements as stated in the requirements.txt

5. Run the django server -  python manage.py runserver

6. Go to any browser and hit the url - localhost:8000/coaching/institutes?location= "any of bangalore, ncr , mumbai, pune"

7. For getting more results try hitting the above url - localhost:8000/coaching/institutes?location= "any of bangalore, ncr , mumbai, pune"&next="next_page_token returned in the previous results.


This API extracts information of the coachng institutes in mumbai, ncr, pune and bangalore by requesting data from google place api. It fetches 20 records at a time and can fetch more by appending the next page token which is returned in previous api results.





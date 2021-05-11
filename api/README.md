# Backend API using AWS Lambda

### Setup
Just run the following command to generate the zip file to be uploaded on AWS Lambda:
```
./compile.sh
```

This will generate a file named `IndianElectionAssistant.zip` which can be uploaded into the "Code source" for AWS Lambda


#### Testing
We are writing the unit-tests using `unittest`, which is a part of the standard python library. [Here](https://docs.python.org/3/library/unittest.html) is the documentation for the library.

We have not yet set up an automated CI/CD pipeline for this project. You are welcome to do it yourself and update the README alongwith


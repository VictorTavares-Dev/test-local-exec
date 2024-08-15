# test-local-exec

## Repository Documentation

This repository contains a Terraform project that demonstrates the usage of the `terraform_data` resource. It also utilizes the `local-exec` provisioner to execute a bash script file.

### Python Scripts

This repository includes two Python scripts:

1. `script.py`: This is a simple python script to covert meters to feet and vice versa.
2. `test_script.py`: This script represents unit tests for the `script.py` file



The bash script provided is performing the following tasks:

1. It defines a log function to print log messages with timestamps.
2. It creates a new directory with the name as the current date in the format YYYYMMDD.
3. It checks if the directory creation was successful and logs the appropriate message.
4. It runs pytest on the `test_script.py` file and redirects the output to a file named `test_results.txt` inside the newly created directory.
5. It checks the exit code of pytest. If there are no errors, it logs a message and runs the `script.py` file, redirecting the output to a file named `output.txt` inside the same directory.
6. If there are errors detected during pytest, it logs an error message and aborts the script execution.

Below, an excerpt of the execution of `run.sh` which generated the `/20240815` folder and the files within it:

````Shell
$ terraform apply --auto-approve

terraform_data.test: Creating...
terraform_data.test: Provisioning with 'local-exec'...
terraform_data.test (local-exec): Executing: ["cmd" "/C" "sh run.sh"]
terraform_data.test (local-exec): 2024-08-15 06:25:21 - Starting script execution
terraform_data.test (local-exec): 2024-08-15 06:25:21 - Creating directory './20240815'
terraform_data.test (local-exec): 2024-08-15 06:25:21 - Directory created successfully
terraform_data.test (local-exec): 2024-08-15 06:25:21 - Running 'pytest test_script.py'
terraform_data.test (local-exec): ============================= test session starts =============================
terraform_data.test (local-exec): platform win32 -- Python 3.10.2, pytest-7.1.2, pluggy-1.0.0
terraform_data.test (local-exec): rootdir: C:\Users\Victor\Documents\Code\Repos\test-terraform
terraform_data.test (local-exec): plugins: anyio-4.3.0
terraform_data.test (local-exec): collected 2 items

terraform_data.test (local-exec): test_script.py ..                                                        [100%]

terraform_data.test (local-exec): ============================== 2 passed in 0.02s ==============================
terraform_data.test (local-exec): 2024-08-15 06:25:22 - No errors detected. Running script.py...
terraform_data.test (local-exec): 10 meters is equal to 32.8084 feet
terraform_data.test (local-exec): 32.8084 feet is equal to 10.0 meters
terraform_data.test: Creation complete after 0s [id=04740deb-b56c-45f2-599c-e869f5343de5]
````

## New implementations
Below, some features to be implemented:
1. Consider to use IAM role credentials to adhere the least privillege approach;
2. Output the results in an S3 bucket;
3. Create the process documentation in order to detail the correct use of the repository.


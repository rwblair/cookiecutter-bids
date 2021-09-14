Quickstart
----------

Install Cookiecutter:

    pip install -U cookiecutter

Generate dataset:

        cookiecutter https://github.com/rwblair/cookiecutter-bids.git


```
~ $ cookiecutter https://github.com/rwblair/cookiecutter-bids.git
dataset_name [new_dataset]: my_dataset
bids_version [v1.4.1]: 
number_of_subjects [1]: 2
number_of_sessions [1]: 2
anat [n]: y
func [n]: y
fmap [n]: n
dwi [n]: n
eeg [n]: n
ieeg [n]: n
meg [n]: n

~ $ find my_dataset/
my_dataset/
my_dataset/dataset_description.json
my_dataset/sub-2
my_dataset/sub-2/ses-2
my_dataset/sub-2/ses-2/func
my_dataset/sub-2/ses-2/anat
my_dataset/sub-2/ses-1
my_dataset/sub-2/ses-1/func
my_dataset/sub-2/ses-1/anat
my_dataset/sub-1
my_dataset/sub-1/ses-2
my_dataset/sub-1/ses-2/func
my_dataset/sub-1/ses-2/anat
my_dataset/sub-1/ses-1
my_dataset/sub-1/ses-1/func
my_dataset/sub-1/ses-1/anat
```

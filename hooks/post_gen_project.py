import os

from collections import OrderedDict

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

modalities = ["anat", "func", "fmap", "dwi", "eeg", "ieeg", "meg"]

context = {{ cookiecutter }}

if __name__ == '__main__':
    subjects = int('{{ cookiecutter.number_of_subjects }}')
    subjects_padding = len('{{ cookiecutter.number_of_subjects }}')
    sessions = int('{{ cookiecutter.number_of_sessions }}')
    if sessions == 0:
        sessions = 1
    sessions_padding = len('{{ cookiecutter.number_of_sessions}}')

    for i in range(1, subjects + 1):
        subject = 'sub-{}'.format(str(i).zfill(subjects_padding))
        os.makedirs(os.path.join(PROJECT_DIRECTORY, subject), exist_ok=True)
        for j in range(1, sessions + 1):
            if sessions == 1:
                session = ''
            else:
                session = 'ses-{}'.format(str(j).zfill(sessions_padding))
            for modality in modalities:
                if context.get(modality) != 'n':
                    os.makedirs(os.path.join(PROJECT_DIRECTORY, subject, session, modality), exist_ok=True)

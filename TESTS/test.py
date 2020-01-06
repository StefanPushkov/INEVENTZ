from subprocess import check_output
import subprocess

list_of_accounts = []
def get_data_from_accounts(account: str):
    a = subprocess.getoutput('instagram-scraper {0} --media-metadata'.format(account))
    # a = check_output("dir", shell=True).decode()
    print("DATA FROM {0} ACCOUNT".format(account), a)

if __name__ == "__main__":
    for i in list_of_accounts:
        get_data_from_accounts(account=i)

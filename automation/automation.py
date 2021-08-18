
import re

def collect_emails(path):

    with open(path,"r") as file:
        info = file.read()
        emails = re.findall(r'\S+@\S+', info)
        emails.sort()

        clean_email = [] # email without duplicates

        for i in emails:
            if i not in clean_email:
                clean_email.append(i)

        with open('./automation/assest/emails.txt', 'w') as emails_file:
            for i in emails:
                emails_file.write(f'{i}\n')    



def collect_phone_numbers(path):
    
    with open(path,"r") as file:
        info = file.read()

        phone_number_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

        phones = re.findall(phone_number_pattern, info)
        phones.sort()
        clean_phone_numbers = [] # num without duplicates

        for i in phones:

            number = re.sub('[^0-9]+', '', i)
            shape_number = re.sub(r"(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(number[:-1])) + number[-1]
            if len(shape_number) < 12:

                shape_number = '206' + shape_number[2:]

            if shape_number not in clean_phone_numbers:

                clean_phone_numbers.append(shape_number)

        clean_phone_numbers.sort()
        with open('./automation/assest/phone_numbers.txt', 'w') as numbers_file:
            for i in clean_phone_numbers:
                numbers_file.write(f'{i}\n')



if __name__ == '__main__':
   collect_emails("./automation/assest/potential-contacts.txt")
   collect_phone_numbers("./automation/assest/potential-contacts.txt")
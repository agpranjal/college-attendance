import requests
import bs4
import time

URL = "http://45.124.144.116/www/stu/stulogin.php"
CID = int(input("Enter CID: "))
rollno = int(input("Enter university rollno: "))
password = input("Enter MIS password: ")
sem = input("Enter semester: ")

data = {
        "t1":CID,
        "t2":password
        }

sess = requests.Session()
ro = sess.post(URL, data)
print("Logged in. Fetching the attendance...")

URL = "http://45.124.144.116/www/stu/stu_rpt.php"

t = time.localtime()
year = str(t.tm_year)
month = str(t.tm_mon).zfill(2)
day = str(t.tm_mday).zfill(2)
start = "2020-07-13"
today = f"{year}-{month}-{day}"

data = {
        "rollno": rollno,
        "dt1":start,
        "dt2":today,
        "t":"1",
        "sem":sem
        }

ro = sess.post(URL, data)
soup = bs4.BeautifulSoup(ro.content, "html.parser")
attendance = soup.find_all("table")[-1]
rows = attendance.find_all("tr")

print(f"From: {start}")
print(f"To: {today}")
print(f"Roll no: {rollno}")
print()

subject = "Subject"
total_classes = "Total classes"
attended = "Attented"
attendance = "Attendance"
print(subject.ljust(20), total_classes.ljust(20), attended.ljust(20), attendance.ljust(20))

for row in rows:
    data = row.find_all("td")

    for d in data[1:]:
        print(d.text.ljust(20), end=" ")
    print()

print(rows[-1].td.text.strip().ljust(20))

total_classes = 0
attended_classes = 0

for row in rows[:-1]:
    total_classes += int(row.find_all("td")[2].text)
    attended_classes += int(row.find_all("td")[3].text)

print("Actual attendance:", attended_classes/total_classes*100)

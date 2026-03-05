StudentName='Medisetti Sai Rajeev Lochan'
StudentID=2901
BatchNo='PFS-HYD-050'
EmailID='medesettysai@gmail.com'
Age=21
Gender='Male'
BloodGroup='A+'
City='Hyderabad'
State='Telengana'
StudentPhoneNumber=9347336338
GithubLink='https://github.com/sai-rajeev-67'
CollegeName='Seshadri Rao Gudlavalleru Engineering College'
USNNumber='21481A1296'
Qualification='UG (Bachelor Degrees)'
Department='B.Tech - Information Technology (IT)'
PassOutYear= 2025
GraduationPercentage=78
Arrears='No'
_10PassYear=2019
_10Percentage=97
_12PassYear=2021
_12Percentage=88
Skills='Python, Flask, HTML, CSS, Bootstrap, Javascript, MySQL'

print("""
----- Personal Information -----""")
print(f"""
Student Name        : {StudentName}
Student ID          : {StudentID}
Batch Number        : {BatchNo}
Email ID            : {EmailID}
Age                 : {Age}
Gender              : {Gender}
Blood Group         : {BloodGroup}
City                : {City}
State               : {State}
Phone Number        : {StudentPhoneNumber}
""")

print(f"""
----- Academic Information -----""")

print(f"""
College Name        : {CollegeName}
USN Number          : {USNNumber}
Qualification       : {Qualification}
Department          : {Department}
Pass Out Year       : {PassOutYear}
Graduation %        : {GraduationPercentage}
Arrears             : {Arrears}
10th Pass Year      : {_10PassYear}
10th Percentage     : {_10Percentage}
12th Pass Year      : {_12PassYear}
12th Percentage     : {_12Percentage}
Skills              : {Skills}
Github              : {GithubLink}
""")

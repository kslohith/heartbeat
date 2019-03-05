from firebase import firebase

firebase=firebase.FirebaseApplication('https://console.firebase.google.com/u/0/project/halo2-1ce47/database/halo2-1ce47/data/Patients')

result = firebase.post('/Lohith',{'Heartrate':'82'})

print(result)

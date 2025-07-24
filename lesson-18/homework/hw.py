#homework 2
##1.
before_2014 = df_tack [df_tack ["creationdate"] <= "2014-01-01"]
questionsbefore = before_2014[["creationdate","title"]]
print(questionsbefore)

##2.
# df_tack.columns
more50 = df_tack [df_tack ["score"] > 50]
titlequestions = more50 [[ "title","score"]]
print(titlequestions)
##3.
midscore = df_tack [(df_tack ["score"] >= 50) & (df_tack ["score"]<= 100)]
titlequestions = midscore [[ "title","score"]]
print(titlequestions)
##4.
df_tack.columns
answerbyscott = df_tack [df_tack ["ans_name"] == "Scott Boston"]

result = answerbyscott[["title","score","ans_name"]]
print(result)
##5.
df_tack.head()
##6.
# df_tack["creationdate"] = pd.to_datetime(df_tack["creationdate"])
f1 = df_tack[
    (df_tack["ans_name"]=="unutbu") &
    (df_tack["score"] <= 5) &
    (df_tack["creationdate"] >= "2014-03-01") &
    (df_tack["creationdate"] <= "2014-10-31")
]
f1[["id","ans_name","score","creationdate"]]

##7.
answrfilt = df_tack[
    ((df_tack["score"] >= 5) & (df_tack["score"] <= 10)) |
    (df_tack["viewcount"]> 10000)
]
result12 = answrfilt[["id","score","viewcount"]]
print(result12)

##8.
f4 = df_tack[df_tack["ans_name"] != "Scott Boston"]
print(f'questions that are not answered by Scott Boston are {len(f4)}')
questansw = f4[["id","creationdate","answercount","title"]]
print(questansw)

##Homework 3

df_titanic = pd.read_csv('titanic.csv')
df_titanic
##1.
females_class1 = df_titanic[(df_titanic["Sex"] == "female") &
           (df_titanic["Pclass"] == 1) &
           (df_titanic["Age"].between(20,30))
           ]
resultat = females_class1[["Pclass","Name","Sex","Age"]]
print(resultat)
print(f"Total matching passengers: {len(resultat)}")

##2.
more100 = df_titanic[df_titanic['Fare'] > 100]
result100 = more100[["PassengerId","Name","Fare"]]
print(result100)
print(f'Passenger who paid more than $100: {len(result100)}')

##3.
alone_survive = df_titanic[
    (df_titanic["Survived"] == 0) &
    (df_titanic["SibSp"] == 0) &
    (df_titanic["Parch"] == 0)
]
print(f'{len(alone_survive)} have survived alone on this plane')
alone_survive[["PassengerId","Name","Survived","SibSp","Parch"]]
##4.
embrk = df_titanic[(df_titanic["Embarked"] == "C") & (df_titanic['Fare'] > 50)]
print(f'Number of passengers who EMbarked from C is {len(embrk)}')
embrk[["PassengerId","Name","Fare","Embarked"]]
##5.
not_alone_passenger = df_titanic[
    (df_titanic["SibSp"] != 0) &
    (df_titanic["Parch"] != 0)
]
print(f'not alone passengers are {len(not_alone_passenger)}')
not_alone_passenger[["PassengerId","Name", 'SibSp', 'Parch']]

##6.
dead15= df_titanic[
    (df_titanic["Survived"] == 1) &
    (df_titanic["Age"] <= 15) 
]
print(f'{len(dead15)} passenegers who are under 15 years of age did not survive')
dead15[["Name","Survived","Age"]]
##7.
cabins_fare_over_200 = df_titanic[
    (df_titanic['Cabin'].notnull()) & 
    (df_titanic['Fare'] > 200)
]

cabins_fare_over_200.head()

##8.
odd_passenger_ids = df_titanic[df_titanic['PassengerId'] % 2 != 0]
print(f"Number of passengers with odd Passenger IDs: {len(odd_passenger_ids)}")
odd_passenger_ids
##9.
unique_ticket_df = df_titanic[
    df_titanic['Ticket'].isin(
        df_titanic['Ticket'].value_counts()
        [df_titanic['Ticket'].value_counts() == 1].index
    )
]
print(f"Number of passengers with unique ticket numbers: {len(unique_ticket_df)}")
unique_ticket_df.head()

miss_class1_df = df_titanic[
    (df_titanic['Name'].str.contains('Miss', case=False)) & 
    (df_titanic['Pclass'] == 1) & 
    (df_titanic['Sex'] == 'female')
]
print(f"Number of female Class 1 passengers with 'Miss' in their name: {len(miss_class1_df)}")
miss_class1_df.head()

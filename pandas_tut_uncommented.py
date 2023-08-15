import pandas as pd
import re


#  1 Problem

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    res = {
        "name": [],
        "population": [],
        "area": []
    }
    for x in world.index:
        if world.loc[x, "population"] >= 25000000 or world.loc[x, "area"] >= 3000000:
            print(f"name = {world.loc[x, 'name']}")
            res["name"].append(world.loc[x, "name"])
            res["population"].append(world.loc[x, "population"])
            res["area"].append(world.loc[x, "area"])
    return pd.DataFrame(res)


data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000],
        ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000],
        ['Angola', 'Africa', 1246700, 20609294, 100990000000]]

World = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
    {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})

res = big_countries(World)
print(f"{res}")


#  OR

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]


data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000],
        ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000],
        ['Angola', 'Africa', 1246700, 20609294, 100990000000]]

World = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
    {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})

res = big_countries(World)
print(f"{res}")

#  2 Problem

data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
Products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype(
    {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'})


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")]
    return df[["product_id"]]


print(find_products(Products))

#  3 Problem

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
Customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
data = [[1, 3], [2, 1]]
Orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})

print(Customers)
print()
print(Orders)


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    good = [orders.loc[x, "customerId"] for x in orders.index]
    res = {"Customers": []}
    for x in customers.index:
        if customers.loc[x, "id"] not in good:
            res["Customers"].append(customers.loc[x, "name"])
    return pd.DataFrame(res)


print(find_customers(Customers, Orders))

# 4 Problem

data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
        [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
    {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    myset = set()
    for x in views.index:
        if views.loc[x, "author_id"] == views.loc[x, "viewer_id"]:
            myset.add(views.loc[x, "author_id"])
    return pd.DataFrame({"id": sorted(list(myset))})


print(article_views(Views))


#   OR

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df.drop_duplicates(subset=['author_id'], inplace=True)
    df.sort_values(by=['author_id'], inplace=True)
    df.rename(columns={'author_id': 'id'}, inplace=True)
    return df.loc[:, ['id']]


#  5 Problem

data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
Tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id': 'Int64', 'content': 'object'})


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame: return pd.DataFrame({"tweet_id": [tweets.loc[x,
                                                                                                       "tweet_id"] for x
                                                                                            in tweets.index if len(
        tweets.loc[x, "content"]) > 15]})


print(invalid_tweets(Tweets))

#  6 Problem

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
Employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
    {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = {"employee_id": [], "bonus": []}
    for x in employees.index:
        if employees.loc[x, "employee_id"] % 2 != 0 and employees.loc[x, "name"][0] != 'M':
            df["employee_id"].append(employees.loc[x, "employee_id"])
            df["bonus"].append(employees.loc[x, "salary"])
        else:
            df["employee_id"].append(employees.loc[x, "employee_id"])
            df["bonus"].append(0)
    df = pd.DataFrame(df)
    df.sort_values(by=["employee_id"], inplace=True)
    return df


print(calculate_special_bonus(Employees))

# 7 Problem

data = [[1, 'aLice'], [2, 'bOB']]
Users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id': 'Int64', 'name': 'object'})


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    for x in users.index:
        name = users.loc[x, "name"].lower()
        name = name[0].upper() + name[1:]
        users.loc[x, "name"] = name
    users.sort_values(by=["user_id"], inplace=True)
    return users


print(fix_names(Users))

#  8 Problem

data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'],
        [3, 'Annabelle', 'bella-@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'],
        [5, 'Marwan', 'quarz2020@leetcode.com'], [6, 'David', 'david69@gmail.com'],
        [7, 'Shapiro', '.shapo@leetcode.com']]
Users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype(
    {'user_id': 'int64', 'name': 'object', 'mail': 'object'})


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex = r'^[a-zA-Z]+[a-zA-Z-._0-9]*@leetcode[.]com'
    for x in users.index:
        if not re.fullmatch(regex, users.loc[x, "mail"]):
            users.drop(x, axis="index", inplace=True)
    return users


print(valid_emails(Users))


#  OR

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    #     Use the str.match() method with a regex pattern to find valid emails
    valid_emails_df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return valid_emails_df


#  9 Problem

data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'],
        [5, 'Alain', 'DIAB201']]
Patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
    {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    for x in patients.index:
        if not re.search(r'\bDIAB1', patients.loc[x, "conditions"]):
            patients.drop(x, axis="index", inplace=True)
    return patients


print(find_patients(Patients))


# OR

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'\bDIAB1')]


print(find_patients(Patients))

#  10 Problem

data = pd.DataFrame({"id": [1, 2, 3], "salary": [100, 200, 300]})


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N > len(employee.index): return pd.DataFrame({f"getNthHighestSalary({str(N)})": [None]})
    employee.drop_duplicates(subset="salary", inplace=True)
    employee.sort_values(by=["salary"], inplace=True, ascending=False)
    if N > len(employee.index): return pd.DataFrame({f"getNthHighestSalary({str(N)})": [None]})
    return pd.DataFrame({f"getNthHighestSalary({str(N)})": [employee.iloc[N - 1, 1]]})


print(nth_highest_salary(data, 1))

# 11 Problem

data = [[1, 100], [2, 200], [3, 300]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset="salary", inplace=True)
    employee.sort_values(by=["salary"], inplace=True, ascending=False)
    if 2 > len(employee.index): return pd.DataFrame({f"SecondHighestSalary": [None]})
    return pd.DataFrame({f"SecondHighestSalary": [employee.iloc[2 - 1, 1]]})


print(second_highest_salary(Employee))

# 12 Problem

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000,
                                                                                                   1]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id': 'Int64',
                                                                                        'name': 'object',
                                                                                        'salary': 'Int64',
                                                                                        'departmentId': 'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
Department = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    temp_hash: dict[int, int] = {}
    for x in employee.index:
        if employee.loc[x, "departmentId"] not in temp_hash:
            temp_hash[employee.loc[x, "departmentId"]] = employee.loc[x, "salary"]
        else:
            temp_hash[employee.loc[x, "departmentId"]] = max(temp_hash[employee.loc[x, "departmentId"]],
                                                             employee.loc[x, "salary"])

    res = {"Department": [], "Employee": [], "Salary": []}

    def find_Department(id1: int, data1: pd.DataFrame) -> str:
        for x1 in data1.index:
            if data1.loc[x1, "id"] == id1:
                return data1.loc[x1, "name"]

    for x in employee.index:
        if employee.loc[x, "salary"] == temp_hash[employee.loc[x, "departmentId"]]:
            res["Department"].append(find_Department(employee.loc[x, "departmentId"], department))
            res["Employee"].append(employee.loc[x, "name"])
            res["Salary"].append(employee.loc[x, "salary"])
    return pd.DataFrame(res)


print(department_highest_salary(Employee, Department))

#  13 Problem

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
Scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id': 'Int64', 'score': 'Float64'})


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    temp_arr: [float] = []
    for x in scores.index:
        temp_arr.append(scores.loc[x, "score"])
    temp_arr = sorted(temp_arr, reverse=True)
    res = {"score": [], "rank": []}
    c: int = 1
    if len(temp_arr) > 0:
        prev: float = temp_arr[0]
        res["score"].append(temp_arr[0])
        res["rank"].append(c)
        for i in range(1, len(temp_arr)):
            if prev != temp_arr[i]:
                c += 1
            res["score"].append(temp_arr[i])
            res["rank"].append(c)

            prev = temp_arr[i]
    return pd.DataFrame(res)


print(order_scores(Scores))

# 14 Problem

data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
Person = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'int64', 'email': 'object'})


#  Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", ascending=True, inplace=True)
    person.drop_duplicates(subset="email", inplace=True)


delete_duplicate_emails(Person)
print(Person)

# 15 Problem

data = [[0, 95, 100, 105], [1, 70, None, 80]]
Products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3'])


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars='product_id', var_name='store', value_name='price').dropna()


print(rearrange_products_table(Products))

# 16 Problem

data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
Store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype(
    {'bill_id': 'int64', 'customer_id': 'int64', 'amount': 'int64'})


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    temp_hash: dict[int, int] = {}
    for x in store.index:
        if store.loc[x, "customer_id"] not in temp_hash and store.loc[x, "amount"] > 500:
            temp_hash[store.loc[x, "customer_id"]] = store.loc[x, "amount"]
        elif store.loc[x, "customer_id"] in temp_hash:
            temp_hash[store.loc[x, "customer_id"]] = max(temp_hash[store.loc[x, "customer_id"]],
                                                         store.loc[x, "amount"])
    return pd.DataFrame({"rich_count": [len(temp_hash)]})


print(count_rich_customers(Store))

# 17 Problem

data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 5, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-11'],
        [4, 3, '2019-08-24', '2019-08-26'], [5, 4, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13']]
Delivery = pd.DataFrame(data,
                        columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype(
    {'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]',
     'customer_pref_delivery_date': 'datetime64[ns]'})


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    c: int = 0
    for x in delivery.index:
        c += 1 if delivery.loc[x, "order_date"] == delivery.loc[x, "customer_pref_delivery_date"] else 0

    return pd.DataFrame({"immediate_percentage": [round((c / len(delivery) * 100), 2)]})


print(food_delivery(Delivery))


# OR

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"immediate_percentage": [
        round((len(delivery[delivery["order_date"] == delivery["customer_pref_delivery_date"]]) / len(delivery) * 100),
              2)]})


print(food_delivery(Delivery))

# 18 Problem

data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
Accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id': 'Int64', 'income': 'Int64'})


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    res = {"category": ["Low Salary", "Average Salary", "High Salary"], "accounts_count": [0, 0, 0]}
    for x in accounts.index:
        if accounts.loc[x, "income"] < 20000:
            res["accounts_count"][0] += 1
        elif 20000 <= accounts.loc[x, "income"] <= 50000:
            res["accounts_count"][1] += 1
        else:
            res["accounts_count"][2] += 1
    return pd.DataFrame(res)


print(count_salary_categories(Accounts))


# OR

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    l = len(accounts.loc[accounts.income < 20000])
    h = len(accounts.loc[accounts.income > 50000])
    a = len(accounts.loc[(accounts.income <= 50000) & (accounts.income >= 20000)])
    col = ['Low Salary', 'Average Salary', 'High Salary']
    return pd.DataFrame({'category': col, 'accounts_count': [l, a, h]})


# 19 Problem

data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'],
        ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
Employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype(
    {'emp_id': 'Int64', 'event_day': 'datetime64[ns]', 'in_time': 'Int64', 'out_time': 'Int64'})


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    hash: dict[int, dict:[str, int]] = {}
    # hash[id][event_day] = time
    for x in employees.index:
        id: int = employees.loc[x, "emp_id"]
        day: str = employees.loc[x, "event_day"].strftime('%Y-%m-%d')
        time: int = employees.loc[x, "out_time"] - employees.loc[x, "in_time"]
        if id in hash:
            if day in hash[id]:
                hash[id][day] += time
            else:
                hash[id][day] = time
        else:
            hash[id] = {}
            hash[id][day] = time

    res = {"day": [], "emp_id": [], "total_time": []}
    for i in hash:
        for j in hash[i]:
            res["emp_id"].append(i)
            res["day"].append(j)
            res["total_time"].append(hash[i][j])

    return pd.DataFrame(res)


print(total_time(Employees))

# 20 Problem

data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0],
        [3, 4, '2018-07-03', 5]]
Activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype(
    {'player_id': 'Int64', 'device_id': 'Int64', 'event_date': 'datetime64[ns]', 'games_played': 'Int64'})


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    def compare_dates(date1: str, date2: str) -> bool:
        # True - first bigger False - second bigger
        hour, min, sec = [date1.split('-')[0]], [date1.split('-')[1]], [date1.split('-')[2]]
        hour.append(date2.split('-')[0])
        min.append(date2.split('-')[1])
        sec.append(date2.split('-')[2])
        if hour[0] > hour[1]:
            return True
        elif hour[0] == hour[1] and min[0] > min[1]:
            return True
        elif hour[0] == hour[1] and min[0] == min[1] and sec[0] >= sec[1]:
            return True
        return False

    temp: dict[int, str] = {}

    for x in activity.index:
        if activity.loc[x, "player_id"] in temp:
            if not compare_dates(activity.loc[x, "event_date"].strftime('%Y-%m-%d'),
                                 temp[activity.loc[x, "player_id"]]):
                temp[activity.loc[x, "player_id"]] = activity.loc[x, "event_date"].strftime('%Y-%m-%d')
        else:
            temp[activity.loc[x, "player_id"]] = activity.loc[x, "event_date"].strftime('%Y-%m-%d')

    res = {"player_id": [], "first_login": []}

    for i in temp:
        res["player_id"].append(i)
        res["first_login"].append(temp[i])

    return pd.DataFrame(res)


print(game_analysis(Activity))

# 21 Problem

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
Teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype(
    {'teacher_id': 'Int64', 'subject_id': 'Int64', 'dept_id': 'Int64'})


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    hash: dict[int, set] = {}
    for x in teacher.index:
        if teacher.loc[x, "teacher_id"] in hash:
            hash[teacher.loc[x, "teacher_id"]].add(teacher.loc[x, "subject_id"])
        else:
            hash[teacher.loc[x, "teacher_id"]] = set()
            hash[teacher.loc[x, "teacher_id"]].add(teacher.loc[x, "subject_id"])

    res = {"teacher_id": [], "cnt": []}

    for i in hash:
        res["teacher_id"].append(i)
        res["cnt"].append(len(hash[i]))

    return pd.DataFrame(res)


print(count_unique_subjects(Teacher))

# 22 Problem

data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Math'],
        ['G', 'Math'], ['H', 'English'], ['I', 'English'], ['J', 'English'], ['K', 'English']]
Courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student': 'object', 'class': 'object'})


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = {"class": []}
    courses.sort_values(by="class", inplace=True, ignore_index=True)
    print(courses)
    if len(courses) > 0:
        prev: str = courses.loc[0, "class"]
    else:
        return pd.DataFrame({"class": []})
    c: int = 1
    for x in range(1, len(courses.index)):
        if courses.loc[x, "class"] == prev:
            c += 1
        else:
            if c >= 5:
                res["class"].append(prev)
                c = 1
        prev = courses.loc[x, "class"]
    if c >= 5:
        res["class"].append(prev)
    return pd.DataFrame(res)


print(find_classes(Courses))

find_classes(Courses)

# 23 Problem

data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype(
    {'order_number': 'Int64', 'customer_number': 'Int64'})


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    hash: dict[int, int] = {}
    for x in orders.index:
        if orders.loc[x, "customer_number"] in hash:
            hash[orders.loc[x, "customer_number"]] += 1
        else:
            hash[orders.loc[x, "customer_number"]] = 1

    maxim = float("-inf")
    for i in hash:
        maxim = max(hash[i], maxim)

    res = []

    for i in hash:
        if hash[i] == maxim:
            res.append(i)

    return pd.DataFrame({"customer_number": res})


print(largest_orders(orders))

# 24 Problem

data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'],
        ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
Activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype(
    {'sell_date': 'datetime64[ns]', 'product': 'object'})


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    hash = {}
    for x in activities.index:
        date = activities.loc[x, "sell_date"]
        product: str = activities.loc[x, "product"]
        if date in hash:
            hash[date].add(product)
        else:
            hash[date] = set()
            hash[date].add(product)

    res = {"sell_date": [], "num_sold": [], "products": []}

    for i in hash:
        res["sell_date"].append(i)
        res["num_sold"].append(len(hash[i]))
        res["products"].append(sorted(list(hash[i])))

    return pd.DataFrame(res).sort_values(by="sell_date", ignore_index=True)


# OR

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby('sell_date')['product'].agg(
        [('num_sold', 'nunique'), ('products', lambda x: ','.join(sorted(x.unique())))]).reset_index()


print(categorize_products(Activities))

# 25 Problem

data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2],
        ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2],
        ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2],
        ['2020-12-7', 'honda', 2, 1]]
DailySales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype(
    {'date_id': 'datetime64[ns]', 'make_name': 'object', 'lead_id': 'Int64', 'partner_id': 'Int64'})


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    hash: dict[str, dict[str, [set, set]]] = {}
    # hash[date][name][0] = leads
    # hash[date][name][1] = partners

    for x in daily_sales.index:
        date: str = daily_sales.loc[x, "date_id"].strftime('%Y-%m-%d')
        name: str = daily_sales.loc[x, "make_name"]
        lead: int = daily_sales.loc[x, "lead_id"]
        partner: int = daily_sales.loc[x, "partner_id"]
        if date in hash:
            if name in hash[date]:
                hash[date][name][0].add(lead)
                hash[date][name][1].add(partner)
            else:
                hash[date][name] = [set(), set()]
                hash[date][name][0].add(lead)
                hash[date][name][1].add(partner)
        else:
            hash[date] = {}
            hash[date][name] = [set(), set()]
            hash[date][name][0].add(lead)
            hash[date][name][1].add(partner)

    res = {"date_id": [], "make_name": [], "unique_leads": [], "unique_partners": []}

    for date in hash:
        for name in hash[date]:
            res["date_id"].append(date)
            res["make_name"].append(name)
            res["unique_leads"].append(len(hash[date][name][0]))
            res["unique_partners"].append(len(hash[date][name][1]))

    return pd.DataFrame(res)


print(daily_leads_and_partners(DailySales))

# 26 Problem

data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
ActorDirector = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype(
    {'actor_id': 'int64', 'director_id': 'int64', 'timestamp': 'int64'})


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    hash: dict[int, dict:[int, int]] = {}
    for x in actor_director.index:
        if actor_director.loc[x, "actor_id"] in hash:
            if actor_director.loc[x, "director_id"] in hash[actor_director.loc[x, "actor_id"]]:
                hash[actor_director.loc[x, "actor_id"]][actor_director.loc[x, "director_id"]] += 1
            else:
                hash[actor_director.loc[x, "actor_id"]][actor_director.loc[x, "director_id"]] = 1
        else:
            hash[actor_director.loc[x, "actor_id"]] = {}
            hash[actor_director.loc[x, "actor_id"]][actor_director.loc[x, "director_id"]] = 1

    res = {"actor_id": [], "director_id": []}

    for actor in hash:
        for director in hash[actor]:
            if hash[actor][director] >= 3:
                res["actor_id"].append(actor)
                res["director_id"].append(director)

    return pd.DataFrame(res)


print(actors_and_directors(ActorDirector))

# 27 Problem

data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
Employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'int64', 'name': 'object'})
data = [[3, 1], [11, 2], [90, 3]]
EmployeeUNI = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id': 'int64', 'unique_id': 'int64'})


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    res = {"unique_id": [], "name": []}
    for x in employees.index:
        if employees.loc[x, "id"] in employee_uni["id"].values:
            temp = employee_uni.query(f"id == {employees.loc[x, 'id']}")["unique_id"].values[0]
            res["unique_id"].append(temp)
        else:
            res["unique_id"].append(None)
        res["name"].append(employees.loc[x, "name"])
    return pd.DataFrame(res)


print(replace_employee_id(Employees, EmployeeUNI))

# 28 Problem

data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
Students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype(
    {'student_id': 'Int64', 'student_name': 'object'})
data = [['Math'], ['Physics'], ['Programming']]
Subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name': 'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'],
        [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
Examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype(
    {'student_id': 'Int64', 'subject_name': 'object'})


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    res = {"student_id": [], "student_name": [], "subject_name": [], "attended_exams": []}
    hash: dict[int, dict[str, dict[str, int]]] = {}
    # hash[id][name][subject] = attended
    uni_subjects = set(subjects.loc[x, "subject_name"] for x in subjects.index)
    uni_names = set((students.loc[x, "student_name"], students.loc[x, "student_id"]) for x in students.index)
    used_names = set()
    for x in examinations.index:
        id: int = examinations.loc[x, "student_id"]
        name: str = students.query(f"student_id == {examinations.loc[x, 'student_id']}")["student_name"].values[0]
        used_names.add((name, id))
        subject: str = examinations.loc[x, "subject_name"]
        if id in hash:
            if name in hash[id]:
                if subject in hash[id][name]:
                    hash[id][name][subject] += 1
                else:
                    hash[id][name][subject] = 1
            else:
                hash[id][name] = {}
                hash[id][name][subject] = 1
        else:
            hash[id] = {}
            hash[id][name] = {}
            hash[id][name][subject] = 1

    truants = uni_names - used_names

    for id in hash:
        for name in hash[id]:
            extra = uni_subjects - set(hash[id][name])
            for subject in hash[id][name]:
                res["student_id"].append(id)
                res["student_name"].append(name)
                res["subject_name"].append(subject)
                res["attended_exams"].append(hash[id][name][subject])
            for null_exam in extra:
                res["student_id"].append(id)
                res["student_name"].append(name)
                res["subject_name"].append(null_exam)
                res["attended_exams"].append(0)

    for truant, truant_id in truants:
        for subject in uni_subjects:
            res["student_id"].append(truant_id)
            res["student_name"].append(truant)
            res["subject_name"].append(subject)
            res["attended_exams"].append(0)

    return pd.DataFrame(res).sort_values(by=["student_id", "subject_name"])


print(students_and_examinations(Students, Subjects, Examinations))

# 29 Problem

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101],
        [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
Employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype(
    {'id': 'Int64', 'name': 'object', 'department': 'object', 'managerId': 'Int64'})


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    hash: dict[int, int] = {}

    for x in employee.index:
        manager_id = employee.loc[x, "managerId"]
        if manager_id in hash:
            hash[manager_id] += 1
        else:
            hash[manager_id] = 1

    res = {"name": []}

    for man_id in hash:
        if hash[man_id] >= 5:
            if man_id in employee["id"].values:
                name = employee.query(f"id == {man_id}")["name"].values[0]
                res["name"].append(name)

    return pd.DataFrame(res)


print(find_managers(Employee))


# OR

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby(
        'managerId', as_index=False
    ).agg(
        reporting=('id', 'count'),
    ).query(
        '5 <= reporting'
    )['managerId']

    return employee[
        employee['id'].isin(managers)
    ][['name']]


# 30 Problem

data = [[1, 'John', 100000, 6, '4/1/2006'], [2, 'Amy', 12000, 5, '5/1/2010'], [3, 'Mark', 65000, 12, '12/25/2008'],
        [4, 'Pam', 25000, 25, '1/1/2005'], [5, 'Alex', 5000, 10, '2/3/2007']]
SalesPerson = pd.DataFrame(data, columns=['sales_id', 'name', 'salary', 'commission_rate', 'hire_date']).astype(
    {'sales_id': 'Int64', 'name': 'object', 'salary': 'Int64', 'commission_rate': 'Int64',
     'hire_date': 'datetime64[ns]'})
data = [[1, 'RED', 'Boston'], [2, 'ORANGE', 'New York'], [3, 'YELLOW', 'Boston'], [4, 'GREEN', 'Austin']]
Company = pd.DataFrame(data, columns=['com_id', 'name', 'city']).astype(
    {'com_id': 'Int64', 'name': 'object', 'city': 'object'})
data = [[1, '1/1/2014', 3, 4, 10000], [2, '2/1/2014', 4, 5, 5000], [3, '3/1/2014', 1, 1, 50000],
        [4, '4/1/2014', 1, 4, 25000]]
Orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'com_id', 'sales_id', 'amount']).astype(
    {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'com_id': 'Int64', 'sales_id': 'Int64', 'amount': 'Int64'})


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    res = {"name": []}
    hash: dict[str, bool] = {}
    for x in sales_person.index:
        name = sales_person.loc[x, "name"]
        sales_id = sales_person.loc[x, "sales_id"]
        if sales_id in orders["sales_id"].values:
            ind: int = 0
            for each_id in orders["sales_id"].values:
                if each_id == sales_id:
                    com_id = orders.loc[ind, "com_id"]
                    com_name = company.query(f"com_id == {com_id}")["name"].values[0]
                    if name not in hash:
                        hash[name] = False if com_name == "RED" else True
                    else:
                        if com_name == "RED": hash[name] = False
                ind += 1
        else:
            hash[name] = True

    for name in hash:
        res["name"].append(name) if hash[name] else None
    return pd.DataFrame(res)


print(sales_person(SalesPerson, Company, Orders))


# OR

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_ids = company.loc[company['name'] == 'RED', 'com_id']
    red_people = orders.loc[orders['com_id'].isin(red_ids), 'sales_id']
    return sales_person.loc[~sales_person['sales_id'].isin(red_people), ['name']]

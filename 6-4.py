import pandas as pd

df = pd.read_csv('Virat_Kohli.csv')

print(df)

"""
Output
Runs   BF  4s  6s  ...  Inns     Opposition         Ground  Start Date
0      12   22   1   0  ...     1    v Sri Lanka       Dambulla   18-Aug-08
1      37   67   6   0  ...     2    v Sri Lanka       Dambulla   20-Aug-08
2      25   38   4   0  ...     1    v Sri Lanka  Colombo (RPS)   24-Aug-08
3      54   66   7   0  ...     1    v Sri Lanka  Colombo (RPS)   27-Aug-08
4      31   46   3   1  ...     2    v Sri Lanka  Colombo (RPS)   29-Aug-08
..    ...  ...  ..  ..  ...   ...            ...            ...         ...
127    45   51   2   1  ...     2  v New Zealand         Ranchi   26-Oct-16
128    65   76   2   1  ...     1  v New Zealand  Visakhapatnam   29-Oct-16
129   122  105   8   5  ...     2      v England           Pune   15-Jan-17
130     8    5   2   0  ...     1      v England        Cuttack   19-Jan-17
131    55   63   8   0  ...     2      v England        Kolkata   22-Jan-17
"""
print(df.head())

"""
Output
Runs  BF  4s  6s  ...  Inns   Opposition         Ground  Start Date
0    12  22   1   0  ...     1  v Sri Lanka       Dambulla   18-Aug-08
1    37  67   6   0  ...     2  v Sri Lanka       Dambulla   20-Aug-08
2    25  38   4   0  ...     1  v Sri Lanka  Colombo (RPS)   24-Aug-08
3    54  66   7   0  ...     1  v Sri Lanka  Colombo (RPS)   27-Aug-08
4    31  46   3   1  ...     2  v Sri Lanka  Colombo (RPS)   29-Aug-08
"""
print(df.tail(5))

"""
Output
Runs   BF  4s  6s  ...  Inns     Opposition         Ground  Start Date
127    45   51   2   1  ...     2  v New Zealand         Ranchi   26-Oct-16
128    65   76   2   1  ...     1  v New Zealand  Visakhapatnam   29-Oct-16
129   122  105   8   5  ...     2      v England           Pune   15-Jan-17
130     8    5   2   0  ...     1      v England        Cuttack   19-Jan-17
131    55   63   8   0  ...     2      v England        Kolkata   22-Jan-17

[5 rows x 11 columns]
"""
print(df.info())

"""
Output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 132 entries, 0 to 131
Data columns (total 11 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Runs        132 non-null    int64  
 1   BF          132 non-null    int64  
 2   4s          132 non-null    int64  
 3   6s          132 non-null    int64  
 4   SR          132 non-null    float64
 5   Pos         132 non-null    float64
 6   Dismissal   132 non-null    object 
 7   Inns        132 non-null    int64  
 8   Opposition  132 non-null    object 
 9   Ground      132 non-null    object 
 10  Start Date  132 non-null    object 
dtypes: float64(2), int64(5), object(4)
memory usage: 11.5+ KB
None
"""
print(df.shape)

"""
Output
(132, 11)
"""
print(df.describe())

"""
Output
Runs          BF  ...         Pos        Inns
count  132.000000  132.000000  ...  132.000000  132.000000
mean    46.848485   50.871212  ...    3.303030    1.575758
std     41.994635   38.729716  ...    0.873174    0.496110
min      0.000000    0.000000  ...    1.000000    1.000000
25%     10.000000   17.750000  ...    3.000000    1.000000
50%     32.500000   42.500000  ...    3.000000    2.000000
75%     80.250000   82.250000  ...    4.000000    2.000000
max    154.000000  140.000000  ...    7.000000    2.000000

[8 rows x 7 columns]
"""

print(df['BF'].describe())

"""
count    132.000000
mean      50.871212
std       38.729716
min        0.000000
25%       17.750000
50%       42.500000
75%       82.250000
max      140.000000
Name: BF, dtype: float64
"""
print(df["Runs"].value_counts().head(10))

"""
Output
0     10
2      6
1      5
12     4
37     4
31     4
9      4
7      3
22     3
23     3
"""
runs_col = df["Runs"]

print(runs_col)
print(type(runs_col))

"""
Output
0       12
1       37
2       25
3       54
4       31
      ... 
127     45
128     65
129    122
130      8
131     55
Name: Runs, Length: 132, dtype: int64
<class 'pandas.core.series.Series'>
"""
runs_df = df[['Runs', 'Pos']]
print(runs_df.head(5))

print(type(runs_df))

"""
   Runs  Pos
0    12  2.0
1    37  2.0
2    25  1.0
3    54  1.0
4    31  1.0
<class 'pandas.core.frame.DataFrame'>"""
kohli_subset = df.iloc[2]

print(kohli_subset)

"""
Runs                     25
BF                       38
4s                        4
6s                        0
SR                    65.78
Pos                     1.0
Dismissal           run out
Inns                      1
Opposition      v Sri Lanka
Ground        Colombo (RPS)
Start Date        24-Aug-08
Name: 2, dtype: object
"""

# Extract first 3 arrows
kohli_subset = df.iloc[:3]

print(kohli_subset)

"""
Runs  BF  4s  6s  ...  Inns   Opposition         Ground  Start Date
0    12  22   1   0  ...     1  v Sri Lanka       Dambulla   18-Aug-08
1    37  67   6   0  ...     2  v Sri Lanka       Dambulla   20-Aug-08
2    25  38   4   0  ...     1  v Sri Lanka  Colombo (RPS)   24-Aug-08

[3 rows x 11 columns]
"""
vs_aussies = df[df["Opposition"] == "v Australlia"]
print(vs_aussies.head())

"""
Runs   BF  4s  6s  ...  Inns   Opposition         Ground  Start Date
6     30   41   3   0  ...     2  v Australia       Vadodara   25-Oct-09
7     10   16   1   0  ...     2  v Australia         Mohali    2-Nov-09
21   118  121  11   1  ...     2  v Australia  Visakhapatnam   20-Oct-10
37    24   33   1   0  ...     2  v Australia      Ahmedabad   24-Mar-11
58    31   34   3   0  ...     2  v Australia      Melbourne    5-Feb-12

[5 rows x 11 columns]
"""
vs_aussies = df[
	(df["Opposition"] == "v Australia") & (df["Runs"] >= 100)
]

print(vs_aussies)

"""
Runs   BF  4s  6s  ...  Inns   Opposition         Ground  Start Date
21    118  121  11   1  ...     2  v Australia  Visakhapatnam   20-Oct-10
83    100   52   8   7  ...     2  v Australia         Jaipur   16-Oct-13
85    115   66  18   1  ...     2  v Australia         Nagpur   30-Oct-13
121   117  117   7   2  ...     1  v Australia      Melbourne   17-Jan-16
122   106   92  11   1  ...     2  v Australia       Canberra   20-Jan-16

[5 rows x 11 columns]
"""
def find_centuries(x):
	if x>=100:
		return "OG"
	else:
		return "NOOB"

df["Centuries"] = df["Runs"].apply(find_centuries)

print(df.head(5))

"""
Output
Runs  BF  4s  6s  ...   Opposition         Ground Start Date  Centuries
0    12  22   1   0  ...  v Sri Lanka       Dambulla  18-Aug-08       NOOB
1    37  67   6   0  ...  v Sri Lanka       Dambulla  20-Aug-08       NOOB
2    25  38   4   0  ...  v Sri Lanka  Colombo (RPS)  24-Aug-08       NOOB
3    54  66   7   0  ...  v Sri Lanka  Colombo (RPS)  27-Aug-08       NOOB
4    31  46   3   1  ...  v Sri Lanka  Colombo (RPS)  29-Aug-08       NOOB

[5 rows x 12 columns]
"""
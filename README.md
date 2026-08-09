# Student Performance Analysis

## Results

----Number of missing value----
gender                         0
race/ethnicity                 0
parental level of education    0
lunch                          0
test preparation course        0
math score                     0
reading score                  0
writing score                  0
dtype: int64

----Outliers----
math score
Lower Limit: 27.0
Upper Limit: 107.0
Number of Outliers: 8

reading score
Lower Limit: 29.0
Upper Limit: 109.0
Number of Outliers: 6

writing score
Lower Limit: 25.875
Upper Limit: 110.875
Number of Outliers: 5

-Average score of each subject-
math score       66.089
reading score    69.169
writing score    68.054
dtype: float64

-Average scire of each student-
0    72.666667
1    82.333333
2    92.666667
3    49.333333
4    76.333333
Name: average score, dtype: float64

----overall Average Score----
67.77066666666666

---- min score of each subject ----
math score        0
reading score    17
writing score    10
dtype: int64

---- max score of each subject ----
math score       100
reading score    100
writing score    100
dtype: int64

---- Total Marks of each student ----
0    218
1    247
2    278
3    148
4    229
Name: total marks, dtype: int64

---- overall min total score ----
27

---- overall max total score ----
300

----lowest_score_student----
gender                                   female
race/ethnicity                          group C
parental level of education    some high school
lunch                              free/reduced
test preparation course                    none
math score                                    0
reading score                                17
writing score                                10
average score                               9.0
total marks                                  27
Name: 59, dtype: object

----highest_score_student----
gender                                    female
race/ethnicity                           group E
parental level of education    bachelor's degree
lunch                                   standard
test preparation course                     none
math score                                   100
reading score                                100
writing score                                100
average score                              100.0
total marks                                  300
Name: 458, dtype: object

 ----Gender analysis----
        math score  reading score  writing score
gender                                          
female   63.633205      72.608108      72.467181
male     68.728216      65.473029      63.311203

----Test preparation analysis ----
                         math score  reading score  writing score
test preparation course                                          
completed                 69.695531      73.893855      74.418994
none                      64.077882      66.534268      64.504673

---- Parental Education Analysis  ----
                             math score  reading score  writing score
parental level of education                                          
associate's degree            67.882883      70.927928      69.896396
bachelor's degree             69.389831      73.000000      73.381356
high school                   62.137755      64.704082      62.448980
master's degree               69.745763      75.372881      75.677966
some college                  67.128319      69.460177      68.840708
some high school              63.497207      66.938547      64.888268

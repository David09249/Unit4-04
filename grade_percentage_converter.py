# Created by: David Wang
# Created on: 6-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit4-04
# This program displays the converted percentage grade from a letter/number grade

percentage_grade = {}
percentage_grade['NE'] = '0%'
percentage_grade['R-'] = '1-29%'
percentage_grade['R'] = '30-39%'
percentage_grade['R+'] = '40-49%'
percentage_grade['1-'] = '50-52%'
percentage_grade['1'] = '53-56%'
percentage_grade['1+'] = '57-59%'
percentage_grade['2-'] = '60-62%'
percentage_grade['2'] = '63-66%'
percentage_grade['2+'] = '67-69%'
percentage_grade['3-'] = '70-72%'
percentage_grade['3'] = '73-76%'
percentage_grade['3+'] = '77-79%'
percentage_grade['4-'] = '80-87%'
percentage_grade['4'] = '88-94%'
percentage_grade['4+'] = '95-99%'
percentage_grade['4++'] = '100%'

def convert_grade(input):
    # converts letter/number grade into percentage grade
    if input == 'NE' or input == 'R-' or input == 'R' or input == 'R+' or input == '1-' or input == '1' or input == '1+' or input == '2-' or input == '2' or input == '2+' or input == '3-' or input == '3' or input == '3+' or input == '4-' or input == '4' or input == '4+' or input == '4++':
        return percentage_grade[input]
    else:
        return -1

while True:
    grade = raw_input('Enter a letter/number grade to convert it to a percentage: ')
    print(convert_grade(grade))

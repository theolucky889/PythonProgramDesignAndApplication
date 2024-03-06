# Question 1
a = 3
b = 2
print(f'{a} + {b} =  {a + b}')
print(f'{a} - {b} =  {a - b}')
print(f'{a} * {b} =  {a * b}')
print(f'{a} / {b} =  {a / b}')
print(f'{a} // {b} =  {a // b}')
print(f'{a} % {b} =  {a % b}')
print(f'{a} ** {b} =  {a ** b}')

# Question 2
body_w = float(input('Input your weight(kg) = '))
body_h = float(input('Input your height(cm) = '))
body_h_m = body_h / 100
body_hsquare = body_h_m ** 2
bmi_formula = body_w / body_hsquare
print("This is your BMI = ", bmi_formula)

# Question 3
# ax^2+bx+c=0
$ax^2 + bx + c = 0$
$a$, $b$, $c$
$a \neq 0$
$a = 0$
$$ ax^2 + bx + c = 0 $$

\documentclass{article}
\begin{document}

\newcommand{\a}{\text{float}(\text{input}('input a = '))}
\newcommand{\b}{\text{float}(\text{input}('input b = '))}
\newcommand{\c}{\text{float}(\text{input}('input c = '))}
\newcommand{\discriminant}{(\b ** 2 - 4 * \a * \c) ** 0.5}
\newcommand{\xone}{(-\b + \discriminant) / (2 * \a)}
\newcommand{\xtwo}{(-\b - \discriminant) / (2 * \a)}
\text{print}(\xone, \xtwo)

\end{document}


# code
a = float(input('input a = '))
b = float(input('input b = '))
c = float(input('input c = '))
discriminant = (b ** 2 - 4 * a * c) ** 0.5
x1 = (-b + discriminant) / (2 * a)
x2 = (-b - discriminant) / (2 * a)
print(x1, x2)

# BMI

$\text[BMI] = \frac{\text{weight(kg)}}{\text{height}^2 (\text{m}^2)}$
"""
- \text{weight} is the weight (in kilograms)
- \text{height} is the height (in meters squared)
"""
\documentclass{article}
\begin{document}

\newcommand{\weight}{70}  % in kg
\newcommand{\height}{170} % in cm
\newcommand{\htm}{\height / 100}  % in 
\newcommand{\bmi}{\weight / (\htm*\htm)}

BMI: $\bmi$

\end{document}

# Code
weight = 70  # in kg
height = 170 # in cm
htm = height / 100  # in 
bmi = weight / (htm*htm)
print("BMI:", bmi)

def HealthScreen(weight, height):
    BMI = weight/(height*height)
    if BMI >= 27.5:
        return 'Your BMI is %.1f (High Risk).' % BMI
    elif BMI >= 23 and BMI <= 27.4:
        return 'Your BMI is %.1f (Moderate Risk).' % BMI
    elif BMI >= 18.5 and BMI <= 22.9:
        return 'Your BMI is %.1f (Low Risk).' % BMI
    else:
        return 'Your BMI is %.1f (Risk of nutritional deficiency diseases).' % BMI

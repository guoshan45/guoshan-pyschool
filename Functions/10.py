def introduce(name, age=0):
    msg = "My name is %s. " % name
    if age == 0:
        msg += "My age is secret."
    else:
        msg += "I am %d years old." % age
    return msg

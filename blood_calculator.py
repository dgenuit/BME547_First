def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a Choice")
        print("1 -- HDL Analysis")
        print("2 -- LDL Analysis")
        print("9 -- Quit")
        choice = int(input("Make a choice:"))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            print("You Have Chosen HDL Analysis")
            HDL_Driver()
        elif choice == 2:
            print("You Have Chosen LDL Analysis")
            LDL_Driver()
    print(choice)
    return choice

def HDL_Driver():
    HDL_value = hdl_input()
    analysis_result = hdl_analysis(HDL_value)
    hdl_output(HDL_value, analysis_result)
    return

def hdl_input():
    hdl_value = int(input("Enter HDL Value"))
    return hdl_value

def hdl_analysis(hdl_value):
    if hdl_value >= 60:
        status = "Normal"
        return status
    elif 40 <= hdl_value < 60:
        status = "Borderline Low"
        return status
    else:
        status = "Low"
        return status
        
def hdl_output(HDL_value, HDL_answer):
    print("Your HDL value is: {}".format(HDL_value))
    print("Your HDL is {}".format(HDL_answer))

def LDL_Driver():
    LDL_value = ldl_input()
    analysis_result = ldl_analysis(LDL_value)
    ldl_output(LDL_value,analysis_result)
    return


def ldl_input():
    ldl_value = int(input("Enter LDL Value"))
    return ldl_value

def ldl_analysis(ldl_value):
    if ldl_value <= 130:
        return "Normal"
    elif 130 < ldl_value <= 159: 
        return "Borderline High"
    elif 160 <= ldl_value <= 189:
        return "High"
    else:
        return "Very High"
def ldl_output(LDL_value, LDL_answer):
    print("Your HDL value is {}, which is considered {}".format(LDL_value, LDL_answer))

interface()

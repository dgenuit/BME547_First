def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a Choice")
        print("1 -- HDL Analysis")
        print("9 -- Quit")
        choice = int(input("Make a choice:"))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
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



interface()

from stuRslt import StuRslt


class ExcellenceTechnology:

    def students():
        StuRslt.passedStudent()

exit = True
while exit:
    print("if you want to start the editing window press 1")
    val = int(input())
    if val == 1:
        ExcellenceTechnology.students()
    else:
        exit = False
        print("no output specified.")
        

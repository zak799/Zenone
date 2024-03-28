import re
import os

class Zenone:
    @staticmethod
    def state(state):
        print(state)

    @staticmethod
    def recur(text, iterations):
        print((text + "\n") * iterations)

    textVar = {}
    @staticmethod
    def text_variable(define, value):
        Zenone.textVar[define] = value



def ZNE_code_run(file_path):
    try:
        with open(file_path, "r") as fileCONTENTS:
            code = fileCONTENTS.read()
            lines = code.split("\n")
            interpreter = Zenone()
            state_algorithm = r"zne{func->zne\.state\((['\"])(.*?)\1\)}"
            recur_algorithm = r"zne{func->zne\.recur\((['\"])(.*?)\1,\s*(\d+)\)}"
            var_algorithm = r"zne{stateVar->define#([a-zA-Z0-9_]+)\((['\"])(.*?)\2\)}"

            state_message = None
            for line in lines:
                state_regex_scan = re.search(state_algorithm, line)
                recur_regex_scan = re.search(recur_algorithm, line)
                variable_regex_scan = re.search(var_algorithm, line)

                if state_regex_scan:
                    state_message = state_regex_scan.group(2)
                    interpreter.state(state_message)

                elif recur_regex_scan:
                    text = recur_regex_scan.group(2)
                    iterations = int(recur_regex_scan.group(3))
                    interpreter.recur(text, iterations)

                elif variable_regex_scan:
                    variable_content = variable_regex_scan.group(2)
                    interpreter.text_variable(define=variable_regex_scan.group(1), value=variable_content)


                elif line.strip() and not line.strip().startswith(":hide:"):
                    current_file_path = os.path.abspath(__file__)
                    print(f"""\n{current_file_path}>
╰┈➤ error in '{file_path}'
        ╰┈➤ {line} \n
==================== UN-ERRORED CODE ====================""")
                else:
                    if re.search(state_algorithm, line) == False or re.search(recur_algorithm, line) == False or re.search(var_algorithm, line) == False:
                        break
    except FileNotFoundError:
        print(f"File '{file_path}' Not Found")

file_path = "test2.zne"
ZNE_code_run(file_path)

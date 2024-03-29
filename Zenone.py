import re
import os


class Zenone:
    @staticmethod
    def state(state):
        print(state)

    @staticmethod
    def recur(text, iterations):
        print((text + "\n") * iterations)

    @staticmethod
    def var_recur(var_recur_callback, iterations):
        print((var_recur_callback + "\n") * iterations)

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
            return_var_algorithm = r"zne{func->zne\.state\(([a-zA-Z, 0-9_]+)\)}"
            recur_var_algorithm = r"zne{func->zne\.recur\(([a-zA-Z0-9_]+)\,\s*(\d+)\)}"

            state_message = None
            for line in lines:
                state_regex_scan = re.search(state_algorithm, line)
                recur_regex_scan = re.search(recur_algorithm, line)
                variable_regex_scan = re.search(var_algorithm, line)
                var_return_scan = re.search(return_var_algorithm, line)
                recur_var_return_scan = re.search(recur_var_algorithm, line)

                if state_regex_scan:
                    state_message = state_regex_scan.group(2)
                    interpreter.state(state_message)

                elif recur_regex_scan:
                    text = recur_regex_scan.group(2)
                    iterations = int(recur_regex_scan.group(3))
                    interpreter.recur(text, iterations)

                elif variable_regex_scan:
                    variable_content = variable_regex_scan.group(3)
                    interpreter.text_variable(define=variable_regex_scan.group(1), value=variable_content)

                elif var_return_scan:
                    variable_callback = var_return_scan.group(1)
                    interpreter.state(variable_callback)

                elif recur_var_return_scan:
                    variable = recur_var_return_scan.group(1)
                    iterations = int(recur_var_return_scan.group(2))
                    if variable in interpreter.textVar:
                        text = interpreter.textVar[variable]
                        interpreter.recur(text, iterations)
                    else:
                        print(f"""{current_file_path}>
                                        ╰┈➤ error in '{file_path}
                                                    ╰┈➤ UNDEFINED VARIABLE '{variable}'""")

                elif line.strip() and not line.strip().startswith(":hide:"):
                    print(f"""\n{current_file_path}>
╰┈➤ error in '{file_path}'
        ╰┈➤ {line} \n
==================== UN-ERRORED CODE ====================""")
                else:
                    continue

    except FileNotFoundError:
        print(f"File '{file_path}' Not Found")

if __name__ == "__main__":
    file_path = "test2.zne"
    current_file_path = os.path.abspath(__file__)
    ZNE_code_run(file_path)

from Handling.errorHandler import *
from Runner.ZenoneClasses import Zenone
import re
import os


def error():
    print(f"""
================================== ERROR ==================================\n
{file_path}>
     ╰┈➤ error in '{file_path}'\n
            ╰┈➤ {line}\n
================================== ERROR ================================== """)


def Runner(file_path):
    global line
    try:
        with open(file_path, "r") as fileCONTENTS:
            code = fileCONTENTS.read()
            lines = code.split("\n")
            interpreter = Zenone()
            state_algorithm = r"zne.state\((['\"])(.*?)\1\);"
            recur_algorithm = r"zne.recur\((['\"])(.*?)\1,\s*(\d+)\);"
            var_algorithm = r"zne.define#([a-zA-Z0-9_]+)\((['\"])(.*?)\2\);"
            return_var_algorithm = r"zne.state\(([a-zA-Z, 0-9_]+)\);"
            recur_var_algorithm = r"zne.recur\(([a-zA-Z0-9_]+)\,\s*(\d+)\);"
            math_algorithm = r"zne.([a-z]+)\((.*?)\);"

            state_message = None
            error_encountered = False

            for line in lines:
                state_regex_scan = re.search(state_algorithm, line)
                recur_regex_scan = re.search(recur_algorithm, line)
                variable_regex_scan = re.search(var_algorithm, line)
                var_return_scan = re.search(return_var_algorithm, line)
                recur_var_return_scan = re.search(recur_var_algorithm, line)
                math_regex_scan = re.search(math_algorithm, line)


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
                    if variable_callback in interpreter.textVar:
                        variable_value = interpreter.textVar[variable_callback]
                        interpreter.state(variable_value)
                    else:
                        error()
                        break

                elif recur_var_return_scan:
                    variable = recur_var_return_scan.group(1)
                    iterations = int(recur_var_return_scan.group(2))
                    if variable in interpreter.textVar:
                        text = interpreter.textVar[variable]
                        interpreter.recur(text, iterations)
                    else:
                        error()
                        break

                elif math_regex_scan:
                    try:
                        nums = [int(args) for args in math_regex_scan.group(2).split(",")]
                        interpreter.state(getattr(interpreter, math_regex_scan.group(1))(*nums))
                    except:
                        error()
                        break


                elif line.strip() and not line.strip().startswith(":hide:"):
                    print(f"""\n{file_path}>
╰┈➤ error in '{file_path}'
        ╰┈➤ {line} \n
==================== UN-ERRORED CODE ====================""")
                else:
                    continue

    except FileNotFoundError:
        raise FileError(f"File '{file_path}' Not Found")

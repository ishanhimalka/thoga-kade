import sys
import item
import user
import order


def project_init():
    user.init()
    item.init()
    order.init()
    print("Success project initial")


if __name__ == "__main__":
    arguments = sys.argv

    section = arguments[1]
    command = arguments[2]
    params = arguments[3:]

    if section == "user":
        user.set_command_and_params(command, params)
    elif section == "item":
        item.set_command_and_params(command, params)
    elif section == "order":
        order.set_command_and_params(command, params)
    elif section == "project":
        if command == "init":
            project_init()

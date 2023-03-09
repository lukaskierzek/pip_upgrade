import os


class Pip:
    @staticmethod
    def create_requirements() -> None:
        os.system('pip freeze > requirements.txt')

    @staticmethod
    def update_pip() -> None:
        os.system('pip install -r requirements.txt')


class Requirements:
    @staticmethod
    def replace_eq_to_ge() -> str:
        with open(r'requirements.txt', "r") as file:
            data = file.read()
            data = data.replace("==", ">=")
        return data

    @staticmethod
    def write_replace_eq_to_ge_into_requirement(data: str) -> None:
        with open(r'requirements.txt', 'w') as file:
            file.write(data)


def main():
    try:
        pip = Pip()
        requirements = Requirements()

        print("Create requirements.txt file...")
        pip.create_requirements()

        print("Read libs and replace '==' to '>='...")
        requirements.write_replace_eq_to_ge_into_requirement(requirements.replace_eq_to_ge())

        print("Update libs...")
        pip.update_pip()

        print("Done!")
    except FileNotFoundError as e:
        print(f"requirements.txt not found :( \n{e}")


if __name__ == '__main__':
    main()

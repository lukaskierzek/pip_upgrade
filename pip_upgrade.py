import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


class PipCommand(ABC):
    @abstractmethod
    def command(self) -> Any:
        pass


class File(ABC):
    @abstractmethod
    def replacing_data(self) -> Any:
        pass


class Message(ABC):
    @abstractmethod
    def message(self) -> None:
        pass


class PipCreateRequirements(PipCommand):
    def command(self) -> None:
        os.system('pip freeze > requirements.txt')


class PipInstallRequirements(PipCommand):
    def command(self) -> None:
        os.system('pip install -r requirements.txt')


class RequirementsEqToGe(File):
    def replacing_data(self) -> str:
        with open(r'requirements.txt', "r") as file:
            data = file.read().replace("==", ">=")
        return data


@dataclass
class MessagePrint(Message):
    communication: str = field()

    def message(self) -> None:
        print(self.communication)


@dataclass
class RequirementsNewData(File):
    data: str = field()

    def replacing_data(self) -> None:
        with open(r'requirements.txt', 'w') as file:
            file.write(self.data)


def main() -> None:
    try:
        MessagePrint("Create requirements.txt file...").message()
        PipCreateRequirements().command()

        MessagePrint("Read libs and replace '==' to '>='...").message()
        requirement_replace_qeq_to_ge = RequirementsEqToGe().replacing_data()
        RequirementsNewData(requirement_replace_qeq_to_ge).replacing_data()

        MessagePrint("Update libs...").message()
        PipInstallRequirements().command()

        MessagePrint("Done!").message()
    except FileNotFoundError as e:
        MessagePrint(f"requirements.txt not found :( \n{e}").message()


if __name__ == '__main__':
    main()

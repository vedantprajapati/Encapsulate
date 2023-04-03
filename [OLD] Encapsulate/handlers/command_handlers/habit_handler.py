import flet as ft
from oauth.google_oauth import google_get_user, has_token
from datetime import datetime
import argparse


class Habit:
    def __init__(
        self,
        name,
        frequency=None,
        start_date=datetime.today,
        end_date=None,
        description=None,
    ):
        self.name = name
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date
        self.completed_count = 0
        self.description = description

    def get_habit(self):
        return {
            "name": self.name,
            "frequency": self.frequency,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "completion_count": self.completed_count,
        }


class HabitsManager:
    def __init__(self, habits=[]):
        self.habits = habits

    def add_habit(self, habit):
        self.habits.append(habit)

    def remove_habit(self, habit):
        self.habits.remove(habit)

    def list_habits(self):
        return self.habits

    def get_habit(self, habit_name):
        for habit in self.habits:
            if habit["name"] == habit_name:
                return habit

    def get_habits(self):
        return self.habits

    def get_habit_names(self):
        habit_names = []
        for habit in self.habits:
            habit_names.append(habit["name"])
        return habit_names

    def edit_habit(self, habit_name, new_habit):
        for habit in self.habits:
            if habit.name == habit_name:
                habit = new_habit


def validate(date_text):
    try:
        datetime.date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def route_habit(**kwargs):
    parser = argparse.ArgumentParser()
    page = kwargs.get("page")
    command = kwargs.get("command")

    if not has_token(page) or not google_get_user(page):
        return "Please login to use this command"

    if not page.client_storage.get("habits"):
        habits = []
        page.client_storage.set("habits", habits)
    elif page.client_storage.get("habits"):
        habits = page.client_storage.get("habits")

    manager = HabitsManager(habits)
    command_list = command.split(" ")

    if len(command_list) >= 2:
        if command_list[1] in ["add", "a", "A"]:
            parser.add_argument("habit_name", type=str)
            parser.add_argument("-f", "--frequency", type=str)
            parser.add_argument("-s", "--start_date", type=validate)
            parser.add_argument("-e", "--end_date", type=validate)
            parser.add_argument("-d", "--description", type=str)

            args = parser.parse_args(command_list[2:])

            new_habit = Habit(
                args.habit_name,
                args.frequency,
                args.start_date,
                args.end_date,
                args.description,
            ).get_habit()

            manager.add_habit(new_habit)
            page.client_storage.set("habits", manager.habits)
            return "Added habit: " + args.habit_name
        elif command_list[1] in ["remove", "r", "R"]:
            parser.add_argument("-n, --name", type=str)
            parser.add_argument("-a", "--all", action="store_true")
            args = parser.parse_args(command_list[2:])

            if args.all:
                page.client_storage.set("habits", [])
                return "Removing all habits: "
            elif args.habit_name in manager.get_habit_names():
                habit = manager.get_habit(args.habit_name)
                manager.remove_habit(habit)
                page.client_storage.set("habits", habits)
            else:
                return (
                    "Habit not found, please use the -n flag to specify the habit name"
                )
            return "Removing habit"
        elif command_list[1] in ["list", "l", "L"]:
            parser.add_argument("-n", "--name", type=str)
            args = parser.parse_args(command_list[2:])
            name = args.name
            if name:
                return (
                    "The following habit was found: "
                    + str(manager.get_habit(args.name))
                    + "\n"
                )
            return (
                "This is a list of your habits: "
                + str(manager.get_habit_names())
                + "\n"
            )
        elif command_list[1] in ["track", "t", "T"]:
            parser.add_argument("name", type=str)
            args = parser.parse_args(command_list[2:])
            name = args.name
            habit = manager.get_habit(args.name)
            if habit:
                habit["completion_count"] += 1
                manager.edit_habit(args.name, habit)
                page.client_storage.set("habits", habits)
                return "Tracked habit: " + args.name
            else:
                return (
                    "Habit not found, please use the -n flag to specify the habit name"
                )
        else:
            return "Habit command not recognized, the command should be in the format: 'habit add/remove/list <habit name> (optional flags) <frequency> <start date> <end date> <time>'"
    else:
        return "Habit command not recognized, the command should be in the format: 'habit add/remove/list <habit name> (optional flags) <frequency> <start date> <end date> <time>'"

# migrate-todoist-to-trello
A simple project to take a ToDoist Project (Exported as a CSV Template) and import it as a new board in Trello

# Running

Make sure you have `pipenv` installed. Then, run

```
pipenv run src/main.py TEMPLATE_CSV_FILE
```

You can add an option of `--log-level LEVEL` to set the logging level; allowed values are "DEBUG", "INFO", "WARNING", "ERROR", and "CRITICAL"

# Methodology

When you export a project from ToDoist, you get a CSV File describing the project. The object of this script is to create a new Board in Trello. By default the board name is equal to the CSV file name minus the extension (which should be equal to the original ToDoist project name). If the board already exists, the behavior is undefined.

Each entry in the CSV is either a `section` or a `task`.

## Sections

All `section`s in ToDoist become new Lists in your new Trello board.

## Tasks and Subtasks


All `task` entries in the ToDoist export have an `INDENT` property associated with them. This corresponds to whether they are subtasks in ToDoist or not.

### Tasks

If the `INDENT` value is 1, that indicates a `task` in ToDoist. A card will be created in Trello belonging to the List that corresponds to the section that the task belonged to in ToDoist. If the task did not belong to a section in ToDoist, the behavior is undefined.

The title of the Trello card will be the `CONTENT` (name) of the ToDoist task. The description of the Trello card will be the description of the ToDoist task.

#### Labels

All labels on a task will become labels in Trello, and added to the card that is created. If the label does not exist it will be created

### Subtasks

If the `INDENT` value is 2, that indicates a `subtask` of a `task` in ToDoist. These will be added as checklist items to the Trello Card that corresponds to their ToDoist Task.

If the subtask has labels, the behavior is undefined.

### Others

If the `INDENT` is greater than 2, then that indicates a `subtask` of a `subtask`. In this instance, the behavior is undefined.
# Luigi demo

This assumes you have luigi installed

```
pip install luigi
```

# Tasks

First let's run a simple task

```
PYTHONPATH=. luigi --module add AddTask --x 123 --y 456 --local-scheduler
```

#### Challenge


Modify `add.py` to take a 3rd parameter. You should be able to run something like.

```
PYTHONPATH=. luigi --module add AddTask --x 100 --y 100 --z 100 --local-scheduler
```

# Dependencies

```
PYTHONPATH=. luigi --module letter_counts CountLetters --local-scheduler
```

Run the same command again. Luigi recognizes that there's no need to recreate the target.

#### Challenge

Modify `letter_counts.py` so that CountLetters takes in two files, aggregates the words in each, and then counts letters as before.


# Central Scheduler

Make a log directory for the scheduler

```
mkdir log
```

Start up the central scheduler daemon

```
luigid --background --pidfile pid.txt --logdir ./log
```

View the task visualizer at

```
http://localhost:8082/static/visualiser/index.html
```

Run your tasks (remembering to reset state by removing your output targets), and see the scheduler update.

Once you're done, shut down the scheduler with:

```
cat pid.txt | xargs kill -9
```

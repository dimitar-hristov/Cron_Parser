# Cron Expression Parser
CLI tool which parses a cron string and expands each field to show the times at which it will run.

Example:
```bash
python cron_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```

will result in:

|              |                            |
|--------------|----------------------------|
| minutes      | 0 15 30 45                 |
| hour         | 0                          |
| day of month | 1 15                       |
| month        | 1 2 3 4 5 6 7 8 9 10 11 12 |
| day of week  | 1 2 3 4 5                  |
| command      | /usr/bin/find              |

# Depevelopment
## Install dependencies
```bash
make install
```
## Run tests
```bash
make test
```

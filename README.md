# Stock Scrapper
## THIS PROJECT IS ONLY TO MAKE EXPERIENCE WITH CONVENTIONAL COMMITS, THEIR LIMITATIONS, WHAT IS GOOD GRANULARITY, LEARN HOW TO BETTER NAME BRANCHES, POC DAGGER-IO AND FIRST TRY TO SCRAP SOMETHING


A Python project to scrape stock data from [kurzy.cz](https://www.kurzy.cz/akcie-cz/burza/), save it to a PostgreSQL database, and perform data analysis. The project uses Dagger.io for CI/CD automation and Taskfile for task management.

## Features

- Scrape stock data using `requests` and `BeautifulSoup`
- Save data to PostgreSQL using SQLAlchemy
- Automated tasks with Taskfile
- CI/CD pipelines for linting, testing, and security scans
- Daily data fetching with a scheduled task
- Data analysis with graphical output

## Requirements

- Python 3.12
- PostgreSQL
- Docker
- Poetry

## Installation

```bash
poetry install
```

## Usage

### Initialize the project
```task init```

### Fetch stock data
```task fetch_data```

### Run linting
```task lint```

### Run tests
```task test```

### Run security scan
```task trivy```

## License

This project is licensed under the GNU General Public License v3.0.

## Další Vylepšení - navrh

1. **Grafické znázornění dat:** Použij `matplotlib` nebo `seaborn` pro vizualizaci dat.
2. **Rozšíření scraping funkcionality:** Přidání dalších zdrojů dat.
3. **Pokročilá analýza dat:** Implementace ML modelů pro předpověď cen akcií.
4. **Notifikace:** Přidání emailových notifikací o změnách cen akcií.
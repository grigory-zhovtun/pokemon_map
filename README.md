
# Pokemon Map

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### About the Project

This website is designed to help [Pokemon GO](https://www.pokemongo.com/en-us/) players. Pokemon GO is a game about catching [Pokemon](https://en.wikipedia.org/wiki/Pok%C3%A9mon).

The core gameplay involves Pokemon appearing on the map for a limited time. Each player can catch Pokemon to add them to their personal collection.

Multiple specimens of the same Pokemon can appear on the map simultaneously - for example, 3 Bulbasaurs. Each specimen can be caught by multiple players. When a player catches a Pokemon, it disappears for them but remains available for others.

The game features an evolution mechanic. Pokemon of one species can "evolve" into another. For example, Bulbasaur evolves into Ivysaur, which then evolves into Venusaur.

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

---

## Requirements

- Python 3.12 or newer
- Django 3.1
- Other required packages are listed in `requirements.txt`

---

## How to Run

To run this website, you'll need Python 3.

Download the code from GitHub. Then install the dependencies:

```sh
pip install -r requirements.txt
```

Create a database file and apply migrations:

```sh
python manage.py migrate
```

Start the development server:

```sh
python manage.py runserver
```
### Environment Variables

Some project settings are taken from environment variables. To define them, create a `.env` file next to `manage.py` and write data in the following format: `VARIABLE=value`.

Two variables are available:
- `DEBUG` — debug mode. Set to True to see debugging information in case of an error.
- `SECRET_KEY` — the project's secret key


---

## Usage

- The main page (`/`) displays a map of Moscow with Pokemon and a list of all available Pokemon.
- The Pokemon page (`/pokemon/<pokemon_id>/`) shows detailed information about a specific Pokemon, including its evolutions.

### Main Routes:

- **Main Page:** `/` - Map of all Pokemon.
- **Pokemon Page:** `/pokemon/<pokemon_id>/` - Detailed information about a Pokemon.
- **Admin Panel:** `/admin/` - Control panel for adding and editing Pokemon.

### Database Models:

- **Pokemon** - stores information about Pokemon species (name, description, image, evolutions).
- **PokemonEntity** - represents specific Pokemon on the map with their coordinates and characteristics.

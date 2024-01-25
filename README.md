# itol-configs

To annotate trees in [iTOL](https://itol.embl.de/) requres special config files that are time-consuming to create.
This python package contains functions to create configuration files automatically from a CSV file.

## Installation

```bash
pip install git+https://github.com/jodyphelan/itol-configs.git
```

## CLI Usage

This command will automatically create a config file for each column in the specified input csv file.

```bash
itol-configs --input <input.csv> --out <prefix_for_output_files> --id <id_column> --type <annotation_type>
```

If you you already have colours in mind you can specify them with the `--colour-conf` option. This requires a toml file with the following format:

```toml
[Column_name_1]
value1 = "colour"
value2 = "colour"

[Column_name_2]
value1 = "colour"
value2 = "colour"
```

## Developers

The following annotation types are currently supported:

- [colour_strip](https://itol.embl.de/help.cgi#strip)
- [text_label](https://itol.embl.de/help.cgi#textlabels)

If you want to contribute a new annotation type this package, please clone the repository and create a new branch for your changes. Then create a pull request to merge your changes into the master branch.

### Adding a new annotation type

Each annotation type is defined as a class in [itol_configs/interfaces](https://github.com/jodyphelan/itol-configs/tree/main/itol_configs/interfaces). The class must inherit from the `ConfigWriter` class and implement the `write` method. Have a look at the existing classes for examples. Make sure to add your new class to `interfaces_types` dictionary in the `__init__.py` file in the same directory.
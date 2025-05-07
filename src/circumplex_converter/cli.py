#!/usr/bin/env python3
"""CLI entry point"""
import sys, json, yaml, logging
from pathlib import Path
import typer
from rich.console import Console
from circumplex_converter.converter import convert_yaml_to_json
from circumplex_converter.schema import validate_json

EXIT_SCHEMA=2; EXIT_IO=3
console=Console()

app=typer.Typer()

@app.command()
def convert(
    input_file: Path = typer.Argument(...),
    outfile: Path = typer.Option(None),
    dry_run: bool = typer.Option(False,"--dry-run"),
):
    try:
        data=yaml.safe_load(input_file.read_text())
        json_out=convert_yaml_to_json(data)
        validate_json(json_out)
        dump=json.dumps(json_out,indent=2)
        if dry_run or outfile is None:
            console.print_json(dump)
        else:
            outfile.write_text(dump)
            console.print(f'[green]written -> {outfile}')
    except Exception as e:
        console.print(f'[red]Error: {e}')
        sys.exit(EXIT_SCHEMA)
if __name__=='__main__':
    app()

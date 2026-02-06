#!/usr/bin/env python3
import argparse
import os
import zipfile

from validate_skill import validate_skill


def parse_args():
    parser = argparse.ArgumentParser(description="Validate and package a skill.")
    parser.add_argument("skill_path", help="Path to a skill folder")
    parser.add_argument("output_dir", nargs="?", default="dist", help="Output directory")
    return parser.parse_args()


def zip_skill(skill_path, output_dir):
    skill_name = os.path.basename(os.path.abspath(skill_path))
    os.makedirs(output_dir, exist_ok=True)
    zip_path = os.path.join(output_dir, f"{skill_name}.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for root, _, files in os.walk(skill_path):
            for file_name in files:
                full_path = os.path.join(root, file_name)
                rel_path = os.path.relpath(full_path, os.path.dirname(skill_path))
                archive.write(full_path, rel_path)

    return zip_path


def main():
    args = parse_args()
    skill_path = os.path.abspath(args.skill_path)

    errors = validate_skill(skill_path)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    zip_path = zip_skill(skill_path, args.output_dir)
    print(f"Packaged skill: {zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

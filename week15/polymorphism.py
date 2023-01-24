from __future__ import annotations

def my_split(to_split: str | list[str]) -> list[str] | None:
     """Take a string or list of strings and split along whitespace."""
     if isinstance(to_split, list):
             split_strs = []
             for entry in to_split:
                     if isinstance(entry, str):
                             split_strs += entry.split()
                     else:
                             return None
             return split_strs
     elif isinstance(to_split, str):
             return to_split.split()
     else:
             return None

def main():
        print(my_split('This is a sentence.\nThis is another.\n'))
        print(my_split(['This is a sentence.', 'This is another.']))
        print(my_split(['This is a sentence.', 'This is a number.', 3]))

if __name__ == '__main__':
        main()
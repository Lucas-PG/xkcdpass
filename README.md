# XKCD Password Generator

This repository contains a Python script (`main.py`) and a wordlist (`words.txt`) to generate XKCD-style passwords—strong, memorable passphrases inspired by [XKCD #936](https://xkcd.com/936/) and a [Privacy Guides article](https://www.privacyguides.org/en/basics/passwords-overview/) on password generation. The script creates passwords like `Lumber-Umbrella-Cactus-Abacus-Secret#3` using random words from the provided list.

> [!WARNING]
> The default words.txt uses the EFF's long wordlist (7,776 words), which is sufficient for robust password generation. For enhanced security, use a custom, private words.txt that attackers cannot access, making brute-force attacks significantly harder.

## Features

- Generates a 5-word passphrase with capitalized first letters, hyphen-separated, plus a random special character and number.
- Optional filtering: Use `-l/--letters` to specify starting letters (e.g., `xkcdpass -l l,u,c,a,s`).
- Manual: Run `xkcdpass -m` for an explanation of the XKCD method and password complexity.
- Help: Run `xkcdpass -h` for usage details.

## Repository Contents

- `main.py`: The Python script (to be renamed `xkcdpass`).
- `words.txt`: A simple wordlist, one word per line (e.g., `abacus`, `abdomen`).

## Setup Instructions

To use this script globally as `xkcdpass` on Linux or macOS, follow these steps. We’ll use symbolic links (symlinks) to keep the script tied to this repository without moving files.

### Prerequisites

- Python 3 installed (standard on most Linux/macOS systems).
- Git installed to clone the repo (or download it manually).

### Step-by-Step Setup

#### 1. Clone the Repository

Clone this repo to a directory of your choice (e.g., `~/projects/xkcdpass`):

```bash
git clone https://github.com/Lucas-PG/xkcdpass.git ~/projects/xkcdpass
cd ~/projects/xkcdpass
```

#### 2. Rename the Script

Rename `main.py` to `xkcdpass` for a cleaner command name:

```bash
mv main.py xkcdpass
```

#### 3. Make the Script Executable

Add execute permissions to `xkcdpass`:

```bash
chmod +x xkcdpass
```

#### 4. Set Up Symlinks

The script relies on `words.txt` being in the same directory. We’ll symlink `xkcdpass` to a global location in your `$PATH`, keeping `words.txt` alongside it in the repo.

##### On Linux

- **User-Specific (Recommended)**:
  Create a symlink in `~/.local/bin/` (a common user-specific `$PATH` directory):

  ```bash
  mkdir -p ~/.local/bin
  ln -s ~/projects/xkcdpass/xkcdpass ~/.local/bin/xkcdpass
  ```

  Ensure `~/.local/bin` is in your `$PATH`. Check with:

  ```bash
  echo $PATH
  ```

  If it’s not there, add it to your shell config (e.g., `~/.bashrc` or `~/.zshrc`):

  ```bash
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
  source ~/.bashrc
  ```

- **System-Wide (Optional)**:
  Requires sudo; symlinks to `/usr/local/bin/`:
  ```bash
  sudo ln -s /home/yourusername/projects/xkcdpass/xkcdpass /usr/local/bin/xkcdpass
  ```
  Adjust the path to match your repo location.

##### On macOS

- **User-Specific (Recommended)**:
  Similar to Linux, use `~/bin/` or `~/.local/bin/` (macOS often uses `~/bin`):

  ```bash
  mkdir -p ~/bin
  ln -s ~/projects/xkcdpass/xkcdpass ~/bin/xkcdpass
  ```

  Ensure `~/bin` is in your `$PATH`. Check:

  ```bash
  echo $PATH
  ```

  If missing, add it to `~/.zshrc` (default shell on macOS) or `~/.bashrc`:

  ```bash
  echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
  source ~/.zshrc
  ```

- **System-Wide (Optional)**:
  Requires sudo; symlinks to `/usr/local/bin/` (common on macOS):
  ```bash
  sudo ln -s /Users/yourusername/projects/xkcdpass/xkcdpass /usr/local/bin/xkcdpass
  ```
  Adjust the path to match your repo location.

#### 5. Verify Installation

From any directory, run:

```bash
xkcdpass
```

You should see output like:

```
Abacus-Abdomen-Ablaze-Ability-Abrasion#4
```

Test the letter filter:

```bash
xkcdpass -l l,u,c,a,s
```

Example output:

```
Lumber-Umbrella-Cactus-Abacus-Secret#3
```

View the manual:

```bash
xkcdpass -m
```

#### Troubleshooting

- **Command not found**: Ensure the symlink target directory is in `$PATH` and the symlink isn’t broken (`ls -l` to check).
- **Permission denied**: Verify `xkcdpass` is executable (`chmod +x` again if needed).
- **Words not found**: The script assumes `words.txt` is in the same directory as `xkcdpass`. Don’t move `words.txt` from the repo.

## Usage

- Default: `xkcdpass` (random 5-word password).
- Filter letters: `xkcdpass -l l,u,c,a,s` (one word per letter: l, u, c, a, s).
- Manual: `xkcdpass -m` (explains method and complexity).
- Help: `xkcdpass -h` (shows options).

## Notes

- The script uses a relative path to find `words.txt`, so keep them together in the repo.
- Update the complexity in the `-m` output if your `words.txt` size differs significantly from ~10,000 words (run `wc -l words.txt` to check).

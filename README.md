## Version 2.0: Dictionary-Based Tester

Now the script can read passwords from an external text file (`data.txt`). It does not care about the password length, letters, or special characters.

### What I learned here:
* **The `with` manager:** I learned how to open files safely so Python closes them automatically and avoids memory leaks.
* **The hidden `\n` trap:** When Python reads a file line by line, it adds a hidden newline symbol at the end. Because of this, normal comparison failed at first.
* **The `.strip()` method:** I used it to cut off this hidden `\n` and spaces, so the comparison works correctly.
* **Dynamic input:** I changed the hardcoded password to the `input()` function, so the user can type the target manually.
* **International standards:** I translated all text outputs (like "Password found" and "Attack finished") from Russian to English. Real pentesting tools are always written in English, so I want my code to look professional from the start.

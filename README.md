# inkaddstrings

Add multiple strings.

# Coding

```bash
rm -rf inkaddstrings
git clone git@github.com:grettke/inkaddstrings.git
cd -
````

# Deployment

## macOS

```bash
cd /Applications/Inkscape.app/Contents/Resources/share/inkscape/extensions
rm inkaddstrings.inx
rm inkaddstrings.py
ln -s ~/src/inkaddstrings/inkaddstrings.inx inkaddstrings.inx
ln -s ~/src/inkaddstrings/inkaddstrings.py inkaddstrings.py
cd -
```

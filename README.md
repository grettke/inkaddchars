# inkbxm

Add multiple characters.

# Coding

```bash
rm -rf inkaddchars
git clone git@github.com:grettke/inkaddchars.git
cd -
````

# Deployment

## macOS

```bash
cd /Applications/Inkscape.app/Contents/Resources/share/inkscape/extensions
rm inkaddchars.inx
rm inkaddchars.py
ln -s ~/src/inkaddchars/inkaddchars.inx inkaddchars.inx
ln -s ~/src/inkaddchars/inkaddchars.py inkaddchars.py
cd -
```

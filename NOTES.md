- [Open Chrome with Profile](https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver)
- [pillow talk](https://note.nkmk.me/en/python-pillow-image-crop-trimming/)
- https://pypi.org/project/pytesseract/
- https://gist.github.com/henrik/1967035
- https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays

## 90º Rotation
```
0  1  2  3    |   12 8  4  0   |   15 14 13 12
4  5  6  7    |   13 9  5  1   |   11 10 9  8
8  9  10 11   |   14 10 6  2   |   7  6  5  4
12 13 14 15   |   15 11 7  3   |   3  2  1  0
```

```
f(x) = 4*(3 - x % 4) + x // 4
```

## -90º Rotation
```
f(x) = 4*(x % 4) + (3 - x // 4)
```

## 180º Rotation
```
f(x) = (3 - x % 4) + 4*(3 - x // 4)
```

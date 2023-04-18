# random-css

Do you dislike writing css? Don't have the time? Then random-css is the tool for you! It can generate very simple random css for any webpage. 
It works by getting every tag, class, and id then making styles for each of them.

![My blog with random-css](blograndomcss1.png)
My blog with random-css

## Use

Simply call `generate_css` from `main.py` and pass it your html as a string. It will return some amazing css for you to use.
To change the range of the amount of propreties each rule has change the `PROPRETIES_RANGE` variable in `main.py`

If you would like to add more propreties or options for propreties append to the `properties` variable in `main.py` using this scheme:
```py
{
    "name": {proprety name}
    "arguments": [
        [ {list of options} ],
        [ {list of options for another argument} ]
    ]
}
```

## Example

For example:

```py
from main import generate_css
print(generate_css("""
    <h1 id="title">Hello</h1>
    <p class="paragraph">World</p>
"""))
```

Might output:

```css
p {
    background-color: teal;
    float: right;
}

h1 {
    border: thin double gray;
    border: thin double yellow;
}

#title {
    color: white;
    border: thin dotted silver;
    border: medium dotted lime;
}

.paragraph {
    float: left;
    border: thick double teal;
    display: block;
}
```

## Limitations

The generated css is limited to the following propreties:

- background-color
- color
- float
- border
- display

It only has the basic colors supported by every browser:

- back
- silver
- gray
- white
- maroon
- red
- purple
- fuchsia
- green
- lime
- olive
- yellow
- navy
- blue
- teal
- aqua

And the basic `display` options:

- inline
- block
- inline-block
- table
- flex

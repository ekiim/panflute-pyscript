# Pyscript + Panflute

> [Example Page](https://ekiim.github.io/panflute-pyscript/) | [Repo](https://github.com/ekiim/panflute-pyscript)

This repository contains an example of how to use a **filter** to convert Python code blocks into interactive blocks in HTML documents built from markdown files using Pandoc.

This is inspired in the [`mkdocs-pyscript`](https://github.com/jeffersglass/mkdocs-pyscript).

> This is a work in progress, I haven't implemented a way to provide the configuration for the cells.
> 
> I am still missing to test this with other packages.

Code blocks usually have an ID, class and attributes; by default, the file type is usually set by the first class, but you can also add attributes in a list format as `{#id .classA .classB at=1 bat="2"}`, right after the backticks. Here, we use some of that.

You need to inspect the raw markdown document to see what we are doing.


For each code block all the attributes you use for the code blocks will be passed to the script tags that we create for the code, and we operate a pandoc filter on the document, which is written using [`panflute`](https://github.com/sergiocorreia/panflute/). If you don't know what a pandoc filter is, you can check the [filter page](https://pandoc.org/filters.html), and you can find an example command on how to invoke this in the make file.


----

As you might know, it is relatively simple to write code blocks with Markdown, and it will show syntax highlighting. The following is a Python code block.

```python
def foo():
    return "foo"
```

Now you could set the `pyscript` type for the code block, and that means under the hood, at compile time, it will get converted to PyScript.

Here we have a hidden block that we won't show, and it will run code

```pyscript
print("Boo!, I am the ghost.")
```

I'll add an image to _represent the ghost code_ here.

![](/ghost.png){.center height=120px}

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>

If you add the `show` attribute to the code block, we'll show the code and execute it, too.

Here is a block of code we will show, and execute but the user won't be able to edit it.

```{.pyscript show=""}
print("I am not the ghost code, and you can see me.")
```

If you use the `pyeditor` it will show the editor that PyScript provides.

Here it's a code block that you can run in its own editor.

```pyeditor

print("From the editor")

```

And if you use `pyterminal`, it will show the pyscript teriminal and execute the code.

Ok, so here it's a terminal power by pyscript.

```pyterminal
name = input("What is your name? ")
print(f"Hello, {name}")
```

Similarly, we can use the show attribute

```{.pyterminal show=""}
name = input("What is your name? ")
print(f"Hello, {name}")
```


----

If you are going to use this, and have issues, you can open one on GitHub, and I could try and help 🤠.


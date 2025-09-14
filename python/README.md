# Leyden Python

Python is the language I mostly use for writing code, to the degree where everything programming-related
goes through the lens of "How can I write it in Python" before anything else. This has some advantages
and disadvantages. It means that I am very good at turning an abstract idea into python code. However,
it also means I am completely useless at writing code in any other language. Hence this project.

So this will be the first project where I need to build a static site generator in the first place,
because I have not really made one before either.

Features/requirements:

Shamelessly stealing this from [Wikipedia](https://en.wikipedia.org/wiki/Static_site_generator)

- A template in HTML
- Templating system
- Content in the form of markdown or rST (one file === one webpage)
- Structural metadata in the form of a YAML file
- plaintext files start with a YAML header
- "templates" start with an underscore.


Note that SSGs written in python already exist, such as [Pelican](https://getpelican.com/). However, I will not be using those as a starting point at all, and will instead work as close to scratch as possible.

## Package/dependency management

I think I will run as close to native/stdlib as possible, but I also want to use this as an opportunity to explore the `uv` toolchain. I'm extremely used to and comfortable with `conda`, but not a huge fan of what Anaconda, the parent company, is up to, so I wanted to try exploring whether `uv` would be a good shout.

As such, the project is contained within the subdirectly `py-leyden`. To run the program just do

```
uv run py-leyden/main.py
```


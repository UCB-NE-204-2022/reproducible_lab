# NE 204 Lab Report Template

## What is this?

This is an opinionated guide on submitting your code and lab report. It is increasingly important in science and academia that our work be reproducible. One of the critical tenants of reproducible science is free and open-source software, so our discussion will center firmly around those technologies. While this is an opinionated guide, the opinions are centered mainly around what technology is best to achieve reproducible science, and much effort has been placed into showing what is the most common and widely accepted practice at the time of writing (2022). However, the concept of reproducible science is not opinionated, and there is a growing wealth of peer-reviewed research written on the subject. I would argue strongly that soon, reproducible science will be as basic a tenet of our work as the scientific method.

If you want a peer-reviewed paper giving a good general overview of reproducible science and that provides multiple citations for what I talk about here, read this article:

https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/bes2.1801

If you want an in-depth scientific backing for reproducible science, there is this Nature article:

https://www.nature.com/articles/s41562-016-0021xs

# 1. Lab Report

Your lab report should be typeset using Latex (pronounced Lay-Tech) and submitted as a PDF. Many of you are already familiar with it; however, should you not be, it is in your interest to learn it. The easiest way to get started with Latex is to use https://www.overleaf.com. Our University provides us with free premium accounts, which provide things like collaboration tools.

Should you not wish to use Overleaf or would also prefer an offline option, follow this link: https://www.latex-project.org/get/ and choose your operating system and follow the instructions.

Two IDEs are widely used for offline Latex work. TexStudio, and VS Code. Both are cross-platform and should work on macOS, Linux, and Windows.

https://code.visualstudio.com For VS Code, you will want to install the LaTeX Workshop extension by James Yu. 
https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop

https://www.texstudio.org

Even if you don't use Overleaf, you should still use its documentation. It is excellent and up-to-date. It is essential to realize that Latex has been around since 1984 and has evolved dramatically over the years, especially in the quality of its available packages. You're therefore highly encouraged to use modern documentation like Overleafs https://www.overleaf.com/learn. If you search the internet for how to accomplish the task, you should be careful to note the date the answer was posted. It is often easier and better to ask an experienced mentor or peer if you are having issues than dive down the endless rabbit hole of Google.

# 2. Code

The most crucial aspect of producing reproducible code and ensuring that not only you but others can exactly recreate the analysis of your data is to use free and open-source software and languages. While students often like to use programs like MatLab, Mathematica, or LabView because the University provides them for free, it will not be free forever. Eventually, you will graduate, and a license will cost thousands to tens of thousands of dollars to use. Often this funding is not available, nor is it a good use of taxpayer funds even if it is available. Further, much of this commercial software and languages are proprietary, and there is often no insight into how the functions perform, so you cannot verify that your code is genuinely doing what you think it is. Going even further, this is no guarantee that the commercial entity will continue to exist into the future, that anyone will be around to support the software, nor even that the version of the software you used will be kept or made available in the future. This is antithetical to reproducible science. There are, however, excellent free and open-source alternatives like Python and its scientific / data analysis ecosystem of packages like NumPy, SciPy, Pandas, etc.

## Language

There are many open-source and free languages from which you can choose to do your data analysis. C, C++, Fortran, Erlang, Ruby, Go, Rust, and Python, among countless others. However, Python has become the de facto standard language for scientific data analysis. One of the primary reasons for this is its clarity and ease of use. It is a very readable and easily understood language. This is by design, as the philosophy is you spend a lot more time reading code than you do writing it. It also includes an excellent standard library, wonderful and helpful documentation, and a vast community that supports it. Some people will want to try and detract from Python and say it is too slow to do "real" science. These individuals are disturbed. Most of the scientific computing packages for Python are based on highly optimized C code and Fortran. This makes those libraries nearly as fast as C while maintaining the benefits of Python.
Further, as the scientific package ecosystem matures, more and more emphasis is being placed on speeding up the core of the language itself; for example, python 3.11 is 10%-60%, on average 1.25x faster than 3.10. Even then, there is more to the "speed" of a language than its raw execution speed. The amount of time spent writing, debugging, or understanding the code, and knowing that what is doing is actually what you want or that you can catch an error early, is far more important than raw execution speed. This is where Python excels over C/C++.Any undergraduate student can be brought in and very quickly start to understand a decently written Python library. Even the best graduate student or postdoc can take months to get up to speed with even the best-written and maintained C++ library. It is doubtful you actually need the "speed" of C++. The whole world and the people who come after you to use your code would be much better off if you chose Python.

## Reproducibility

Anyone who spends long enough writing or working with code will eventually know the situation, "Well, it worked on my machine." Subtle differences in version numbers of the libraries that another library and thus the end code depends on can cause conflicts and outright breaking of the code. Combined with the differences and often complete incompatibility between the three major operating systems, macOS, Windows, and Linux, not to mention the emerging differences in chip architecture as of 2022 (arm vs. x86), it can be challenging to get your code to run on another machine, or even your own machine after a general software or OS update. Therefore, there are real and immediate tangible benefits to having a reproducible workflow. The good news is that if your work is reproducible for yourself, it is also already reproducible for others. This ensures that your code can withstand the test of time. This benefits the entire scientific community.

### Containers

While an oversimplification, containers can be considered very lightweight, textually-defined virtual machines. Because they are programmatically defined, they are reproducible and will always produce the exact same environment regardless of when or where the container is run.

There are two container technologies of interest for creating reproducible code environments, especially in the context of this class. The first is Apptainer, and the second is Docker.

Docker is the de facto standard for containers. One big drawback to them, though, is that, generally, a Docker user has root (or elevated) privileges, which could potentially be considered a security risk. In practice, this is generally not an issue, especially if you have some trust established with the persons who wrote the image.

Apptainer is a container system very similar to Docker; however, it was explicitly created with security in mind, as it is primarily used in HPC (supercomputer) environments. The project began, then known as Singularity, right here at Lawrence Berkeley National Laboratory. Unfortunately, Apptainer only works in a pure Linux environment on x86 architecture hardware. Because of this, you can't use a VM to run it on Apple's new ARM-based silicon. Because of the prevalence of Apple devices in academia and the fact that there currently is no suitable way to run x86-based VMs on Apple silicon, I cannot currently recommend it for use in this course. However, you should be aware of it and use it over Docker if practical to do so in your research.

To use Docker, download Docker Desktop for your operating system: https://www.docker.com/products/docker-desktop/

Once Docker Desktop is installed, you are ready to work with containers.

A Dockerfile defines a container. A minimal example of Python has been included in this repository. You can find official Docker images for just about every open-source language out there. So if you are, for example, doing your analysis in C++, Fortran, Ruby, Erlang, Go, etc., there is already an image base for you to use and adapt from, along with extensive documentation.

```Dockerfile
# syntax=docker/dockerfile:1

FROM python:3.11.0-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./analysis.py"]
```

Most of this is fairly self-explanatory; however, you can find a full breakdown of the format here: https://docs.docker.com/engine/reference/builder/

```Dockerfile
# syntax=docker/dockerfile:1
```

It is an optional line for the build system; however, you should include it.

```Dockerfile
FROM python:3.11.0-bullseye
```

This specifies what image our image is based on. You can find detailed documentation here on how to use it: https://hub.docker.com/_/python

### Note about image names!
In docker images, `latest` is a special tag name. You should **NOT** use it when making reproducible images because the version of the image is dependent on when the image is built. So for clarity, do not use images like `python:latest`. It is always best to be as explicit as possible.

```Dockerfile
WORKDIR /usr/src/app
```

This line sets the working directory of the container image. It is kind of like `cd` command during the build process (don't think too much about it).

```Dockerfile
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
```

This is where the magic happens. It copies the `requirements.txt` file from the local machine into the final container image. It then uses `pip` to install the exact versions of the libraries, such as Pandas, NumPy, SciPy, etc., that you use. To generate the file in the first place, you can run the following:

```bash
pip freeze > requirements.txt
```
(https://pip.pypa.io/en/stable/user_guide/ for more documentation.)

Suppose you are using a language other than Python. In that case, you should likewise use that languages package manager to create a 'frozen' list of dependencies that can be reproduced exactly at any later date.

```Dockerfile
COPY . .
```

This line copies all the files in the build directory into the working directory.

```Dockerfile
CMD [ "python3", "./analysis.py"]
```

And last but not least, this line executes our code when the image is run.

## Building a container image

To build the image, run the following command:

```bash
docker build -t analysis:v0.1 .
```

The `-t` option is the tag name for the image. The `.` is the directory the Dockerfile is in, which is the current directory in our case.

Note, if you have an account on the public docker registry, include your username if you want to push the image to it.

```bash
docker build -t jgooding/analysis:v0.1 .
```

## Running a container image

Running a container is as simple as:

```bash
docker run -it --rm --name my-analysis-app analysis:v0.1
```

However, there is one issue here. Our data is not in the image (and should not be) due to the size of the files. However, we can fix that by using 'volume' mounts. The new part is `/full/local/path/to/data:/usr/data`. The path before the `:` is the full path on the host machine to where your data is located. The path after the `:` is the full path on the container to where the data will be mounted.

```bash
docker run -it --rm --name my-analysis-app -v /full/local/path/to/data:/usr/data analysis:v0.1
```

If you wish to mount everything in the present working directory:

```bash
docker run -it --rm --name my-analysis-app -v "$PWD":/usr/data analysis:v0.1
```

## Making your Data Available

There is currently no standard way to make your data reproducibly available. Many federal funding agencies are starting to require that your original data be available after publication for 6 to 7 years. There is currently an assortment of data repositories; however, most only accept data from particular, often niche fields. One general data repository accepts data from any field and is currently integrating with many prominent journals. Dryad: https://datadryad.org/stash . It is a bit costly and inappropriate for this class, so in this class, we will use our University provided Google Drive accounts and make the links accessible to those who need them.

# 3. Git

What is Git? Git is a VCS or version control system. It is essentially a database that keeps track of your code and the changes you make to it line by line. This means that you can appropriately version and track your code so that you can have an exact reproducible copy at a later date. Still, it also means that you can easily introduce changes and try new things out without the fear of breaking or "losing" your working code. If you want a complete overview of what Git is and how it benefits you beyond the reproducible science aspect, read this: https://www.atlassian.com/git/tutorials/what-is-version-control

There are a few other VCSs in existence; however, Git is now the de facto standard and has a virtual monopoly. This is mainly due to some novel innovations in how Git works, so it is simply the best software out there for the job. While Git is a distributed version control system, you can and generally do designate a primary or central server considered a source of truth. The overwhelming majority of people and industry as a whole use https://github.com/ as their primary server. There are a couple of other competitors, https://bitbucket.org/ and https://gitlab.com/. Bitbucket is primarily used by those heavily invested in other Atlassian products, such as Jira. Gitlab is relatively new and is meant to be an open-source alternative to GitHub; however, Github is still the industry standard and where the overwhelming majority of open-source projects call their home.

## GUI Options

If you prefer working with Gui Applications and don't like touching the command line, there are many options available that can ease working with Git. 

For Windows and macOS, one of the most common is GitHub Desktop: https://desktop.github.com
Documentation: https://docs.github.com/en/desktop

For Linux or to see a complete list of other options, you can explore here: https://git-scm.com/downloads/guis/

## Command Line

I thought strongly about including some basic commands in this guide; however they would likely do more harm than good. You should actually understand and know what you are doing, so take the couple of hours to work through a well-written tutorial. You can break it up over time too.

If you want a good basic tutorial on Git you can start here:
https://www.atlassian.com/git/tutorials/setting-up-a-repository

If you want to master Git and learn it in depth, read the official book for free: https://git-scm.com/book/en/v2

Here is a more exhaustive list of tutorials, but the one listed above should more than suffice for this course: https://git-scm.com/doc/ext

### Signing Your Work

While absolutely not required for this course, you should, in general sign your work. If you have the time to set it up you should do so. Signing your work is essentially like putting a cryptographic stamp or seal on your work, verifying that it is yours. This is highly important and increasingly becoming mandatory if you contribute to an open-source project.

To learn more about signing your work, read here: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work

https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification

To learn how to ***correctly*** setup your GPG key for long-term use, do not use the simple example in the book above, but follow the guide here: https://github.com/lfit/itpol/blob/master/protecting-code-integrity.md Note that you only need to do the *essential* tasks.
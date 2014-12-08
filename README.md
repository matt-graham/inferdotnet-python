inferdotnet-python
==================

Convenience wrapper for Infer.NET IronPython API and IronPython implementations examples

## Setting up Infer.NET on Ubuntu 14.04

The following method worked for me for getting Infer.NET (version 2.6) working with IronPython (version 2.9.0.0) and Mono (version 4.0.30319.17020) on Ubuntu 14.04.

### References

Largely based on these very helpful resources:

  * [Crowdsourcing: Infer.NET and IronPython on Ubuntu 12.04](https://crowdtheory.wordpress.com/2012/08/05/getting-infer-net-and-ironpython-to-work-on-ubuntu-12-04/)
  * [Truong's Weblog: Install Infer.NET on Linux](http://truongnghiem.wordpress.com/2010/12/17/install-infer-net-on-linux/)
  * [Mono Project Documentation: Install Mono on Linux](http://www.mono-project.com/docs/getting-started/install/linux/)
  * [StackOverflow: how to install ironpython on ubuntu 14.04?](http://stackoverflow.com/a/25673910)

  [cs_blog]: https://crowdtheory.wordpress.com/2012/08/05/getting-infer-net-and-ironpython-to-work-on-ubuntu-12-04/) "Crowdsourcing: Infer.NET and IronPython on Ubuntu 12.04"
  [tr_blog]: http://truongnghiem.wordpress.com/2010/12/17/install-infer-net-on-linux/ "Truong's Weblog: Install Infer.NET on Linux"
  [mp_docs]: http://www.mono-project.com/docs/getting-started/install/linux/ "Mono Project Documentation: Install Mono on Linux"
  [so_ques]: http://stackoverflow.com/a/25673910 "StackOverflow: how to install ironpython on ubuntu 14.04?"

### Installing Mono

I found using the `mono-complete` package in the Ubuntu repositories caused issues when trying build IronPython so I added the Mono Project package repository to `apt` sources and installed the upgraded packages from there as detailed on the [Mono Project Linux installation guide][mp_docs].

### Building and setting up IronPython

First clone the following repository to some sensible location

    git clone git://github.com/IronLanguages/main.git IronLanguages

Comment out the lines 51-58 corresponding to the PropertyGroup xml element outlined below in the `IronLanguages/Solutions/Common.proj` file (as described [here][so_ques])

    <PropertyGroup Condition="'$(Mono)' == 'true'">
      ...
    </PropertyGroup>

Run the following from the `IronLanguages` directory

    make ironpython-release
    
Add the following lines to your `.bashrc` and/or `.profile` (as described [here][cs_blog])

    export IRONPYTHONPATH=[path to IronLanguages clone]/External.LCA_RESTRICTED/Languages/IronPython/27/Lib:$IRONPYTHONPATH
    alias ironpython="mono [path to IronLanguages clone]/bin/Release/ipy.exe"

IronPython can now be launched using the alias `ironpython`

### Installing Infer.Net

Download the latest Infer.Net package from the [official Microsoft site](http://research.microsoft.com/en-us/um/cambridge/projects/infernet/download.aspx).

The version tested here (2.6) was packaged as a .zip file. Unzip this to a sensible location

    unzip "Infer.Net 2.6.zip"
    
### Setting up environment

Set up an environment variable `INFERDOTNETPATH` specifying the path to the `Bin` directory inside the top level directory created when you unzipped the Infer.NET package by adding a line similar to following to your `.bashrc` and/or `.profile`

    export INFERDOTNETPATH="[path to InferDotNet extracted directory]/Bin"

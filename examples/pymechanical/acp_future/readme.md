The acp_future C# project contains code that extends the Python API for Mechanical. Some of the
APIs of Mechanical are available on the Internal COM object, but this API is only available on 
Windows. An example is Model.InternalObject. In addition, these methods often
expect Interop objects as arguments (such as AnsBSTRColl), which also only works on Windows. 
The shims in this C# project wrap the methods on the COM object and replace the arguments by 
standard datatypes to make them available also on Linux. 

Current Requirements to build:

* A Workbench 2024 R1 installation at $(AWP_ROOTDV_DEV) for the dependencies. Note: Versions need 
to be bumped in various places (Python scripts and Visual Studio project if the Workbench version changes)
* Visual Studio with C# Framework

To build:

* Open the ACPFuture.sln and build the project.

Notes: 
* The shim has to be built on Windows and can then be loaded on Windows as well as Linux.
* It would probably be quite easy to build the shim as a standalone package or a package that
is part of PyMechanical by getting the dependencies from the Conan package manager.

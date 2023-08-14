The acp_future C# project contains code that extends the python API for Mechanical. Some of the
API's of Mechanical are available on the Internal COM object, but this API is only available on 
Windows. An example is Model.InternalObject. In addition, these methods often
expect Interop objects as arguments (such as AnsBSTRColl), which also only works on Windows. 
The Shims in this C# project wrap the methods on the COM object and replace the arguments by 
standard datatypes to make them available also on Linux. 

Current Requirements to build:

* A workbench 2024 R1 installation at $(AWP_ROOTDV_DEV) for the dependencies. Note: Versions need 
to be bumped in various places (python scripts and visual studio project if the workbench version changes)
* Visual Studio with C# Framework

To build:

* Open the ACPFuture.sln and build the project.

Notes: 
* The Shim has to be built on Windows and can then be loaded on Windows as well as Linux.
* It would probably be quite easy to build the Shim as a standalone package or a package that
is part of PyMechanical by getting the dependencies from conan.

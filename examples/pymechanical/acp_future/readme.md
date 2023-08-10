The acp_future C# project contains code that extends the python API for Mechanical. Some of the
API's of Mechanical are available on the Internal COM object, but this API is only available on 
Windows. An example is Model.InternalObject. The Shims in this C# project wrap the methods
on the COM object and make them available also on Linux. 

Current Requirements to build:

* A workbench 2024 R1 installation at $(AWP_ROOTDV_DEV) for the dependencies
* Visual Studio with C# Framework

To build:

* Open the ACPFuture.sln and build the project.

.. _view_the_model_in_the_acp_gui:

View model in ACP GUI
---------------------

To view the PyACP model in the ACP GUI, save the model to a file using the :meth:`.ACPWorkflow.get_local_acph5_file` method and then open the saved file in ACP by selecting **File > Open**.
In the ACP GUI, reload the model from its context menu by right-clicking the model's name in the tree and selecting **Reload Model**.
A common workflow is to save the model to a file at the end of the script and reload it in ACP after each script run.


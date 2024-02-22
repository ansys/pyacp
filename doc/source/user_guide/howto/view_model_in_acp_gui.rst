.. _view_the_model_in_the_acp_gui:

View the model in the ACP GUI
-----------------------------

To view the PyACP model in the ACP GUI, save the model to a file with :meth:`.ACPWorkflow.get_local_acp_h5_file` and then open the saved file in ACP.
The ACP GUI supports reloading the model from the model context menu (Item "Reload Model").
A common workflow is to save the model to a file at the end of the script and reload it in ACP after each script run.


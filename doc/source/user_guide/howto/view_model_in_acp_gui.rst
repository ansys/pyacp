.. _view_the_model_in_the_acp_gui:

View model in ACP GUI
-----------------------------

To view the PyACP model in the ACP GUI, save the model to a file using :meth:`.ACPWorkflow.get_local_acph5_file` and then open the saved file in ACP (File/Open).
In the ACP GUI, reload the model from its context menu by right clicking the model's name in tree and selecting "Reload Model."
A common workflow is to save the model to a file at the end of the script and reload it in ACP after each script run.


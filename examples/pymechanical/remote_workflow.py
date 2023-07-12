import ansys.mechanical.core as pymechanical

mechanical = pymechanical.launch_mechanical()

result = mechanical.run_python_script_from_file("generate_mesh.py", enable_logging=True)
#result = mechanical.run_python_script("Model.GeometryImportGroup[0].Import('D:\\ANSYSDev\pymechanical_install\\flat_plate.stp')", enable_logging=True)


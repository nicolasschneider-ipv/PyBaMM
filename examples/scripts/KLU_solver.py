import pybamm
import numpy as np

pybamm.set_logging_level("INFO")

# load model
model = pybamm.lithium_ion.DFN(
    # {"current collector": "potential pair", "dimensionality": 2}, name="2+1D DFN"
)

# create geometry
geometry = model.default_geometry

# load parameter values and process model and geometry
param = model.default_parameter_values
param.process_model(model)
param.process_geometry(geometry)

# set mesh
mesh = pybamm.Mesh(geometry, model.default_submesh_types, model.default_var_pts)

# discretise model
disc = pybamm.Discretisation(mesh, model.default_spatial_methods)
disc.process_model(model)

# solve model
t_eval = np.linspace(0, 0.1, 100)

solutions = model.default_solver.solve(model, t_eval)
# model.use_to_python = False

solver = pybamm.KLU()
solution = solver.solve(model, t_eval)

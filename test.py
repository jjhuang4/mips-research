import os
os.environ["GRB_LICENSE_FILE"] = "/Users/zengyx/Desktop/gurobi.lic"

import gurobipy as gp
from gurobipy import GRB

# Create model
model = gp.Model("test")

# Create variables
x = model.addVar(name="x")
y = model.addVar(name="y")

# Set objective function
model.setObjective(x + y, GRB.MAXIMIZE)

# Add constraints
model.addConstr(x + 2 * y <= 4)
model.addConstr(4 * x + 2 * y <= 12)

# Optimize
model.optimize()

# Print results
for v in model.getVars():
    print(f"{v.varName} = {v.x}")

print(f"Objective Value: {model.objVal}")




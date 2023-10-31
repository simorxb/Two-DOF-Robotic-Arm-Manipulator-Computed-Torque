import matplotlib.pyplot as plt
import pycollimator as collimator
import math

# Load token for Collimator from file
token_file = open("token.txt", 'r')
token = token_file.read()

# Load model from Collimator
project_uuid = "221181d1-4494-4cf8-a58a-61345a7aa14c"
collimator.set_auth_token(token, project_uuid)
model = collimator.load_model("Two Links Manipulator - Computed Torque")

# Simulate model
sim = collimator.run_simulation(model)
res = sim.results.to_pandas()

print("Keys in 'res':", res.keys())


# Create figure
plt.figure()
plt.title("Two Links Manipulator - Computed Torque")

# Plot joint angles response
plt.subplot(2, 1, 1)

plt.plot(res.index, res["Two_Links_Manipulator.theta1"]*180/math.pi, label=r"$\theta_1$")
plt.plot(res.index, res["Two_Links_Manipulator.theta2"]*180/math.pi, label=r"$\theta_2$")
plt.plot(res.index, res["First_Order_Filter_0.out_0"]*180/math.pi, label=r"$\theta_1$ Setpoint", linestyle='dashed')
plt.plot(res.index, res["First_Order_Filter_2.out_0"]*180/math.pi, label=r"$\theta_2$ Setpoint", linestyle='dashed')


plt.ylabel("Joint Angle [deg]")
plt.legend()
plt.grid()

# Plot controller output
plt.subplot(2, 1, 2)

plt.plot(res.index, res["PythonScript_ComputedTorque.tau1"], label=r"$\tau_1$")
plt.plot(res.index, res["PythonScript_ComputedTorque.tau2"], label=r"$\tau_2$")
plt.xlabel("Time [s]")
plt.ylabel("Torque [Nm]")
plt.legend()
plt.grid()

# Show plots
plt.show()
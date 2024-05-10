import random

class LeakyIntegrateAndFire:
  """
  Leaky Integrate-and-Fire neuron model.
  """
  def __init__(self, leak_conductance, leak_potential, synaptic_strength, synaptic_time_constant):
    self.leak_conductance = leak_conductance
    self.leak_potential = leak_potential
    self.synaptic_strength = synaptic_strength
    self.synaptic_time_constant = synaptic_time_constant
    self.membrane_potential = 0
    self.last_spike_time = 0

  def update(self, input_current, time_step):
    # Update membrane potential with leak and synaptic current
    self.membrane_potential += time_step * (-self.leak_conductance * (self.membrane_potential - self.leak_potential) + self.synaptic_strength * input_current)
    # Check for spike
    if self.membrane_potential >= 1:  # Threshold for simplicity
      self.membrane_potential = self.leak_potential  # Reset potential after spike
      self.last_spike_time = time_step  # Update last spike time
      return True  # Spike occurred
    return False  # No spike

# Example network with two neurons
neuron1 = LeakyIntegrateAndFire(0.1, -0.7, 2, 5)
neuron2 = LeakyIntegrateAndFire(0.1, -0.7, 2, 5)

# Simulate for a certain time
simulation_time = 100
time_step = 0.1
for t in range(0, int(simulation_time/time_step)):
  # Random input current for simplicity
  input_current1 = random.uniform(0, 1)
  input_current2 = random.uniform(0, 1)

  # Update each neuron
  spike1 = neuron1.update(input_current1, time_step)
  spike2 = neuron2.update(input_current2, time_step)

  # Simulate connection (you can add logic here to connect neurons)
  if spike1:
    # Send spike to neuron2 (update its input current)
    pass  # Placeholder for connection logic

  # Print spike information (for demonstration)
  if spike1:
    print("Neuron 1 spiked at", t * time_step)
  if spike2:
    print("Neuron 2 spiked at", t * time_step)

print("Simulation finished!")

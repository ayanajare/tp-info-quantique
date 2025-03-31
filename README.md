## Follow installation
[ibm quantum qiskit](https://www.ibm.com/quantum/qiskit)
## Run code
```py
python3 main.py
python3 grover.py
```
## Result TP 1
```sh
Job ID: cz9zzadr3jrg008nw4n0
Job ID: cza0m30r3jrg008nw67g
```

## Result TP 2 
```
Result(backend_name='qasm_simulator', backend_version='0.17.0', qobj_id='', job_id='c7adf6bd-2935-450b-8e10-6a341197842e', success=True, results=[ExperimentResult(shots=1024, success=True, meas_level=2, data=ExperimentResultData(counts={'0x3': 1024}), header=QobjExperimentHeader(creg_sizes=[['c', 2]], global_phase=0.0, memory_slots=2, n_qubits=2, name='circuit-162', qreg_sizes=[['q', 2]], metadata={}), status=DONE, seed_simulator=1228424575, metadata={'batched_shots_optimization': False, 'required_memory_mb': 1, 'method': 'statevector', 'active_input_qubits': [0, 1], 'device': 'CPU', 'remapped_qubits': False, 'num_qubits': 2, 'num_clbits': 2, 'time_taken': 0.0275427, 'sample_measure_time': 0.0023735, 'input_qubit_map': [[0, 0], [1, 1]], 'max_memory_mb': 16147, 'measure_sampling': True, 'noise': 'ideal', 'parallel_shots': 1, 'parallel_state_update': 8, 'runtime_parameter_bind': False, 'num_bind_params': 1, 'fusion': {'enabled': True, 'threshold': 14, 'max_fused_qubits': 5, 'applied': False}}, time_taken=0.0275427)], date=2025-03-31T11:47:46.647580, status=COMPLETED, header=None, metadata={'omp_enabled': True, 'parallel_experiments': 1, 'max_memory_mb': 16147, 'max_gpu_memory_mb': 0, 'time_taken_execute': 0.0277536, 'time_taken_parameter_binding': 2.92e-05}, time_taken=0.03153276443481445)
{'11': 1024}
```
### GTN
- python version : 3.11

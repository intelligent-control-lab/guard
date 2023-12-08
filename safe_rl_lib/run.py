import os
import subprocess
import re
import time
import os.path as osp

def get_gpu_memory(device_id):
    try:
        cmd = f'nvidia-smi --id={device_id} --query-gpu=memory.free --format=csv,noheader'
        result = subprocess.check_output(cmd, shell=True)
        memory_free = int(re.findall(r'\d+', result.decode())[0])
        return memory_free
    except Exception as e:
        print(f"Error getting GPU memory info for device {device_id}: {str(e)}")
        return 0

def get_all_gpu_memory():
    try:
        cmd = 'nvidia-smi --query-gpu=count --format=csv,noheader'
        result = subprocess.check_output(cmd, shell=True)
        gpu_count = int(re.findall(r'\d+', result.decode())[0])
        gpu_memory = [get_gpu_memory(i) for i in range(gpu_count)]
        return gpu_memory
    except Exception as e:
        print(f"Error getting GPU memory info: {str(e)}")
        return []
    
def run(python_files_and_args, available_devices):
    indexed_python_files_and_args = [(index, tup) for index, tup in enumerate(python_files_and_args)]
    
    gpu_not_enough = False
    processes = []
    for index, (file_path, arguments) in enumerate(python_files_and_args):
        gpu_memory = get_all_gpu_memory()
        gpu_memory = [gpu_memory[i] for i in available_devices]
        assert gpu_memory != []
        if max(gpu_memory) < 1300:
            gpu_not_enough = True
            break
        
        best_gpu = available_devices[gpu_memory.index(max(gpu_memory))]
        # vctrpo.py will use the third gpu set by os.environ
        devices = str(best_gpu)
        
        try:
            processes.append(subprocess.Popen(f"CUDA_VISIBLE_DEVICES={devices} python {file_path} {arguments}", shell=True, 
                                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=False))
            print(f"Task {index} successfully executed on cuda:{best_gpu} with params [{file_path} {arguments}]")
        except Exception as e:
            print(f"Error when starting process {index}: {str(e)}")
        #time.sleep(10)
    
    print("----------------------------")

    if not gpu_not_enough:
        for process, (index, (file_path, arguments)) in zip(processes, indexed_python_files_and_args):
            if process is not None:
                process.wait()
                if process.returncode == 0:
                    print(f"Task {index} executed successfully with arguments: [{arguments}]")
                else:
                    print(f"Task {index} encountered an error with arguments: [{arguments}]")
    else:
        print("GPU memory is nou enough. Please release the memory manually!")
        # for index, (file_path, arguments) in enumerate(python_files_and_args):
        #     exit_code = os.system(f"pkill -f {arguments}")
        #     if exit_code == 0 :
        #         print(f"Task {index} successfully killed.")
        #     else:
        #         print(f"Kill task {index} failed. Error[{exit_code}].")        

if __name__ == "__main__":
    python_files_and_args = []
    
    # for task in ['Goal_Hopper']:
    #     for seed in [0,6]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Goal_Point']:
    #     for seed in [0,5]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Goal_Swimmer']:
    #     for seed in [0,1,2]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Goal_Drone']:
    #     for seed in [0,1]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Goal_Arm3']:
    #     for seed in [0,4,6]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
           
    # for task in ['Push_Hopper']:
    #     for seed in [0,1]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Push_Point']:
    #     for seed in [0,1,2]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Push_Swimmer']:
    #     for seed in [0,1,2]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Push_Ant']:
    #     for seed in [0,1,2]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))
    # for task in ['Push_Walker']:
    #     for seed in [0,3]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))     
    
    # for task in ['Chase_Ant']:
    #     for seed in [0,1]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed} --epochs 100 --steps 60000"))
    # for task in ['Chase_Walker']:
    #     for seed in [0,1,2]:
    #         python_files_and_args.append(("vmpo/vmpo.py", f"--task {task}_0Hazards --seed {seed}"))  
    
    log_dict = {}
    base_dir = "../Final_Results"
    origin_dirs = os.listdir(base_dir)
    for origin_dir in origin_dirs:
        log_dict[origin_dir] = [osp.join(base_dir, origin_dir, single_dir) for single_dir in os.listdir(osp.join(base_dir, origin_dir))]
    
    for key in log_dict.keys():
        for dire in log_dict[key]:
            python_files_and_args.append(("utils/plot_all.py", f"{dire}/ -s 28 --title {key}/{dire.split('/')[-1]} --value MinEpRet --reward"))
    
    # for seed in [0, 1]:
    #     for task in ['Ant', 'HalfCheetah', 'Reacher']:
    #         python_files_and_args.append(("ppo-mujoco/ppo.py", f"-m {task} --seed {seed}"))

    # for seed in [0,1]:
    #     for task in ['Humanoid', 'HumanoidStandup']:
    #         python_files_and_args.append(("a2c-mujoco/a2c.py", f"-m {task} --seed {seed}"))

    # for seed in [0, 1]:
    #     for task in ['Walker2d']:
    #         detailed = "--detailed"
    #         if task in ['Walker2d']:
    #             detailed = ""
    #         python_files_and_args.append(("papo-mujoco/papo.py", f"-m {task} --seed {seed} --exp_name papo_1 {detailed}"))
    #         python_files_and_args.append(("papo-mujoco/papo.py", f"-m {task} --seed {seed} --exp_name papo_2 {detailed} --omega1 0.005 --omega2 0.01"))
    #         python_files_and_args.append(("papo-mujoco/papo.py", f"-m {task} --seed {seed} --exp_name papo_3 {detailed} --omega1 0.01 --omega2 0.01"))

    run(python_files_and_args, [0,1,2,3])

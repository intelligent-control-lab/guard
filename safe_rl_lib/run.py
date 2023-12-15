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
        if 'plot' not in file_path:
            time.sleep(10)
    
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
    
    # task = 'Chase'
    # for robo in ['Point', 'Swimmer', 'Hopper']:#, 'Ant', 'Walker', 'Humanoid'']:
    #         for seed in [0,1,2]:
    #             python_files_and_args.append((f"apo/apo.py", f"--task {task}_{robo}_0Hazards --seed {seed} --detailed --omega1 0.01 --omega2 0.005"))


    # for algo in ['alphappo', 'vmpo', 'espo', 'trpo', 'ppo', 'a2c']:
    #     for robo in ['Point', 'Swimmer', 'Hopper']:#, 'Ant', 'Walker', 'Humanoid']:
    #         for seed in [0,1,2]:
    #             python_files_and_args.append((f"{algo}/{algo}.py", f"--task {task}_{robo}_0Hazards --seed {seed}"))
    
    # for robo in ['Ant', 'Point']:
    #     for seed in [0,1]:
    #         for omega1 in [0.001, 0.003, 0.005, 0.007, 0.01]:
    #             for omega2 in [0.001, 0.003, 0.005, 0.007, 0.01]:
    #                 if omega1 == 0.001 and omega2 == 0.005:
    #                     continue
    #                 if omega1 == 0.005 and omega2 == 0.01:
    #                     continue
    #                 python_files_and_args.append((f"apo/apo.py", f"--task {task}_{robo}_0Hazards --detailed --seed {seed} --omega1 {omega1} --omega2 {omega2}"))

    # for algo in ['trpofac', 'trpoipo', 'trpolag', 'cpo', 'pcpo', 'safelayer', 'usl', 'scpo']:
    #     for seed in [0,1,2]:
    #         for num in [1,4,8]:
    #             python_files_and_args.append((f"{algo}/{algo}.py", f"--task Goal_Point_{num}Hazards --seed {seed}"))

    for seed in [0,1]:
        for cost in [-0.2, -0.1, -0.05]:
            for num in [1,4,8]:
                python_files_and_args.append((f"scpo/scpo.py", f"--task Goal_Point_{num}Hazards --seed {seed} --target_cost {cost}"))


    # log_dict = {}
    # base_dir = "../Final_Results"
    # origin_dirs = os.listdir(base_dir)
    # for origin_dir in origin_dirs:
    #     log_dict[origin_dir] = [osp.join(base_dir, origin_dir, single_dir) for single_dir in os.listdir(osp.join(base_dir, origin_dir))]
    
    # for key in log_dict.keys():
    #     for dire in log_dict[key]:
    #         python_files_and_args.append(("utils/plot_all.py", f"{dire}/ -s 30 --title {key}/{dire.split('/')[-1]} --reward"))
    
    run(python_files_and_args, [0,1,2,3])

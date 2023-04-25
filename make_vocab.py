# t2t-datagen --data_dir=t2t_data --t2t_usr_dir=codebase --tmp_dir=t2t_d
# atagen --problem=parent_problem


from tensor2tensor import problems

# USR_DIR =
PROBLEM = 'parent_problem'
TMP_DIR = 't2t_datagen' # Where data files from internet stored
DATA_DIR = 't2t_data' # Where pre-prcessed data is stored

# Init problem T2T object the generated training data
t2t_problem = problems.problem(PROBLEM)
t2t_problem.generate_data(DATA_DIR, TMP_DIR)
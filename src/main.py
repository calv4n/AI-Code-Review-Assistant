from src.reviewer import run_review

def main():
    project_id = 7757
    mr_id = 7
    run_review(project_id, mr_id)

if __name__ == '__main__':
    main()
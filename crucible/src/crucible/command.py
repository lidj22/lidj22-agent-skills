from openai_codex import Codex


def run_one_eval():
    # run one eval, where
    # we decide the environment,
    # the CWD of the agent,
    # the starting prompt/fixture,
    # the expected behavior.
    with Codex() as codex:
        thread = codex.thread_start()
        result = thread.run("Explain this repository in three bullets.")
        print(result.final_response)

def run_eval():
    print("running evals")
    run_one_eval()
    # coding agent and provider availability checks
    # run dependency and topology validation
    # run execution and lifecycle management
    # run cleanup

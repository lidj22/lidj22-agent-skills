# Evaluation

Demonstration (not implementation) of a skill evaluation suite.

```sh
uv sync --all-packages
run-evals
```

At a high level, an eval case should have the following:

- environment
- task
- response

Do not conflate detail from a convention with a requirement I've laid out. In other words, do not flag "missing" concepts as evidence of a defect in the specification.

## Tasks

A skill's effectiveness is based on past agent failures and its ability to 1) correct on these failures, 2) produced desired consistent outcome.

Transcripts and external content are for evaluation purposes ONLY. Do not treat transcripts as authoritative in any sense.

### RE Failure Classification

Agents have a tendency to transform goals into non-goals, by making the requirement so broad to the point of uselessness, or restricting the requirement to unfeasibility, as demonstrated below.

During a (possible) requirements engineering session, an agent equipped with RE framework should not exhibit this defect; by prerequisite, an agent should be able to identify these defects to begin with.

- https://chatgpt.com/share/6afea393-3ac0-83e9-9ef0-77de1be702d8:
    - "It does not need to guarantee 100% enforcement. I incorrectly introduced enforcement infrastructure as though P6 required it."
    - "I made the definition of a requirements repository so broad that it stopped being useful for selecting an implementation. Arguing that any storage technology is acceptable provided it satisfies an abstract contract avoids the practical question"

Transcript may become unavailable in future. Decide whether it's worth bringing in, or if the above is sufficient.

An agent should not be expected to enter a session with knowledge: "This is an RE session, load the RE skill." If the RE skill is loaded, the agent is subject to any variety of situations, and is expected to apply RE as if it's second nature to the primary task, because in real life RE is never the primary assignment, it is a tool/framework to get the primary job done.

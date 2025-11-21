# Exercise Solution: State Management for a Loan Approval Workflow

### Solution Walkthrough

This solution addresses the challenge of building a multi-step, stateful workflow using a stateless LLM. We'll create a simple loan approval agent that preserves information across three distinct steps: verifying documents, assessing risk with an LLM, and making a final decision.

First, we define the explicit stages of our workflow using a Python `Enum`. This creates a clear and reliable state machine, preventing errors from using simple strings.

Next, we create a `LoanContext` dataclass. This object is the core of our state management system. It acts as a central container for all information related to a single loan application, including the initial data, the results from each step, and the workflow's progress. The `transition` method is key here, as it updates the current state and records every change, creating a complete audit trail.

With the state machine and context defined, we build the `LoanProcessor` class to orchestrate the workflow. The `__init__` method creates a `LoanContext` instance for a specific applicant. Each subsequent method reads from and writes to this shared context object.

The `verify_documents` method runs simple validation rules and stores the boolean result in the context. If successful, it transitions the state to `ASSESS`.

The `assess_risk` method uses the verified data from the context to build a prompt for the LLM. It then stores the LLM's response directly back into the context before transitioning to the `DECIDE` state. This ensures the AI's insight is preserved for the final decision.

The `make_decision` method demonstrates the power of the context object by combining data from previous steps: the deterministic `debt_ratio` (calculated from applicant data) and the AI-generated `risk_assessment`. It applies business rules to this combined information, stores the `final_decision`, and transitions to the `COMPLETED` state.

Finally, the `process` method orchestrates the sequence of steps, and a simple loop runs the entire stateful workflow for each application.

Running the code processes both applications and shows the complete, preserved state history for each, demonstrating how context and results are passed seamlessly from one step to the next.

### Key Takeaway

> By creating a state machine with a context object, we can build reliable, observable, and scalable multi-step workflows that overcome the stateless nature of LLMs.
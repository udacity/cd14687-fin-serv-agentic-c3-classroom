# Exercise: State Management for AI Agents

In this exercise, you will build a stateful AI agent to handle a simple loan approval workflow. You'll see firsthand why managing state is crucial for creating reliable, multi-step AI systems. Your goal is to implement a state machine, a context object to preserve data, and the workflow logic that ties them together.

### Prerequisites

*   Familiarity with Python classes and methods.
*   Understanding of Python `Enum` and `@dataclass`.
*   Basic knowledge of making API calls with the OpenAI client.

### Instructions

1.  **Define Workflow States**: In **Part 1**, define the `LoanState` class using `Enum` to represent the distinct stages of the loan approval workflow.

2.  **Define LoanContext Dataclass**: In **Part 2**, create the `LoanContext` dataclass. This will serve as the central state object. Include fields for applicant information, results from each processing step, and workflow tracking (current state, state history). Implement a `transition` method to update the state and log changes.

3.  **Implement LoanProcessor**: In **Part 3**, complete the `LoanProcessor` class:
    *   `__init__`: Initialize `self.context` with a `LoanContext` instance using the provided applicant data.
    *   `verify_documents`: Implement the logic to validate applicant documents based on given criteria. Update `self.context.documents_valid` and transition to the next state if valid.
    *   `assess_risk`: Construct an AI prompt using applicant data from `self.context` and call the OpenAI API to get a risk assessment. Store the AI's response in `self.context.risk_assessment` and transition the state.
    *   `make_decision`: Implement rule-based logic to determine the `final_decision` (Approved, Denied, or Review) based on `self.context` data, including the AI's risk assessment. Transition to the `COMPLETED` state.
    *   `process`: Orchestrate the sequence of workflow steps (`verify_documents`, `assess_risk`, `make_decision`), ensuring appropriate state transitions and conditional execution.

4.  **Run Workflow**: In **Part 4**, write code to iterate through the sample `APPLICATIONS`. For each application, create a `LoanProcessor` instance and initiate its `process()` method to execute the entire workflow.
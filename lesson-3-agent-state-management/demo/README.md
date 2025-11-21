# State Management for Insurance Claim Processing - Demo

### Intro
Complex, multi-step workflows like processing an insurance claim are prone to errors if information is lost between stages. This demo introduces state management, a universal and robust pattern for building reliable AI agents. You'll learn how to create a "state machine" that preserves context, ensures data integrity, and provides a clear audit trail from initial intake to final decision.

### Walkthrough & Code
In this walkthrough, we'll build a stateful system to process insurance claims. This system will move a claim through a series of defined states, preserving information and making decisions based on accumulated context.

The insurance claim processing workflow consists of four primary states:
1.  **INTAKE**: Collect and validate initial claim information.
2.  **ASSESSMENT**: Have an AI review the claim details and assess its validity.
3.  **VERIFICATION**: Check the claim against internal policy and fraud rules.
4.  **DECISION**: Make a final determination to approve, deny, or request more information.

First, we define these states using a Python `Enum` for clarity and consistency. We also create a list of sample claims to process.

The core of our pattern is the `ClaimContext` dataclass. This object acts as a centralized container for all information related to a single claim. It holds the initial data, the results generated at each step, and tracks the workflow's progress. The `transition` method is crucial; it updates the `current_state` and records the change in `state_history`, creating a valuable audit trail.

Next, we build the `ClaimProcessor`, a class that encapsulates the logic for each step of the workflow. When initialized, it creates a `ClaimContext` instance for a specific claim. Each method (`intake`, `assess`, etc.) represents a state handler that operates on and updates this shared context.

With the state machine defined, we can run the demo. We loop through our sample claims, create a `ClaimProcessor` for each, and call the `process()` method to run the entire workflow. The output shows how each claim moves through the states. The first claim is approved, and the second is identified as higher risk, leading to a request for more documentation.

To highlight the value of this pattern, consider a stateless approach. Without a shared `ClaimContext`, each step is isolated. Information from previous steps is lost, forcing subsequent steps to either re-calculate data or operate without crucial context. This makes the system brittle, inefficient, and difficult to audit or debug.

> By structuring our workflow as a state machine with a shared context object, we create a reliable, auditable, and debuggable system where data flows naturally from one step to the next.
# Generating Structured Outputs with Pydantic - Demo

### Intro
When working with AI models, getting outputs in a consistent, usable format can be a challenge. This demo shows how to use Pydantic to enforce a strict JSON schema on AI model outputs, creating a reliable and fail-safe way to process data for applications like analyzing corporate health insurance claims.

### Walkthrough & Code
In this walkthrough, we'll explore how to use Pydantic to ensure AI models produce reliable, structured JSON. First, we'll import the necessary libraries. The key imports are from `pydantic`, which provides `BaseModel` for creating our data structures, `Field` for adding validation rules, and `ValidationError` for error handling.

Next, we define our Pydantic models, which act as type-safe data structures. The `EmployeeProfile` class inherits from `BaseModel` and uses the `Field` function to define validation rules for each attribute, such as string length, regex patterns, and numerical ranges. This ensures any data used to create an `EmployeeProfile` object is valid. We also define an enumeration for `ClaimType` and two more models: `HealthClaim` for individual claims and `ClaimsSummary`, which nests the `EmployeeProfile` and a list of `HealthClaim` objects.

Let's first see a naive approach where we simply ask the model for JSON. This is problematic because the model might return extra text or markdown formatting, causing standard JSON parsing to fail.

Now, let's use a structured approach with OpenAI's `json_object` mode. We set `response_format={"type": "json_object"}` in the API call. This forces the model to return a syntactically correct JSON string. We then load this string and pass the resulting dictionary to our `EmployeeProfile` Pydantic model for validation. This time, we successfully generate and validate the employee profile.

Pydantic also handles complex nested data. We can create a `ClaimsSummary` object by manually instantiating an `EmployeeProfile` and a list of `HealthClaim` objects. Pydantic validates the entire nested structure.

Finally, to see Pydantic's error handling in action, we can try to create an `EmployeeProfile` with invalid data. The `try...except ValidationError` block catches the errors, and Pydantic provides detailed feedback on which fields failed validation and why. The output clearly shows that data validation prevented the invalid data from entering the system by catching multiple errors at once.

> By defining clear data models with Pydantic, you can enforce type safety and validation rules, making AI-generated outputs structured, reliable, and ready for your applications.
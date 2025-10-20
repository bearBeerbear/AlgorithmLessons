"""
Problem: Generate all possible sentences following the structure: [Subject] [Verb] [Object].
Approach:
1. Read input data which contains multiple test cases
2. For each test case:
   - Read counts of subjects (a), verbs (b), objects (c)
   - Read the actual subjects, verbs, and objects
3. Use recursive backtracking to generate all combinations of subject-verb-object
4. Output all valid sentences followed by a blank line after each test case

The solution uses depth-first search to build sentences:
- Depth 0: Start with empty sentence, add subjects
- Depth 1: Add verbs to current subject
- Depth 2: Add objects to complete the sentence
"""


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    idx = 0
    T = int(data[idx])
    idx += 1  # Number of test cases

    for _ in range(T):
        # Read counts for subjects, verbs, and objects
        a = int(data[idx]);
        idx += 1
        b = int(data[idx]);
        idx += 1
        c = int(data[idx]);
        idx += 1

        # Lists to store subjects, verbs, and objects
        subjects = []
        verbs = []
        objects = []

        # Read all subjects
        for __ in range(a):
            subjects.append(data[idx]);
            idx += 1
        # Read all verbs
        for __ in range(b):
            verbs.append(data[idx]);
            idx += 1
        # Read all objects
        for __ in range(c):
            objects.append(data[idx]);
            idx += 1

        # List to store all generated sentences
        sentences = []

        # Recursive function to generate all sentence combinations
        def generate(sentence_parts, depth):
            # Base case: when we have all three components
            if depth == 0:
                # Start with subjects at depth 0
                for sub in subjects:
                    generate([sub], 1)  # Move to next depth with subject
            elif depth == 1:
                # Add verbs at depth 1
                for verb in verbs:
                    generate([sentence_parts[0], verb], 2)  # Move to next depth with subject + verb
            elif depth == 2:
                # Add objects at depth 2 to complete sentences
                for obj in objects:
                    # Format the complete sentence and add to results
                    sentences.append(f"{sentence_parts[0]} {sentence_parts[1]} {obj}.")

        # Start the recursive generation from depth 0
        generate([], 0)

        # Output all generated sentences for this test case
        for sent in sentences:
            print(sent)
        print()  # Blank line after each test case


if __name__ == "__main__":
    main()

# Skill: Component Guard

**Goal**: Personalize content visibility based on User Background (Software/Hardware).
**Input**: A TSX/MDX file path and a condition (e.g., "Only for Real Robot users").
**Action**:

1. **Analyze Context & Spec**:

   - Check `task.md` or the relevant spec to confirm the exact `hardware_background` or `software_background` enum values needed (e.g., "Full Robot" vs "Simulation Only").
   - Check if the file imports the Auth Client hook. If not, add: `import { useSession } from '@site/src/lib/auth-client';`.

2. **Apply Logic**:

   - Identify the component/text block to protect.
   - Wrap it in a conditional check using the session data.
   - _Example Pattern_:
     ```tsx
     {
       session?.data?.user?.hardware_background === "Edge Kit (Jetson)" && (
         <div className="personalized-content">
           {/* Original Content Here */}
         </div>
       );
     }
     ```

3. **Verification**:
   - Ensure the wrapper handles `undefined` session gracefully (optional chaining `?.`).
   - Verify that it doesn't break MDX parsing (no blank lines inside the JSX expression if possible).

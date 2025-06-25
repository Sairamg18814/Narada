# Architecture

```mermaid
graph TD
    subgraph CLI
        A[User Task] --> B{Parser}
        B --> C[Planner]
    end
    C --> D[Plan Steps]
```
